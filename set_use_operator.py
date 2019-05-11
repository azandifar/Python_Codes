def define_matrix():
    mat=[]
    for i in range(2):
        t=[]
        for j in range(2):
            t.append(int(input()))
        mat.append(t)
    return mat

m1 = define_matrix()
m2 = define_matrix()
m3 =[]
for i in range(2):
    t=[]
    for j in range(2):
        t.append(m1[i][j]+m2[i][j])
    m3.append(t)
#for x in m3:
#    print(x)
print(print(*m3))