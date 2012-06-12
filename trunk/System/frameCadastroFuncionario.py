#Boa:Frame:frameCadastroFuncionario
#! /usr/bin/env python
#-*-coding: latin1-*-
#-*-coding: iso-8859-1-*-  

import wx
import wx.lib.masked.textctrl
import urllib  
import cgi
import bridge

def create(parent):
    return frameCadastroFuncionario(parent)

[wxID_FRAMECADASTROFUNCIONARIO, wxID_FRAMECADASTROFUNCIONARIOBOTAOBUSCARCEP, 
 wxID_FRAMECADASTROFUNCIONARIOBOTAOLIMPARFUNCIONARIO, 
 wxID_FRAMECADASTROFUNCIONARIOBOTAOSALVAR, 
 wxID_FRAMECADASTROFUNCIONARIOBOTAOVOLTAR, 
 wxID_FRAMECADASTROFUNCIONARIOCAMPOANIVERSARIO, 
 wxID_FRAMECADASTROFUNCIONARIOCAMPOBAIRRO, 
 wxID_FRAMECADASTROFUNCIONARIOCAMPOCELULAR, 
 wxID_FRAMECADASTROFUNCIONARIOCAMPOCEP, 
 wxID_FRAMECADASTROFUNCIONARIOCAMPOCIDADE, 
 wxID_FRAMECADASTROFUNCIONARIOCAMPOCOMPLEMENTO, 
 wxID_FRAMECADASTROFUNCIONARIOCAMPOCONFIRMARSENHA, 
 wxID_FRAMECADASTROFUNCIONARIOCAMPOCPF, 
 wxID_FRAMECADASTROFUNCIONARIOCAMPOENDERECO, 
 wxID_FRAMECADASTROFUNCIONARIOCAMPOLOGIN, 
 wxID_FRAMECADASTROFUNCIONARIOCAMPONOMEFUNCIONARIO, 
 wxID_FRAMECADASTROFUNCIONARIOCAMPONUMERO, 
 wxID_FRAMECADASTROFUNCIONARIOCAMPOSENHA, 
 wxID_FRAMECADASTROFUNCIONARIOCAMPOTELEFONE, 
 wxID_FRAMECADASTROFUNCIONARIOCAMPOUF, 
 wxID_FRAMECADASTROFUNCIONARIOCPFINVALIDO, 
 wxID_FRAMECADASTROFUNCIONARIOCPFVALIDO, 
 wxID_FRAMECADASTROFUNCIONARIODATANASCIMENTO, 
 wxID_FRAMECADASTROFUNCIONARIOLINHACADASTROFUNCIONARIOS, 
 wxID_FRAMECADASTROFUNCIONARIOLOGOIFPE, 
 wxID_FRAMECADASTROFUNCIONARIONOMEBAIRRO, 
 wxID_FRAMECADASTROFUNCIONARIONOMECELULAR, 
 wxID_FRAMECADASTROFUNCIONARIONOMECEP, 
 wxID_FRAMECADASTROFUNCIONARIONOMECIDADE, 
 wxID_FRAMECADASTROFUNCIONARIONOMECOMPLEMENTO, 
 wxID_FRAMECADASTROFUNCIONARIONOMECONFIMARSENHA, 
 wxID_FRAMECADASTROFUNCIONARIONOMECPF, 
 wxID_FRAMECADASTROFUNCIONARIONOMEENDERECO, 
 wxID_FRAMECADASTROFUNCIONARIONOMEERRO, 
 wxID_FRAMECADASTROFUNCIONARIONOMELOGIN, 
 wxID_FRAMECADASTROFUNCIONARIONOMENOMEALUNO, 
 wxID_FRAMECADASTROFUNCIONARIONOMENUMERO, 
 wxID_FRAMECADASTROFUNCIONARIONOMESENHA, 
 wxID_FRAMECADASTROFUNCIONARIONOMETELEFONE, 
 wxID_FRAMECADASTROFUNCIONARIONOMEUF, 
 wxID_FRAMECADASTROFUNCIONARIOPAINELEDICAOFUNCIONARIO, 
 wxID_FRAMECADASTROFUNCIONARIOSELECIONASEXO, 
 wxID_FRAMECADASTROFUNCIONARIOSELECIONATIPOUSUARIO, 
 wxID_FRAMECADASTROFUNCIONARIOVALIDARCPF, 
] = [wx.NewId() for _init_ctrls in range(44)]

