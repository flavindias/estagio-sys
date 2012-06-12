#!/usr/bin/env python
#Boa:App:BoaApp

import wx
#importa todos os Frames
import FrameLogin
import frameAdm
import frameGerenciamentoAluno
import frameCadastroAluno
import frameEdicaoAluno
import frameGerenciamentoEmpresa
import frameGerenciamentoFuncionario

class FrameLoginApp(wx.App):
    def OnInit(self):
        self.main = FrameLogin.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def mainAppLogin():
    global modules
    modules ={u'FrameLogin': [1, 'Main frame of Application', u'FrameLogin.py']}
    application = FrameLoginApp(0)
    application.MainLoop()

class frameAdmApp(wx.App):
    def OnInit(self):
        self.main = frameAdm.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True
    
def mainAppADM():
    global modules
    modules ={u'frameAdm': [1, 'Main frame of Application', u'frameAdm.py']}
    application = frameAdmApp(0)
    application.MainLoop()
    
class frameGerenciamentoAlunoApp(wx.App):
    def OnInit(self):
        self.main = frameGerenciamentoAluno.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True
def mainAppGerenciamentoAluno():
    global modules
    modules ={u'frameGerenciamentoAluno': [1, 'Main frame of Application', u'frameGerenciamentoAluno.py']}
    application = frameGerenciamentoAlunoApp(0)
    application.MainLoop()

class frameGerenciamentoEmpresaApp(wx.App):
    def OnInit(self):
        self.main = frameGerenciamentoEmpresa.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True
def mainAppGerenciamentoEmpresa():
    global modules
    modules ={u'frameGerenciamentoEmpresa': [1, 'Main frame of Application', u'frameGerenciamentoEmpresa.py']}
    application = frameGerenciamentoEmpresaApp(0)
    application.MainLoop()

class frameGerenciamentoFuncionarioApp(wx.App):
    def OnInit(self):
        self.main = frameGerenciamentoFuncionario.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True
def mainAppGerenciamentoFuncionario():
    global modules
    modules ={u'frameGerenciamentoFuncionario': [1, 'Main frame of Application', u'frameGerenciamentoFuncionario.py']}
    application = frameGerenciamentoFuncionarioApp(0)
    application.MainLoop()



