#Νικόλαος Φουρτούνης
#icsd13195

__author__ = "NFourtounis"
__date__ = "$Mar 30, 2018 7:26:32 PM$"

def isInt(character):#Function που ελέγχει αν ένας χαρακτήρας είναι int
    try:#Αν παίζει το try χωρίς να πετάξει error η int() πάει να πει ότι ο χαρακτήρας είναι int
        int(character)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    str1=input('Enter a string:')#Ζητάω από τον χρήστη ένα string
    str2=""
    for i in range(0,len(str1),1):#Περνάω κάθε χαρακτήρα του string 
        if(isInt(str1[i])):# Αν βρω integer
            str2+=str1[i+1]*(int(str1[i])-1)#προσθέτω στο δεύτερο string, τον χαρακτήρα μετά τον int
                                            #έτσι ώστε να προσθέσω τόσα γράμματα όσο το νούμερο
        else:#αλλιως προσθέτω στο δεύτερο string, το μοναδικό γράμμα που βρήκα
            str2+=str1[i]
    print(str2)#Εκτυπώνω το string