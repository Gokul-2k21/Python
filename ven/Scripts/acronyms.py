def addacronym():
    acronynm = input('What is the Acronym to be added ? \n')
    fullform=input('What is the full definition ? \n')
    with open('SOFTWARE-acronymns.txt','w') as file :
        file.write(acronynm+' - '+fullform)

def findacronym():
    search = input('What acronym to be searched ? \n')
    with open('SOFTWARE-acronymns.txt','r') as file :  #IF FILE NOT THERE, AUTOMATICALY CREATES FILE
        for line in file.readlines():
            if search in line :
                print(line)
                break

def main():
    addacronym()
    findacronym()

main()