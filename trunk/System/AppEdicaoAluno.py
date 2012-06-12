#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import frameEdicaoAluno

class BoaApp(wx.App):
    def OnInit(self):
        self.main = frameEdicaoAluno.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    global modules
    modules ={u'frameEdicaoAluno': [1, 'Main frame of Application', u'frameEdicaoAluno.py']}
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
