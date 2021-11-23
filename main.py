import wx
import noname


class MainFrame(noname.MyFrame2):
    def __init__(self, parent):
        noname.MyFrame2.__init__(self, parent)

    def HideOrShow(self, event):
        if self.AntalMedlemmerBox.GetCurrentSelection() == 0:
            self.Navn4.Hide()
        elif self.AntalMedlemmerBox.GetCurrentSelection() == 1:
            self.Navn4.Show()

    def GemNavne(self, event):
        print(f"Holdnavnet er: {self.HoldNavnBox.GetValue()}")
        print(self.Navn1.GetValue())
        print(self.Navn2.GetValue())
        print(self.Navn3.GetValue())
        if self.AntalMedlemmerBox.GetCurrentSelection() == 1:
            print(self.Navn4.GetValue())
        #Nu skal vi indsætte dem i databasen

    """
        self.txt = ""
        self.karakterer = "ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅabcdefghijklmnopqrstuvwxyzæøå !?."

    def vKrypter( self, event ):
        self.txt = self.klartxt.GetValue()

        def kryptering():
            konverter = ""
            key = self.trin1.GetSelection() + 3
            for c in self.txt:
                k_index = self.karakterer.find(c)
                if k_index == -1:
                    konverter += c
                k_index += key
                if k_index >= len(self.karakterer):
                    k_index -= len(self.karakterer)
                elif k_index < 0:
                    k_index += len(self.karakterer)
                konverter += self.karakterer[k_index]
            return konverter

        def set_key():
            key = 0
            while True:
                key += int(self.trin1.GetSelection)
                print(key)

        self.ciffertxt.SetValue(kryptering())
        self.klartxt.Clear()
    def vDekrypter( self, event ):
        self.txt = self.ciffertxt.GetValue()

        def dkryptering():
            konverter = ""
            key = self.trin2.GetSelection() + 3
            for c in self.txt:
                k_index = self.karakterer.find(c)
                if k_index == -1:
                    konverter += c
                k_index -= key
                if k_index >= len(self.karakterer):
                    k_index -= len(self.karakterer)
                elif k_index < 0:
                    k_index += len(self.karakterer)
                konverter += self.karakterer[k_index]
            return konverter

        def set_key():
            key = 0
            while True:
                key += int(self.trin2.GetSelection)
                print(key)

        self.klartxt.SetValue(dkryptering())
        self.ciffertxt.Clear()
        """

    #def afslut( self, event):
     #   exit(0)

app = wx.App(False)
frame = MainFrame(None)
frame.Show(True)
app.MainLoop()
