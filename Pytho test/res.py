with open("my_file.txt",'r+' ) as obj :
     arr = obj.readlines()
     arrg = []
     def sorti (arg):
        arr_sort = arg[0].split(' ')
        for i in range(len(arr_sort) - 1):
            arrg.append(int(arr_sort[i]))  
     sorti (arr)
      
     list_sort = [(i , i**2 ) for i in arrg if i%2 ]
     arg = [ str(i)   for i in list_sort]  
     obj.seek(0) 
     for i in arg:
         obj.write( i + '\n')       
     print(arg)







