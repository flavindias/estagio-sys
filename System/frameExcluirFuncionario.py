#Boa:Frame:frameExclusaoFuncionarios
#! /usr/bin/env python
#-*-coding: latin1-*-
#-*-coding: iso-8859-1-*-  

import wx
import wx.lib.masked.textctrl
import urllib  
import cgi
import bridge

def create(parent):
    return frameExclusaoFuncionarios(parent)

[wxID_FRAMEEXCLUSAOFUNCIONARIOS, wxID_FRAMEEXCLUSAOFUNCIONARIOSBOTAOEXCLUIR, 
 wxID_FRAMEEXCLUSAOFUNCIONARIOSBOTAOVOLTAR, 
 wxID_FRAMEEXCLUSAOFUNCIONARIOSBUSCARLOGIN, 
 wxID_FRAMEEXCLUSAOFUNCIONARIOSCAMPOLOGIN, 
 wxID_FRAMEEXCLUSAOFUNCIONARIOSCAMPOLOGINFUNCIONARIO, 
 wxID_FRAMEEXCLUSAOFUNCIONARIOSCAMPONOMEFUNCIONARIO, 
 wxID_FRAMEEXCLUSAOFUNCIONARIOSCAMPOSENHA, 
 wxID_FRAMEEXCLUSAOFUNCIONARIOSCPFENCONTRADO, 
 wxID_FRAMEEXCLUSAOFUNCIONARIOSCPFNAOENCONTRADO, 
 wxID_FRAMEEXCLUSAOFUNCIONARIOSLINHAEXCLUSAOFUNCIONAIOS, 
 wxID_FRAMEEXCLUSAOFUNCIONARIOSLOGOIFPE, 
 wxID_FRAMEEXCLUSAOFUNCIONARIOSNOMEERRO, 
 wxID_FRAMEEXCLUSAOFUNCIONARIOSNOMELOGIN, 
 wxID_FRAMEEXCLUSAOFUNCIONARIOSNOMELOGINFUNCIONARIO, 
 wxID_FRAMEEXCLUSAOFUNCIONARIOSNOMENOMEALUNO, 
 wxID_FRAMEEXCLUSAOFUNCIONARIOSNOMESENHA, 
 wxID_FRAMEEXCLUSAOFUNCIONARIOSPAINELEXCLUIR, 
] = [wx.NewId() for _init_ctrls in range(18)]

