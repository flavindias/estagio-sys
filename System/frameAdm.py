#Boa:Frame:frameInicioAdm

import wx
import bridge

def create(parent):
    return frameInicioAdm(parent)

[wxID_FRAMEINICIOADM, wxID_FRAMEINICIOADMBOTAOBUROCRATICO, 
 wxID_FRAMEINICIOADMBOTAOEMPRESARIAL, wxID_FRAMEINICIOADMBOTAOESTUDANTIL, 
 wxID_FRAMEINICIOADMBOTAOSAIR, wxID_FRAMEINICIOADMLINHATELAINICIOSUPERIOR, 
 wxID_FRAMEINICIOADMLOGOCANTOIFPE, wxID_FRAMEINICIOADMLOGOIFPE, 
 wxID_FRAMEINICIOADMNOMEALUNO, wxID_FRAMEINICIOADMNOMEBUROCRATICO, 
 wxID_FRAMEINICIOADMNOMEEMPRESARIAL, wxID_FRAMEINICIOADMPAINELHOME, 
] = [wx.NewId() for _init_ctrls in range(12)]

class frameInicioAdm(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEINICIOADM, name=u'frameInicioAdm',
              parent=prnt, pos=wx.Point(700, 273), size=wx.Size(1040, 614),
              style=wx.DEFAULT_FRAME_STYLE,
              title=u'Est\xe1gio Curricular - Programa de Est\xe1gio Currcular')
        self.SetClientSize(wx.Size(1024, 576))
        self.SetIcon(wx.Icon(u'./Graficos/icone.ico',
              wx.BITMAP_TYPE_ICO))
        self.Center(wx.BOTH)
        self.SetMaxSize(wx.Size(1040, 614))
        self.SetMinSize(wx.Size(1040, 614))

        self.painelHome = wx.Panel(id=wxID_FRAMEINICIOADMPAINELHOME,
              name=u'painelHome', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(1024, 576),
              style=wx.STATIC_BORDER | wx.TAB_TRAVERSAL)
        self.painelHome.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.logoIFPE = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/logo.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEINICIOADMLOGOIFPE,
              name=u'logoIFPE', parent=self.painelHome, pos=wx.Point(8, 8),
              size=wx.Size(175, 70), style=0)

        self.logoCantoIFPE = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/logoBG.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEINICIOADMLOGOCANTOIFPE,
              name=u'logoCantoIFPE', parent=self.painelHome, pos=wx.Point(856,
              352), size=wx.Size(168, 227), style=0)

        self.linhaTelaInicioSuperior = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/linhaTelaInicioSuperior.png',
              wx.BITMAP_TYPE_PNG),
              id=wxID_FRAMEINICIOADMLINHATELAINICIOSUPERIOR,
              name=u'linhaTelaInicioSuperior', parent=self.painelHome,
              pos=wx.Point(0, 80), size=wx.Size(1024, 23), style=0)

        self.botaoEstudantil = wx.BitmapButton(bitmap=wx.Bitmap(u'./Graficos/botao_user_cfg.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEINICIOADMBOTAOESTUDANTIL,
              name=u'botaoEstudantil', parent=self.painelHome, pos=wx.Point(159,
              209), size=wx.Size(184, 184), style=wx.BU_AUTODRAW)
        self.botaoEstudantil.SetLabel(u'Editar')
        self.botaoEstudantil.SetHelpText(u'Bot\xe3o para editar cadastro de alunos')
        self.botaoEstudantil.Bind(wx.EVT_BUTTON, self.OnBotaoEstudantilButton,
              id=wxID_FRAMEINICIOADMBOTAOESTUDANTIL)

        self.botaoEmpresarial = wx.BitmapButton(bitmap=wx.Bitmap(u'./Graficos/botao_enter_cfg.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEINICIOADMBOTAOEMPRESARIAL,
              name=u'botaoEmpresarial', parent=self.painelHome,
              pos=wx.Point(414, 209), size=wx.Size(184, 184),
              style=wx.BU_AUTODRAW)
        self.botaoEmpresarial.SetLabel(u'Excluir')
        self.botaoEmpresarial.SetHelpText(u'Bot\xe3o para excluir cadastro de alunos')
        self.botaoEmpresarial.Bind(wx.EVT_BUTTON, self.OnBotaoEmpresarialButton,
              id=wxID_FRAMEINICIOADMBOTAOEMPRESARIAL)

        self.botaoBurocratico = wx.BitmapButton(bitmap=wx.Bitmap(u'./Graficos/botao_form_cfg.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEINICIOADMBOTAOBUROCRATICO,
              name=u'botaoBurocratico', parent=self.painelHome,
              pos=wx.Point(653, 210), size=wx.Size(184, 184),
              style=wx.BU_AUTODRAW)
        self.botaoBurocratico.SetLabel(u'Pesquisar')
        self.botaoBurocratico.SetHelpText(u'Bot\xe3o para pesquisar alunos')
        self.botaoBurocratico.Bind(wx.EVT_BUTTON, self.OnBotaoBurocraticoButton,
              id=wxID_FRAMEINICIOADMBOTAOBUROCRATICO)

        self.nomeAluno = wx.StaticText(id=wxID_FRAMEINICIOADMNOMEALUNO,
              label=u'Estudantil', name=u'nomeAluno', parent=self.painelHome,
              pos=wx.Point(206, 418), size=wx.Size(96, 26), style=0)
        self.nomeAluno.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Myriad Pro'))

        self.nomeEmpresarial = wx.StaticText(id=wxID_FRAMEINICIOADMNOMEEMPRESARIAL,
              label=u'Empresarial', name=u'nomeEmpresarial',
              parent=self.painelHome, pos=wx.Point(451, 418), size=wx.Size(112,
              26), style=0)
        self.nomeEmpresarial.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Myriad Pro'))

        self.nomeBurocratico = wx.StaticText(id=wxID_FRAMEINICIOADMNOMEBUROCRATICO,
              label=u'Burocr\xe1tico', name=u'nomeBurocratico',
              parent=self.painelHome, pos=wx.Point(694, 418), size=wx.Size(108,
              26), style=0)
        self.nomeBurocratico.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Myriad Pro'))

        self.botaoSair = wx.BitmapButton(bitmap=wx.Bitmap(u'./Graficos/botao_sair.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEINICIOADMBOTAOSAIR,
              name=u'botaoSair', parent=self.painelHome, pos=wx.Point(8, 509),
              size=wx.Size(57, 57), style=wx.BU_AUTODRAW)
        self.botaoSair.SetLabel(u'Logout')
        self.botaoSair.SetHelpText(u'Bot\xe3o para sair do sistema e voltar para a tela de login')
        self.botaoSair.Bind(wx.EVT_BUTTON, self.OnBotaoSairButton,
              id=wxID_FRAMEINICIOADMBOTAOSAIR)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnBotaoSairButton(self, event):
        event.Skip()

    def OnBotaoEstudantilButton(self, event):
        event.Skip()

    def OnBotaoEmpresarialButton(self, event):
        event.Skip()

    def OnBotaoBurocraticoButton(self, event):
        event.Skip()
