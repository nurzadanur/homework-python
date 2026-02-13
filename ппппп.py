class Passenger:
    def __init__(self, start_floor, target_floor):
        self.start_floor = start_floor
        self.target_floor = target_floor


    def introduce(self):
        print(f" я стою на {self.start_floor} этаже и хочу на {self.target_floor} этаж ")


class Elevator:
    def __init__(self, max_floor, capacity):
        self.max_floor = max_floor
        self.capacity = capacity
        self.current_floor = 1
        self.direction = 1
        self.passengers = []

for  in
    def drop_off(self):
        print("высадка пассажиров ")

    def pick_up(self):
        print("посадка пассажиров ")

    def move(self):
        print("лифт двигается")

ppl = Passenger(3, 5)
ppl2 = Passenger(4, 6)
ppl3 = Passenger(5, 7)
ppl4 = Passenger(6, 8)
ppl5 = Passenger(7, 9)
ppl6 = Passenger(8, 10)
ppl7 = Passenger(9, 1)
ppl8 = Passenger(10, 2)
ppl9 = Passenger(1, 3)
passengers = [ppl, ppl2, ppl3, ppl4, ppl5, ppl6, ppl7, ppl8, ppl9]

elevator = Elevator(10, 4)
elevator.drop_off()
elevator.pick_up(passengers)
elevator.move()



elevator = Elevator(10, 4)

elevator.drop_off()
elevator.pick_up()
elevator.move()

for person in passengers:
    person.introduce()
