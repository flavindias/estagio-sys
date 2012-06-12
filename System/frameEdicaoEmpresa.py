#Boa:Frame:frameEdicaoEmpresa
#! /usr/bin/env python
#-*-coding: latin1-*-
#-*-coding: iso-8859-1-*-  

import wx
import wx.lib.masked.textctrl
import urllib  
import cgi
import bridge
import re


def create(parent):
    return frameEdicaoEmpresa(parent)

[wxID_FRAMEEDICAOEMPRESA, wxID_FRAMEEDICAOEMPRESAABACONTATO, 
 wxID_FRAMEEDICAOEMPRESAABALOGIN, wxID_FRAMEEDICAOEMPRESAABAPESSOAL, 
 wxID_FRAMEEDICAOEMPRESABOTAOBUSCARCEP, 
 wxID_FRAMEEDICAOEMPRESABOTAOLIMPARCONTATO, 
 wxID_FRAMEEDICAOEMPRESABOTAOLIMPAREMPRESARIAL, 
 wxID_FRAMEEDICAOEMPRESABOTAOLIMPARLOGIN, wxID_FRAMEEDICAOEMPRESABOTAOSALVAR, 
 wxID_FRAMEEDICAOEMPRESABOTAOVOLTAR, wxID_FRAMEEDICAOEMPRESACAMPOBAIRRO, 
 wxID_FRAMEEDICAOEMPRESACAMPOCELULAR, wxID_FRAMEEDICAOEMPRESACAMPOCEP, 
 wxID_FRAMEEDICAOEMPRESACAMPOCIDADE, wxID_FRAMEEDICAOEMPRESACAMPOCNPJ, 
 wxID_FRAMEEDICAOEMPRESACAMPOCOMPLEMENTO, 
 wxID_FRAMEEDICAOEMPRESACAMPOCONFIRMARSENHA, 
 wxID_FRAMEEDICAOEMPRESACAMPOEMAIL, wxID_FRAMEEDICAOEMPRESACAMPOENDERECO, 
 wxID_FRAMEEDICAOEMPRESACAMPOLOGIN, wxID_FRAMEEDICAOEMPRESACAMPONOMEFANTASIA, 
 wxID_FRAMEEDICAOEMPRESACAMPONOMERESPONSAVEL, 
 wxID_FRAMEEDICAOEMPRESACAMPONUMERO, wxID_FRAMEEDICAOEMPRESACAMPORAZAOSOCIAL, 
 wxID_FRAMEEDICAOEMPRESACAMPOSENHA, wxID_FRAMEEDICAOEMPRESACAMPOSITE, 
 wxID_FRAMEEDICAOEMPRESACAMPOTELEFONE, wxID_FRAMEEDICAOEMPRESACAMPOUF, 
 wxID_FRAMEEDICAOEMPRESACARREGARCNPJ, wxID_FRAMEEDICAOEMPRESACNPJINVALIDO, 
 wxID_FRAMEEDICAOEMPRESACNPJVALIDO, wxID_FRAMEEDICAOEMPRESADADOSDOSALUNOS, 
 wxID_FRAMEEDICAOEMPRESALINHAEDICAOEMPRESAS, wxID_FRAMEEDICAOEMPRESALOGO, 
 wxID_FRAMEEDICAOEMPRESANOMEBAIRRO, wxID_FRAMEEDICAOEMPRESANOMECELULAR, 
 wxID_FRAMEEDICAOEMPRESANOMECEP, wxID_FRAMEEDICAOEMPRESANOMECIDADE, 
 wxID_FRAMEEDICAOEMPRESANOMECNPJ, wxID_FRAMEEDICAOEMPRESANOMECOMPLEMENTO, 
 wxID_FRAMEEDICAOEMPRESANOMECONFIRMARSENHA, wxID_FRAMEEDICAOEMPRESANOMEEMAIL, 
 wxID_FRAMEEDICAOEMPRESANOMEENDERECO, wxID_FRAMEEDICAOEMPRESANOMEERRO, 
 wxID_FRAMEEDICAOEMPRESANOMEERROSENHA, wxID_FRAMEEDICAOEMPRESANOMELOGIN, 
 wxID_FRAMEEDICAOEMPRESANOMENOMEFANTASIA, 
 wxID_FRAMEEDICAOEMPRESANOMENOMERESPONSAVEL, 
 wxID_FRAMEEDICAOEMPRESANOMENUMERO, wxID_FRAMEEDICAOEMPRESANOMERAZAOSOCIAL, 
 wxID_FRAMEEDICAOEMPRESANOMESENHA, wxID_FRAMEEDICAOEMPRESANOMESITE, 
 wxID_FRAMEEDICAOEMPRESANOMETELEFONE, wxID_FRAMEEDICAOEMPRESANOMEUF, 
 wxID_FRAMEEDICAOEMPRESAPAINELCADASTRO, 
] = [wx.NewId() for _init_ctrls in range(55)]

