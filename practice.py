
def filesystem():
    with open("C:/PythonCourse/practicefile.txt","r") as fp:
        l=fp.readlines()
        for i in l:
            print(i)
        k=[]
        for i in l:
            x=i[:len(i)-1]
            k.append(list(map(int,x.split(","))))

        k.sort(key=lambda x:x[3],reverse=True )

        print(k)

        k2 = [i[0] for i in k]

        print(k2)


def main():
    filesystem()


if __name__=="__main__":
    main()

