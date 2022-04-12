passwordlist= open("Passwords.txt","w+")
notes = open("Notes.txt", "w")

masterlist = [ ]
count = 1

while 1 > 0:
  selection = str(input("Welcome to BreadOfish's password manager, please select a function (type 3 to see the avalible functions): "))
  if selection == "1":
    newname = str(input("input the display name: "))
    newusername = str(input("input the username: "))
    newpasswords = str(input("input the password: "))
    #stores the info in a var
    
    confirm = [ ]
    #code addds them to a temperary list until the user confirms
    confirm.append(newname)
    confirm.append(newusername)
    confirm.append(newpasswords)
    print("Is this info corrrect?")
    print(confirm)
    confirm1 = str(input('Confirm(Y/N): '))
    if confirm1 == "Y" or "y":
      print("-------------------")
      masterlist.append(confirm)
      File = open("Passwords.txt", "w")
      File.writelines('|')
      File.writelines(confirm)
      File.close() 
      print("current list")
      print(masterlist)
    elif confirm1 == "N" or "n": 
      print("returning")
      break
    else: 
      print("That is not an valid option")
 
  if selection == "2":
    print("current saved passwords are:")
    print(masterlist)
  
  if selection == "3":
    print("input 1 to create a new listing")
    print("--------------------------------------")
    print("input 2 to view the current list")
  if selection == "delete":
    print(masterlist)
    remove = input("please input the number of the password you would like to remove (reminder 1 is 0 in python")
    masterlist.remove(remove)
    print("the new list is" + remove)
  if selection == "4":
    print("Insert text below")
    note = str(input(" "))
    print("saving")
    Notes = open("Notes.txt", "w")
    Notes.writelines('|')
    Notes.writelines(note)
    Notes.close() 
    print("Done")