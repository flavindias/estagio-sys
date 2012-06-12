#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import frameGerenciamentoEmpresa


class BoaApp(wx.App):
    def OnInit(self):
        self.main = frameGerenciamentoEmpresa.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True
def main():
    global modules
    modules ={u'frameGerenciamentoEmpresa': [1, 'Main frame of Application', u'frameGerenciamentoEmpresa.py']}
    application = BoaApp(0)
    application.MainLoop()


if __name__ == '__main__':
    main()
