import sys
import os
import random
from datetime import datetime
import FileReader as fr
import Score

if __name__ == '__main__':
    # readfile_1 = sys.argv[1]
    # readfile_2 = sys.argv[2]
    readfile_1 = "seq1.fasta"
    readfile_2 = "seq1.fasta"
    genome1, name1 = fr.readFastA(readfile_1)
    genome2, name2 = fr.readFastA(readfile_2)

    len1 = len(genome1)
    len2 = len(genome2)
    i = 0;
    j = 0
    s1 = genome1[0]
    s2 = genome2[0]
    # print(s1,s2)

    D = [[0 for j in range(0, len(s2) + 1)] for i in range(0, len(s1) + 1)]
    print(D)
    D = Score.score(s1, s2)
    for i in range(0, len(s1) + 1):
        for j in range(0, len(s2) + 1):
            print(D[i][j], end=' ')
        print('\n')
    print("Score: ", D[len(s1)][len(s2)])

    x, y = Score.dfs(D, s1, s2)
    print(f"Elso fos: {x}")
    print(f"Masodik fos: {y}")
    # i = len(s1)
    # j = len(s2)
    # while i != 0:
    #     while j != 0:
    #         if()

    # D = []
    # for i in range(len(s1)):
    #     D.append([0]*(len(s2)))
