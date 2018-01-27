inn = open("input.txt",'r')
for line in inn:
    print (float)(eval(line))
    print('\n')
inn.close()

