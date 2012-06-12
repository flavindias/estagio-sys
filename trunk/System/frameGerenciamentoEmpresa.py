#Boa:Frame:frameGerenciamentoEmpresa

import wx
import bridge

def create(parent):
    return frameGerenciamentoEmpresa(parent)

[wxID_FRAMEGERENCIAMENTOEMPRESA, wxID_FRAMEGERENCIAMENTOEMPRESABOTAOADICIONAR, 
 wxID_FRAMEGERENCIAMENTOEMPRESABOTAOEDITAR, 
 wxID_FRAMEGERENCIAMENTOEMPRESABOTAOEXCLUIR, 
 wxID_FRAMEGERENCIAMENTOEMPRESABOTAOVOLTA, 
 wxID_FRAMEGERENCIAMENTOEMPRESABUTAOPESQUISAR, 
 wxID_FRAMEGERENCIAMENTOEMPRESALINHATELAINICIOSUPERIOR, 
 wxID_FRAMEGERENCIAMENTOEMPRESALOGOCANTOIFPE, 
 wxID_FRAMEGERENCIAMENTOEMPRESALOGOIFPE, 
 wxID_FRAMEGERENCIAMENTOEMPRESANOMECADASTRAR, 
 wxID_FRAMEGERENCIAMENTOEMPRESANOMEEDITAR, 
 wxID_FRAMEGERENCIAMENTOEMPRESANOMEEXCLUIR, 
 wxID_FRAMEGERENCIAMENTOEMPRESANOMEPESQUISAR, 
 wxID_FRAMEGERENCIAMENTOEMPRESAPAINELHOME, 
] = [wx.NewId() for _init_ctrls in range(14)]

