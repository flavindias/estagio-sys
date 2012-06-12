#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import frameCadastroAluno

class BoaApp(wx.App):
    def OnInit(self):
        self.main = frameCadastroAluno.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    global modules
    modules ={u'frameCadastroAluno': [1, 'Main frame of Application', u'frameCadastroAluno.py']}
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
