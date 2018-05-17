import random


class Room(object):
    def __init__(self, name, north, northeast, northwest, west, south, southeast, southwest, east, description):
        self.name = name
        self.north = north
        self.northeast = northeast
        self.northwest = northwest
        self.west = west
        self.south = south
        self.southeast = southeast
        self.southwest = southwest
        self.east = east
        self.description = description
        self.items = []

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


class Item(object):
    def __init__(self, name, description, weight, color, material, size):
        self.name = name
        self.description = description
        self.weight = weight
        self.color = color
        self.material = material
        self.size = size


class Flashlight(Item):
    def __init__(self, name, description, weight, color, material, size):
        super(Flashlight, self).__init__(name, description, weight, color, material, size)
        self.name = 'LED Flashlight'
        self.color = 'Black'

    def drop(self):
        print("You drop the %s" % self.name)

    def item(self):
        if self.description:
            self.description = True
            print('The %s battery is full' % self.name)
        else:
            print('The %s is dead' % self.name)


class Sack(Item):
    def __init__(self, name, description, weight, color, material, size):
        super(Sack, self).__init__(name, description, weight, color, material, size)
        self.name = 'Brown sack'
        self.weight = 'Heavy'
        self.color = 'Tan'
        self.material = 'Leather'

    def pick_up(self):
        print('You pick up the %s bag' % self.material)


class Rope(Item):
    def __init__(self, name, description, weight, color, material, size):
        super(Rope, self).__init__(name, description, weight, color, material, size)
        self.name = 'Climbing Rope'
        self.color = 'Tan'
        self.material = 'Nylon'

    def throw(self):
        print('You throw the %s' % self.name)


class Consumable(Item):
    def __init(self, name, description, weight, color, material, size):
        super(Consumable, self).__init__(name, description, weight, color, material, size)

    def eat(self):
        print('You eat the consumable')


class Apple(Consumable):
    def __init__(self, name, description, weight, color, material, size):
        super(Apple, self).__init__(name, description, weight, color, material, size)
        self.color = 'Red'
        self.name = 'Apple'


class Pepper(Consumable):
    def __init__(self, name, description, weight, color, material, size):
        super(Pepper, self).__init__(name, description, weight, color, material, size)
        self.name = 'Bell Pepper'
        self.color = 'Red'
        self.description = 'Red Bell Peppers found in sack'

    def eat(self):
        print("You eat the red pepper")


class Bottle(Consumable):
    def __init__(self, name, description, weight, color, material, size):
        super(Bottle, self).__init__(name, description, weight, color, material, size)
        self.name = 'Water Bottle'
        self.description = 'The bottle is half full'

    def drop(self):
        print("You drop the %s" % self.name)

    def item(self):
        if self.description:
            self.description = True
            print('The %s is half full' % self.name)
        else:
            print('The %s is full' % self.name)


class Drink(Consumable):
    def __init__(self, name, description, weight, color, material, size):
        super(Drink, self).__init__(name, description, weight, color, material, size)
        self.name = 'Energy Drink'

    def drop(self):
        print("You drop the %s" % self.name)

    def item(self):
        if self.description:
            self.description = True
            print('The %s is half full' % self.name)
        else:
            print('The %s is full' % self.name)


class Soda(Consumable):
    def __init__(self, name, description, weight, color, material, size):
        super(Soda, self).__init__(name, description, weight, color, material, size)
        self.name = 'Soda can'
        self.description = 'The %s is full'

    def use(self):
        if self.description:
            self.description = False
            print('The %s is full')
        else:
            self.description = True
            print('The %s is empty')


class Egg(Consumable):
    def __init__(self, name, description, weight, color, material, size):
        super(Egg, self).__init__(name, description, weight, color, material, size)
        self.color = 'Turquoise'
        self.material = 'Jeweled'
        self.description = 'The egg is dropped and shatters'
        self.name = 'Egg'

    def throw(self):
        if self.description:
            self.description = True
            print('You throw the %s egg down' % self.description)
        else:
            self.description = False
            print('This can not be done right now')

    def drop(self):
        if self.description:
            self.description = True
            print('The egg is dropped and shatters')
        else:
            print('The egg is shattered on the ground')


