#Boa:Frame:frameGerenciamentoAluno

import wx
import bridge

def create(parent):
    return frameGerenciamentoAluno(parent)

[wxID_FRAMEGERENCIAMENTOALUNO, wxID_FRAMEGERENCIAMENTOALUNOBOTAOADICIONAR, 
 wxID_FRAMEGERENCIAMENTOALUNOBOTAOEDITAR, 
 wxID_FRAMEGERENCIAMENTOALUNOBOTAOEXCLUIR, 
 wxID_FRAMEGERENCIAMENTOALUNOBOTAOSAIR, 
 wxID_FRAMEGERENCIAMENTOALUNOBUTAOPESQUISAR, 
 wxID_FRAMEGERENCIAMENTOALUNOLINHATELAINICIOSUPERIOR, 
 wxID_FRAMEGERENCIAMENTOALUNOLOGOCANTOIFPE, 
 wxID_FRAMEGERENCIAMENTOALUNOLOGOIFPE, 
 wxID_FRAMEGERENCIAMENTOALUNONOMECADASTRAR, 
 wxID_FRAMEGERENCIAMENTOALUNONOMEEDITAR, 
 wxID_FRAMEGERENCIAMENTOALUNONOMEEXCLUIR, 
 wxID_FRAMEGERENCIAMENTOALUNONOMEPESQUISAR, 
 wxID_FRAMEGERENCIAMENTOALUNOPAINELHOME, 
] = [wx.NewId() for _init_ctrls in range(14)]

