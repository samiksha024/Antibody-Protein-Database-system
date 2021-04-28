import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="abdb"
)
mycursor = mydb.cursor()
def Prott():
     print("\nIt forms a complex with a PROTEIN antigen\n")
     dl=int(input("Do you want to view the file?\nEnter 1 if you want to view the complete file\nEnter 2 if you want to get specific information\nEnter 3 if you want to know about the chains\n"))
     if dl == 1:
         print("Choose a numbering scheme:\n")
         ask=int(input("\n1.Kabat\n2.Martin\n"))
         if ask == 1:
             f = open("{}_1.txt".format(log))
             print(f.read())
         if ask ==2:
             f = open("{}.txt".format(log))
             print(f.read())
                             
     if dl==2:
         print("Choose a numbering scheme:\n")
         ask=int(input("\n1.Kabat\n2.Martin\n"))
         print("Species are :")
         if ask == 1:
             f = open("{}_1.txt".format(log))
             content=f.readlines()
             print(content[12])
             print(content[14])
         if ask == 2:
             f = open("{}.txt".format(log))
             content=f.readlines()
             print(content[12])
             print(content[14])
             
     if dl==3:
         print("Choose a numbering scheme:\n")
         ask=int(input("\n1.Kabat\n2.Martin\n"))
         print("Chains are :")
         if ask == 1:
             f = open("{}_1.txt".format(log))
             content=f.readlines()
             print("Chain:")
             print(content[9])
             print("Chain:")
             print(content[11])
            
         if ask == 2:
             f = open("{}.txt".format(log))
             content=f.readlines()
             print("Chain:")
             print(content[9])
             print("Chain:")
             print(content[11])   
                    
def Nonprott():
    print("\nIt forms a complex with a NON PROTEIN antigen\n")
    dl=int(input("Do you want to view the file?\nEnter 1 if you want to view the complete file\nEnter 2 if you want to view the basic information\nEnter 3 if you want to know about the chains\n"))
    if dl == 1:
        print("Choose a numbering scheme:\n")
        ask=int(input("\n1.Kabat\n2.Martin\n"))
        if ask == 1:
            f = open("{}_1.txt".format(log))
            print(f.read())
        if ask ==2:
            f = open("{}.txt".format(log))
            print(f.read())
                             
    if dl==2:
        print("Choose a numbering scheme:\n")
        ask=int(input("\n1.Kabat\n2.Martin\n"))
        if ask == 1:
            print("Species are :")
            f = open("{}_1.txt".format(log))
            content=f.readlines()
            print(content[9])
            print(content[11])
        if ask ==2:
            print("Species are :")
            f = open("{}.txt".format(log))
            content=f.readlines()
            print(content[9])
            print(content[11])

    if dl==3:
        print("Choose a numbering scheme:\n")
        ask=int(input("\n1.Kabat\n2.Martin\n"))
        if ask == 1:
            print("Chains are :")
            f = open("{}_1.txt".format(log))
            content=f.readlines()
            print("Chain:")
            print(content[8])
            print("Chain:")
            print(content[10])
        if ask ==2:
            print("Chains are :")
            f = open("{}.txt".format(log))
            content=f.readlines()
            print("Chain:")
            print(content[8])
            print("Chain:")
            print(content[10])

def Antibodyf():
    print("\nIt is a free antibody\n")
    dl=int(input("Do you want to view the file?\nEnter 1 if you want to view the complete file\nEnter 2 if you want to view the basic information\nEnter 3 if you want to know about the chains\n"))
    if dl == 1:
        print("Choose a numbering scheme:\n")
        ask=int(input("\n1.Kabat\n2.Martin\n"))
        if ask == 1:
            f = open("{}_1.txt".format(log))
            print(f.read())
            if ask ==2:
                f = open("{}.txt".format(log))
                print(f.read())
    if dl==2:
        print("Choose a numbering scheme:\n")
        ask=int(input("\n1.Kabat\n2.Martin\n"))
        if ask == 1:
            print("Species are :")
            f = open("{}_1.txt".format(log))
            content=f.readlines()
            print(content[8])        
        if ask ==2:
            print("Species are :")
            f = open("{}.txt".format(log))
            content=f.readlines()
            print(content[8])
    if dl==3:
        print("Choose a numbering scheme:\n")
        ask=int(input("\n1.Kabat\n2.Martin\n"))
        if ask == 1:
            print("Chains are :")
            f = open("{}_1.txt".format(log))
            content=f.readlines()
            print("Chain:")
            print(content[7])
        if ask ==2:
            print("Chains are :")
            f = open("{}.txt".format(log))
            content=f.readlines()
            print("Chain:")
            print(content[7])                
while True:
    ch = int(input("\n1.Search by code\n2.Search by species\n\nPlease choose an option "))
    if ch==1:
        log =input("Enter the code value for the respective protein\n")
        sg=('{}'.format(log))
        sqq="SELECT type FROM antibodies_complex WHERE name = %s"
        dd=(sg,)
        mycursor.execute(sqq,dd)
        rows1=mycursor.fetchall()
        
        
        for x in rows1:
            if x==('Protein',):
                Prott()
                    
            elif x==('Non Protein',):
                Nonprott()
                
            elif x==('Free antibody',):
                Antibodyf()
          

    if ch==2:
        Antibody=int(input("\n1.Homo Sapiens\n2.Zaire Ebolavirus\n3.Mus Musculus\n4.Influenza A Virus\n5.Artificial Gene\n6.Camelus Dromedarius\n0.None\nPlease enter the antibody species\n"))
        Antigen=int(input("Please enter the antigen species\n"))
        if Antibody ==1 and Antigen ==2:
            log='5KEM'
            Prott()
        if Antibody ==3 and Antigen ==1:
            log='1AJ7'
            Nonprott()
        if Antibody ==1 and Antigen ==1:
            log='3HI6'
            Prott()    
        if Antibody ==1 and Antigen ==4:
            log='5K9K'
            Prott()
        if Antibody ==1 and Antigen ==5:
            log='3H3P'
            Prott()            
        if Antibody ==3 and Antigen ==3:
            print("\n2 antibodies available\n1.1A4K\n2.4FAB")
            selec=int(input("Enter your choice\n"))
            if selec ==1:
                log='1A4K'
            elif selec ==2:
                log='4FAB'
            Nonprott() 
        if Antibody ==3 and Antigen ==0:
            log='1MAJ'
            Antibodyf()
        if Antibody ==6 and Antigen ==0:
            log='1F2X'
            Antibodyf()    
           
           

