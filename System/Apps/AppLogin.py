#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import FrameLogin

class BoaApp(wx.App):
    def OnInit(self):
        self.main = FrameLogin.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    global modules
    modules ={u'FrameLogin': [1, 'Main frame of Application', u'FrameLogin.py']}
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
