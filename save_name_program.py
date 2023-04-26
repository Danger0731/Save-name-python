import time
Saved_Names=[]
Delete_slot=0
i=0
while(i<1):
  abc=float(input("Save names, Check names or Delete names? (1/2/3)"))
  if abc == 1:
    Num_names=int(input("Numbers of names you want to save: "))
    while(Num_names!=0):
      Name_input=input("Name that you want to save:")
      Saved_Names.append(Name_input)
      print("The name \""+str(Name_input)+"\" has been saved successfully")
      Num_names=Num_names-1
  elif abc == 2:
    if bool(Saved_Names)==False:
      print("No names has been saved.")
    else:
      print("The names are: "+str(Saved_Names))
  elif abc == 3:
    Deleted_name=input("Which name do you want to delete? (Please check the name before deleting)(Type Delete all to Delete all)")
    if Deleted_name=="Delete all":
      Rusure=input("Are you sure? (Yes/No)")
      if Rusure=="Yes":
        Saved_Names=[]
        print("Cleared successfully")
      else:
        print("Action stopped")
    elif Deleted_name in Saved_Names:
      Saved_Names.remove(Deleted_name)
      print("The name \""+str(Deleted_name)+"\" has been deleted successfully.")
    else:
      print("The name \""+str(Deleted_name)+"\" is not in the list.")
  elif abc==5:
    print("Loading...")
    print("Please wait")
    time.sleep(2)
    Stopping=input("Are you sure? (Saved names will be cleared) (Yes/No)")
    if Stopping == "Yes" or Stopping == "yes":
      print("Stopping...")
      time.sleep(2)
      break
    elif Stopping == "No" or Stopping == "no":
      print("Reverting...")  
    else:
      print("Error")
  else:
    print("Error")