class frameGerenciamentoEmpresa(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEGERENCIAMENTOEMPRESA,
              name=u'frameGerenciamentoEmpresa', parent=prnt, pos=wx.Point(700,
              273), size=wx.Size(1040, 614), style=wx.DEFAULT_FRAME_STYLE,
              title=u'Est\xe1gio Curricular - Gerenciamento Empresarial')
        self.SetClientSize(wx.Size(1024, 576))
        self.SetIcon(wx.Icon(u'./Graficos/icone.ico',
              wx.BITMAP_TYPE_ICO))
        self.Center(wx.BOTH)
        self.SetMaxSize(wx.Size(1040, 614))
        self.SetMinSize(wx.Size(1040, 614))

        self.painelHome = wx.Panel(id=wxID_FRAMEGERENCIAMENTOEMPRESAPAINELHOME,
              name=u'painelHome', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(1024, 576),
              style=wx.STATIC_BORDER | wx.TAB_TRAVERSAL)
        self.painelHome.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.logoIFPE = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/logo.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERENCIAMENTOEMPRESALOGOIFPE,
              name=u'logoIFPE', parent=self.painelHome, pos=wx.Point(8, 8),
              size=wx.Size(175, 70), style=0)

        self.logoCantoIFPE = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/logoBG.png',
              wx.BITMAP_TYPE_PNG),
              id=wxID_FRAMEGERENCIAMENTOEMPRESALOGOCANTOIFPE,
              name=u'logoCantoIFPE', parent=self.painelHome, pos=wx.Point(856,
              352), size=wx.Size(168, 227), style=0)

        self.linhaTelaInicioSuperior = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/LinhaGerenciamentoEmpresarial.png',
              wx.BITMAP_TYPE_PNG),
              id=wxID_FRAMEGERENCIAMENTOEMPRESALINHATELAINICIOSUPERIOR,
              name=u'linhaTelaInicioSuperior', parent=self.painelHome,
              pos=wx.Point(0, 80), size=wx.Size(1024, 25), style=0)

        self.botaoAdicionar = wx.BitmapButton(bitmap=wx.Bitmap(u'./Graficos/botao_enter_add.png',
              wx.BITMAP_TYPE_PNG),
              id=wxID_FRAMEGERENCIAMENTOEMPRESABOTAOADICIONAR,
              name=u'botaoAdicionar', parent=self.painelHome, pos=wx.Point(40,
              209), size=wx.Size(184, 184), style=wx.BU_AUTODRAW)
        self.botaoAdicionar.SetLabel(u'Cadastrar')
        self.botaoAdicionar.SetHelpText(u'Bot\xe3o para cadastrar novos alunos')
        self.botaoAdicionar.Bind(wx.EVT_BUTTON, self.OnBotaoAdicionarButton,
              id=wxID_FRAMEGERENCIAMENTOEMPRESABOTAOADICIONAR)

        self.botaoEditar = wx.BitmapButton(bitmap=wx.Bitmap(u'./Graficos/botao_enter_edt.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERENCIAMENTOEMPRESABOTAOEDITAR,
              name=u'botaoEditar', parent=self.painelHome, pos=wx.Point(295,
              209), size=wx.Size(184, 184), style=wx.BU_AUTODRAW)
        self.botaoEditar.SetLabel(u'Editar')
        self.botaoEditar.SetHelpText(u'Bot\xe3o para editar cadastro de alunos')
        self.botaoEditar.Bind(wx.EVT_BUTTON, self.OnBotaoEditarButton,
              id=wxID_FRAMEGERENCIAMENTOEMPRESABOTAOEDITAR)

        self.botaoExcluir = wx.BitmapButton(bitmap=wx.Bitmap(u'./Graficos/botao_enter_del.png',
              wx.BITMAP_TYPE_PNG),
              id=wxID_FRAMEGERENCIAMENTOEMPRESABOTAOEXCLUIR,
              name=u'botaoExcluir', parent=self.painelHome, pos=wx.Point(550,
              209), size=wx.Size(184, 184), style=wx.BU_AUTODRAW)
        self.botaoExcluir.SetLabel(u'Excluir')
        self.botaoExcluir.SetHelpText(u'Bot\xe3o para excluir cadastro de alunos')
        self.botaoExcluir.Bind(wx.EVT_BUTTON, self.OnBotaoExcluirButton,
              id=wxID_FRAMEGERENCIAMENTOEMPRESABOTAOEXCLUIR)

        self.butaoPesquisar = wx.BitmapButton(bitmap=wx.Bitmap(u'./Graficos/botao_enter_sch.png',
              wx.BITMAP_TYPE_PNG),
              id=wxID_FRAMEGERENCIAMENTOEMPRESABUTAOPESQUISAR,
              name=u'butaoPesquisar', parent=self.painelHome, pos=wx.Point(789,
              210), size=wx.Size(184, 184), style=wx.BU_AUTODRAW)
        self.butaoPesquisar.SetLabel(u'Pesquisar')
        self.butaoPesquisar.SetHelpText(u'Bot\xe3o para pesquisar alunos')
        self.butaoPesquisar.Bind(wx.EVT_BUTTON, self.OnButaoPesquisarButton,
              id=wxID_FRAMEGERENCIAMENTOEMPRESABUTAOPESQUISAR)

        self.nomeCadastrar = wx.StaticText(id=wxID_FRAMEGERENCIAMENTOEMPRESANOMECADASTRAR,
              label=u'Cadastrar', name=u'nomeCadastrar', parent=self.painelHome,
              pos=wx.Point(81, 418), size=wx.Size(91, 26), style=0)
        self.nomeCadastrar.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Myriad Pro'))

        self.nomeEditar = wx.StaticText(id=wxID_FRAMEGERENCIAMENTOEMPRESANOMEEDITAR,
              label=u'Editar', name=u'nomeEditar', parent=self.painelHome,
              pos=wx.Point(357, 418), size=wx.Size(57, 26), style=0)
        self.nomeEditar.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Myriad Pro'))

        self.nomeExcluir = wx.StaticText(id=wxID_FRAMEGERENCIAMENTOEMPRESANOMEEXCLUIR,
              label=u'Excluir', name=u'nomeExcluir', parent=self.painelHome,
              pos=wx.Point(614, 418), size=wx.Size(63, 26), style=0)
        self.nomeExcluir.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Myriad Pro'))

        self.nomePesquisar = wx.StaticText(id=wxID_FRAMEGERENCIAMENTOEMPRESANOMEPESQUISAR,
              label=u'Pesquisar', name=u'nomePesquisar', parent=self.painelHome,
              pos=wx.Point(846, 418), size=wx.Size(90, 26), style=0)
        self.nomePesquisar.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Myriad Pro'))

        self.botaoVolta = wx.BitmapButton(bitmap=wx.Bitmap(u'./Graficos/botao_voltar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERENCIAMENTOEMPRESABOTAOVOLTA,
              name=u'botaoVolta', parent=self.painelHome, pos=wx.Point(952, 13),
              size=wx.Size(57, 57), style=wx.BU_AUTODRAW)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnBotaoAdicionarButton(self, event):

        event.Skip()

    def OnBotaoEditarButton(self, event):
        event.Skip()

    def OnBotaoExcluirButton(self, event):
        event.Skip()

    def OnButaoPesquisarButton(self, event):
        event.Skip()
