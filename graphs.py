#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import time

def adj_list ():
    start = time.time()
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)  # 有向グラフなら消す
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
    print (sys.getsizeof(graph))
    #print(graph)

def adj_list_weight ():
    start = time.time()
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u-1].append((v-1, w))
        graph[v-1].append((u-1, w))  # 有向グラフなら消す
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
    print (sys.getsizeof(graph))
    #print(graph)

def adj_mtx ():
    start = time.time()
    n, m = map(int, input().split())
    graph = [[0]*n for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a-1][b-1] = 1
        graph[b-1][a-1] = 1  # 有向グラフなら消す
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
    print (sys.getsizeof(graph))
    #print(graph)

def adj_mtx_weight ():
    start = time.time()
    n, m = map(int, input().split())
    graph = [[0]*n for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u-1][v-1] = w
        graph[v-1][u-1] = w  # 有向グラフなら消す
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
    print (sys.getsizeof(graph))
    #print(graph)

def adj_dict ():
    start = time.time()
    n, m = map(int,input().split())
    graph = {}
    for i in range(1,n+1):
        graph[i] = []
    for _ in range(m):
        a, b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a) # 有効グラフなら消す
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
    print (sys.getsizeof(graph))
    #print(graph)

def adj_dict_weight ():
    start = time.time()
    n, m = map(int,input().split())
    graph = {}
    for i in range(1,n+1):
        graph[i] = []
    for _ in range(m):
        u, v, w = map(int,input().split())
        graph[u].append((v,w))
        graph[v].append((u,w)) # 有効グラフなら消す
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
    print (sys.getsizeof(graph))
    #print(graph)

"""
試したいグラフ取得処理を以下で実行する
./graphs.py < ${graphfile}
"""
#adj_list()
#adj_list_weight()
#adj_mtx()
#adj_mtx_weight()
#adj_dict()
#adj_dict_weight()