class Weapon(Item):
    def __init__(self, name, description, weight, color, material, size):
        super(Weapon, self).__init__(name, description, weight, color, material, size)

    def pick_up(self):
        if self.name:
            self.name = True
            print('You pick up the weapon')
            print('What weapon?')
        if self.name:
            self.name = True
            print('You pick up a %s' % self.name)


class Dagger(Weapon):
    def __init__(self, name, description, weight, color, grip_type, material, size):
        super(Dagger, self).__init__(name, description, weight, color, material, size)
        self.handle = grip_type
        self.weight = 1.02
        self.grip_type = 'Metal'
        self.material = 'Rusty'
        self.name = 'Dagger'

    def drop(self):
        print('You drop the %s dagger' % self.material)


class Pan(Weapon):
    def __init__(self, name, description, weight, color, grip_type, material, size):
        super(Pan, self).__init__(name, description, weight, color, material, size)
        self.name = 'Frying Pan'
        self.weight = 2.00
        self.grip_type = 'Metal'
        self.material = 'Black Metal Rust'
        self.handle = grip_type


class Axe(Weapon):
    def __init__(self, name, description, weight, color, grip_type, material, size):
        super(Axe, self).__init__(name, description, weight, color, material, size)
        self.handle = grip_type
        self.grip_type = 'Wood'
        self.name = 'Axe'

    def pick_up(self):
        print('You pick up the axe')


class Nunchaku(Weapon):
    def __init__(self, name, description, weight, color, grip_type, material, size):
        super(Nunchaku, self).__init__(name, description, weight, color, material, size)
        self.name = 'Nunchucks'
        self.color = 'Black'
        self.material = 'Metal'
        self.handle = grip_type


class Bat(Weapon):
    def __init__(self, name, description, weight, color, material, size):
        super(Bat, self).__init__(name, description, weight, color, material, size)
        self.color = 'Black'
        self.material = 'Metal'
        self.name = 'Metal Bat'


class Wearable(Item):
    def __init__(self, name, description, weight, color, material, size):
        super(Wearable, self).__init__(name, description, weight, color, material, size)

    def pick_up(self):
        print('You pick up the wearable')


class Boots(Wearable):
    def __init__(self, name, description, weight, color, material, size):
        super(Boots, self).__init__(name, description, weight, color, material, size)
        self.name = 'Leather Boots'
        self.color = 'Brown'
        self.material = 'Leather'


class Jeans(Wearable):
    def __init__(self, name, description, weight, color, material, size):
        super(Jeans, self).__init__(name, description, weight, color, material, size)
        self.color = 'Black'
        self.description = 'Black Jean Slacks'
        self.name = 'Jeans'


class Vest(Wearable):
    def __init__(self, name, description, weight, color, material, size):
        super(Vest, self).__init__(name, description, weight, color, material, size)
        self.name = 'Armored Vest'
        self.color = 'Black'

    def drop(self):
        print('You drop the %s' % self.name)

    def wear(self):
        print('You put on the %s' % self.name)


class Coat(Wearable):
    def __init__(self, name, description, weight, color, material, size):
        super(Coat, self).__init__(name, description, weight, color, material, size)
        self.name = 'Trench Coat'
        self.color = 'Brown'
        self.material = 'Leather'

    def drop(self):
        print('You drop the %s' % self.name)

    def wear(self):
        print('You put on the %s' % self.name)


class Jacket(Wearable):
    def __init__(self, name, description, weight, color, material, size):
        super(Jacket, self).__init__(name, description, weight, color, material, size)
        self.color = 'Black'
        self.material = 'Leather'
        self.name = 'Leather Jacket'

    def wear(self):
        print('You wear the %s jacket' % self.material)


class Helmet(Wearable):
    def __init__(self, name, description, weight, color, material, size):
        super(Helmet, self).__init__(name, description, weight, color, material, size)
        self.color = 'Blue'
        self.name = 'Blue Helmet'

    def use(self):
        print('You wear the %s helmet' % self.color)

    def drop(self):
        print('You drop the %s helmet' % self.color)


