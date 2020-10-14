'''{lista = [{'a': ['a1', 'a2', 'a3'],
           'b': ['b1', 'b2', 'b3'],
           'c': ['c1', 'c2']},
          {'d': ['d1', 'd2'],
           'e': ['e1']},
          {'f': ['f1', 'f2', 'f3'],
           'g': ['g1']}}
'''


class Turntable ():
    def __init__(self, parameters):
        self.parameters = parameters
        self.turntable = self.go(self.parameters)

    def go(self, lista):
        table_a = self.make_table_a(lista)
        if len(table_a) == 0:
            dummy = [dict() for _ in lista]
            return[dummy]
        suits = self.compose_suits(table_a)
        turntable = self.reapply(suits)
        return turntable

    def make_table_a(self, lista):
        table_a = []
        for machine_index in range(len(lista)):
            for parameter in lista[machine_index]:
                parameter_indexed = '//'.join((str(machine_index), parameter))
                table_a.append([parameter_indexed, lista[machine_index][parameter]])
        return table_a

    def compose_suits(self, table_a):
        suits = []
        suit = dict()
        suit, suits = self.cycle(suit, suits, table_a)
        return suits

    def cycle(self, suit, suits, table_a):
        suit, suits = suit, suits
        for turn in range(len(table_a[0][1])): #dla każdej wartości parametru
            parameter = table_a[0][0]
            value = table_a[0][1][turn]
            if len(table_a) > 1:
                suit.update({parameter: value})
                suit_returned, suits = self.cycle(suit, suits, table_a[1:])
            else:
                suit.update({parameter: value})
                suits.append(suit.copy())
                #suit = dict()
        return suit, suits

    def reapply(self, suits):
        turntable = []
        for suit in suits:
            turn_suits = []
            for machine_index in range(len(self.parameters)):
                machine_suit = dict()
                for param in suit:
                    if int(param.split('//')[0]) == machine_index:
                        machine_suit.update({param.split('//')[1]: suit[param]})
                turn_suits.append(machine_suit)
            turntable.append(turn_suits)
        return turntable

