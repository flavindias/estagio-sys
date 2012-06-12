#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import frameGerenciamentoFuncionario

class BoaApp(wx.App):
    def OnInit(self):
        self.main = frameGerenciamentoFuncionario.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True
def main():
    global modules
    modules ={u'frameGerenciamentoFuncionario': [1, 'Main frame of Application', u'frameGerenciamentoFuncionario.py']}
    application = BoaApp(0)
    application.MainLoop()


if __name__ == '__main__':
    main()