class Gloves(Wearable):
    def __init__(self, name, description, weight, color, material, size):
        super(Gloves, self).__init__(name, description, weight, color, material, size)
        self.name = 'Fingerless Gloves'
        self.color = 'Black'
        self.material = 'Leather'

    def pick_up(self):
        print('You pick up the %s' % self.name)


class Armor(Item):
    def __init__(self, name, description, weight, color, material, size):
        super(Armor, self).__init__(name, description, weight, color, material, size)


class Potion(Armor):
    def __init__(self, name, description, weight, color, material, size):
        super(Potion, self).__init__(name, description, weight, color, material, size)
        self.name = 'Health Potion'
        self.color = 'Blue'

    def use(self):
        print('You drink the %s' % self.name)

    def drop(self):
        print('The %s drops and shatters' % self.name)


class Medication(Armor):
    def __init__(self, name, description, weight, color, material, size):
        super(Medication, self).__init__(name, description, weight, color, material, size)
        self.name = 'Medication Pills'
        self.description = 'Medications'

    def eat(self):
        print('You take some %s' % self.name)


class Painkillers(Armor):
    def __init__(self, name, description, weight, color, material, size):
        super(Painkillers, self).__init__(name, description, weight, color, material, size)
        self.name = 'Health Painkillers'


class Bandages(Armor):
    def __init__(self, name, description, weight, color, material, size):
        super(Bandages, self).__init__(name, description, weight, color, material, size)
        self.name = 'Bandages'

    def use(self):
        print('You patch yourself using %s' % self.name)


class Firearm(Item):
    def __init__(self, name, description, weight, color, material, size, grip_type, ammo_type, damage):
        super(Firearm, self).__init__(name, description, weight, color, material, size)
        self.handle = grip_type
        self.cases = ammo_type
        self.damage_hit = damage

    def pick_up(self):
        print('You pick up the %s' % self.name)

    def drop(self):
        print('You drop the %s on the ground' % self.name)


class Crossbow(Firearm):
    def __init__(self, name, description, weight, color, material, size, grip_type, ammo_type, damage):
        super(Crossbow, self).__init__(name, description, weight, color, material, size, grip_type,
                                       ammo_type, damage)
        self.handle = grip_type
        self.cases = ammo_type
        self.ammo_type = 'Arrows'
        self.name = 'Crossbow'
        self.damage = 20

    def pick_up(self):
        print('You pick up the %s' % self.name)


class AK(Firearm):
    def __init__(self, name, description, weight, color, material, size, grip_type, ammo_type, damage):
        super(AK, self).__init__(name, description, weight, color, material, size, grip_type,
                                 ammo_type, damage)
        self.handle = grip_type
        self.cases = ammo_type
        self.ammo_type = '7.62mm'
        self.name = 'AK-47'
        self.description = 'Burst'
        self.damage = 35

    def use(self):
        print('You pull the trigger and fire a %s bullet' % self.ammo_type)

    def drop(self):
        print('You drop the %s' % self.name)


class SCAR(Firearm):
    def __init__(self, name, description, weight, color, material, size, grip_type, ammo_type, damage):
        super(SCAR, self).__init__(name, description, weight, color, material, size, grip_type,
                                   ammo_type, damage)
        self.handle = grip_type
        self.cases = ammo_type
        self.ammo_type = '7.62mm'
        self.name = 'SCAR-H'
        self.color = 'Tan'
        self.damage = 50

    def replace_ammo_type(self):
        print('You replace the empty ammunition cartridge from the %s' % self.name)


class Remington(Firearm):
    def __init__(self, name, description, weight, color, material, size, grip_type, ammo_type, damage):
        super(Remington, self).__init__(name, description, weight, color, material, size, grip_type,
                                        ammo_type, damage)
        self.handle = grip_type
        self.cases = ammo_type
        self.ammo_type = 'Explosive'
        self.name = 'Remington 870'
        self.color = 'Black'
        self.description = 'The shotgun has no rounds left'
        self.damage = 20

    def throw(self):
        print('You throw the %s on the ground' % self.name)

    def replace_ammo(self):
        print('You replace the empty ammunition cartridge from the %s' % self.name)


