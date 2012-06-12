#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import frameCadastroFuncionario

class BoaApp(wx.App):
    def OnInit(self):
        self.main = frameCadastroFuncionario.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    global modules
    modules ={u'frameCadastroFuncionario': [1,
                               'Main frame of Application',
                               u'frameCadastroFuncionario.py']}
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
