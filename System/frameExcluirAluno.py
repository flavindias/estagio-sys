#Boa:Frame:frameExclusaoAluno
#! /usr/bin/env python
#-*-coding: latin1-*-
#-*-coding: iso-8859-1-*-  

import wx
import wx.lib.masked.textctrl
import urllib  
import cgi
import bridge


def create(parent):
    return frameExclusaoAluno(parent)

[wxID_FRAMEEXCLUSAOALUNO, wxID_FRAMEEXCLUSAOALUNOBOTAOEXCLUIR, 
 wxID_FRAMEEXCLUSAOALUNOBOTAOVOLTAR, wxID_FRAMEEXCLUSAOALUNOBUSCARCPF, 
 wxID_FRAMEEXCLUSAOALUNOCAMPOCPF, wxID_FRAMEEXCLUSAOALUNOCAMPOLOGIN, 
 wxID_FRAMEEXCLUSAOALUNOCAMPONOMEALUNO, wxID_FRAMEEXCLUSAOALUNOCAMPOSENHA, 
 wxID_FRAMEEXCLUSAOALUNOCPFENCONTRADO, 
 wxID_FRAMEEXCLUSAOALUNOCPFNAOENCONTRADO, 
 wxID_FRAMEEXCLUSAOALUNOLINHAEXCLUSAOALUNOS, wxID_FRAMEEXCLUSAOALUNOLOGOIFPE, 
 wxID_FRAMEEXCLUSAOALUNONOMECPF, wxID_FRAMEEXCLUSAOALUNONOMEERRO, 
 wxID_FRAMEEXCLUSAOALUNONOMELOGIN, wxID_FRAMEEXCLUSAOALUNONOMENOMEALUNO, 
 wxID_FRAMEEXCLUSAOALUNONOMESENHA, wxID_FRAMEEXCLUSAOALUNOPAINELEXCLUIR, 
] = [wx.NewId() for _init_ctrls in range(18)]

