import time
import random
import math

speedL =1
armorL = 1

Throttle = 100
MAXspeed = 50 + speedL*50
maksymalnaWysokosc = 3400
iteracje = 0
IloscZrobionychMisji = 0
pitch = 0
money=1500
plane = 0
level = 0
damage=20
armor=10
speed=50
health=100
#poziomy = ['W hangarze', 'Las', 'Miasto', 'Pustynia', 'Góra', 'Morze']
#mapa = "Mapa bitwy: \n1. " + poziomy[0] + " \n2. " + poziomy[1] + " \n3. " + poziomy[2] + " \n4. " + poziomy[3] + " \n5. " + poziomy[4]
lenght = 2400
X = 0
Y = 2000  



def dystans():
    return(lenght -X/100)
    
def clear():
    print("\n" * 100)
print("Witaj w grze! Twoim zadaniem jest Bezpiecznie Dolecieć do celu. Powodzenia!")
def staty():
    print("Twoje statystyki:")
    print("Poziom:", level)
    #print("Obrażenia:", damage)
    print("Pancerz:", armor)
    print("Szybkość:", speed)
    print("Zdrowie:", health)


listaMisji=[f'Misja 1 : Pozostań na wysokośći ponad Y3000', f'Misja 2 : Ulepsz silnik do poziomu 3', f'Misja 3 : Ulepsz pancerz do poziomu 3', f'Misja 4 : Poleć mniej niż 100 metrów nad ziemią bez rozbicia się']
nagrodaMisji = 3000
numerMisji = 0
def sprawdzCzyMisjaZrobiona():
    global numerMisji, IloscZrobionychMisji
    if numerMisji == 0:
        if Y > 3000:
            print("Ukończyłeś misję: Pozostań na wysokośći ponad Y3000")
            IloscZrobionychMisji += 1
            numerMisji += 1
    elif numerMisji == 1:
        if speedL >= 3:
            print("Ukończyłeś misję: Ulepsz silnik do poziomu 3")
            IloscZrobionychMisji += 1
            numerMisji += 1
    elif numerMisji == 2:
        if armorL >= 3:
            print("Ukończyłeś misję: Ulepsz pancerz do poziomu 3")
            IloscZrobionychMisji += 1
            numerMisji += 1
    elif numerMisji == 3:
        if Y < 100:
            print("Ukończyłeś misję: Poleć mniej niż 100 metrów nad ziemią bez rozbicia się")
            IloscZrobionychMisji += 1
            numerMisji += 1
    elif numerMisji >= len(listaMisji):
        print("Ukończyłeś wszystkie misje! Gratulacje!")



'''
print('wybierz co chcesz zrobić: 1. Zacznij bitwę 2. Zobacz statystyki 3. Ulecz się 4. Ulepsz broń 5. Ulepsz pancerz 6. Ulepsz silnik')
x = input("Wybierz opcję: ")
if x == "1":
    print(mapa)
    print('obecny poziom:', poziomy[level],'\n następny poziom:', poziomy[level+1])
    time.sleep(2)
    print("Rozpoczynasz bitwę...")
    time.sleep(2)
    clear()
elif x == "2":
    staty()'''

start = time.time()


def potwierdzenie(cena,rzecz):
    global money
    print(f"Czy chcesz kupić {rzecz} za {cena} $?")
    opcja = input("Wybierz opcję: tak(Y) nie(N) ")
    if opcja.lower() == "y":
        if money >= cena:
            money -= cena
            print("-" * 50)
            print(f"Kupiłeś {rzecz} za {cena} $. Pozostało Ci {money} $.\n")
            input("\nNaciśnij Enter, aby kontynuować...")
            return True
        else:
            print("-" * 50)
            print("Nie masz wystarczająco pieniędzy, aby dokonać tej transakcji.\n")
            input("\nNaciśnij Enter, aby kontynuować...")
            return False
    elif opcja.lower() == "n":
        print("Nie kupiłeś tej rzeczy.")
        return False




def panel():
    clear()
    print(f"Odległość do celu: {round(dystans())} km \nZdrowie: {health} \nSzybkość: {speed} km/h\nPieniądze: {money} $ \n\n Kordynat(w metrach): X: {round(X)} Y: {round(Y)} \n Nachylenie: {pitch}°, \n Throttle: {Throttle}%")

    sprawdzCzyMisjaZrobiona()
    nagrodaMisji = 3000 + IloscZrobionychMisji*1000
    print(f'\nOBECNA MISJA:' + listaMisji[numerMisji], '\nNagroda za ukończenie: ' + str(nagrodaMisji) + ' $')
    print(f'\nDane Techniczne: (Poziom silnika: {speedL}) (Poziom pancerza: {armorL}) (maksymalna wysokosc): {maksymalnaWysokosc}\n (Maksymalna Prędkość: {MAXspeed} km/h)')
    print("-" * 50)

