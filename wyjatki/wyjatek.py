
def dzialanie():
    a = 10
    b = 20
    c = 10
    
    d = (a +b) / c
    print(d)

dzialanie()    # 3

def dzialanie():
    try:
        a = 10
        b = 20
        c = 0

        d = (a +b) / c
        print(d)
    except ZeroDivisionError:
        print('Nie może być zero') 
        #raise Exception('To jest wywołany błąd')       
    except TypeError:
        print('Nie ten typ danych')  
    else:
        print('Bo nie ma wyjątku')   
    finally:
        print('Zawsze się wykonam')                    

dzialanie()    