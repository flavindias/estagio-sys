#Boa:Frame:frameLogin

import wx
import bridge

def create(parent):
    return frameLogin(parent)

[wxID_FRAMELOGIN, wxID_FRAMELOGINBOTAOACESSAR, wxID_FRAMELOGINCAIXALOGIN, 
 wxID_FRAMELOGINCAIXASENHA, wxID_FRAMELOGINCAIXAUSUARIO, 
 wxID_FRAMELOGINLINHATELALOGINSUPERIOR, wxID_FRAMELOGINLOGOCANTOIFPE, 
 wxID_FRAMELOGINLOGOIFPE, wxID_FRAMELOGINNOMESENHA, 
 wxID_FRAMELOGINNOMEUSUARIO, wxID_FRAMELOGINNUMEROVERSAO, 
 wxID_FRAMELOGINPANELLOGIN, 
] = [wx.NewId() for _init_ctrls in range(12)]

class frameLogin(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMELOGIN, name=u'frameLogin',
              parent=prnt, pos=wx.Point(700, 273), size=wx.Size(1040, 614),
              style=wx.DEFAULT_FRAME_STYLE,
              title=u'Est\xe1gio Curricular - Bem vindo!')
        self.SetClientSize(wx.Size(1024, 576))
        self.SetIcon(wx.Icon(u'./Graficos/icone.ico',
              wx.BITMAP_TYPE_ICO))
        self.Center(wx.BOTH)
        self.SetMaxSize(wx.Size(1040, 614))
        self.SetMinSize(wx.Size(1040, 614))

        self.panelLogin = wx.Panel(id=wxID_FRAMELOGINPANELLOGIN,
              name=u'panelLogin', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(1024, 576), style=wx.TAB_TRAVERSAL)
        self.panelLogin.Center(wx.BOTH)
        self.panelLogin.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.logoIFPE = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/logo.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMELOGINLOGOIFPE, name=u'logo',
              parent=self.panelLogin, pos=wx.Point(8, 8), size=wx.Size(175, 70),
              style=0)

        self.linhaTelaLoginSuperior = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/LinhaBoasVindas.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMELOGINLINHATELALOGINSUPERIOR,
              name=u'linhaTelaLoginSuperior', parent=self.panelLogin,
              pos=wx.Point(0, 80), size=wx.Size(1024, 21), style=0)

        self.LogoCantoIFPE = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/logoBG.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMELOGINLOGOCANTOIFPE,
              name=u'LogoCantoIFPE', parent=self.panelLogin, pos=wx.Point(856,
              352), size=wx.Size(168, 227), style=0)

        self.caixaLogin = wx.StaticBox(id=wxID_FRAMELOGINCAIXALOGIN,
              label=u'Login:', name=u'caixaLogin', parent=self.panelLogin,
              pos=wx.Point(328, 298), size=wx.Size(368, 224), style=0)

        self.nomeUsuario = wx.StaticText(id=wxID_FRAMELOGINNOMEUSUARIO,
              label=u'Nome de usu\xe1rio:', name=u'nomeUsuario',
              parent=self.panelLogin, pos=wx.Point(345, 336), size=wx.Size(85,
              13), style=0)

        self.caixaUsuario = wx.TextCtrl(id=wxID_FRAMELOGINCAIXAUSUARIO,
              name=u'caixaUsuario', parent=self.panelLogin, pos=wx.Point(352,
              362), size=wx.Size(320, 21), style=0, value=u'')

        self.nomeSenha = wx.StaticText(id=wxID_FRAMELOGINNOMESENHA,
              label=u'Senha:', name=u'nomeSenha', parent=self.panelLogin,
              pos=wx.Point(345, 415), size=wx.Size(35, 13), style=0)

        self.caixaSenha = wx.TextCtrl(id=wxID_FRAMELOGINCAIXASENHA,
              name=u'caixaSenha', parent=self.panelLogin, pos=wx.Point(352,
              441), size=wx.Size(320, 21), style=wx.TE_PASSWORD, value=u'')
        self.caixaSenha.Bind(wx.EVT_TEXT_ENTER, self.OnCaixaSenhaTextEnter,
              id=wxID_FRAMELOGINCAIXASENHA)

        self.botaoAcessar = wx.Button(id=wxID_FRAMELOGINBOTAOACESSAR,
              label=u'Acessar', name=u'botaoAcessar', parent=self.panelLogin,
              pos=wx.Point(594, 483), size=wx.Size(75, 23), style=0)

        self.numeroVersao = wx.StaticText(id=wxID_FRAMELOGINNUMEROVERSAO,
              label=u'vers\xe3o 1.0.0.0', name=u'numeroVersao', parent=self,
              pos=wx.Point(948, 560), size=wx.Size(73, 13), style=0)
        self.numeroVersao.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.numeroVersao.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.NORMAL,
              False, u'Tahoma'))

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnCaixaSenhaTextEnter(self, event):
        event.Skip()
