if __name__ == '__main__' :
# ini adalah jawaban nomor 3
    l1 = [2,4,3]
    l2 = [5,6,4]
    nL1,nL2 = ' ', ' '

    for i in l1[::-1]:
        nL1 += str(i)
    for j in l2[::-1]:
        nL2 += str(j)
    sumL = int(nL1) + int(nL2)
    sumLstr= str(sumL)
    sumLlist = list(sumLstr)
    sumLlist.reverse()
    print(sumLlist)

