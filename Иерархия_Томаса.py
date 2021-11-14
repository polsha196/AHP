
while True :
    n=input("Введите количество критериев ") #проверка на то, что это число
    try:
       val=int(n)
       if int(n)>0:
            break
       else:
            raise ValueError
    except ValueError:
       print("Введено некоректное значение. Попробуйте еще раз!")
n=int(n)
tab=[[0 for k in range(n)] for kk in range(n)] #создание матрицы нулей размерностью n*n
for i in range(0,n): 
    for j in range(0,n):
        if tab[i][j] ==0:
            if i==j:#заполнение главной диагонали единицами 
                tab[i][j]=1 
            else:  #заполнение ячеек над главной диагональю
                while True:
                    print("Введите данные попарного сравнения ", i+1, " и " , j+1, "критериев")
                    coef=input()
                    try:
                        val=float(coef)
                        if float(coef)>0:
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print("Введено некоректное значение. Попробуйте еще раз!")
                tab[i][j]=float(coef)
                tab[j][i]=1/tab[i][j] #заполнение ячеек под главной диагональю
Sum=0
Sum_str=0
for i in range(0,n): #сумма всех ячеек
    for j in range(0,n):
        Sum+=tab[i][j]
for i in range(0,n): #сумма ячеек в строке
    for j in range(0,n):
        Sum_str+=tab[i][j]
    weight_coef=Sum_str/Sum
    Sum_str=0
    weight_coef='%.2f'%(weight_coef) #округление до сотых
    print("Весовой коэффициент для ", i+1 , " критерия = ", weight_coef)