class Tactical(Firearm):
    def __init__(self, name, description, weight, color, material, size, grip_type, ammo_type, damage):
        super(Tactical, self).__init__(name, description, weight, color, material, size, grip_type,
                                       ammo_type, damage)
        self.handle = grip_type
        self.cases = ammo_type
        self.ammo_type = 'Pump'
        self.name = 'Tactical Shotgun'
        self.color = 'Black'
        self.damage = 35

    def throw(self):
        print('You throw the %s on the ground' % self.name)

    def replace_ammo(self):
        print('You replace the empty ammunition cartridge from the %s' % self.name)


class M4(Firearm):
    def __init__(self, name, description, weight, color, material, size, grip_type, ammo_type, damage):
        super(M4, self).__init__(name, description, weight, color, material, size, grip_type,
                                 ammo_type, damage)
        self.handle = grip_type
        self.cases = ammo_type
        self.ammo_type = '5.56mm'
        self.name = 'M4A1'
        self.damage = 72

    def wear(self):
        print('You put on the %s gun sling' % self.name)

    def throw(self):
        print('You throw the %s on the ground' % self.name)


class Glock(Firearm):
    def __init__(self, name, description, weight, color, material, size, grip_type, ammo_type, damage):
        super(Glock, self).__init__(name, description, weight, color, material, size, grip_type,
                                    ammo_type, damage)
        self.name = 'G-18'
        self.handle = grip_type
        self.cases = ammo_type
        self.ammo_type = '9mm'
        self.name = 'G-18'
        self.color = 'Black'
        self.damage = 15

    def drop(self):
        print('You drop the %s' % self.name)

    def use(self):
        print('You replace the empty ammunition cartridge from the %s' % self.name)


class Revolver(Firearm):
    def __init__(self, name, description, weight, color, material, size, grip_type, ammo_type, damage):
        super(Revolver, self).__init__(name, description, weight, color, material, size, grip_type,
                                       ammo_type, damage)
        self.handle = grip_type
        self.cases = ammo_type
        self.ammo_type = '9mm'
        self.name = 'Revolver'
        self.color = 'Gray'
        self.damage = 10


class Sniper(Firearm):
    def __init__(self, name, description, weight, color, material, size, grip_type, ammo_type, damage):
        super(Sniper, self).__init__(name, description, weight, color, material, size, grip_type,
                                     ammo_type, damage)
        self.handle = grip_type
        self.cases = ammo_type
        self.ammo_type = 308
        self.name = 'Bolt Action Sniper Rifle'
        self.color = 'Dark Gray'
        self.damage = 85

    def drop(self):
        print('You drop the %s' % self.name)

    def use(self):
        print('You replace the empty ammunition cartridge from the %s' % self.name)


class AR(Firearm):
    def __init__(self, name, description, weight, color, material, size, grip_type, ammo_type, damage):
        super(AR, self).__init__(name, description, weight, color, material, size, grip_type,
                                 ammo_type, damage)
        self.handle = grip_type
        self.cases = ammo_type
        self.ammo_type = 5.56
        self.name = 'Blue AR-15 Rifle'
        self.color = 'Blue'
        self.color = 70


class Explosive(Item):
    def __init__(self, name, description, weight, color, material, size, damage):
        super(Explosive, self).__init__(name, description, weight, color, material, size)
        self.damage_hit = damage


class Grenade(Explosive):
    def __init__(self, name, description, weight, color, material, size, damage):
        super(Grenade, self).__init__(name, description, weight, color, material, size, damage)
        self.name = 'Grenade'
        self.color = 'Green'
        self.damage_hit = damage
        self.damage = 90


class AT(Explosive):
    def __init__(self, name, description, weight, color, material, size, damage):
        super(AT, self).__init__(name, description, weight, color, material, size, damage)
        self.name = 'AT-14 Grenade Launcher'
        self.color = 'Black'
        self.material = 'Rusty'
        self.damage = 100


class Attachment(Item):
    def __init__(self, name, description, weight, color, material, size, damage):
        super(Attachment, self).__init__(name, description, weight, color, material, size)
        self.damage_hit = damage
        self.damage = 0


class LScope(Attachment):
    def __init__(self, name, description, weight, color, material, size, damage):
        super(LScope, self).__init__(name, description, weight, color, material, size, damage)
        self.name = '2x Scope'
        self.description = ('2x Scope for %s' % self.name)
        self.damage = 0


