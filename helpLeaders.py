
#función que reciba los argumentos y los temas
from pickle import TRUE


def main():
    #FROM HERE UNTIL LINE 35: INPUT PART
    n=int(input())
    used=[]
    toPrint=[]
    nCounter= 1
    while nCounter<=n: #OJO: DELIMITAR LAS VARIABLES
        aux= input().split()
        t= int(aux[0])
        p= int(aux[1])
        s= int(aux[2])
        #Cicle for the topics input
        topicsList= []
        while t>0:
            topicsList.append(input().strip().upper())
            t=t-1
        #Cicle for the prohibited pairs
        prohibitedSet=[]
        while p>0:
            splittedVar=input().strip().upper().split() #This variable will save two words that should not be together
            splittedVar.sort()
            splittedVar.sort(key = len, reverse=True)
            #The next list is saving the tuples s-tuples combitations of the previous words and the s-tuples with the same words
            #splittedList=permutation(splittedVar)
            #This loop is converting each s-tuple of splittedList to a string separated by empty spaces and saving them in the
            # prohibitedList.
            prohibitedSet.append(' '.join(splittedVar))
            p=p-1
        # INPUT PART ENDS HERE AND PROCESSING PART STARTS IN THE LINE BELOW
        '''
        See "The sorting method" numeral for further explanation about the sorter.
        '''
        topicsList.sort()
        topicsList.sort(key = len, reverse=True)

        #The lines 46 and 48 are in charge of the titles of each set and the line scape at the end of them
        used.append('Set '+str(nCounter)+':')
        used=generator(topicsList, s, prohibitedSet, used)
        used.append('')

        nCounter+=1

    printer(used)

def generator(tl, s, banned, used):
    outter=[]
    if s==1:
        while len(tl)>0:
            used.append(tl.pop(0))
        return used
    if s==2:
        '''
        In this if and the next one, what I do is to make a kind of pop (save the head and then remove it)
        so it won't repeat again in the next loops, because each loop makes all the possible permutations
        for that head, so is not necessary that ir remains in the list. More over, each loops iterates over
        a list that, of course, does not include the head: We have a list of 8 elementes (1-8), the 
        firstWord variables save the element [1], then the code remove it from the list (list = 2-8) and will
        start iterating over it; when the loop ends, we do the same with the remaining list: we take its head
        in firstWord=2 and when we remove the element from the list, it looks like list=3-8 and repeat the 
        process. This mechanism assures that there will not be repetitions of any kind.

        THE BACKTRACKING MECHANISM: Having the list of banned s-tuples, when the code creates a new s-tuple, 
        it compares it with all the elements of the banned list with the 'not in' command, if the s-tuple does not
        appears in 'banned' the it will be concatenated to the 'used' list and then the combination that makes the 
        s-tuple posible will be removed; on the contrary, if it finds that the s-tuple appears in the banned list, 
        it would not be stored and the combination that makes the s-tuple posible will be removed.
        '''
        while len(tl)>=s:
            firstWord=tl.pop(0) #The last tl word is the longest one, so I will start from here
            
            #The remaining list will be duplicated so I can manipulate to rotate the words and make the n-tuples.
            auxList=tl.copy()
            while len(auxList)>0:
                #The next variable concatenates the first word with the first incomplete set of auxList
                comparator=firstWord+" "+auxList[0]
                if comparator not in banned:
                    used.append(comparator)
                auxList.pop(0)
                
    else:
        outter=used.copy()
        while len(tl)>=s:
            used.clear()
            firstWord=tl.pop(0) #The last tl word is the longest one, so I will start from here
            #The remaining list will be duplicated so I can manipulate to rotate the words and make the n-tuples.
            auxList=tl.copy()
            auxList2=used.copy()
            #The next variable is the list of n-tuples that ver previously created by recursion
            prevList=generator(auxList, s-1,banned, auxList2).copy()

            while len(prevList)>0:
                #The next variables saves the generated permutation so it can be compared to the banned pairs
                generated=firstWord+" "+prevList[0]
                
                if  comp(generated, s, banned):
                    outter.append(generated)
                prevList.pop(0)
        used=outter.copy()
    return used
               
'''
This method was created based on Pablo Maya's comp Method; I have his permission'''
def comp(A, s, banned):
    for p in banned:
        z = p.split(" ")
        if (z[0] + " ") in (A + " ") and (z[1] + " ") in (A + " "):
            return False
    return True # It's valid

# The goal of this method is to organize the output
def printer(used):
    s = "\n".join(used)
    print(s)
    used.clear()

main()