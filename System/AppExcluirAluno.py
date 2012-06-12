#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import frameExcluirAluno

class BoaApp(wx.App):
    def OnInit(self):
        self.main = frameExcluirAluno.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    global modules
    modules ={u'frameExcluirAluno': [1,
                        'Main frame of Application',
                        u'frameExcluirAluno.py']}
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
