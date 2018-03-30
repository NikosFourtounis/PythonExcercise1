__author__ = "NFourtounis"
__date__ = "$Mar 30, 2018 7:26:32 PM$"

def isInt(character):
    try:
        int(character)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    #str1=input('Enter a string:')
    str1="3t4m6i3ry2j"
    str2=""
    print(len(str1))
    for i in range(0,len(str1),1):  
        if(isInt(str1[i])):
            #print(str1[i+1]*int(str1[i]))
            str2+=str1[i+1]*(int(str1[i])-1)
        else:
            str2+=str1[i]
    print(str2)