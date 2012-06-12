#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import frameAdm

class BoaApp(wx.App):
    def OnInit(self):
        self.main = frameAdm.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True
    
def main():
    global modules
    modules ={u'frameAdm': [1, 'Main frame of Application', u'frameAdm.py']}
    application = BoaApp(0)
    application.MainLoop()


if __name__ == '__main__':
    main()
