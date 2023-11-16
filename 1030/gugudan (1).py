
gugudan = []
for n in range(2, 10):
    n_dan = []
    for i in range(1, 10):
        n_dan.append(n * i)
    # print(n_dan)
    gugudan.append(n_dan)

from pprint import pprint
pprint(gugudan)

def make_n_dan(n):
    n_dan = []
    for i in range(1, 10):
        n_dan.append(n * i)

    return n_dan

gugudan = []
for n in range(2, 10):
    n_dan = make_n_dan(n)
    gugudan.append(n_dan)


#  1919단
gugudan = []
for n in range(2, 20):
    n_dan = []
    for i in range(1, 20):
        n_dan.append(n * i)
    # print(n_dan)
    gugudan.append(n_dan)
# pprint(gugudan)

def make_m_m_dan(m1, m2):
    gugudan = []
    for n in range(2, m1+1):
        n_dan = []
        for i in range(1, m2+1):
            n_dan.append(n * i)
        # print(n_dan)
        gugudan.append(n_dan)
    return gugudan

pprint(make_m_m_dan(7, 9))

