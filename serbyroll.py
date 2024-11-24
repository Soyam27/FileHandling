#part-1: to enter records:
import pickle
def input_():
        global x
        try:
            x = int(input("how many records:"))
            main()

        except Exception as e:
            print(e)
        input_()
    

def main():
    l=[]
    for i in range(0,x):
        a = input("enter your name:")
        b = input("enter your roll number")
        l.append([a,b])
        f = open("file.dat","wb+")
        pickle.dump(l,f)
        f.close()

    #part-2: roll number check:
    f = open("file.dat","rb+")
    s= pickle.load(f)
    f.close()
    print(s)
    y = input("enter roll num to be searched:")
    c = None
    for i in s:
        if i[1]==y:
            print(i[0])
            c = True
            break
        else:
            c = False
    if c is False:
        print("roll num not found")
input_()
        
