
from pickle import FALSE
import pygame
import random
from threading import Thread
import time
pygame.init()

MAX_NODES = 25
MAX_DEGREE = 3

def gen_degree():
    ops = [1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3]
    i = random.randint(0,len(ops)-1)
    return ops[i]

# Set up the drawing window
screen = pygame.display.set_mode([1000, 1000])

vertices = []
edges = []

for i in range(random.randint(10, MAX_NODES)):
    vertices.append(i)

print("Generated vertices")

for u in vertices:
    for i in range(gen_degree()):
        v = random.randint(0,len(vertices)-1)
        if (u,v) not in edges and (v,u) not in edges and u != v:
            edges.append( (u,v) )

extra_edges = []
# # Opposite edge adding:
# for e in edges:
#     extra_edges.append( (e[1], e[0]) )
# for e in extra_edges:
#     edges.append(e)

print("Generated graph")
print(vertices)
print(edges)
locations = {}
x_step = 800 / MAX_NODES
y_step = 800 / MAX_NODES
pos_locs = []
for x in range (MAX_NODES):
    for y in range (MAX_NODES):
        pos_locs.append( (x_step*x+200, y_step*y+200) )

for v in vertices:
    i = random.randint(0,len(pos_locs))
    locations[v] = pos_locs[i]
    del pos_locs[i]

# DFS ALGO:
explored_stat = {}
for v in vertices:
    explored_stat[v] = 0

traversed_stat = {}
for e in edges:
    traversed_stat[e] = 0

def search(v):
    explored_stat[v] = 1
    for e in edges:
        if e[0] == v:
            w = e[1]
            if explored_stat[w] == 0:
                traversed_stat[e] = 1
                search(w)

def dfs_algo(V,E):
    print("STARTED")
    for v in V:
        if explored_stat[v] == 0:
            search(v)


dfs_algo(vertices, edges)
# Run until the user asks to quit
running = True

thread = Thread(target = dfs_algo, args = (1, ))
thread.start()


while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    for e in edges:
        if traversed_stat[e] == 1:
            pygame.draw.line(screen, (255,0,255), locations[e[0]], locations[e[1]], 2)
        else:
            pygame.draw.line(screen, (0,0,0), locations[e[0]], locations[e[1]], 2)        

    # Draw a solid blue circle in the center
    for vertex, cords in locations.items():
        if explored_stat[vertex] == 1:
            pygame.draw.circle(screen, (255, 0, 0), (cords[0], cords[1]), 10)
        else:
            pygame.draw.circle(screen, (0, 0, 255), (cords[0], cords[1]), 10)
    
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()