class frameGerenciamentoAluno(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEGERENCIAMENTOALUNO,
              name=u'frameGerenciamentoAluno', parent=prnt, pos=wx.Point(700,
              273), size=wx.Size(1040, 614), style=wx.DEFAULT_FRAME_STYLE,
              title=u'Est\xe1gio Curricular - Gerenciamento Estudantil')
        self.SetClientSize(wx.Size(1024, 576))
        self.SetIcon(wx.Icon(u'./Graficos/icone.ico',
              wx.BITMAP_TYPE_ICO))
        self.Center(wx.BOTH)
        self.SetMaxSize(wx.Size(1040, 614))
        self.SetMinSize(wx.Size(1040, 614))

        self.painelHome = wx.Panel(id=wxID_FRAMEGERENCIAMENTOALUNOPAINELHOME,
              name=u'painelHome', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(1024, 576),
              style=wx.STATIC_BORDER | wx.TAB_TRAVERSAL)
        self.painelHome.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.logoIFPE = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/logo.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERENCIAMENTOALUNOLOGOIFPE,
              name=u'logoIFPE', parent=self.painelHome, pos=wx.Point(8, 8),
              size=wx.Size(175, 70), style=0)

        self.logoCantoIFPE = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/logoBG.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERENCIAMENTOALUNOLOGOCANTOIFPE,
              name=u'logoCantoIFPE', parent=self.painelHome, pos=wx.Point(856,
              352), size=wx.Size(168, 227), style=0)

        self.linhaTelaInicioSuperior = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/LinhaGerenciamentoEstudantil.png',
              wx.BITMAP_TYPE_PNG),
              id=wxID_FRAMEGERENCIAMENTOALUNOLINHATELAINICIOSUPERIOR,
              name=u'linhaTelaInicioSuperior', parent=self.painelHome,
              pos=wx.Point(0, 80), size=wx.Size(1024, 23), style=0)

        self.botaoAdicionar = wx.BitmapButton(bitmap=wx.Bitmap(u'./Graficos/botao_user_add.png',
              wx.BITMAP_TYPE_PNG),
              id=wxID_FRAMEGERENCIAMENTOALUNOBOTAOADICIONAR,
              name=u'botaoAdicionar', parent=self.painelHome, pos=wx.Point(40,
              209), size=wx.Size(184, 184), style=wx.BU_AUTODRAW)
        self.botaoAdicionar.SetLabel(u'Cadastrar')
        self.botaoAdicionar.SetHelpText(u'Bot\xe3o para cadastrar novos alunos')
        self.botaoAdicionar.Bind(wx.EVT_BUTTON, self.OnBotaoAdicionarButton,
              id=wxID_FRAMEGERENCIAMENTOALUNOBOTAOADICIONAR)

        self.botaoEditar = wx.BitmapButton(bitmap=wx.Bitmap(u'./Graficos/botao_user_edt.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERENCIAMENTOALUNOBOTAOEDITAR,
              name=u'botaoEditar', parent=self.painelHome, pos=wx.Point(295,
              209), size=wx.Size(184, 184), style=wx.BU_AUTODRAW)
        self.botaoEditar.SetLabel(u'Editar')
        self.botaoEditar.SetHelpText(u'Bot\xe3o para editar cadastro de alunos')
        self.botaoEditar.Bind(wx.EVT_BUTTON, self.OnBotaoEditarButton,
              id=wxID_FRAMEGERENCIAMENTOALUNOBOTAOEDITAR)

        self.botaoExcluir = wx.BitmapButton(bitmap=wx.Bitmap(u'./Graficos/botao_user_del.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERENCIAMENTOALUNOBOTAOEXCLUIR,
              name=u'botaoExcluir', parent=self.painelHome, pos=wx.Point(550,
              209), size=wx.Size(184, 184), style=wx.BU_AUTODRAW)
        self.botaoExcluir.SetLabel(u'Excluir')
        self.botaoExcluir.SetHelpText(u'Bot\xe3o para excluir cadastro de alunos')
        self.botaoExcluir.Bind(wx.EVT_BUTTON, self.OnBotaoExcluirButton,
              id=wxID_FRAMEGERENCIAMENTOALUNOBOTAOEXCLUIR)

        self.butaoPesquisar = wx.BitmapButton(bitmap=wx.Bitmap(u'./Graficos/botao_user_sch.png',
              wx.BITMAP_TYPE_PNG),
              id=wxID_FRAMEGERENCIAMENTOALUNOBUTAOPESQUISAR,
              name=u'butaoPesquisar', parent=self.painelHome, pos=wx.Point(789,
              210), size=wx.Size(184, 184), style=wx.BU_AUTODRAW)
        self.butaoPesquisar.SetLabel(u'Pesquisar')
        self.butaoPesquisar.SetHelpText(u'Bot\xe3o para pesquisar alunos')
        self.butaoPesquisar.Bind(wx.EVT_BUTTON, self.OnButaoPesquisarButton,
              id=wxID_FRAMEGERENCIAMENTOALUNOBUTAOPESQUISAR)

        self.nomeCadastrar = wx.StaticText(id=wxID_FRAMEGERENCIAMENTOALUNONOMECADASTRAR,
              label=u'Cadastrar', name=u'nomeCadastrar', parent=self.painelHome,
              pos=wx.Point(81, 418), size=wx.Size(91, 26), style=0)
        self.nomeCadastrar.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Myriad Pro'))

        self.nomeEditar = wx.StaticText(id=wxID_FRAMEGERENCIAMENTOALUNONOMEEDITAR,
              label=u'Editar', name=u'nomeEditar', parent=self.painelHome,
              pos=wx.Point(357, 418), size=wx.Size(57, 26), style=0)
        self.nomeEditar.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Myriad Pro'))

        self.nomeExcluir = wx.StaticText(id=wxID_FRAMEGERENCIAMENTOALUNONOMEEXCLUIR,
              label=u'Excluir', name=u'nomeExcluir', parent=self.painelHome,
              pos=wx.Point(614, 418), size=wx.Size(63, 26), style=0)
        self.nomeExcluir.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Myriad Pro'))

        self.nomePesquisar = wx.StaticText(id=wxID_FRAMEGERENCIAMENTOALUNONOMEPESQUISAR,
              label=u'Pesquisar', name=u'nomePesquisar', parent=self.painelHome,
              pos=wx.Point(846, 418), size=wx.Size(90, 26), style=0)
        self.nomePesquisar.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Myriad Pro'))

        self.botaoSair = wx.BitmapButton(bitmap=wx.Bitmap(u'./Graficos/botao_sair.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEGERENCIAMENTOALUNOBOTAOSAIR,
              name=u'botaoSair', parent=self.painelHome, pos=wx.Point(8, 509),
              size=wx.Size(57, 57), style=wx.BU_AUTODRAW)
        self.botaoSair.SetLabel(u'Logout')
        self.botaoSair.SetHelpText(u'Bot\xe3o para sair do sistema e voltar para a tela de login')
        self.botaoSair.Bind(wx.EVT_BUTTON, self.OnBotaoSairButton,
              id=wxID_FRAMEGERENCIAMENTOALUNOBOTAOSAIR)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnBotaoAdicionarButton(self, event):

        event.Skip()

    def OnBitmapButton1Button(self, event):
        event.Skip()

    def OnBotaoEditarButton(self, event):
        event.Skip()

    def OnBotaoExcluirButton(self, event):
        event.Skip()

    def OnButaoPesquisarButton(self, event):
        event.Skip()

    def OnBotaoSairButton(self, event):
        event.Skip()
