#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import frameExcluirEmpresa

class BoaApp(wx.App):
    def OnInit(self):
        self.main = frameExcluirEmpresa.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    global modules
    modules ={u'frameExcluirEmpresa': [1,
                          'Main frame of Application',
                          u'frameExcluirEmpresa.py']}
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