class MScope(Attachment):
    def __init__(self, name, description, weight, color, material, size, damage):
        super(MScope, self).__init__(name, description, weight, color, material, size, damage)
        self.name = '4x Scope'
        self.description = ('4x Scope attachment for %s' % self.name)
        self.damage = 0


class QScope(Attachment):
    def __init__(self, name, description, weight, color, material, size, damage):
        super(QScope, self).__init__(name, description, weight, color, material, size, damage)
        self.name = '8x Scope'
        self.description = ('8x Scope attachment for %s' % self.name)
        self.damage = 0


class HScope(Attachment):
    def __init__(self, name, description, weight, color, material, size, damage):
        super(HScope, self).__init__(name, description, weight, color, material, size, damage)
        self.name = '16x Scope'
        self.description = ('16x Scope attachment for %s' % self.name)
        self.damage = 0


class Character(object):
    def __init__(self, name, description, health, attack, death, dialogue, status):
        self.name = name
        self.description = description
        self.health = health
        self.attack = attack
        self.death = death
        self.dialogue = dialogue
        self.status = status
        self.inventory = []

    def take(self, item):
        self.inventory.append(item)
        print("You pick up the %s" % item.name)

    def drop(self, item):
        self.inventory.pop(item)
        print('You drop the %s' % item.name)


class Player1(Character):
    def __init__(self, name, description, health, attack, death, dialogue, status):
        super(Player1, self).__init__(name, description, health, attack, death, dialogue, status)
        self.name = 'Player1'
        self.description = description
        self.health = 100
        self.attack = attack
        self.death = death
        self.dialogue = dialogue
        self.status = status

    def name(self):
            print("Player1 name is %s" % self.name)

    def health(self):
        if self.health:
            self.health = False
            print("You are full on health")
        else:
            self.health = True
            print('You are low on health')

    def attack(self):
        if self.attack:
            self.attack = True
            print("Player1 attacks the %s" % self.name)
        else:
            if self.attack:
                self.attack = False
                print("You can not attack this")

    def dialogue(self):
        if self.dialogue:
            self.dialogue = False
            print("Nothing happens")

    def death(self):
        if self.death:
            self.death = True
            print("%s dies" % self.name)
        else:
            if self.death:
                self.death = False
                print("You have died")


class Troll(Character):
    def __init__(self, name, description, health, attack, death, dialogue, status):
        super(Troll, self).__init__(name, description, health, attack, death, dialogue, status)
        self.name = 'Troll'
        self.description = description
        self.health = 100
        self.attack = attack
        self.death = death
        self.dialogue = dialogue
        self.status = status

    def dialogue(self):
        if self.dialogue:
            self.dialogue = True
            print('You shall not pass human')

    def attack(self):
        if self.attack:
            self.attack = True
            print('The %s charges at you' % character.name)
        else:
            self.attack = False
            print('Nothing happens')


class Civilian(Character):
    def __init__(self, name, description, health, attack, death, dialogue, status):
        super(Civilian, self). __init__(name, description, health, attack, death, dialogue, status)
        self.name = 'Civilian'
        self.description = description
        self.health = 100
        self.attack = attack
        self.death = death
        self.dialogue = dialogue
        self.status = status


class Thief(Character):
    def __init__(self, name, description, health, attack, death, dialogue, status):
        super(Thief, self).__init__(name, description, health, attack, death, dialogue, status)
        self.name = 'Masked Thief'
        self.description = description
        self.health = 100
        self.attack = attack
        self.death = death
        self.dialogue = dialogue
        self.status = status

    def attack(self):
        if self.attack:
            self.attack = True
            print("The masked thief charges at you with his knife")
        else:
            if self.attack:
                self.attack = False
                print("You can not do this")


class Inmate(Character):
    def __init__(self, name, description, health, attack, death, dialogue, status):
        super(Inmate, self).__init__(name, description, health, attack, death, dialogue, status)
        self.name = 'Prison Inmate'
        self.description = description
        self.health = 100
        self.attack = attack
        self.death = death
        self.dialogue = dialogue
        self.status = status


