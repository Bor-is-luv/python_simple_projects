import random


class Forest:
    def __init__(self, herbi, beasts, grass, trees):
        self.herbi = herbi
        self.beasts = beasts
        self.grass = grass
        self.trees = trees

    def __str__(self):
        value = ''
        for var in self.herbi, self.beasts, self.grass, self.trees:
            for item in var:
                value += str(item)
                value += '\n'

        return value


class Animal:
    def __init__(self, name, kind, hunger, weight):
        self.name = name
        self.kind = kind
        self.hunger = hunger
        self.weight = weight

    def __str__(self):
        value = ''
        if isinstance(self, Beast):
            value += f'Name = {self.name}, Type = Beast, Hunger = {self.hunger},' \
                     f'Weight = {self.weight}'
        elif isinstance(self, Herbivore):
            value += f'Name = {self.name}, Type = Herbivore, Hunger = {self.hunger},' \
                     f'Weight = {self.weight},' \
                     f'Sort = {self.sort}'

        return value

    def find_and_eat(self, forest):
        if isinstance(self, Herbivore):
            print(f'{self} want to eat')
            for item in forest.grass:
                if self.sort == item.sort and self.hunger > 0 and item.edible:
                    print(f'{self} съел {item} grass')
                    forest.grass.remove(item)
                    self.hunger -= 1
                elif self.hunger == 0:
                    print(f'{self} наелся')
                    break

            if self.hunger > 0:
                for item in forest.trees:
                    if self.sort == item.sort and self.hunger > 0 and item.edible and item.fruit_count > 0:
                        print(f'{self} съел {item}')
                        if self.hunger > item.fruit_count:
                            self.hunger -= item.fruit_count
                        else:
                            self.hunger = 0

                        item.fruit_count = 0

                    elif self.hunger == 0:
                        print(f'{self} наелся')
                        break
            if self.hunger > 0: print(f'{self} не наелся')

        elif isinstance(self, Beast):
            print(f'{self} want to eat')
            for item in forest.herbi:
                if self.weight > item.weight and self.hunger > 0:
                    minus_hunger = round(item.weight/10)
                    print(f'{self} съел {item}')
                    forest.herbi.remove(item)
                    if self.hunger > minus_hunger:
                        self.hunger -= minus_hunger
                    else:
                        self.hunger = 0

                elif self.hunger == 0:
                    print(f"{self} наелся")
                    break

            if self.hunger > 0:
                print(f'{self} не наелся')


class Plant:
    def __init__(self,name, height, sort, edible):
        self.name = name
        self.height = height
        self.sort = sort
        self.edible = edible

    def __str__(self):
        value = ''
        if isinstance(self, Grass):
            value += f'Name = {self.name}, Type = Grass, Sort = {self.sort},' \
                     f'Edible = {self.edible}'
        elif isinstance(self, Tree):
            value += f'Name = {self.name}, Type = Tree, Sort = {self.sort},' \
                     f'Edible = {self.edible}, fruit count = {self.fruit_count}'

        return value


class Beast(Animal):
    def __init__(self,name, kind, hunger, weight, fang_length,
                 claw_length):
        super().__init__(name, kind, hunger, weight)
        self.fang_length = fang_length
        self.claw_length = claw_length


class Herbivore(Animal):
    def __init__(self, name, kind, hunger, weight, run_speed, sort):
        super().__init__(name, kind, hunger, weight)
        self.run_speed = run_speed
        self.sort = sort


class Grass(Plant):
    def __init__(self, name, height, sort, edible, one_year, color):
        super().__init__(name, height, sort, edible)
        self.one_year = one_year
        self.color = color


class Tree(Plant):
    def __init__(self, name, height, sort, edible, fruit_color,
                 leafs_color, fruit_count):
        super().__init__(name, height, sort, edible)
        self.fruit_color = fruit_color
        self.leafs_color = leafs_color
        self.fruit_count = fruit_count


def main():
    if __name__ == "__main__":
        beasts_count = 10
        herbi_count = 20
        grass_count = 100
        trees_count = 10

        beasts = []
        herbi = []
        grass = []
        trees = []
        beast_kind = ('Wolf', 'Lion', 'Tiger', 'Bear')
        herbi_kind = ('Cow', 'Sheep', 'Rabbit')
        sort = ('Raspberries', 'Pear', 'Watermelon')
        color = 'red', 'green', 'blue', 'black', 'yellow'

        num = 0
        for i in range(beasts_count):
            num += 1
            rand_hunger = random.randint(0, 100)
            rand_weight = random.randint(0, 300)
            rand_kind = beast_kind[random.randint(0, 3)]
            rand_fang_length = random.randint(0, 10)
            rand_claw_length = random.randint(0, 10)
            beasts.append(Beast(num, rand_kind, rand_hunger,
                                rand_weight, rand_fang_length,
                                rand_claw_length))

        num = 0
        for i in range(herbi_count):
            num += 1
            rand_hunger = random.randint(0, 100)
            rand_weight = random.randint(0, 300)
            rand_kind = herbi_kind[random.randint(0, 2)]
            rand_speed = random.randint(0, 30)
            rand_sort = sort[random.randint(0, 2)]
            herbi.append(Herbivore(num, rand_kind, rand_hunger, rand_weight,
                                   rand_speed, rand_sort))

        num = 0
        for i in range(grass_count):
            num += 1
            rand_height = random.randint(0, 50)
            rand_sort = sort[random.randint(0, 2)]
            if random.random() > 0.5:
                rand_edible = True
            else:
                rand_edible = False

            if random.random() > 0.5:
                one_year = True
            else:
                one_year = False

            rand_color = color[random.randint(0, 4)]

            grass.append(Grass(num, rand_height, rand_sort,
                               rand_edible, one_year,
                               rand_color))

        num = 0
        for i in range(trees_count):
            num += 1
            rand_height = random.randint(0, 60)
            rand_sort = sort[random.randint(0, 2)]
            if random.random() > 0.5:
                rand_edible = True
            else:
                rand_edible = False

            rand_fruit_color = color[random.randint(0, 4)]
            rand_leafs_color = color[random.randint(0, 4)]
            rand_fruit_count = random.randint(0, 50)
            trees.append(Tree(num, rand_height, rand_sort,
                              rand_edible,
                              rand_fruit_color,
                              rand_leafs_color, rand_fruit_count))

        forest = Forest(herbi, beasts, grass, trees)

        print(forest)

        forest.herbi[10].find_and_eat(forest)
        forest.beasts[7].find_and_eat(forest)

        print(forest)


if __name__ == "__main__":
    main()
