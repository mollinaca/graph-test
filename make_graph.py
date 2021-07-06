#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ランダムのグラフのinputサンプルを作るスクリプト
"""
print ("node : ",end="")
n = int(input())
print ("path : ",end="")
m = int(input())
print ("weight[y/n] : ",end="")
x = input()
if x == "y":
    _weight = True
else:
    _weight = False
print ("filename : ",end="")
filename = input()
if _weight:
    filename = "graphs/" + filename + "_weight" + ".txt"
else:
    filename = "graphs/" + filename + ".txt"

c = 0
graph_d = {} # 生成されたグラフの管理（有向扱いする）
graph = []   # 出力するグラフ情報
for i in range(1,n+1):
    graph_d[i] = []
import random

while True:

    if c == m:
        break
    
    u = random.randint(1,n)
    v = random.randint(1,n)

    if u == v:
        continue

    if v in graph_d[u]:
        continue

    graph_d[u].append(v)
    graph_d[v].append(u)

    if _weight:
        w = random.randint(1,n)
        print (u,v,w)
        graph.append((u,v,w))
    else:
        print (u,v)
        graph.append((u,v))

    c += 1

with open(filename, mode='a') as f:
    f.write(str(n)+" "+str(m)+"\n")
    for g in graph:
        if _weight:
            f.write(str(g[0])+" "+str(g[1])+" "+str(g[2])+"\n")
        else:
            f.write(str(g[0])+" "+str(g[1])+"\n")
