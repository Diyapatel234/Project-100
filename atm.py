class atm(object):
    def __init__(self, CardNumber, pinNumber):
        self.CardNumber = CardNumber
        self.pinNumber = pinNumber

    def on(self):
        print('On')


    def off(self):
        print('Off')

    def CardNumber(self):
        print('Payment accepted')

    def Card(self):
        print('Card not accepted')

HSBC = atm('047689576987','*****')
print(HSBC.CardNumber)