class TSO_State:
    def __init__(self, ok=True, scaner=True, paper=True, currencydetector=True, ink=True, pos=True):
        self.OK=ok
        self.SCANER=scaner
        self.PAPER=paper
        self.CURRENCYDETECTOR=currencydetector
        self.INK=ink
        self.POS=pos