class frameEdicaoEmpresa(wx.Frame):
    def _init_coll_dadosDosAlunos_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.abaPessoal, select=True,
              text=u'Dados Empresariais')
        parent.AddPage(imageId=-1, page=self.abaContato, select=False,
              text=u'Contato')
        parent.AddPage(imageId=-1, page=self.abaLogin, select=False,
              text=u'Login')

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEEDICAOEMPRESA,
              name=u'frameEdicaoEmpresa', parent=prnt, pos=wx.Point(700, 273),
              size=wx.Size(1040, 614), style=wx.DEFAULT_FRAME_STYLE,
              title=u'Est\xe1gio Curricular - Edi\xe7\xe3o de Empresas')
        self.SetClientSize(wx.Size(1024, 576))
        self.Center(wx.BOTH)
        self.SetIcon(wx.Icon(u'./Graficos/icone.ico',wx.BITMAP_TYPE_ICO))
        self.SetMaxSize(wx.Size(1040, 614))
        self.SetMinSize(wx.Size(1040, 614))

        self.painelCadastro = wx.Panel(id=wxID_FRAMEEDICAOEMPRESAPAINELCADASTRO,
              name=u'painelCadastro', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(1024, 576), style=wx.TAB_TRAVERSAL)
        self.painelCadastro.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.logo = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/logo.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEEDICAOEMPRESALOGO, name=u'logo',
              parent=self.painelCadastro, pos=wx.Point(8, 8), size=wx.Size(175,
              70), style=0)

        self.linhaEdicaoEmpresas = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/LinhaEdicaoEmpresas.png',
              wx.BITMAP_TYPE_PNG),
              id=wxID_FRAMEEDICAOEMPRESALINHAEDICAOEMPRESAS,
              name=u'linhaEdicaoEmpresas', parent=self.painelCadastro,
              pos=wx.Point(0, 80), size=wx.Size(1024, 26), style=0)

        self.dadosDosAlunos = wx.Notebook(id=wxID_FRAMEEDICAOEMPRESADADOSDOSALUNOS,
              name=u'dadosDosAlunos', parent=self.painelCadastro,
              pos=wx.Point(20, 120), size=wx.Size(984, 424), style=0)
        self.dadosDosAlunos.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.dadosDosAlunos.SetForegroundColour(wx.Colour(255, 255, 255))
        self.dadosDosAlunos.SetThemeEnabled(True)

        self.abaPessoal = wx.Window(id=wxID_FRAMEEDICAOEMPRESAABAPESSOAL,
              name=u'abaPessoal', parent=self.dadosDosAlunos, pos=wx.Point(0,
              0), size=wx.Size(976, 398), style=wx.TAB_TRAVERSAL)

        self.campoCNPJ = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRAMEEDICAOEMPRESACAMPOCNPJ,
              name=u'campoCNPJ', parent=self.abaPessoal, pos=wx.Point(24, 34),
              size=wx.Size(200, 21), style=0, value=u'')
        self.campoCNPJ.SetMask(u'XX.XXX.XXX/XXXX-XX')
        self.campoCNPJ.SetAutoformat('')
        self.campoCNPJ.SetFormatcodes('')
        self.campoCNPJ.SetDescription('')
        self.campoCNPJ.SetExcludeChars('')
        self.campoCNPJ.SetValidRegex('')
        self.campoCNPJ.SetMaxLength(18)
        self.campoCNPJ.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))
        self.campoCNPJ.SetDefaultEncoding(u'latin1')
        self.campoCNPJ.SetFillChar(u' ')
        self.campoCNPJ.SetDatestyle('MDY')

        self.nomeCNPJ = wx.StaticText(id=wxID_FRAMEEDICAOEMPRESANOMECNPJ,
              label=u'CNPJ:', name=u'nomeCNPJ', parent=self.abaPessoal,
              pos=wx.Point(11, 15), size=wx.Size(30, 13), style=0)

        self.cnpjInvalido = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/botao_invalido.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEEDICAOEMPRESACNPJINVALIDO,
              name=u'cnpjInvalido', parent=self.abaPessoal, pos=wx.Point(279,
              36), size=wx.Size(14, 14), style=0)
        self.cnpjInvalido.Show(False)

        self.cnpjValido = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/botao_valido.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEEDICAOEMPRESACNPJVALIDO,
              name=u'cnpjValido', parent=self.abaPessoal, pos=wx.Point(279, 36),
              size=wx.Size(14, 14), style=0)
        self.cnpjValido.Show(False)

        self.carregarCNPJ = wx.BitmapButton(bitmap=wx.Bitmap(u'./Graficos/botao_carregar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEEDICAOEMPRESACARREGARCNPJ,
              name=u'carregarCNPJ', parent=self.abaPessoal, pos=wx.Point(243,
              30), size=wx.Size(26, 26), style=wx.BU_AUTODRAW)
        self.carregarCNPJ.Bind(wx.EVT_BUTTON, self.OnValidarCNPJButton,
              id=wxID_FRAMEEDICAOEMPRESACARREGARCNPJ)

        self.nomeRazaoSocial = wx.StaticText(id=wxID_FRAMEEDICAOEMPRESANOMERAZAOSOCIAL,
              label=u'Raz\xe3o Social:', name=u'nomeRazaoSocial',
              parent=self.abaPessoal, pos=wx.Point(11, 70), size=wx.Size(65,
              13), style=0)

        self.campoRazaoSocial = wx.TextCtrl(id=wxID_FRAMEEDICAOEMPRESACAMPORAZAOSOCIAL,
              name=u'campoRazaoSocial', parent=self.abaPessoal, pos=wx.Point(24,
              89), size=wx.Size(496, 21), style=0, value=u'')
        self.campoRazaoSocial.SetMaxLength(50)

        self.nomeNomeFantasia = wx.StaticText(id=wxID_FRAMEEDICAOEMPRESANOMENOMEFANTASIA,
              label=u'Nome Fantasia:', name=u'nomeNomeFantasia',
              parent=self.abaPessoal, pos=wx.Point(11, 125), size=wx.Size(76,
              13), style=0)

        self.campoNomeFantasia = wx.TextCtrl(id=wxID_FRAMEEDICAOEMPRESACAMPONOMEFANTASIA,
              name=u'campoNomeFantasia', parent=self.abaPessoal,
              pos=wx.Point(24, 145), size=wx.Size(496, 21), style=0, value=u'')
        self.campoNomeFantasia.SetMaxLength(50)

        self.nomeCEP = wx.StaticText(id=wxID_FRAMEEDICAOEMPRESANOMECEP,
              label=u'CEP:', name=u'nomeCEP', parent=self.abaPessoal,
              pos=wx.Point(11, 184), size=wx.Size(24, 13), style=0)

        self.campoCEP = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRAMEEDICAOEMPRESACAMPOCEP,
              name=u'campoCEP', parent=self.abaPessoal, pos=wx.Point(24, 203),
              size=wx.Size(104, 21), style=0, value=u'  .   -   ')
        self.campoCEP.SetMask(u'XX.XXX-XXX')
        self.campoCEP.SetAutoformat('')
        self.campoCEP.SetFormatcodes('')
        self.campoCEP.SetDescription('')
        self.campoCEP.SetExcludeChars('')
        self.campoCEP.SetValidRegex('')
        self.campoCEP.SetMaxLength(10)
        self.campoCEP.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))
        self.campoCEP.SetDatestyle('MDY')

        self.botaoBuscarCEP = wx.BitmapButton(bitmap=wx.Bitmap(u'./Graficos/botao_buscar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEEDICAOEMPRESABOTAOBUSCARCEP,
              name=u'botaoBuscarCEP', parent=self.abaPessoal, pos=wx.Point(136,
              200), size=wx.Size(26, 26), style=wx.BU_AUTODRAW)
        self.botaoBuscarCEP.Bind(wx.EVT_BUTTON, self.OnBotaoBuscarCEPButton,
              id=wxID_FRAMEEDICAOEMPRESABOTAOBUSCARCEP)

        self.nomeNumero = wx.StaticText(id=wxID_FRAMEEDICAOEMPRESANOMENUMERO,
              label=u'N\xfamero:', name=u'nomeNumero', parent=self.abaPessoal,
              pos=wx.Point(160, 184), size=wx.Size(42, 13), style=0)

        self.campoNumero = wx.TextCtrl(id=wxID_FRAMEEDICAOEMPRESACAMPONUMERO,
              name=u'campoNumero', parent=self.abaPessoal, pos=wx.Point(173,
              203), size=wx.Size(100, 21), style=0, value=u'')

        self.nomeComplemento = wx.StaticText(id=wxID_FRAMEEDICAOEMPRESANOMECOMPLEMENTO,
              label=u'Complemento:', name=u'nomeComplemento',
              parent=self.abaPessoal, pos=wx.Point(293, 184), size=wx.Size(70,
              13), style=0)

        self.abaLogin = wx.Window(id=wxID_FRAMEEDICAOEMPRESAABALOGIN,
              name=u'abaLogin', parent=self.dadosDosAlunos, pos=wx.Point(0, 0),
              size=wx.Size(976, 398), style=wx.TAB_TRAVERSAL)

        self.abaContato = wx.Window(id=wxID_FRAMEEDICAOEMPRESAABACONTATO,
              name=u'abaContato', parent=self.dadosDosAlunos, pos=wx.Point(0,
              0), size=wx.Size(976, 398), style=wx.TAB_TRAVERSAL)

        self.nomeNomeResponsavel = wx.StaticText(id=wxID_FRAMEEDICAOEMPRESANOMENOMERESPONSAVEL,
              label=u'Nome Respons\xe1vel', name=u'nomeNomeResponsavel',
              parent=self.abaContato, pos=wx.Point(11, 18), size=wx.Size(92,
              13), style=0)

        self.campoNomeResponsavel = wx.TextCtrl(id=wxID_FRAMEEDICAOEMPRESACAMPONOMERESPONSAVEL,
              name=u'campoNomeResponsavel', parent=self.abaContato,
              pos=wx.Point(24, 37), size=wx.Size(496, 21), style=0, value=u'')
        self.campoNomeResponsavel.SetMaxLength(50)

        self.campoEmail = wx.TextCtrl(id=wxID_FRAMEEDICAOEMPRESACAMPOEMAIL,
              name=u'campoEmail', parent=self.abaContato, pos=wx.Point(24, 94),
              size=wx.Size(312, 21), style=0, value=u'')

        self.campoSite = wx.TextCtrl(id=wxID_FRAMEEDICAOEMPRESACAMPOSITE,
              name=u'campoSite', parent=self.abaContato, pos=wx.Point(24, 147),
              size=wx.Size(312, 21), style=0, value=u'')

        self.nomeSite = wx.StaticText(id=wxID_FRAMEEDICAOEMPRESANOMESITE,
              label=u'Site:', name=u'nomeSite', parent=self.abaContato,
              pos=wx.Point(11, 128), size=wx.Size(23, 13), style=0)

        self.nomeEmail = wx.StaticText(id=wxID_FRAMEEDICAOEMPRESANOMEEMAIL,
              label=u'E-Mail:', name=u'nomeEmail', parent=self.abaContato,
              pos=wx.Point(11, 75), size=wx.Size(33, 13), style=0)

        self.campoComplemento = wx.TextCtrl(id=wxID_FRAMEEDICAOEMPRESACAMPOCOMPLEMENTO,
              name=u'campoComplemento', parent=self.abaPessoal,
              pos=wx.Point(306, 203), size=wx.Size(214, 21), style=0,
              value=u'')

        self.nomeTelefone = wx.StaticText(id=wxID_FRAMEEDICAOEMPRESANOMETELEFONE,
              label=u'Telefone:', name=u'nomeTelefone', parent=self.abaContato,
              pos=wx.Point(11, 179), size=wx.Size(47, 13), style=0)

        self.nomeEndereco = wx.StaticText(id=wxID_FRAMEEDICAOEMPRESANOMEENDERECO,
              label=u'Endere\xe7o:', name=u'nomeEndereco',
              parent=self.abaPessoal, pos=wx.Point(11, 239), size=wx.Size(50,
              13), style=0)

        self.campoEndereco = wx.TextCtrl(id=wxID_FRAMEEDICAOEMPRESACAMPOENDERECO,
              name=u'campoEndereco', parent=self.abaPessoal, pos=wx.Point(24,
              260), size=wx.Size(496, 21), style=0, value=u'')

        self.nomeBairro = wx.StaticText(id=wxID_FRAMEEDICAOEMPRESANOMEBAIRRO,
              label=u'Bairro:', name=u'nomeBairro', parent=self.abaPessoal,
              pos=wx.Point(11, 293), size=wx.Size(33, 13), style=0)

        self.nomeCidade = wx.StaticText(id=wxID_FRAMEEDICAOEMPRESANOMECIDADE,
              label=u'Cidade:', name=u'nomeCidade', parent=self.abaPessoal,
              pos=wx.Point(265, 293), size=wx.Size(38, 13), style=0)

        self.campoBairro = wx.TextCtrl(id=wxID_FRAMEEDICAOEMPRESACAMPOBAIRRO,
              name=u'campoBairro', parent=self.abaPessoal, pos=wx.Point(24,
              312), size=wx.Size(224, 21), style=0, value=u'')

        self.campoCidade = wx.TextCtrl(id=wxID_FRAMEEDICAOEMPRESACAMPOCIDADE,
              name=u'campoCidade', parent=self.abaPessoal, pos=wx.Point(278,
              312), size=wx.Size(186, 21), style=0, value=u'')

        self.botaoLimparLogin = wx.Button(id=wxID_FRAMEEDICAOEMPRESABOTAOLIMPARLOGIN,
              label=u'Limpar', name=u'botaoLimparLogin', parent=self.abaLogin,
              pos=wx.Point(880, 20), size=wx.Size(75, 23), style=0)
        self.botaoLimparLogin.Bind(wx.EVT_BUTTON, self.OnBotaoLimparLoginButton,
              id=wxID_FRAMEEDICAOEMPRESABOTAOLIMPARLOGIN)

        self.botaoVoltar = wx.BitmapButton(bitmap=wx.Bitmap(u'./Graficos/botao_voltar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEEDICAOEMPRESABOTAOVOLTAR,
              name=u'botaoVoltar', parent=self.painelCadastro, pos=wx.Point(952,
              13), size=wx.Size(57, 57), style=wx.BU_AUTODRAW)
        self.botaoVoltar.Bind(wx.EVT_BUTTON, self.OnBotaoVoltarButton,
              id=wxID_FRAMEEDICAOEMPRESABOTAOVOLTAR)

        self.nomeUF = wx.StaticText(id=wxID_FRAMEEDICAOEMPRESANOMEUF,
              label=u'UF:', name=u'nomeUF', parent=self.abaPessoal,
              pos=wx.Point(480, 293), size=wx.Size(18, 13), style=0)

        self.campoUF = wx.TextCtrl(id=wxID_FRAMEEDICAOEMPRESACAMPOUF,
              name=u'campoUF', parent=self.abaPessoal, pos=wx.Point(493, 312),
              size=wx.Size(27, 21), style=0, value=u'')
        self.campoUF.SetMaxLength(2)

        self.botaoLimparEmpresarial = wx.Button(id=wxID_FRAMEEDICAOEMPRESABOTAOLIMPAREMPRESARIAL,
              label=u'Limpar', name=u'botaoLimparEmpresarial',
              parent=self.abaPessoal, pos=wx.Point(880, 20), size=wx.Size(75,
              23), style=0)
        self.botaoLimparEmpresarial.Bind(wx.EVT_BUTTON,
              self.OnBotaoLimparEmpresarialButton,
              id=wxID_FRAMEEDICAOEMPRESABOTAOLIMPAREMPRESARIAL)

        self.nomeErro = wx.StaticText(id=wxID_FRAMEEDICAOEMPRESANOMEERRO,
              label=u'', name=u'nomeErro', parent=self.abaPessoal,
              pos=wx.Point(541, 36), size=wx.Size(0, 13),
              style=wx.ALIGN_CENTRE)
        self.nomeErro.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, True,
              u'Tahoma'))
        self.nomeErro.SetAutoLayout(True)

        self.campoTelefone = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRAMEEDICAOEMPRESACAMPOTELEFONE,
              name=u'campoTelefone', parent=self.abaContato, pos=wx.Point(24,
              198), size=wx.Size(136, 21), style=0, value=u'(  )    -    ')
        self.campoTelefone.SetAutoformat('')
        self.campoTelefone.SetMask(u'(XX)XXXX-XXXX')
        self.campoTelefone.SetFormatcodes('')
        self.campoTelefone.SetDescription('')
        self.campoTelefone.SetExcludeChars('')
        self.campoTelefone.SetValidRegex('')
        self.campoTelefone.SetMaxLength(13)
        self.campoTelefone.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))

        self.nomeCelular = wx.StaticText(id=wxID_FRAMEEDICAOEMPRESANOMECELULAR,
              label=u'Celular:', name=u'nomeCelular', parent=self.abaContato,
              pos=wx.Point(11, 236), size=wx.Size(38, 13), style=0)

        self.campoCelular = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRAMEEDICAOEMPRESACAMPOCELULAR,
              name=u'campoCelular', parent=self.abaContato, pos=wx.Point(24,
              255), size=wx.Size(136, 21), style=0, value=u'')
        self.campoCelular.SetAutoformat('')
        self.campoCelular.SetMask(u'(XX)XXXX-XXXX')
        self.campoCelular.SetFormatcodes('')
        self.campoCelular.SetDescription('')
        self.campoCelular.SetExcludeChars('')
        self.campoCelular.SetValidRegex('')
        self.campoCelular.SetMaxLength(13)
        self.campoCelular.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))

        self.botaoLimparContato = wx.Button(id=wxID_FRAMEEDICAOEMPRESABOTAOLIMPARCONTATO,
              label=u'Limpar', name=u'botaoLimparContato',
              parent=self.abaContato, pos=wx.Point(880, 20), size=wx.Size(75,
              23), style=0)
        self.botaoLimparContato.Bind(wx.EVT_BUTTON,
              self.OnBotaoLimparContatoButton,
              id=wxID_FRAMEEDICAOEMPRESABOTAOLIMPARCONTATO)

        self.botaoSalvar = wx.Button(id=wxID_FRAMEEDICAOEMPRESABOTAOSALVAR,
              label=u'Salvar', name=u'botaoSalvar', parent=self.abaLogin,
              pos=wx.Point(885, 360), size=wx.Size(75, 23), style=0)
        self.botaoSalvar.Bind(wx.EVT_BUTTON, self.OnBotaoSalvarButton,
              id=wxID_FRAMEEDICAOEMPRESABOTAOSALVAR)

        self.nomeLogin = wx.StaticText(id=wxID_FRAMEEDICAOEMPRESANOMELOGIN,
              label=u'Login:', name=u'nomeLogin', parent=self.abaLogin,
              pos=wx.Point(11, 24), size=wx.Size(30, 13), style=0)

        self.campoLogin = wx.TextCtrl(id=wxID_FRAMEEDICAOEMPRESACAMPOLOGIN,
              name=u'campoLogin', parent=self.abaLogin, pos=wx.Point(24, 43),
              size=wx.Size(312, 21), style=0, value=u'')

        self.nomeSenha = wx.StaticText(id=wxID_FRAMEEDICAOEMPRESANOMESENHA,
              label=u'Senha:', name=u'nomeSenha', parent=self.abaLogin,
              pos=wx.Point(11, 75), size=wx.Size(35, 13), style=0)

        self.campoSenha = wx.TextCtrl(id=wxID_FRAMEEDICAOEMPRESACAMPOSENHA,
              name=u'campoSenha', parent=self.abaLogin, pos=wx.Point(24, 94),
              size=wx.Size(312, 21), style=wx.TE_PASSWORD, value=u'')

        self.nomeConfirmarSenha = wx.StaticText(id=wxID_FRAMEEDICAOEMPRESANOMECONFIRMARSENHA,
              label=u'Confirmar Senha:', name=u'nomeConfirmarSenha',
              parent=self.abaLogin, pos=wx.Point(11, 128), size=wx.Size(85, 13),
              style=0)

        self.campoConfirmarSenha = wx.TextCtrl(id=wxID_FRAMEEDICAOEMPRESACAMPOCONFIRMARSENHA,
              name=u'campoConfirmarSenha', parent=self.abaLogin,
              pos=wx.Point(24, 147), size=wx.Size(312, 21),
              style=wx.TE_PASSWORD, value=u'')

        self.nomeErroSenha = wx.StaticText(id=wxID_FRAMEEDICAOEMPRESANOMEERROSENHA,
              label=u'', name=u'nomeErroSenha', parent=self.abaLogin,
              pos=wx.Point(541, 36), size=wx.Size(0, 13),
              style=wx.ALIGN_CENTRE)
        self.nomeErroSenha.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              True, u'Tahoma'))
        self.nomeErroSenha.SetAutoLayout(True)

        self._init_coll_dadosDosAlunos_Pages(self.dadosDosAlunos)

    def __init__(self, parent):
        self._init_ctrls(parent)
        
    def validar_cnpj(self, cnpj):   
        cnpj = ''.join(re.findall('\d', str(cnpj)))
        if (not cnpj) or (len(cnpj) < 14):
            return False
        inteiros = map(int, cnpj)
        novo = inteiros[:12]
    
        prod = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        while len(novo) < 14:
            r = sum([x*y for (x, y) in zip(novo, prod)]) % 11
            if r > 1:
                f = 11 - r
            else:
                f = 0
            novo.append(f)
            prod.insert(0, 6)
    
    
        if novo == inteiros:
            return True
        else:
            return False
    
    def busca_cep(self, cep):
        global endereco
        url = "http://cep.republicavirtual.com.br/web_cep.php?cep=" + cep + "&formato=query_string"
        pagina = urllib.urlopen(url)  
        conteudo = pagina.read();  
        resultado = cgi.parse_qs(conteudo);
        if resultado['resultado'][0] == '1':  
            rua = ((resultado['tipo_logradouro'][0]) + (" ") + (resultado['logradouro'][0]) + (" ")).upper()
            bairro = (resultado['bairro'][0]).upper()
            cidade = (resultado['cidade'][0]).upper()
            estado = (resultado['uf'][0]).upper()
            endereco = [True, rua, bairro, cidade, estado]
            
            
        elif resultado['resultado'][0] == '2':
            rua = ''
            bairro = ''  
            cidade = (resultado['cidade'][0]).upper()
            estado = (resultado['uf'][0]).upper()
            endereco = [True, rua, bairro, cidade, estado]
            
    
        else:  
            endereco = [False, '', '', '', '']
        
        return endereco



    def OnBotaoBuscarCEPButton(self, event):
        cep = self.campoCEP.GetValue()
        CEP = cep[0:2:1] + cep[3:6:1] + cep[7:10:1]
        self.busca_cep(CEP)
        if endereco[0] == True:
            self.campoEndereco.SetValue(endereco[1])
            self.campoBairro.SetValue(endereco[2])
            self.campoCidade.SetValue(endereco[3])
            self.campoUF.SetValue(endereco[4])
            self.nomeErro.SetLabel('')
            
        else:
            self.nomeErro.SetLabel('CEP Invalido!')
            
        event.Skip()



    def OnBotaoVoltarButton(self, event):
        event.Skip()

    def OnBotaoSalvarButton(self, event):
        
        event.Skip()

    def OnBotaoLimparEmpresarialButton(self, event):
        self.campoCNPJ.SetValue('')
        self.campoRazaoSocial.SetValue('')
        self.campoNomeFantasia.SetValue('')
        self.campoCEP.SetValue('')
        self.campoNumero.SetValue('')
        self.campoComplemento.SetValue('')
        self.campoEndereco.SetValue('')
        self.campoBairro.SetValue('')
        self.campoCidade.SetValue('')
        self.campoUF.SetValue('')
        self.nomeErro.SetLabel('')
        
        event.Skip()


    def OnBotaoLimparLoginButton(self, event):
        self.campoLogin.SetValue('')
        self.campoSenha.SetValue('')
        self.campoConfirmarSenha.SetValue('')
        self.nomeErroSenha.SetLabel('')
        
        event.Skip()

    def OnBotaoLimparContatoButton(self, event):
        self.campoNomeResponsavel.SetValue('')
        self.campoEmail.SetValue('')
        self.campoSite.SetValue('')
        self.campoTelefone.SetValue('')
        self.campoCelular.SetValue('')
        
        event.Skip()

    def OnValidarCNPJButton(self, event):
        event.Skip()

