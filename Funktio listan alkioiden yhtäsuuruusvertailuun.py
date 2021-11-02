"""
COMP.CS.100 Funktio listan alkioiden yhtäsuuruusvertailuun?
Creator: Onni Ahonen
Student id number: 150641526
"""
import numpy

def are_all_members_same(*num):
    """returns false if one is not the same else true"""
    y = 0
    #len(a[0] != 1)
    #if len(numpy.shape(num)) == 2:
    try:
        if len(num[0]) != 1:
            check = num[0][0]
            for i in range(len(num[0])):
                if check == num[0][i]:
                    y += 1
                else: 
                    return False
    except:
        check = num[0]
        for i in range(len(num)):
            if check == num[i]:
                y += 1
            else: 
                return False

    if y > 0:
        return True

def main():
    """main 123456789 123456789 123456789"""
    x = are_all_members_same(5, 5, 5, 5, 5, 5, 5, 5, 5)
    print(x)

if __name__ == "__main__":
    main()
