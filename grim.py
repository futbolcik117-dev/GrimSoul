
from random import*
class player():
    def __init__(player,hp,damage,weapon):
        player.hp=hp
        player.damage=damage
        player.weapon=weapon
        player.backpack=["Верёвка","Ткань","Слиток меди","Слиток меди","Слиток меди"]
    def battle(player):
        a = input("                                             Введите номер выбранного события: ")
        if a == "1":
            print("При осмотре кладбища на вас напали зомби.(2)")
            while True:
                if len(mpc) == 0:
                    print("Все зомби были убиты.")
                    break
                b = input("Выберите какому зомби вы хотите нанести удар.(1,2): ")
                if b == "1":
                    if len(mpc) == 1 and mpc[0] == mpc2:
                        print("*** Зомби уже убит ***")
                    if mpc[0].hp > 0 and len(mpc) == 2:
                        mpc[0].hp -= player.damage
                        print("Вы ударили первого зомби, оставив ему здоровья: ",mpc[0].hp)
                        player.hp -= (mpc[0].damage + mpc[1].damage)
                        print("Зомби ударили по вам, оставив вам здоровья: ",player.hp)
                    if mpc[0].hp > 0 and len(mpc) == 1 and mpc[0] == mpc1:
                        mpc[0].hp -= player.damage
                        print("Вы ударили первого зомби, оставив ему здоровья: ", mpc[0].hp)
                        player.hp -= mpc[0].damage
                        print("Зомби ударил по вам, оставив вам здоровья: ", player.hp)
                    if mpc[0].hp <= 0:
                        print("Зомби был убит вами.(1)")
                        mpc.remove(mpc[0])
                        kubik = randint(1, 2)
                        if kubik == 1:
                            player.backpack.append("Слиток меди")
                            player.backpack.append("Ткань")
                            print("Удача на вашей стороне из зомби выпал слиток меди(1) и ткань(1)")
                        else:
                            print("Удача обошла вас стороной, с зомби не выпало ничего")
                if b == "2":
                    if len(mpc) == 1 and mpc[0] == mpc1:
                        print("*** Зомби уже убит ***")
                    if len(mpc) == 2 and mpc[1].hp > 0 :
                        mpc[1].hp -= player.damage
                        print("Вы ударили второго зомби, оставив ему здоровья: ", mpc[1].hp)
                        player.hp -= (mpc[0].damage + mpc[1].damage)
                        print("Зомби ударили по вам, оставив вам здоровья: ",player.hp)
                    if len(mpc) == 1 and mpc[0].hp > 0 and mpc[0] == mpc2:
                        mpc[0].hp -= player.damage
                        print("Вы ударили второго зомби, оставив ему здоровья: ", mpc[0].hp)
                        player.hp -= mpc[0].damage
                        print("Зомби ударил по вам, оставив вам здоровья: ", player.hp)
                    if len(mpc) == 2 and mpc[1].hp <= 0:
                        print("Зомби был убит вами.(2)")
                        mpc.remove(mpc[1])
                        kubik = randint(1, 2)
                        if kubik == 1:
                            player.backpack.append("Ткань")
                            print("Удача на вашей стороне из зомби выпала ткань(1)")
                        else:
                            print("Удача обошла вас стороной, с зомби не выпало ничего")
                    if len(mpc) == 1 and mpc[0].hp <= 0:
                        print("Зомби был убит вами.(2)")
                        mpc.remove(mpc[0])
                        kubik = randint(1, 2)
                        if kubik == 1:
                            player.backpack.append("Ткань")
                            print("Удача на вашей стороне из зомби выпал ткань(1)")
                        else:
                            print("Удача обошла вас стороной, с зомби не выпало ничего")
        if a == "2":
            print("Ваш инвентарь: ",player.backpack)
            while True:
                print("Ваш доступный крафт: 1) Бинты \n                     2) Меч")
                s = input("Если вы хотите выйти из крафта напишите (да): ")
                if s == "да":
                    print("Вы вышли из крафта")
                    print("Ваш инвентарь: ", player.backpack)
                    break
                a = input("Введите номер того, чей крафт хотите посмотреть: ")
                if a == "1":
                    print("Бинт(1) = Ткань(1),Верёвка(1)")
                    a1 = input("Напишите крафтить, чтобы скрафтить ресурс: ")
                    if a1 == "крафтить":
                        if "Верёвка" in player.backpack and "Ткань" in player.backpack:
                            player.backpack.remove("Верёвка")
                            player.backpack.remove("Ткань")
                            player.backpack.append("Бинт")
                            print("Бинт был успешно скравчен")
                        else:
                            print("Вам недостаточно ресурсов")
                if a == "2":
                    print("Меч(1) = Слиток меди(5)")
                    a1 = input("Напишите крафтить, чтобы скрафтить ресурс: ")
                    if a1 == "крафтить":
                        if player.backpack.count("Слиток меди") >= 5:
                            print("Меч был успешно создан")
                            player.backpack.remove("Слиток меди")
                            player.backpack.remove("Слиток меди")
                            player.backpack.remove("Слиток меди")
                            player.backpack.remove("Слиток меди")
                            player.backpack.remove("Слиток меди")
                            player.backpack.append("Меч")
                        else:
                            print("Вам недостаточно ресурсов")
        if a == "3":
            print("Вы прошли кладбище и дошли до старой хижины.")
    def house(player,MPC):
        print("Вы дошли до старой хижины, где вы наткнулись на Проклятого рыцаря(1)")
        while True:
            a = input("Напиши удар, что бы ударить: ")
            if a == "удар":
                MPC.hp -= player.damage
                print("Остаток хп у проклятого рыцаря равен: ",MPC.hp)
                player.hp -= MPC.damage
                print("Остаток вашего хп упал до: ", player.hp)
                if player.hp <= 0:
                    print("Вы умерли")
                    break
                if MPC.hp <= 0:
                    print("Проклятый рыцарь был повержен")
                    kubik = randint(1,2)
                    if kubik == 1:
                        player.backpack.append("Бинт")
                        player.backpack.append("Верёвка")
                        print("Удача на вашей стороне из рыцаря выпала верёвка(1) и бинт(1)")
                    else:
                        print("Удача обошла вас стороной, вы не получили ничего за убийство рыцаря")
                    break
            else:
                player.hp -= MPC.damage
                print("Остаток вашего хп упал до: ", player.hp)
                print("Вы получили урон от проклятого рыцаря пропустив свой удар")
                if player.hp <= 0:
                    print("Вы умерли")
                    break
    def inventary(player):
        print("Ваш инвентарь: ", player.backpack)
        while True:
            print("Ваш доступный крафт: 1) Бинты \n                     2) Меч")
            s = input("Если вы хотите выйти из крафта напишите (да): ")
            if s == "да":
                print("Вы вышли из крафта")
                print("Ваш инвентарь: ", player.backpack)
                break
            a = input("Введите номер того, чей крафт хотите посмотреть: ")
            if a == "1":
                print("Бинт(1) = Ткань(1),Верёвка(1)")
                a1 = input("Напишите крафтить, чтобы скрафтить ресурс: ")
                if a1 == "крафтить":
                    if "Верёвка" in player.backpack and "Ткань" in player.backpack:
                        player.backpack.remove("Верёвка")
                        player.backpack.remove("Ткань")
                        player.backpack.append("Бинт")
                        print("Бинт был успешно скравчен")
                    else:
                        print("Вам недостаточно ресурсов")
            if a == "2":
                print("Меч(1) = Слиток меди(5)")
                a1 = input("Напишите крафтить, чтобы скрафтить ресурс: ")
                if a1 == "крафтить":
                    if player.backpack.count("Слиток меди") >= 5:
                        print("Меч был успешно создан")
                        player.backpack.remove("Слиток меди")
                        player.backpack.remove("Слиток меди")
                        player.backpack.remove("Слиток меди")
                        player.backpack.remove("Слиток меди")
                        player.backpack.remove("Слиток меди")
                        player.backpack.append("Меч")
                    else:
                        print("Вам недостаточно ресурсов")
    def craft(player):
        print("Сейчас вы можете улучшить свои характеристики, пока у вас есть шанс.")
        a = input("Введите цифру один что бы открыть крафт, иначе просто нажмите enter")
        if a == "1":
            player.inventary()
        print("Вы скрафтили всё что хотели, настало время улучшить свои характеристики.")
        while True:
            q = input("Если хотити выйти из прокачки напишите хватит, иначе enter:  ")
            if q == "хватит":
                break
            else:
                s = input("Введите 1, что бы использовать бинт восстановив 50 хп, введите цифру 2 чтобы надеть меч(добавит 10 к урону).\n Введите число:")
                if s == "1":
                    if player.backpack.count("Бинт") >= 1:
                        player.backpack.remove("Бинт")
                        player.hp += 50
                        print("Хп героя было восстановлено до ",player.hp)
                    else:
                        print(" вас недостатачно ресурсов")
                if s == "2":
                    if player.backpack.count("Меч") >= 1:
                        player.backpack.remove("Меч")
                        player.weapon.replace("кулаки","Меч")
                        player.damage.replace(player.damage,10)
                        print("Урон от вашего оружия был увеличен до ",player.damage)
                    else:
                        print(" вас недостатачно ресурсов")
                print("Ваша характеристика: ",player.hp," ваше хп, ",player.damage," ваш урон, ",player.weapon," ваше оружие, ",player.backpack,"ваш инвентарь.")

Player=player(100,5,"кулаки")

class zombi():
    def __init__(self,damage,hp):
        self.damage=damage
        self.hp=hp

mpc1=zombi(5,10)
mpc2=zombi(5,10)
mpc=[mpc1,mpc2]
MPC=zombi(15,15)

print("                                                 ---Grimm Soul---\n")
print("             Вы один выживший в этом мире, вам надо выжить в этом зомби апокалипсисе, создать базу и стать королём этой игры.")
print("             У вас есть выбор действий:")
print("                     1) Осмотреть кладбище")
print("                     2) Зайти в крафт")
print("                     3) Пойти дальше")
Player.battle()
Player.house(MPC)
Player.inventary()
Player.craft()