def dalej():
    global speed
    #if speed <MAXspeed: #throtla
    speed+= speedL*Throttle/50
    if Throttle<50:
        speed-= speedL*(100-Throttle)/50
    speed = speed - (pitch/20)/((speedL+1)/3)#pitch
    #if speed> MAXspeed: #drag
    speed -= speed/100
    speed = round(speed,2)
    
    global X, Y
    # wzór od wikipedii
    rad = math.radians(pitch)

    # pozycjeee x i y
    X += speed * math.cos(rad)
    Y += speed * math.sin(rad)

def poradnik():
    global lenght, speedL ,armorL ,Throttle ,MAXspeed ,maksymalnaWysokosc ,iteracje ,IloscZrobionychMisji ,pitch ,money ,damage ,armor, speed ,health ,X ,Y
    clear()
    print(f"Poradnik do gry:\n\nTwoim zadaniem jest bezpiecznie dolecieć do celu, odległość kilometrów od celu ustalisz zaraz po przeczytaniu poradnika. Musisz zarządzać swoim samolotem, ulepszać go i unikać zagrożeń, aby osiągnąć sukces.\n\n1. Zarządzanie prędkością: Używaj Throttle, aby kontrolować prędkość swojego samolotu. Pamiętaj, że zbyt wysoka prędkość może prowadzić do rozbicia, a zbyt niska może spowodować utratę kontroli.\n\n2. Ulepszanie samolotu: Inwestuj w ulepszenia silnika i pancerza, aby zwiększyć swoje szanse na przetrwanie i dotarcie do celu.\n\n3. Unikanie zagrożeń: Bądź czujny na ataki przeciwników i staraj się naprawiać swój samolot, aby nie stracić zdrowia.\n\n4. Wykonywanie misji: Ukończenie misji pozwoli Ci zdobyć dodatkowe pieniądze, które możesz przeznaczyć na ulepszenia.\n\nPowodzenia w grze!")
    print("Ustaw długość trasy (w km): ")
    user_input = input('Dla Nie zdecydoowanych : [Łatwe-500, Normalne-2400, Exstrymalne-5000]  ')
    try:
        lenght = int(user_input)    
    except ValueError:
        s = user_input.strip().lower()
        if s in ("łatwe", "latwe"):
            lenght = 500    
        elif s == "normalne":
            lenght = 2400
        elif s in ("ekstremalne", "ekstrymalne"):
            lenght = 5000
        else:
            print("Nieprawidłowy wybór, ustawiono na Normalne (2400 km).")
            lenght = 2400

    print("Wybierz samolot: \n1. Samolot 1 (Szybki, ale słaby pancerz) \n2. Samolot 2 (Zbalansowany) \n3. Samolot 3 (Wolny, ale mocny pancerz)")
    plane = input("Wybierz samolot (1, 2, 3): ")
    if plane == "1":
        speedL = 2
        armorL = 1
    elif plane == "2":
        speedL = 1
        armorL = 1
    elif plane == "3":
        speedL = 1
        armorL = 2
    else:
        print("Nieprawidłowy wybór, ustawiono na Samolot 2 (Zbalansowany).")
        speedL = 1
        armorL = 1

    input("\nNaciśnij Enter, aby rozpocząć grę...")

    Throttle = 100
    MAXspeed = 50 + speedL*50
    maksymalnaWysokosc = 3400
    iteracje = 0
    IloscZrobionychMisji = 0
    pitch = 0
    money=1500
    damage=20
    armor=10
    speed=50
    health=100

    X = 0
    Y = 2000  

poradnik()













