import sys
 
def initial_phonebook():
     rows,cols=int(input("enter initial rows of your contacts" )),5
     phonebook=[]
     print(phonebook)
     for i  in range (rows):
          print("\nEnter contact %d details in the following order (ONLY):"% (i+1))
          print("NOTE: * indicates mandatory fields")
          print("....................................................................")
          temp=[]
          for j in range (cols):  
                if j==0:
                    temp.append(str(input("Enter Name*: ")))
                    if temp[j]==''or temp[j]=='':
                          sys.exit("Name is a mandatory field. Exiting the program.")
                if j==1: 
                                temp.append(str(input("Enter Phone Number*: ")))
                                if temp[j]==''or temp[j]==' ':
                                     sys.exit("Phone Number is a mandatory field. Exiting the program.")
                if j==2:                  
                                temp.append(str(input("Enter email Address: ")))
                                if temp[j]==''or temp[j]=='':
                                        temp[j]=None
                                        
                                            
                if j==3:             
                              temp.append(str(input("Enter (dd/mm/yyyy): ")))
                              if temp[j]==''or temp[j]==' ':
                                     temp[j]=None
                if j==4:
                                temp.append(str(input("family/friends/other: ")))
                                if temp[j]==''or temp[j]==' ':
                                         temp[j]=None                    
     phonebook.append(temp)
     print(phonebook)          
     return phonebook     
