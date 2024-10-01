
class House:
    def __init__(self,name, number_of_floors ):
        self.name = name                          # номер этажа
        self.number_of_floors = number_of_floors   #кол-во этажей

    def __len__(self):                           #кол-во этажей здания
        self.floors = self.number_of_floors
        return  self.number_of_floors


    def __str__(self):
        print (f'"Название": {self.name},',  "Количество этажей:", self.number_of_floors)


    def go_to(self, new_floor):   # на который нужно приехать.

        for i in range(1, new_floor + 1):

            if 1 <= new_floor  <= self.number_of_floors:
                print(i)
            else:
                print("Такого этажа не существует")
                break





h1 = House('ЖК Elbrus', 10)
h2 = House('ЖК Akathia', 20)

#h1.go_to(5)
#h2.go_to(10)
#print()
#h1.go_to(13)
#h2.go_to(4)
print()
h1.__str__()
h2.__str__()
print(len(h1))
print(len(h2))
