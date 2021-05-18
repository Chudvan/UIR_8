FILE_NAME = 'log.txt'


class TSO_State:
    @staticmethod
    def create_id(id):
        try:
            with open(FILE_NAME, 'r') as f:
                prev_id = int(f.read())
                id = prev_id + 1
        except (FileNotFoundError, ValueError):
            with open(FILE_NAME, 'w') as f:
                f.write(str(id))
        return id

    def update_id(self):
        with open(FILE_NAME, 'w+') as f:
            f.write(str(self.id))
        self.id += 1

    def __init__(self, ok=True, scaner=True, paper=True, currencydetector=True,
                 ink=True, pos=True, number=5, id=1):
        self.OK=ok
        self.SCANER=scaner
        self.PAPER=paper
        self.CURRENCYDETECTOR=currencydetector
        self.INK=ink
        self.POS=pos

        self.TSO_number = number
        self.id = self.create_id(id)

        self.CARD = True
        self.PCARD = True
        self.CASH = True
