#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import frameExcluirFuncionario

class BoaApp(wx.App):
    def OnInit(self):
        self.main = frameExcluirFuncionario.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    global modules
    modules ={u'frameExcluirFuncionario': [1,
                              'Main frame of Application',
                              u'frameExcluirFuncionario.py']}
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