class frameExclusaoAluno(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEEXCLUSAOALUNO,
              name=u'frameExclusaoAluno', parent=prnt, pos=wx.Point(700, 273),
              size=wx.Size(1040, 614), style=wx.DEFAULT_FRAME_STYLE,
              title=u'Est\xe1gio Curricular - Edi\xe7\xe3o Cadastral de Alunos')
        self.SetClientSize(wx.Size(1024, 576))
        self.Center(wx.BOTH)
        self.SetIcon(wx.Icon(u'./Graficos/icone.ico',wx.BITMAP_TYPE_ICO))
        self.SetMaxSize(wx.Size(1040, 614))
        self.SetMinSize(wx.Size(1040, 614))

        self.painelExcluir = wx.Panel(id=wxID_FRAMEEXCLUSAOALUNOPAINELEXCLUIR,
              name=u'painelExcluir', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(1024, 576), style=wx.TAB_TRAVERSAL)
        self.painelExcluir.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.logoIFPE = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/logo.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEEXCLUSAOALUNOLOGOIFPE,
              name=u'logoIFPE', parent=self.painelExcluir, pos=wx.Point(8, 8),
              size=wx.Size(175, 70), style=0)

        self.nomeCPF = wx.StaticText(id=wxID_FRAMEEXCLUSAOALUNONOMECPF,
              label=u'CPF:', name=u'nomeCPF', parent=self.painelExcluir,
              pos=wx.Point(11, 122), size=wx.Size(24, 13), style=0)

        self.campoCPF = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRAMEEXCLUSAOALUNOCAMPOCPF,
              name=u'campoCPF', parent=self.painelExcluir, pos=wx.Point(24,
              141), size=wx.Size(104, 21), style=0, value=u'')
        self.campoCPF.SetMask(u'XXX.XXX.XXX-XX')
        self.campoCPF.SetAutoformat('')
        self.campoCPF.SetFormatcodes('')
        self.campoCPF.SetDescription('')
        self.campoCPF.SetExcludeChars('')
        self.campoCPF.SetValidRegex('')
        self.campoCPF.SetMaxLength(14)
        self.campoCPF.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))
        self.campoCPF.SetDefaultEncoding(u'latin1')
        self.campoCPF.SetFillChar(u' ')

        self.linhaExclusaoAlunos = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/LinhaExclusaoAlunos.png',
              wx.BITMAP_TYPE_PNG),
              id=wxID_FRAMEEXCLUSAOALUNOLINHAEXCLUSAOALUNOS,
              name=u'linhaExclusaoAlunos', parent=self.painelExcluir,
              pos=wx.Point(0, 80), size=wx.Size(1024, 25), style=0)

        self.cpfEncontrado = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/botao_valido.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEEXCLUSAOALUNOCPFENCONTRADO,
              name=u'cpfEncontrado', parent=self.painelExcluir,
              pos=wx.Point(170, 143), size=wx.Size(14, 14), style=0)
        self.cpfEncontrado.Show(False)

        self.cpfNaoEncontrado = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/botao_invalido.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEEXCLUSAOALUNOCPFNAOENCONTRADO,
              name=u'cpfNaoEncontrado', parent=self.painelExcluir,
              pos=wx.Point(170, 143), size=wx.Size(14, 14), style=0)
        self.cpfNaoEncontrado.Show(False)

        self.BuscarCPF = wx.BitmapButton(bitmap=wx.Bitmap(u'./Graficos/botao_carregar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEEXCLUSAOALUNOBUSCARCPF,
              name=u'BuscarCPF', parent=self.painelExcluir, pos=wx.Point(134,
              137), size=wx.Size(26, 26), style=wx.BU_AUTODRAW)
        self.BuscarCPF.Bind(wx.EVT_BUTTON, self.OnBuscarCPFButton,
              id=wxID_FRAMEEXCLUSAOALUNOBUSCARCPF)

        self.nomeNomeAluno = wx.StaticText(id=wxID_FRAMEEXCLUSAOALUNONOMENOMEALUNO,
              label=u'Nome do Aluno:', name=u'nomeNomeAluno',
              parent=self.painelExcluir, pos=wx.Point(11, 177), size=wx.Size(77,
              13), style=0)

        self.campoNomeAluno = wx.TextCtrl(id=wxID_FRAMEEXCLUSAOALUNOCAMPONOMEALUNO,
              name=u'campoNomeAluno', parent=self.painelExcluir,
              pos=wx.Point(24, 196), size=wx.Size(496, 21),
              style=wx.TE_READONLY, value=u'')
        self.campoNomeAluno.SetMaxLength(50)

        self.nomeLogin = wx.StaticText(id=wxID_FRAMEEXCLUSAOALUNONOMELOGIN,
              label=u'Login:', name=u'nomeLogin', parent=self.painelExcluir,
              pos=wx.Point(11, 228), size=wx.Size(30, 13), style=0)

        self.campoLogin = wx.TextCtrl(id=wxID_FRAMEEXCLUSAOALUNOCAMPOLOGIN,
              name=u'campoLogin', parent=self.painelExcluir, pos=wx.Point(24,
              247), size=wx.Size(240, 21), style=0, value=u'')
        self.campoLogin.SetMaxLength(50)

        self.nomeSenha = wx.StaticText(id=wxID_FRAMEEXCLUSAOALUNONOMESENHA,
              label=u'Senha:', name=u'nomeSenha', parent=self.painelExcluir,
              pos=wx.Point(11, 277), size=wx.Size(35, 13), style=0)

        self.campoSenha = wx.TextCtrl(id=wxID_FRAMEEXCLUSAOALUNOCAMPOSENHA,
              name=u'campoSenha', parent=self.painelExcluir, pos=wx.Point(24,
              296), size=wx.Size(240, 21), style=wx.TE_PASSWORD, value=u'')
        self.campoSenha.SetMaxLength(50)

        self.nomeErro = wx.StaticText(id=wxID_FRAMEEXCLUSAOALUNONOMEERRO,
              label=u'', name=u'nomeErro', parent=self.painelExcluir,
              pos=wx.Point(576, 144), size=wx.Size(0, 13), style=0)
        self.nomeErro.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))

        self.botaoExcluir = wx.Button(id=wxID_FRAMEEXCLUSAOALUNOBOTAOEXCLUIR,
              label=u'Excluir', name=u'botaoExcluir', parent=self.painelExcluir,
              pos=wx.Point(896, 520), size=wx.Size(75, 23), style=0)
        self.botaoExcluir.Bind(wx.EVT_BUTTON, self.OnBotaoExcluirButton,
              id=wxID_FRAMEEXCLUSAOALUNOBOTAOEXCLUIR)

        self.botaoVoltar = wx.BitmapButton(bitmap=wx.Bitmap(u'./Graficos/botao_voltar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEEXCLUSAOALUNOBOTAOVOLTAR,
              name=u'botaoVoltar', parent=self.painelExcluir, pos=wx.Point(952,
              13), size=wx.Size(57, 57), style=wx.BU_AUTODRAW)
        self.botaoVoltar.Bind(wx.EVT_BUTTON, self.OnBotaoVoltarButton,
              id=wxID_FRAMEEXCLUSAOALUNOBOTAOVOLTAR)

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



