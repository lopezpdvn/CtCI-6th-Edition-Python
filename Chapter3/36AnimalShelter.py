class Animal: pass
class Dog(Animal): pass
class Cat(Animal): pass

class Shelter:
    def __init__(self):
        from collections import deque
        self.cats = deque()
        self.dogs = deque()
        self.count_anml = 0
        self.i_anml = 0

    def enqueue(self, animal):
        if isinstance(animal, Dog):
            self.dogs.append((self.i_anml, animal))
        else:
            self.cats.append((self.i_anml, animal))
        self.i_anml += 1
        self.count_anml += 1
        return self.count_anml

    def dequeue(self):
        if not self.count_anml: raise Exception()
        if not self.cats:
            animal = self.dogs.popleft()[1]
        elif not self.dogs:
            animal = self.cats.popleft()[1]
        else:
            animal = (self.dogs.popleft()[1]
                if self.dogs[0][0] < self.cats[0][0]
                else self.cats.popleft()[1])
        self.count_anml -= 1
        return animal

    def dequeue_dog(self):
        anml = self.dogs.popleft()[1]
        self.count_anml -= 1
        return anml

    def dequeue_cat(self):
        anml = self.cats.popleft()[1]
        self.count_anml -= 1
        return anml

shelter = Shelter()
assert shelter.enqueue(Dog()) == 1
assert shelter.enqueue(Dog()) == 2
assert shelter.enqueue(Cat()) == 3
assert shelter.enqueue(Dog()) == 4
assert isinstance(shelter.dequeue(), Dog)
assert isinstance(shelter.dequeue(), Dog)
assert isinstance(shelter.dequeue(), Cat)
assert isinstance(shelter.dequeue(), Dog)