list_of_characters = [Player1, Troll, Civilian, Thief, Inmate]

character = Character('Character', None, None, None, None, None, None)
player1 = Player1('Player1', None, 100, None, None, None, None)
troll = Troll('Troll', None, 100, None, None, None, None)
civilian = Civilian('Civilian', None, 100, None, None, None, None)
thief = Thief('Masked Thief', None, 100, None, None, None, None)
inmate = Inmate('Prison Inmate', None, 100, None, None, None, None)

north_hospital = Room('North of Hospital', None, 'west_kin', 'east_yale', None, None, None, None, None,
                      'You are north of Hospital.')
west_kin = Room('West of Kin', None, None, None, None, 'east_hay_fields', None, 'west_bunker', None,
                'You are west of Kin.')
east_vernal = Room('East of Vernal', None, None, 'east_tower', None, None, None, None, 'north_garage',
                   'You are east of Vernal.')
north_garage = Room('North of Garage', None, None, 'north_vernal', None, None, 'west_hark', None, None,
                    'You are north of Garage.')
southeast_trinity = Room('Southeast of Trinity', None, None, None, None, None, 'southeast_cemetery',
                         'west_kin', None, 'You are southeast of Trinity.')
southeast_cemetery = Room('Southeast of Cemetery', 'southwest_docks', None, 'southeast_trinity', None,
                          None, None, None, None, 'You are southeast of Cemetery.')
north_prison = Room('North of Prison', None, None, None, None, 'west_korri', None, None, 'west_factory',
                    'You are north of Prison.')
west_bunker = Room('West of Bunker', None, None, None, None, None, None, None, 'east_hay_fields',
                   'You are west of Bunker.')
east_hay_field = Room('East of Hayfield', None, None, None, None, None, None, None, 'north_prison',
                      'You are east of Hayfield')
south_mansion = Room('South of Mansion', None, None, None, None, None, 'west_bunker', None, None,
                     'You are south of Mansion.')
east_radio_tower = Room('East of Tower', None, None, None, None, 'east_yale', None, None, 'south_mansion',
                        'You are east of Radio Tower.')
west_korri = Room('West of Korri', None, None, None, None, None, None, 'east_base', None,
                  'You are west of Korri.')
east_yale = Room('East of Yale', 'south_tower', 'south_mansion', None, None, None, None, None, None,
                 'You are east of Yale.')
west_hark = Room('West of Hark', None, None, None, None, None, 'southeast_hay_fields', None, 'east_base',
                 'You are west of Hark.')
east_base = Room('East of Base', None, None, None, None, None, None, None, 'west_korri',
                 'You are east of Military Base.')
south_tower = Room('South of Tower', None, None, None, None, None, None, None, 'west_kin',
                   'You are south of Tower.')
southwest_docks = Room('Southwest of Docks', None, None, None, 'southeast_trinity', None,
                       None, 'northeast_cemetery', None, 'You are southwest of Docks.')
west_factory = Room('West of Factory', 'southeast_cemetery', None, None, None, None, 'west_korri', None, None,
                    'You are west of Factory.')

