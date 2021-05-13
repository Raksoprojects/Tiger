#Oskar Fąk 175984
#Współczesne narzędzia obliczeniowe
#Wykonałem:
#Generowanie tygrysów przy użyciu klasy 'Tygrys' (1pkt + *1pkt)
#Zaimplementowanie algorytmu Jarvisa(2pkt)
#Utworzenie elips wokół 'tygrysów' i modyfikacja algorytmu Jarvisa(2pkt)
#Brak dodania kroku czasowego i animacji

import numpy as np
from matplotlib import pyplot as plt 

class Tygrys:
    '''
    Klasa tygrys, współrzędne tygrysa oraz parametry elipsy
    '''
    def __init__(self,x=0.,y=0.,a=0.,b=0.):
        self.x = x
        self.y = y
        self.a = a
        self.b = b

    def drawElipse(self): #funckja rysująca elipsę wokół 'tygrysa'
        t = np.linspace(0,2*np.pi,200)
        x_t = self.a*np.cos(t)+self.x
        y_t = self.b*np.sin(t)+self.y
        plt.plot(x_t, y_t, 'r')  

def leftturn(a, b, c, t_x, t_y):
    '''
    Funkcja sprawdzająca czy punkt jest po lewej od wektora, liczenie wyznacznika
    '''
    return ((b.x - a.x)*(c.y - a.y) - (b.y - a.y)*(c.x - a.x)) > 0

def radiany(center,x,y):
    '''
    Funkcja licząca kąt od centroidu do tygrysa
    '''
    delta_x = x - center[0]
    delta_y = y - center[1]
    theta = np.arctan2(delta_y,delta_x)
    return theta

def centroid(X,Y):
    '''
    Wyliczanie środka ciężkości wszystkich tygrysów
    '''
    c_x = np.sum(X)/len(X)
    c_y = np.sum(Y)/len(Y)
    return [c_x,c_y]    
    
def Jarvis(tygrysy,center):
    '''
    Implementacja algorytmu Jarvisa, poszukiwanie punktu najbardziej od lewej
    i dodawanie na stos następnych granicznych punktów
    '''
    stack = []
    p0 = min(tygrysy, key = lambda tygrys: (tygrys.x - tygrys.b)) #szukanie minimalnego punktu
    i = 0
    #Pętla którą kończy warunek zamknięcie otoczki, tzn. kiedy następny wybrany punkt
    #będzie pierwszym punktem na stosie
    while(True):
        stack.append(p0)
        endpoint = tygrysy[0]
        #pętla for przechodząca przez całą liste tygrysów i wybierające odpowiednie punkty
        for j in range(len(tygrysy)):
            #liczenie współrzędnych elipsy wokół tygrysa
            t = radiany(center, tygrysy[j].x, tygrysy[j].y)
            t_x = tygrysy[j].a * np.cos(t)
            t_y = tygrysy[j].b * np.sin(t)
            #warunek sprawedzający czy endpoint jest taki jak punkt p0 i czy punkt jest po lewej
            #od wektora łączącego endpoint i następnego tygrysa
            if(endpoint == p0 or leftturn(stack[i], endpoint ,tygrysy[j], t_x, t_y)):
                endpoint = tygrysy[j]
        i = i+1
        p0 = endpoint
        #zwraca stos punktów jeśli wroci do początku
        if(endpoint == stack[0]):
            return stack


if __name__ == "__main__":

    #deklarowanie list
    tygrysy = []
    X = []
    Y = []
    punktyX = []
    punktyY = []
    #generowanie losowych współrzędnych i parametrów elipsy oraz
    #dodawanie tygrysów do listy tygrysów
    for i in range(20):
        x=np.random.uniform(0,100)
        y=np.random.uniform(0,100)
        a=np.random.uniform(1,3)
        b=np.random.uniform(1,3)
        tygrys = Tygrys(x,y,a,b)
        tygrysy.append(tygrys)
        punktyX.append(x) #pomocnicza lista by łątwiej rysować 'tygrysy'
        punktyY.append(y) #jak wyżej 
        tygrys.drawElipse()
    
    center = centroid(punktyX,punktyY) #wyliczanie i rysowanie centroidu
    plt.scatter(center[0],center[1])
    stack = Jarvis(tygrysy,center) #utworzenie stosu, wywołanie funkcji Jarvis
    
    #Dodanie współrzędnych zewnętrznych tygrysów do list, by móc je narysować
    for tygrys in stack:
        t = radiany(center, tygrys.x, tygrys.y)
        t_x = tygrys.a * np.cos(t)
        t_y = tygrys.b * np.sin(t)
        X.append(tygrys.x + t_x)
        Y.append(tygrys.y + t_y)
    
    t = radiany(center, stack[0].x, stack[0].y)
    t_x = stack[0].a * np.cos(t)
    t_y = stack[0].b * np.sin(t)    
    X.append(stack[0].x + t_x) #pomocnicze punkty na koniec listy
    Y.append(stack[0].y + t_y) #w celu zamknięcia krzywej   
    plt.scatter(punktyX,punktyY)      
    plt.plot(X,Y)
    plt.show()             