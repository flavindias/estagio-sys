#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import frameEdicaoFuncionario

class BoaApp(wx.App):
    def OnInit(self):
        self.main = frameEdicaoFuncionario.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    global modules
    modules ={u'frameEdicaoFuncionario': [1,
                             'Main frame of Application',
                             u'frameEdicaoFuncionario.py']}
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