flashlight = Flashlight('LED Flashlight', False, False, 'Black', False, False)
sack = Sack('Brown sack', False, 'Heavy', 'Tan', 'Leather', False)
rope = Rope('Climbing Rope', False, False, 'Tan', 'Nylon', False)
apple = Apple('Apple', False, False, 'Red', False, False)
pepper = Pepper('Bell Pepper', 'Red Bell Pepper found in sack', False, 'Red', False, False)
bottle = Bottle('Water Bottle', 'The bottle is half full', False, False, False, False)
drink = Drink('Energy Drink', False, False, False, False, False)
soda = Soda('Soda can', 'The %s is full', False, False, False, False)
egg = Egg("Egg", False, False, 'Turquoise', 'Jeweled', False)
dagger = Dagger('Dagger', False, 1.02, False, 'Metal', 'Rusty', False)
pan = Pan('Frying Pan', False, 2.00, 'Black', False, 'Black Metal Rust', False)
axe = Axe('Axe', False, False, False, 'Wood', False, False)
nunchaku = Nunchaku('Nunchucks', False, False, 'Black', False, 'Metal', False)
bat = Bat("Bat", False, False, False, 'Metal', False)
boots = Boots('Leather Boots', False, False, 'Brown', 'Leather', False)
jeans = Jeans('Jeans', 'Black Jean Slacks', False, 'Black', False, False)
vest = Vest('Armored Vest', False, False, 'Black', False, False)
coat = Coat('Trench Coat', False, False, 'Brown', 'Leather', False)
jacket = Jacket('Leather Jacket', False, False, 'Black', 'Leather', False)
helmet = Helmet('Blue Helmet', False, False, 'Blue', False, False)
gloves = Gloves('Fingerless Gloves', False, False, 'Black', 'Leather', False)
potion = Potion('Health Potion', False, False, 'Blue', False, False)
medication = Medication('Medication Pills', 'Medications', False, False, False, False)
painkillers = Painkillers('Health Painkillers', False, False, False, False, False)
bandages = Bandages('Bandages', False, False, False, False, False)
crossbow = Crossbow('Crossbow', False, False, False, False, False, False, 'Arrows', 20)
ak = AK('AK-47', 'Burst', False, False, False, False, False, '7.62mm', 35)
scar = SCAR('SCAR-H', False, False, 'Tan', False, False, False, '7.62mm', 50)
remington = Remington('Remington 870', 'The shotgun has no rounds left', False, 'Black', False, False,
                      False, 'Buckshot', 20)
tactical = Tactical('Tactical Shotgun', False, False, 'Black', False, False, False, 'Pump', 35)
m4 = M4('M4A1', False, False, False, False, False, False, False, 72)
glock = Glock('G-18', False, False, 'Black', False, False, False, '9mm', 15)
revolver = Revolver('Revolver', False, False, 'Gray', False, False, False, '9mm', 10)
sniper = Sniper('Bolt Action Sniper Rifle', False, False, 'Dark Gray', False,
                False, False, 308, 85)
ar = AR('Blue AR-15 Rifle', False, False, 'Blue', False, False, False, 223, 70)
grenade = Grenade('Grenade', False, False, 'Green', False, False, 90)
at = AT('AT-14 Grenade Launcher', False, False, 'Black', 'Rusty', False, 100)
lscope = LScope('2x Scope', False, False, False, False, False, 0)
mscope = MScope('4x Scope', False, False, False, False, False, 0)
qscope = QScope('8x Scope', False, False, False, False, False, 0)
hscope = HScope('16x Scope', False, False, False, False, False, 0)


list_of_items = [flashlight, sack, rope, apple, pepper, bottle, drink, soda, egg,
                 dagger, pan, axe, nunchaku, bat, boots, jeans, vest, coat, jacket,
                 helmet, gloves, potion, medication, painkillers, bandages, crossbow,
                 ak, scar, remington, tactical, m4, glock, revolver, sniper, ar, grenade,
                 at, lscope, mscope, qscope, hscope]

list_of_rooms = [south_tower, southwest_docks, west_factory, west_kin, north_hospital, north_prison,
                 north_garage, east_vernal, east_yale, east_base, east_radio_tower, southeast_cemetery,
                 southeast_trinity, south_mansion, west_hark, west_hark, west_korri, west_bunker]


def randomize_item_locations():
    for item in list_of_items:
        selected_room = random.choice(list_of_rooms)
        selected_room.items.append(item)


randomize_item_locations()
current_node = north_hospital
directions = ['north', 'northeast', 'northwest', 'west', 'south', 'southeast', 'southwest', 'east']
short_directions = ['n', 'ne', 'nw', 'w', 's', 'se', 'sw', 'e']

