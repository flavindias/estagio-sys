#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import frameEdicaoEmpresa

class BoaApp(wx.App):
    def OnInit(self):
        self.main = frameEdicaoEmpresa.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    global modules
    modules ={u'frameEdicaoEmpresa': [1,
                         'Main frame of Application',
                         u'frameEdicaoEmpresa.py']}
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
