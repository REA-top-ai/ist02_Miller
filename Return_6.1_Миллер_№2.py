def get_force(mass, acceleration):
    return mass * acceleration

train_mass = 22680
train_acceleration = 10

train_force = get_force(train_mass, train_acceleration)
print(train_force)

print(f"Поезд GE поставляет {train_force} ньютонов силы")


def get_energy(mass, c=3 * 10**8):
    return mass * c**2

bomb_mass = 1
bomb_energy = get_energy(bomb_mass)

print(f"1 кг бомбы составляет {bomb_energy} Джоулей")


def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    work = force * distance
    return work

train_distance = 100
train_work = get_work(train_mass, train_acceleration, train_distance)

print(f"Поезд выполняет {train_work} Джоулей за {train_distance} метров.")
