#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import frameGerenciamentoAluno

class BoaApp(wx.App):
    def OnInit(self):
        self.main = frameGerenciamentoAluno.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True
def main():
    global modules
    modules ={u'frameGerenciamentoAluno': [1, 'Main frame of Application', u'frameGerenciamentoAluno.py']}
    application = BoaApp(0)
    application.MainLoop()


if __name__ == '__main__':
    main()
