#break - se encarga de detener procesos

for i in range (1, 6):
    if i ==3:    #el 3 se encarga de detener
        break
    print ("Inside the loop.", i)
print ("Outside the loop.")