class frameCadastroFuncionario(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMECADASTROFUNCIONARIO,
              name=u'frameCadastroFuncionario', parent=prnt, pos=wx.Point(700,
              273), size=wx.Size(1040, 614), style=wx.DEFAULT_FRAME_STYLE,
              title=u'Est\xe1gio Curricular - Cadastro de Funcion\xe1rios')
        self.SetClientSize(wx.Size(1024, 576))
        self.Center(wx.BOTH)
        self.SetIcon(wx.Icon(u'./Graficos/icone.ico',wx.BITMAP_TYPE_ICO))
        self.SetMaxSize(wx.Size(1040, 614))
        self.SetMinSize(wx.Size(1040, 614))

        self.painelEdicaoFuncionario = wx.Panel(id=wxID_FRAMECADASTROFUNCIONARIOPAINELEDICAOFUNCIONARIO,
              name=u'painelEdicaoFuncionario', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(1024, 576), style=wx.TAB_TRAVERSAL)
        self.painelEdicaoFuncionario.SetBackgroundColour(wx.Colour(255, 255,
              255))

        self.logoIFPE = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/logo.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMECADASTROFUNCIONARIOLOGOIFPE,
              name=u'logoIFPE', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(8, 8), size=wx.Size(175, 70), style=0)

        self.linhaCadastroFuncionarios = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/LinhaCadastroFuncionarios.png',
              wx.BITMAP_TYPE_PNG),
              id=wxID_FRAMECADASTROFUNCIONARIOLINHACADASTROFUNCIONARIOS,
              name=u'linhaCadastroFuncionarios',
              parent=self.painelEdicaoFuncionario, pos=wx.Point(0, 80),
              size=wx.Size(1024, 21), style=0)

        self.nomeCPF = wx.StaticText(id=wxID_FRAMECADASTROFUNCIONARIONOMECPF,
              label=u'CPF:', name=u'nomeCPF',
              parent=self.painelEdicaoFuncionario, pos=wx.Point(11, 132),
              size=wx.Size(24, 13), style=0)

        self.campoCPF = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRAMECADASTROFUNCIONARIOCAMPOCPF,
              name=u'campoCPF', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(24, 150), size=wx.Size(104, 21), style=0, value=u'')
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

        self.CPFInvalido = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/botao_invalido.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMECADASTROFUNCIONARIOCPFINVALIDO,
              name=u'CPFInvalido', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(170, 152), size=wx.Size(14, 14), style=0)
        self.CPFInvalido.Show(False)

        self.validarCPF = wx.BitmapButton(bitmap=wx.Bitmap(u'./Graficos/botao_buscar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMECADASTROFUNCIONARIOVALIDARCPF,
              name=u'validarCPF', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(134, 146), size=wx.Size(26, 26),
              style=wx.BU_AUTODRAW)
        self.validarCPF.Bind(wx.EVT_BUTTON, self.OnValidarCPFButton,
              id=wxID_FRAMECADASTROFUNCIONARIOVALIDARCPF)

        self.dataNascimento = wx.StaticText(id=wxID_FRAMECADASTROFUNCIONARIODATANASCIMENTO,
              label=u'Data de nascimento:', name=u'dataNascimento',
              parent=self.painelEdicaoFuncionario, pos=wx.Point(202, 130),
              size=wx.Size(100, 13), style=0)

        self.campoAniversario = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRAMECADASTROFUNCIONARIOCAMPOANIVERSARIO,
              name=u'campoAniversario', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(215, 149), size=wx.Size(104, 21), style=0,
              value=u'')
        self.campoAniversario.SetMask(u'XX/XX/XXXX')
        self.campoAniversario.SetAutoformat('')
        self.campoAniversario.SetFormatcodes('')
        self.campoAniversario.SetDescription('')
        self.campoAniversario.SetExcludeChars('')
        self.campoAniversario.SetValidRegex('')
        self.campoAniversario.SetMaxLength(10)
        self.campoAniversario.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))
        self.campoAniversario.SetDatestyle('MDY')

        self.selecionaSexo = wx.RadioBox(choices=['Feminino', 'Masculino'],
              id=wxID_FRAMECADASTROFUNCIONARIOSELECIONASEXO, label=u'Sexo:',
              majorDimension=1, name=u'selecionaSexo',
              parent=self.painelEdicaoFuncionario, pos=wx.Point(342, 130),
              size=wx.Size(176, 43), style=wx.RA_SPECIFY_ROWS)
        self.selecionaSexo.SetStringSelection(u'Feminino')

        self.nomeNomeAluno = wx.StaticText(id=wxID_FRAMECADASTROFUNCIONARIONOMENOMEALUNO,
              label=u'Nome Completo:', name=u'nomeNomeAluno',
              parent=self.painelEdicaoFuncionario, pos=wx.Point(11, 186),
              size=wx.Size(80, 13), style=0)

        self.campoNomeFuncionario = wx.TextCtrl(id=wxID_FRAMECADASTROFUNCIONARIOCAMPONOMEFUNCIONARIO,
              name=u'campoNomeFuncionario', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(24, 205), size=wx.Size(496, 21), style=0, value=u'')
        self.campoNomeFuncionario.SetMaxLength(50)
        self.campoNomeFuncionario.SetToolTipString(u'campoNomeFuncionario')

        self.nomeCEP = wx.StaticText(id=wxID_FRAMECADASTROFUNCIONARIONOMECEP,
              label=u'CEP:', name=u'nomeCEP',
              parent=self.painelEdicaoFuncionario, pos=wx.Point(11, 240),
              size=wx.Size(24, 13), style=0)

        self.campoCEP = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRAMECADASTROFUNCIONARIOCAMPOCEP,
              name=u'campoCEP', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(24, 259), size=wx.Size(104, 21), style=0,
              value=u'  .   -   ')
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
              wx.BITMAP_TYPE_PNG),
              id=wxID_FRAMECADASTROFUNCIONARIOBOTAOBUSCARCEP,
              name=u'botaoBuscarCEP', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(136, 256), size=wx.Size(26, 26),
              style=wx.BU_AUTODRAW)
        self.botaoBuscarCEP.Bind(wx.EVT_BUTTON, self.OnBotaoBuscarCEPButton,
              id=wxID_FRAMECADASTROFUNCIONARIOBOTAOBUSCARCEP)

        self.nomeNumero = wx.StaticText(id=wxID_FRAMECADASTROFUNCIONARIONOMENUMERO,
              label=u'N\xfamero:', name=u'nomeNumero',
              parent=self.painelEdicaoFuncionario, pos=wx.Point(160, 240),
              size=wx.Size(42, 13), style=0)

        self.campoNumero = wx.TextCtrl(id=wxID_FRAMECADASTROFUNCIONARIOCAMPONUMERO,
              name=u'campoNumero', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(173, 259), size=wx.Size(100, 21), style=0,
              value=u'')

        self.nomeComplemento = wx.StaticText(id=wxID_FRAMECADASTROFUNCIONARIONOMECOMPLEMENTO,
              label=u'Complemento:', name=u'nomeComplemento',
              parent=self.painelEdicaoFuncionario, pos=wx.Point(293, 240),
              size=wx.Size(70, 13), style=0)

        self.campoComplemento = wx.TextCtrl(id=wxID_FRAMECADASTROFUNCIONARIOCAMPOCOMPLEMENTO,
              name=u'campoComplemento', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(306, 259), size=wx.Size(214, 21), style=0,
              value=u'')
        self.campoComplemento.SetToolTipString(u'campoComplemento')

        self.nomeEndereco = wx.StaticText(id=wxID_FRAMECADASTROFUNCIONARIONOMEENDERECO,
              label=u'Endere\xe7o:', name=u'nomeEndereco',
              parent=self.painelEdicaoFuncionario, pos=wx.Point(11, 295),
              size=wx.Size(50, 13), style=0)

        self.campoEndereco = wx.TextCtrl(id=wxID_FRAMECADASTROFUNCIONARIOCAMPOENDERECO,
              name=u'campoEndereco', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(24, 316), size=wx.Size(496, 21), style=0, value=u'')

        self.nomeBairro = wx.StaticText(id=wxID_FRAMECADASTROFUNCIONARIONOMEBAIRRO,
              label=u'Bairro:', name=u'nomeBairro',
              parent=self.painelEdicaoFuncionario, pos=wx.Point(11, 349),
              size=wx.Size(33, 13), style=0)

        self.campoBairro = wx.TextCtrl(id=wxID_FRAMECADASTROFUNCIONARIOCAMPOBAIRRO,
              name=u'campoBairro', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(24, 368), size=wx.Size(224, 21), style=0, value=u'')

        self.nomeCidade = wx.StaticText(id=wxID_FRAMECADASTROFUNCIONARIONOMECIDADE,
              label=u'Cidade:', name=u'nomeCidade',
              parent=self.painelEdicaoFuncionario, pos=wx.Point(265, 349),
              size=wx.Size(38, 13), style=0)

        self.campoCidade = wx.TextCtrl(id=wxID_FRAMECADASTROFUNCIONARIOCAMPOCIDADE,
              name=u'campoCidade', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(278, 368), size=wx.Size(186, 21), style=0,
              value=u'')

        self.nomeUF = wx.StaticText(id=wxID_FRAMECADASTROFUNCIONARIONOMEUF,
              label=u'UF:', name=u'nomeUF', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(480, 349), size=wx.Size(18, 13), style=0)

        self.campoUF = wx.TextCtrl(id=wxID_FRAMECADASTROFUNCIONARIOCAMPOUF,
              name=u'campoUF', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(493, 368), size=wx.Size(27, 21), style=0, value=u'')
        self.campoUF.SetMaxLength(2)

        self.nomeTelefone = wx.StaticText(id=wxID_FRAMECADASTROFUNCIONARIONOMETELEFONE,
              label=u'Telefone:', name=u'nomeTelefone',
              parent=self.painelEdicaoFuncionario, pos=wx.Point(11, 396),
              size=wx.Size(47, 13), style=0)

        self.campoTelefone = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRAMECADASTROFUNCIONARIOCAMPOTELEFONE,
              name=u'campoTelefone', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(24, 415), size=wx.Size(136, 21), style=0,
              value=u'(  )    -    ')
        self.campoTelefone.SetAutoformat('')
        self.campoTelefone.SetMask(u'(XX)XXXX-XXXX')
        self.campoTelefone.SetFormatcodes('')
        self.campoTelefone.SetDescription('')
        self.campoTelefone.SetExcludeChars('')
        self.campoTelefone.SetValidRegex('')
        self.campoTelefone.SetMaxLength(13)
        self.campoTelefone.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))

        self.campoCelular = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRAMECADASTROFUNCIONARIOCAMPOCELULAR,
              name=u'campoCelular', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(379, 417), size=wx.Size(136, 21), style=0,
              value=u'')
        self.campoCelular.SetAutoformat('')
        self.campoCelular.SetMask(u'(XX)XXXX-XXXX')
        self.campoCelular.SetFormatcodes('')
        self.campoCelular.SetDescription('')
        self.campoCelular.SetExcludeChars('')
        self.campoCelular.SetValidRegex('')
        self.campoCelular.SetMaxLength(13)
        self.campoCelular.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))

        self.nomeCelular = wx.StaticText(id=wxID_FRAMECADASTROFUNCIONARIONOMECELULAR,
              label=u'Celular:', name=u'nomeCelular',
              parent=self.painelEdicaoFuncionario, pos=wx.Point(366, 398),
              size=wx.Size(38, 13), style=0)

        self.nomeLogin = wx.StaticText(id=wxID_FRAMECADASTROFUNCIONARIONOMELOGIN,
              label=u'Login:', name=u'nomeLogin',
              parent=self.painelEdicaoFuncionario, pos=wx.Point(14, 449),
              size=wx.Size(30, 13), style=0)

        self.campoLogin = wx.TextCtrl(id=wxID_FRAMECADASTROFUNCIONARIOCAMPOLOGIN,
              name=u'campoLogin', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(27, 470), size=wx.Size(224, 21), style=0, value=u'')

        self.selecionaTipoUsuario = wx.RadioBox(choices=['Administrador',
              'Operador'], id=wxID_FRAMECADASTROFUNCIONARIOSELECIONATIPOUSUARIO,
              label=u'Tipo de Usu\xe1rio:', majorDimension=1,
              name=u'selecionaTipoUsuario', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(335, 449), size=wx.Size(184, 43),
              style=wx.RA_SPECIFY_ROWS)
        self.selecionaTipoUsuario.SetStringSelection(u'Operador')

        self.nomeSenha = wx.StaticText(id=wxID_FRAMECADASTROFUNCIONARIONOMESENHA,
              label=u'Senha:', name=u'nomeSenha',
              parent=self.painelEdicaoFuncionario, pos=wx.Point(11, 499),
              size=wx.Size(35, 13), style=0)

        self.campoSenha = wx.TextCtrl(id=wxID_FRAMECADASTROFUNCIONARIOCAMPOSENHA,
              name=u'campoSenha', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(24, 520), size=wx.Size(224, 21),
              style=wx.TE_PASSWORD, value=u'')

        self.nomeConfimarSenha = wx.StaticText(id=wxID_FRAMECADASTROFUNCIONARIONOMECONFIMARSENHA,
              label=u'Confirmar Senha:', name=u'nomeConfimarSenha',
              parent=self.painelEdicaoFuncionario, pos=wx.Point(282, 499),
              size=wx.Size(85, 13), style=0)

        self.campoConfirmarSenha = wx.TextCtrl(id=wxID_FRAMECADASTROFUNCIONARIOCAMPOCONFIRMARSENHA,
              name=u'campoConfirmarSenha', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(296, 520), size=wx.Size(224, 21),
              style=wx.TE_PASSWORD, value=u'')

        self.botaoSalvar = wx.Button(id=wxID_FRAMECADASTROFUNCIONARIOBOTAOSALVAR,
              label=u'Salvar', name=u'botaoSalvar',
              parent=self.painelEdicaoFuncionario, pos=wx.Point(920, 536),
              size=wx.Size(75, 23), style=0)
        self.botaoSalvar.Bind(wx.EVT_BUTTON, self.OnBotaoSalvarButton,
              id=wxID_FRAMECADASTROFUNCIONARIOBOTAOSALVAR)

        self.cpfValido = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/botao_valido.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMECADASTROFUNCIONARIOCPFVALIDO,
              name=u'cpfValido', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(170, 151), size=wx.Size(14, 16), style=0)
        self.cpfValido.Show(False)

        self.botaoVoltar = wx.BitmapButton(bitmap=wx.Bitmap(u'./Graficos/botao_voltar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMECADASTROFUNCIONARIOBOTAOVOLTAR,
              name=u'botaoVoltar', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(952, 13), size=wx.Size(57, 57),
              style=wx.BU_AUTODRAW)
        self.botaoVoltar.Bind(wx.EVT_BUTTON, self.OnBotaoVoltarButton,
              id=wxID_FRAMECADASTROFUNCIONARIOBOTAOVOLTAR)

        self.botaoLimparFuncionario = wx.Button(id=wxID_FRAMECADASTROFUNCIONARIOBOTAOLIMPARFUNCIONARIO,
              label=u'Limpar', name=u'botaoLimparFuncionario',
              parent=self.painelEdicaoFuncionario, pos=wx.Point(880, 129),
              size=wx.Size(75, 23), style=0)
        self.botaoLimparFuncionario.Bind(wx.EVT_BUTTON,
              self.OnBotaoLimparFuncionarioButton,
              id=wxID_FRAMECADASTROFUNCIONARIOBOTAOLIMPARFUNCIONARIO)

        self.nomeErro = wx.StaticText(id=wxID_FRAMECADASTROFUNCIONARIONOMEERRO,
              label=u'', name=u'nomeErro', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(544, 144), size=wx.Size(0, 13), style=0)
        self.nomeErro.SetAutoLayout(True)
        self.nomeErro.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, True,
              u'Tahoma'))

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

    def OnValidarCPFButton(self, event):
        cpf = self.campoCPF.GetValue()
        cpf = cpf[0:3:1]+cpf[4:7:1]+cpf[8:11:1]+cpf[12:14:1]
        if self.validar_cpf(cpf) == True:
            self.CPFInvalido.Show(False)
            self.cpfValido.Show(True)
            self.nomeErro.SetLabel('')
        else:
            self.CPFInvalido.Show(True)
            self.cpfValido.Show(False)
            self.nomeErro.SetLabel('CPF Invalido!') 
        event.Skip()

    def OnBotaoVoltarButton(self, event):
        event.Skip()

    def OnBotaoSalvarButton(self, event):
        nome = self.campoNomeFuncionario.GetValue()
        nome = nome.upper()
        self.campoNomeFuncionario.SetValue(nome)

    	Complemento = self.campoComplemento.GetValue()
        Complemento = Complemento.upper()
        self.campoComplemento.SetValue(Complemento)

    	Endereco = self.campoEndereco.GetValue()
        Endereco = Endereco.upper()
        self.campoEndereco.SetValue(Endereco)
        
        Bairro = self.campoBairro.GetValue()
        Bairro = Bairro.upper()
        self.campoBairro.SetValue(Bairro)

        Email = self.campoEmail.GetValue()
        Email = Email.upper()
        self.campoEmail.SetValue(Email)
        
        event.Skip()

    def OnBotaoLimparFuncionarioButton(self, event):
        self.campoCPF.SetValue('')
        self.campoAniversario.SetValue('')
        self.campoNomeFuncionario.SetValue('')
        self.campoCEP.SetValue('')
        self.campoNumero.SetValue('')
        self.campoComplemento.SetValue('')
        self.campoEndereco.SetValue('')
        self.campoBairro.SetValue('')
        self.campoCidade.SetValue('')
        self.campoUF.SetValue('')
        self.nomeErro.SetLabel('')
        self.campoTelefone.SetValue('')
        self.campoCelular.SetValue('')
        self.campoLogin.SetValue('')
        self.campoSenha.SetValue('')
        self.campoConfirmarSenha.SetValue('')
        self.CPFInvalido.Show(False)
        self.cpfValido.Show(False)
        self.selecionaSexo.SetStringSelection(u'Feminino')
        self.selecionaTipoUsuario.SetStringSelection(u'Operador')
        
        event.Skip()

