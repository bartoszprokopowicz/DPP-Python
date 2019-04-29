from event import Event
import datetime
from datetime import timedelta
import os
import sys

events = []
year = 0
month = 0
day = 0
offset = 0
note = ""

def test():
    print("Hello World!")

def sort():
    events.sort(key=lambda x: x.date, reverse=False)

def addEvent():
    os.system('clear')
    print("addEvent")
    try:
        year = int(input("Podaj rok: "))
        month = int(input("Podaj miesiąc: "))
        day = int(input("Podaj dzień: "))
        date1 = datetime.date(year, month, day)
        note = str(input("Podaj notatke: "))
        event = Event(date1, note)
        events.append(event)
    except ValueError:
        print("Podano błędne liczby")
    else:
        os.system('clear')
        print("Dodano notatke!")
    sort()

#removes element in array which contains same date
def removeEvent():
    tempArray = events.copy()
    events.clear()
    os.system('clear')
    print("removeEvent")
    try:
        year = int(input("Podaj rok: "))
        month = int(input("Podaj miesiąc: "))
        day = int(input("Podaj dzień: "))
        date1 = datetime.date(year, month, day)
    except ValueError:
        print("Podano błędne liczby")
    else:
        os.system('clear')
    
    for x in tempArray:
        if date1 != x.date:
            events.append(x)
            print("Usunięto notatkę!")
    sort()


def printEvents():
    for event in events:
        print(str(event.date) + " " + str(event.note))

def futureEvent():
    print("futureEvent")
    try:
        year = int(input("Podaj rok: "))
        month = int(input("Podaj miesiąc: "))
        day = int(input("Podaj dzień: "))
        offset = int(input("Podaj ilość dni do przodu do przeszukania: "))
        date1 = datetime.date(year, month, day)
        date2 = date1 + timedelta(days=offset)
    except ValueError:
        print("Podano błędne liczby")
    else:
        os.system('clear')
    for event in events:
        if event.date >= date1 and event.date <= date2:
            print(str(event.date) + " " + str(event.note))

def choose(arg):
    if arg == '1':
        addEvent()
    elif arg == '2':
        removeEvent()
    elif arg == '3':
        futureEvent()
    elif arg == '4':
        printEvents()
    elif arg == '5':
        sys.exit(0)

def mainLoop():
    while True:
        print("Menu")
        print("Podaj jaką chcesz wykonać akcję:")
        print("1.Dodaj wydarzenie")
        print("2.Usuwanie wydarzeń z danego dnia")
        print("3.Co kryje przyszłość?")
        print("4.Pokaż wydarzenia")
        print("5.Wyjdź")
        choose(input("Opcja: "))

def main():
    mainLoop()

if __name__== "__main__":
    main()