from colorama import Fore #, init

#init(autoreset=True) #Colorama init - autoreset colors after each print

class Weapon:
    instances = []
    
    def __init__(self, name: str, damageType: str, damage: int, critChance: int, speed: float):
        self.name = name
        self.damageType = damageType
        self.damage = damage
        self.critChance = critChance
        self.speed = speed
        Weapon.instances.append(self)

    def __str__(self):
        return f"{self.name}, {self.damageType}, {self.damage}, {self.speed}"

    def calcDPS(self):
        DPS = (self.damage * self.speed) * (1 + (self.critChance / 100))
        if DPS < 0:
            return 0
        # Round to 2 decimal places
        
        return "%.1f" % DPS
    
    def weaponDescription(self):
        clrName = f"{Fore.CYAN}{self.name}{Fore.RESET}"
        
        if self.damageType == "Melee":
            clrDamageType = f"{Fore.LIGHTRED_EX}{self.damageType}{Fore.RESET}"
            clrDamage = f"{Fore.LIGHTRED_EX}{self.damage}{Fore.RESET}"
        elif self.damageType == "Ranged":
            clrDamageType = f"{Fore.LIGHTGREEN_EX}{self.damageType}{Fore.RESET}"
            clrDamage = f"{Fore.LIGHTGREEN_EX}{self.damage}{Fore.RESET}"
        elif self.damageType == "Magic":
            clrDamageType = f"{Fore.LIGHTMAGENTA_EX}{self.damageType}{Fore.RESET}"
            clrDamage = f"{Fore.LIGHTMAGENTA_EX}{self.damage}{Fore.RESET}"
        else: #No damage type
            clrDamageType = f"{Fore.LIGHTWHITE_EX}{self.damageType}{Fore.RESET}"
            clrDamage = f"{Fore.LIGHTWHITE_EX}{self.damage}{Fore.RESET}"
            
        clrCritChance = f"{Fore.LIGHTBLUE_EX}{self.critChance}%{Fore.RESET}"
        clrSpeed = f"{Fore.LIGHTYELLOW_EX}{self.speed}{Fore.RESET}"
        clrDPS = f"{Fore.GREEN}{self.calcDPS()}{Fore.RESET}"
        
        description = ( f"{clrName}\n"
                        "-------------------\n"
                        f"{clrDamage} {clrDamageType} damage\n"
                        f"{clrCritChance} critical strike chance\n"
                        f"{clrSpeed} hits per second\n"
                        f"{clrDPS} DPS\n")
        return description

GargantuanAxe = Weapon("Gargantuan Axe", "Melee", 100, 60, 0.4)
TomeOfFire1 = Weapon("Tome of Fire 1", "Magic", 12, 8, 5)
TomeOfFire2 = Weapon("Tome of Fire 2", "Magic", 29, 10, 7)
BowOfTheMaker = Weapon("Bow of the Maker", "Ranged", 219, 15, 2)

for obj in Weapon.instances:
    print(obj.weaponDescription())

# print(GargantuanAxe.weaponDescription())
# print(TomeOfFire1.weaponDescription())
# print(TomeOfFire2.weaponDescription())
# print(BowOfTheMaker.weaponDescription())
