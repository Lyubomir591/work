with open("my_file.txt", 'w') as my_file:
    arg = [ str(i) + " " for i in range (1,101)]
    
    my_file.writelines(arg)