class frameExclusaoFuncionarios(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEEXCLUSAOFUNCIONARIOS,
              name=u'frameExclusaoFuncionarios', parent=prnt, pos=wx.Point(700,
              273), size=wx.Size(1040, 614), style=wx.DEFAULT_FRAME_STYLE,
              title=u'Est\xe1gio Curricular - Exclus\xe3o de Funcion\xe1rios')
        self.SetClientSize(wx.Size(1024, 576))
        self.Center(wx.BOTH)
        self.SetIcon(wx.Icon(u'./Graficos/icone.ico',wx.BITMAP_TYPE_ICO))
        self.SetMaxSize(wx.Size(1040, 614))
        self.SetMinSize(wx.Size(1040, 614))

        self.painelExcluir = wx.Panel(id=wxID_FRAMEEXCLUSAOFUNCIONARIOSPAINELEXCLUIR,
              name=u'painelExcluir', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(1024, 576), style=wx.TAB_TRAVERSAL)
        self.painelExcluir.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.logoIFPE = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/logo.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEEXCLUSAOFUNCIONARIOSLOGOIFPE,
              name=u'logoIFPE', parent=self.painelExcluir, pos=wx.Point(8, 8),
              size=wx.Size(175, 70), style=0)

        self.campoLoginFuncionario = wx.TextCtrl(id=wxID_FRAMEEXCLUSAOFUNCIONARIOSCAMPOLOGINFUNCIONARIO,
              name=u'campoLoginFuncionario', parent=self.painelExcluir,
              pos=wx.Point(24, 140), size=wx.Size(240, 20), style=0, value=u'')
        self.campoLoginFuncionario.SetMaxLength(50)

        self.nomeLoginFuncionario = wx.StaticText(id=wxID_FRAMEEXCLUSAOFUNCIONARIOSNOMELOGINFUNCIONARIO,
              label=u'Login do Funcion\xe1rios:', name=u'nomeLoginFuncionario',
              parent=self.painelExcluir, pos=wx.Point(11, 122),
              size=wx.Size(108, 13), style=0)

        self.linhaExclusaoFuncionaios = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/LinhaExclusaoFuncionario.png',
              wx.BITMAP_TYPE_PNG),
              id=wxID_FRAMEEXCLUSAOFUNCIONARIOSLINHAEXCLUSAOFUNCIONAIOS,
              name=u'linhaExclusaoFuncionaios', parent=self.painelExcluir,
              pos=wx.Point(0, 80), size=wx.Size(1024, 25), style=0)

        self.cpfEncontrado = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/botao_valido.png',
              wx.BITMAP_TYPE_PNG),
              id=wxID_FRAMEEXCLUSAOFUNCIONARIOSCPFENCONTRADO,
              name=u'cpfEncontrado', parent=self.painelExcluir,
              pos=wx.Point(309, 143), size=wx.Size(14, 14), style=0)
        self.cpfEncontrado.Show(False)

        self.cpfNaoEncontrado = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/botao_invalido.png',
              wx.BITMAP_TYPE_PNG),
              id=wxID_FRAMEEXCLUSAOFUNCIONARIOSCPFNAOENCONTRADO,
              name=u'cpfNaoEncontrado', parent=self.painelExcluir,
              pos=wx.Point(309, 143), size=wx.Size(14, 14), style=0)
        self.cpfNaoEncontrado.Show(False)

        self.BuscarLogin = wx.BitmapButton(bitmap=wx.Bitmap(u'./Graficos/botao_carregar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEEXCLUSAOFUNCIONARIOSBUSCARLOGIN,
              name=u'BuscarLogin', parent=self.painelExcluir, pos=wx.Point(273,
              137), size=wx.Size(26, 26), style=wx.BU_AUTODRAW)
        self.BuscarLogin.Bind(wx.EVT_BUTTON, self.OnBuscarCPFButton,
              id=wxID_FRAMEEXCLUSAOFUNCIONARIOSBUSCARLOGIN)

        self.nomeNomeAluno = wx.StaticText(id=wxID_FRAMEEXCLUSAOFUNCIONARIOSNOMENOMEALUNO,
              label=u'Nome do Funcion\xe1rio:', name=u'nomeNomeAluno',
              parent=self.painelExcluir, pos=wx.Point(11, 177),
              size=wx.Size(105, 13), style=0)

        self.campoNomeFUncionario = wx.TextCtrl(id=wxID_FRAMEEXCLUSAOFUNCIONARIOSCAMPONOMEFUNCIONARIO,
              name=u'campoNomeFUncionario', parent=self.painelExcluir,
              pos=wx.Point(24, 196), size=wx.Size(496, 21),
              style=wx.TE_READONLY, value=u'')
        self.campoNomeFUncionario.SetMaxLength(50)

        self.nomeLogin = wx.StaticText(id=wxID_FRAMEEXCLUSAOFUNCIONARIOSNOMELOGIN,
              label=u'Login:', name=u'nomeLogin', parent=self.painelExcluir,
              pos=wx.Point(11, 228), size=wx.Size(30, 13), style=0)

        self.campoLogin = wx.TextCtrl(id=wxID_FRAMEEXCLUSAOFUNCIONARIOSCAMPOLOGIN,
              name=u'campoLogin', parent=self.painelExcluir, pos=wx.Point(24,
              247), size=wx.Size(240, 21), style=0, value=u'')
        self.campoLogin.SetMaxLength(50)

        self.nomeSenha = wx.StaticText(id=wxID_FRAMEEXCLUSAOFUNCIONARIOSNOMESENHA,
              label=u'Senha:', name=u'nomeSenha', parent=self.painelExcluir,
              pos=wx.Point(11, 277), size=wx.Size(35, 13), style=0)

        self.campoSenha = wx.TextCtrl(id=wxID_FRAMEEXCLUSAOFUNCIONARIOSCAMPOSENHA,
              name=u'campoSenha', parent=self.painelExcluir, pos=wx.Point(24,
              296), size=wx.Size(240, 21), style=wx.TE_PASSWORD, value=u'')
        self.campoSenha.SetMaxLength(50)

        self.nomeErro = wx.StaticText(id=wxID_FRAMEEXCLUSAOFUNCIONARIOSNOMEERRO,
              label=u'', name=u'nomeErro', parent=self.painelExcluir,
              pos=wx.Point(576, 144), size=wx.Size(0, 13), style=0)
        self.nomeErro.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))

        self.botaoExcluir = wx.Button(id=wxID_FRAMEEXCLUSAOFUNCIONARIOSBOTAOEXCLUIR,
              label=u'Excluir', name=u'botaoExcluir', parent=self.painelExcluir,
              pos=wx.Point(896, 520), size=wx.Size(75, 23), style=0)
        self.botaoExcluir.Bind(wx.EVT_BUTTON, self.OnBotaoExcluirButton,
              id=wxID_FRAMEEXCLUSAOFUNCIONARIOSBOTAOEXCLUIR)

        self.botaoVoltar = wx.BitmapButton(bitmap=wx.Bitmap(u'./Graficos/botao_voltar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEEXCLUSAOFUNCIONARIOSBOTAOVOLTAR,
              name=u'botaoVoltar', parent=self.painelExcluir, pos=wx.Point(952,
              13), size=wx.Size(57, 57), style=wx.BU_AUTODRAW)
        self.botaoVoltar.Bind(wx.EVT_BUTTON, self.OnBotaoVoltarButton,
              id=wxID_FRAMEEXCLUSAOFUNCIONARIOSBOTAOVOLTAR)

    def __init__(self, parent):
        self._init_ctrls(parent)
        
    def validar_cpf(self, cpf):
        digitos = [int(c) for c in cpf if c.isdigit()]
        if len(digitos) == 11:
            if cpf == "11111111111":
                return False
            elif cpf == "22222222222":
                return False
            elif cpf == "33333333333":
                return False
            elif cpf == "44444444444":
                return False
            elif cpf == "55555555555":
                return False
            elif cpf == "66666666666":
                return False
            elif cpf == "77777777777":
                return False
            elif cpf == "88888888888":
                return False
            elif cpf == "99999999999":
                return False
            elif cpf == "00000000000":
                return False
            else:
                a,b,c,d,e,f,g,h,i,j,k = digitos
                numeros = [a,b,c,d,e,f,g,h,i]
                r = range(10, 1, -1)
                soma = sum([x * y for x, y in zip(numeros, r)])
                resto = soma % 11
                dv1 = (11 - resto if 11 - resto < 10 else 0)
                numeros = [a,b,c,d,e,f,g,h,i,dv1]
                r = range(11, 1, -1)
                soma = sum([x*y for x, y in zip(numeros, r)])
                resto = soma % 11
                dv2 = (11 - resto if 11 - resto < 10 else 0)
                return dv1 == j and dv2 == k
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



    def OnBotaoLimparPessoalButton(self, event):
        self.campoCPF.SetValue('')
        self.campoAniversario.SetValue('')
        self.campoNomeAluno.SetValue('')
        self.campoNomeMae.SetValue('')
        self.campoNomePai.SetValue('')
        self.campoCEP.SetValue('')
        self.campoNumero.SetValue('')
        self.campoComplemento.SetValue('')
        self.campoEndereco.SetValue('')
        self.campoBairro.SetValue('')
        self.campoCidade.SetValue('')
        self.campoUF.SetValue('')
        self.nomeErro.SetLabel('')
        event.Skip()


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



    def OnBotaoLimparProfissionalButton(self, event):
        self.campoMatricula.SetValue('')
        
        self.campoAnoConclusao.SetValue('')
        self.opcaoManha.SetValue(False)
        self.opcaoTarde.SetValue(False)
        self.opcaoNoite.SetValue(False)
        
        event.Skip()

    def OnBotaoVoltarButton(self, event):
        event.Skip()

    def OnBuscarCPFButton(self, event):
        event.Skip()

    def OnVerificarEstagioRadiobox(self, event):
        event.Skip()
        
    def OnBotaoLimparContatoButton(self, event):
        self.campoEmail.SetValue('')
        self.campoTelefone.SetValue('')
        self.campoCelular.SetValue('')
        
        event.Skip()

    def OnBotaoSalvarButton(self, event):
        NomeAluno = self.campoNomeAluno.GetValue()
        NomeAluno = NomeAluno.upper()
        self.campoNomeAluno.SetValue(NomeAluno)

        NomeMae = self.campoNomeMae.GetValue()
        NomeMae = NomeMae.upper()
        self.campoNomeMae.SetValue(NomeMae)

        NomePai = self.campoNomePai.GetValue()
        NomePai = NomePai.upper()
        self.campoNomePai.SetValue(NomePai)

        Complemento = self.campoComplemento.GetValue()
        Complemento = Complemento.upper()
        self.campoComplemento.SetValue(Complemento)

        Endereco = self.campoEndereco.GetValue()
        Endereco = Endereco.upper()
        self.campoEndereco.SetValue(Endereco)

        Bairro = self.campoBairro.GetValue()
        Bairro = Bairro.upper()
        self.campoBairro.SetValue(Bairro)

        Matricula = self.campoMatricula.GetValue()
        Matricula = Matricula.upper()
        self.campoMatricula.SetValue(Matricula)

        Email = self.campoEmail.GetValue()
        Email = Email.upper()
        self.campoEmail.SetValue(Email)
        
        event.Skip()

    def OnBotaoExcluirButton(self, event):
        event.Skip()



