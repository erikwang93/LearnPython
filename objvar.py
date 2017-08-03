class Person():
    population = 0

    def __init__(self,name):
        self.name = name
        print('(Initializing %s)' % self.name)
        Person.population += 1
    def __del__(self):
        print('%s says bye' % self.name)
        Person.population -= 1

        if Person.population == 0:
            print('I am the last one')
        else:
            print('There still %d person left.' % Person.population)

    def sayHi(self):
        '''Greeting by the person.

        Really, that's all it does'''
        print('Hi, my name is %s.' % self.name)

    def howMany(self):
        '''Prints the current population.'''
        if Person.population == 1:
            print('I am the only person here.')
        else:
            print('We have %d persons here.' % Person.population)

erik = Person('Erik')
erik.sayHi()
erik.howMany()

june = Person('June')
june.sayHi()
june.howMany()

erik.sayHi()
erik.howMany()