while True:
    print(current_node.name)
    print(current_node.description)
    if len(current_node.items) > 0:
        print("There are the following items in the room:")
        for item in current_node.items:
            print(item.name)

    command = input('>_')
    if command == 'quit':
        quit(0)

    if 'pick up' in command:
        item_requested = command[8:]
        for item in current_node.items:
            # print(item)
            if item_requested.lower() == item.name.lower():
                player1.take(item)

    if 'drop' in command:
        item_requested = command[8:]
        for item in current_node.items:
            if item_requested.lower() == item.name.lower():
                player1.drop(item)

    if command == 'inspect':
        print('You look around the room')
    if command == 'Kill self':
        print('Suicide is not the answer')
    if command == 'drop Flashlight':
        item = input('You drop the LED Flashlight')
        print()
    if command == 'drop Brown sack':
        item = input('You dropped the Brown Sack')
        print()
    if command == 'drop Rope':
        item = input('You dropped the Climbing Rope')
        print()
    if command == 'drop Apple':
        item = input('You dropped the Apple')
        print()
    if command == 'drop Bell Pepper':
        item = input('You dropped the Pepper')
        print()
    if command == 'drop Water Bottle':
        item = input('You dropped the Water Bottle')
        print()
    if command == 'drop Energy Drink':
        item = input('You dropped the Energy drink')
        print()
    if command == 'drop Soda can':
        item = input('You dropped the Soda can')
        print()
    if command == 'drop Egg':
        item = input('You dropped the Egg')
        print()
    if command == 'drop Dagger':
        item = input('You dropped the Dagger')
        print()
    if command == 'drop Pan':
        item = input('You dropped the Frying Pan')
        print()
    if command == 'drop Axe':
        item = input('You dropped the Axe')
        print()
    if command == 'drop Nunchucks':
        item = input('You dropped the Nunchucks')
        print()
    if command == 'drop Bat':
        item = input('You dropped the Bat')
        print()
    if command == 'drop Vest':
        item = input('You dropped the Armored Vest')
        print()
    if command == 'drop Trench Coat':
        item = input('You dropped the Brown Trench coat')
        print()
    if command == 'drop Jacket':
        item = input('You dropped the Black Leather Jacket')
        print()
    if command == 'drop Blue Helmet':
        item = input('You dropped the Blue Helmet')
        print()
    if command == 'drop Gloves':
        item = input('You dropped the Black Gloves')
        print()
    if command == 'drop Health Potion':
        item = input('You dropped the Health Potion')
        print()
    if command == 'drop Medications':
        item = input('You dropped the Medication Pills')
        print()
    if command == 'drop Painkillers':
        item = input('You dropped the Painkillers')
        print()
    if command == 'drop Bandages':
        item = input('You dropped the bandages')
        print()
    if command == 'drop Crossbow':
        item = input('You dropped the Crossbow')
        print()
    if command == 'drop AK-47':
        item = input('You dropped the AK-47')
        print()
    if command == 'drop SCAR-H':
        item = input('You dropped the SCAR-H')
        print()
    if command == 'drop Remington':
        item = input('You dropped the Remington-870')
        print()
    if command == 'drop Tactical Shotgun':
        item = input('You dropped the Tactical Shotgun')
        print()
    if command == 'drop M4A1':
        item = input('You dropped the M4A1')
        print()
    if command == 'drop Glock':
        item = input('You dropped the G-18')
        print()
    if command == 'drop Revolver':
        item = input('You dropped the Gray Revolver')
        print()
    if command == 'drop Sniper Rifle':
        item = input('You dropped the BA-SR')
        print()
    if command == 'drop AR-15 Rifle':
        item = input('You dropped the Blue AR-15 Rifle')
        print()
    if command == 'drop Grenade':
        item = input('You dropped the Grenade')
        print()
    if command == 'drop AT Rocket':
        item = input('You dropped the AT-14 Rocket Grenade')
        print()
    if command == 'drop 2x Scope':
        item = input('You dropped the 2x Scope')
        print()
    if command == 'drop 4x Scope':
        item = input('You dropped the 4x Scope')
        print()
    if command == 'drop 8x Scope':
        item = input('You drop the 8x Scope')
        print()
    if command == 'drop 16x Scope':
        item = input('You dropped the 16x Scope')
        print()
    if 'attach 2x' in command:
        item = input('You attach the 2x Scope')
        print()
    if 'attach 4x' in command:
        item = input('You attach the 4x Scope')
        print()
    if 'attach 8x' in command:
        item = input('You attach the 8x Scope')
        print()
    if 'attach 16x' in command:
        item = input('You attach the 16x Scope')
        print()
    if command in short_directions:
        position = short_directions.index(command)
        command = directions[position]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("This is the wrong way")