while dystans() > 0 and health > 0 and Y>0 and Y < maksymalnaWysokosc and speed < MAXspeed+100 and speed > 25:
    iteracje += 1
    money+=1
    panel()
    print("Wybierz co chcesz zrobić: (ENTER. Lecieć dalej) (1. Napraw samolot) (2. Ulepsz pancerz) (3. Ulepsz silnik) (4. Zmień Kierunek)\n (5.Zmień moc silnika) (6.PORADNIK[po wybraniu zaczynasz od nowa])")
    e =input("Naciśnij Enter (Przytrzymaj aby przyśpieszyć), aby Lecieć dalej...")
    if e == "":
        pass
    elif e == "1":
        cena = (100 - health) * 2/armorL
        cena = round(cena)
        if potwierdzenie(cena,"naprawa samolotu"):
            health =100
            print("Naprawiłeś samolot! Zdrowie zostało przywrócone.")
        else:
            print("Nie masz wystarczająco pieniędzy, aby naprawić samolot.")
    elif e == "2":
        cena= 100*(armorL**2 + armorL) / 2
        cena = round(cena)
        if potwierdzenie(cena,"ulepszenie pancerza"):
            if money >= cena:
                armor += 10
                armorL += 1
                money -= cena
                print("Ulepszyłeś pancerz! Pancerz został zwiększony o 5.")
            else:
                print("Nie masz wystarczająco pieniędzy, aby ulepszyć pancerz.")
                input("\nNaciśnij Enter, aby kontynuować...")
    elif e == "3":
        cena= 100*(speedL**2 + speedL) / 2
        cena= round(cena)
        if potwierdzenie(cena,"ulepszenie silnika"):
            if money >= cena:
                
                speed += 10
                speedL += 1
                MAXspeed = 100 + speedL*100
                maksymalnaWysokosc = 3400 + 1500*(speedL**2 + speedL) / 2
                money -= cena
                print("Ulepszyłeś silnik! Szybkość została zwiększona o 5 km/h.")
            else:
                print("Nie masz wystarczająco pieniędzy, aby ulepszyć silnik.")
    elif e == "4":
        pitch = int(input('Ustaw kąt nachylenia (90, -90): '))
        if pitch > 90 or pitch < -90:
            print("Nieprawidłowy kąt nachylenia. Ustawiono na 0.")
            pitch = 0
            input("Naciśnij Enter, aby kontynuować...")
    elif e == "5":
        Throttle = int(input('Ustaw moc silnika (0-100): '))
        if Throttle > 100 or Throttle < 0:
            print("Nieprawidłowa moc silnika. Ustawiono na 100.")
            Throttle = 100
            input("Naciśnij Enter, aby kontynuować...")
    elif e == "6":
        poradnik()
        continue


    if random.random() < 0.1:  # 10% 
        clear()
        print("Atak przeciwnika!")
        print('-'* 50)
        print(f'Pancerz oszczędzil ci {round(armor/3)} uszkodzenia.')
        damage_taken = max(0, 10 - round(armor/3))  #  obrażenia po pancerzu
        health -= damage_taken
        print(f"Zostałeś trafiony! Straciłeś {damage_taken} zdrowia.")
        input("Naciśnij Enter, aby kontynuować...")
    if random.random() < 0.05:  # 5% szans na awarię silnika
        clear()
        print(f"Awaria silnika! Straciłeś {round(speed/3)} km/h prędkości.")
        speed -= round(speed/3)
        input("Naciśnij Enter, aby kontynuować...")


    

    dalej()

    



            
'''
    if random.random() < 0.3:  # 30% szans na atak przeciwnika
        print("Atak przeciwnika!")
        damage_taken = max(0, damage - armor)  # Oblicz obrażenia po uwzględnieniu pancerza
        health -= damage_taken
        print(f"Zostałeś trafiony! Straciłeś {damage_taken} zdrowia.")
    else:
        print("Brak ataku przeciwnika.")'''
clear()
if health <= 0:
    print("Twój samolot został zestrzelony przez wroga! Przegrałeś.")
elif Y <= 0:
    print("Twój samolot rozbił się o ziemię! Przegrałeś.") 
elif Y >= maksymalnaWysokosc:
    print("Twój samolot poleciał za wysoko, gdzie powietrze jest zbyt rzadkie i nie dał rady! Przegrałeś.")
elif speed >= MAXspeed+100:
    print("Twój samolot rozbił się z powodu nadmiernej prędkości! Przegrałeś.")
elif speed <= 25:
    print("Wytraciłeś całą prędkość i wpadłeś w korkociąg, rozbijając się w ziemię! Przegrałeś.")
print('-' * 50)
print(f" -------Dzięki za grę!-------")
print("-" * 50)
if dystans() <= 0:
    print("Gratulacje! Bezpiecznie doleciałeś do celu! Wygrałeś!")
else:
    print("Niestety nie udało Ci się dotrzeć do celu. Spróbuj ponownie!")
end = time.time()
elapsed = end - start
print('Statystyki końcowe:\n')
print(f'Pieniądze: {money}')
print(f'Poziom silnika: {speedL}')
print(f'Poziom pancerza: {armorL}')
print(f'Ilość ukończonych misji: {IloscZrobionychMisji}')
print(f'ilość iteracji: {iteracje}')
print(f'Końcowe kordynaty: X: {round(X)} Y: {round(Y)}')
print(f'Końcowa prędkość: {speed} km/h')
print(f'Przebyty dystans: {round(2400 - dystans())} km')
print(f'Czas gry: {round(elapsed)} sekund!')
