from random import*
class Mob():
    def __init__(mobs,name,hp,damage):
        mobs.name=name
        mobs.hp=hp
        mobs.damage=damage

class Player():
    def __init__(player,name,hp,damage):
        player.name=name
        player.hp=hp
        player.damage=damage
        player.backpack=[]
    def voina(player,mobs):
        while True:
            if player.hp and mobs.hp > 0:
                mobs.hp -= player.damage
                print(player.name," ударил ",mobs.name," хп зомби упало до ",mobs.hp)
                player.hp -= mobs.damage
                print(mobs.name," ударил ",player.name," хп игрока упало до ",player.hp)
            if player.hp <= 0:
                print("Вы были убиты!")
                break
            if mobs.hp <= 0:
                print(mobs.name," был убит!")
                cub = [1,2]
                if choice(cub) == 1:
                    print("Удача на вашей стороне из ",mobs.name," выпала веревка и ткань")
                    player.backpack.append("верёвка")
                    player.backpack.append("ткань")
                    print("Ваш инвентарь: ",player.backpack)
                    break
                else:
                    print("Удача прошла вас стороной")
                    print("Ваш инвентарь: ", player.backpack)
                    break

class Mob2(Mob):
    def __init__(mobs,name,hp,damage,super_ataka):
        super().__init__(name,hp,damage)
        mobs.super_ataka=super_ataka
    def randomm(mobs):
        if randint(1,2) == 2:
            print(mobs.name," сделал крит удар")
            return True
        else:
            return False
class Mob3(Mob):
    def __init__(mobs,name,hp,damage,voscreshenie):
        super().__init__(name,hp,damage)
        mobs.voscreshenie=voscreshenie

mob1=Mob("Прокаженный солдат",100,10)
mob2=Mob2("Проклятый рыцарь",50,10,15)
mob3=Mob3("Проклятый храмовник",40,10,"50%")
player=Player("Выживший",100,20)
player.voina(mob1)

