#1
from functools import wraps
import time
import random

#задание
def is_alive(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        hero = args[0]
        if hero.health <= 0:
            print(f"{hero.name} мертв и не может действовать!")
            return None
        return func(*args, **kwargs)
    return wrapper


def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Начало действия: {func.__name__}")
        result = func(*args, **kwargs)
        print("[LOG] Действие завершено")
        return result
    return wrapper


class Hero:
    def __init__(self, name, hero_class):
        self.name = name
        self.hero_class = hero_class

        if hero_class == "волшебник":
            self.health = 60
            self.mana = 50
        elif hero_class == "воин":
            self.health = 100
            self.mana = 10
        else:
            raise ValueError("Неизвестный класс героя")

        self.spells_names = {}
        self.items = {}

    @is_alive
    def attack(self, damage):
        print(f"{self.name} нанес урон: {damage}")

    @log_action
    def heal(self, amount):
        self.health += amount
        print(f"{self.name} восстановил {amount} здоровья. Текущее здоровье: {self.health}")

    @is_alive
    def cast_spell(self, spell_name):
        if spell_name not in self.spells_names:
            print("Заклинание не изучено!")
            return

        spell = self.spells_names[spell_name]

        if self.mana < spell["mana_cost"]:
            print("Недостаточно маны!")
            return

        self.mana -= spell["mana_cost"]
        print(f"{self.name} использует {spell_name}")

        if spell["attack_damage"] > 0:
            print(f"Урон: {spell['attack_damage']}")

        if spell["health_increase"] > 0:
            self.health += spell["health_increase"]
            print(f"Лечение: {spell['health_increase']}")

    def add_spell(self, spell_name, mana_cost, attack_damage, health_increase):
        self.spells_names[spell_name] = {
            "mana_cost": mana_cost,
            "attack_damage": attack_damage,
            "health_increase": health_increase
        }

    def add_item(self, item_name, stat, value):
        if len(self.items) >= 6:
            print("Максимум 6 предметов!")
            return

        self.items[item_name] = {stat: value}

        if stat == "health":
            self.health += value
        elif stat == "mana":
            self.mana += value


#самостоятельная
#пасхальный буст здоровья (x2)
def easter_health_boost(duration):
    def decorator(func):
        @wraps(func)
        def wrapper(hero, *args, **kwargs):
            original_health = hero.health
            hero.health *= 2
            print(f"[EVENT] Здоровье увеличено: {hero.health}")

            result = func(hero, *args, **kwargs)

            time.sleep(duration)

            hero.health = original_health
            print(f"[EVENT] Эффект здоровья закончился: {hero.health}")

            return result
        return wrapper
    return decorator


#пасхальный буст маны (×1.5 + 5 для волшебников)
def easter_mana_boost(duration):
    def decorator(func):
        @wraps(func)
        def wrapper(hero, *args, **kwargs):
            original_mana = hero.mana

            if hero.hero_class == "волшебник":
                hero.mana = int(hero.mana * 1.5) + 5
                print(f"[EVENT] Мана увеличена: {hero.mana}")

            result = func(hero, *args, **kwargs)

            time.sleep(duration)

            hero.mana = original_mana
            print(f"[EVENT] Эффект маны закончился: {hero.mana}")

            return result
        return wrapper
    return decorator


#мой декоратор
#добавляет шанс критического удара (x2 урон)
def critical_hit(func):
    @wraps(func)
    def wrapper(hero, damage, *args, **kwargs):
        if random.random() < 0.3:
            damage *= 2
            print("[CRIT] Критический урон!")
        return func(hero, damage, *args, **kwargs)
    return wrapper


Hero.attack = critical_hit(Hero.attack)


@easter_health_boost(2)
def fight(hero):
    print(f"{hero.name} сражается с бустом здоровья!")


@easter_mana_boost(2)
def cast(hero):
    print(f"{hero.name} колдует с бустом маны!")



hero = Hero("Гэндальф", "волшебник")

hero.add_spell("Огонь", 10, 30, 0)

hero.attack(10)
hero.heal(5)

fight(hero)
cast(hero)

hero.health = 0
hero.attack(10)  # не сработает
hero.cast_spell("Огонь")  # не сработает