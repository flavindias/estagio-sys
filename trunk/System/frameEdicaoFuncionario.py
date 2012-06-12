#Boa:Frame:frameEdicaoFuncionario
#! /usr/bin/env python
#-*-coding: latin1-*-
#-*-coding: iso-8859-1-*-  

import wx
import wx.lib.masked.textctrl
import urllib  
import cgi
import bridge

departamentos = {'DACI': [None], 'DAFG': [None], 'DAIC': [None], 'DASE' : ["ANALISE E DESENVOLVIMENTO DE SISTEMAS", "ELETRONICA", "ELETROTECNICA", "TELECOMUNICACOES"], 'DASS' : [None], 'DGTI' : [None], 'DIAP' : [None]}
listdepartamentos = departamentos.keys()

def create(parent):
    return frameEdicaoFuncionario(parent)

[wxID_FRAMEEDICAOFUNCIONARIO, wxID_FRAMEEDICAOFUNCIONARIOBOTAOBUSCARCEP, 
 wxID_FRAMEEDICAOFUNCIONARIOBOTAOCARREGAR, 
 wxID_FRAMEEDICAOFUNCIONARIOBOTAOLIMPARFUNCIONARIO, 
 wxID_FRAMEEDICAOFUNCIONARIOBOTAOSALVAR, 
 wxID_FRAMEEDICAOFUNCIONARIOBOTAOVOLTAR, 
 wxID_FRAMEEDICAOFUNCIONARIOCAMPOANIVERSARIO, 
 wxID_FRAMEEDICAOFUNCIONARIOCAMPOBAIRRO, 
 wxID_FRAMEEDICAOFUNCIONARIOCAMPOCELULAR, wxID_FRAMEEDICAOFUNCIONARIOCAMPOCEP, 
 wxID_FRAMEEDICAOFUNCIONARIOCAMPOCIDADE, 
 wxID_FRAMEEDICAOFUNCIONARIOCAMPOCOMPLEMENTO, 
 wxID_FRAMEEDICAOFUNCIONARIOCAMPOCONFIRMARSENHA, 
 wxID_FRAMEEDICAOFUNCIONARIOCAMPOCPF, 
 wxID_FRAMEEDICAOFUNCIONARIOCAMPOENDERECO, 
 wxID_FRAMEEDICAOFUNCIONARIOCAMPOLOGIN, 
 wxID_FRAMEEDICAOFUNCIONARIOCAMPONOMEFUNCIONARIO, 
 wxID_FRAMEEDICAOFUNCIONARIOCAMPONUMERO, 
 wxID_FRAMEEDICAOFUNCIONARIOCAMPOSENHA, 
 wxID_FRAMEEDICAOFUNCIONARIOCAMPOTELEFONE, wxID_FRAMEEDICAOFUNCIONARIOCAMPOUF, 
 wxID_FRAMEEDICAOFUNCIONARIOCPFINVALIDO, wxID_FRAMEEDICAOFUNCIONARIOCPFVALIDO, 
 wxID_FRAMEEDICAOFUNCIONARIODATANASCIMENTO, 
 wxID_FRAMEEDICAOFUNCIONARIOLINHACADASTROFUNCIONARIOS, 
 wxID_FRAMEEDICAOFUNCIONARIOLOGOIFPE, wxID_FRAMEEDICAOFUNCIONARIONOMEBAIRRO, 
 wxID_FRAMEEDICAOFUNCIONARIONOMECELULAR, wxID_FRAMEEDICAOFUNCIONARIONOMECEP, 
 wxID_FRAMEEDICAOFUNCIONARIONOMECIDADE, 
 wxID_FRAMEEDICAOFUNCIONARIONOMECOMPLEMENTO, 
 wxID_FRAMEEDICAOFUNCIONARIONOMECONFIMARSENHA, 
 wxID_FRAMEEDICAOFUNCIONARIONOMECPF, wxID_FRAMEEDICAOFUNCIONARIONOMEENDERECO, 
 wxID_FRAMEEDICAOFUNCIONARIONOMEERRO, wxID_FRAMEEDICAOFUNCIONARIONOMELOGIN, 
 wxID_FRAMEEDICAOFUNCIONARIONOMENOMEALUNO, 
 wxID_FRAMEEDICAOFUNCIONARIONOMENUMERO, wxID_FRAMEEDICAOFUNCIONARIONOMESENHA, 
 wxID_FRAMEEDICAOFUNCIONARIONOMETELEFONE, wxID_FRAMEEDICAOFUNCIONARIONOMEUF, 
 wxID_FRAMEEDICAOFUNCIONARIOPAINELEDICAOFUNCIONARIO, 
 wxID_FRAMEEDICAOFUNCIONARIOSELECIONASEXO, 
 wxID_FRAMEEDICAOFUNCIONARIOSELECIONATIPOUSUARIO, 
 wxID_FRAMEEDICAOFUNCIONARIOVALIDARCPF, 
] = [wx.NewId() for _init_ctrls in range(45)]

class frameEdicaoFuncionario(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEEDICAOFUNCIONARIO,
              name=u'frameEdicaoFuncionario', parent=prnt, pos=wx.Point(700,
              273), size=wx.Size(1040, 614), style=wx.DEFAULT_FRAME_STYLE,
              title=u'Est\xe1gio Curricular - Edi\xe7\xe3o de Funcion\xe1rios')
        self.SetClientSize(wx.Size(1024, 576))
        self.Center(wx.BOTH)
        self.SetIcon(wx.Icon(u'./Graficos/icone.ico',wx.BITMAP_TYPE_ICO))
        self.SetMaxSize(wx.Size(1040, 614))
        self.SetMinSize(wx.Size(1040, 614))

        self.painelEdicaoFuncionario = wx.Panel(id=wxID_FRAMEEDICAOFUNCIONARIOPAINELEDICAOFUNCIONARIO,
              name=u'painelEdicaoFuncionario', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(1024, 576), style=wx.TAB_TRAVERSAL)
        self.painelEdicaoFuncionario.SetBackgroundColour(wx.Colour(255, 255,
              255))

        self.nomeLogin = wx.StaticText(id=wxID_FRAMEEDICAOFUNCIONARIONOMELOGIN,
              label=u'Login:', name=u'nomeLogin',
              parent=self.painelEdicaoFuncionario, pos=wx.Point(12, 127),
              size=wx.Size(30, 13), style=0)

        self.campoLogin = wx.TextCtrl(id=wxID_FRAMEEDICAOFUNCIONARIOCAMPOLOGIN,
              name=u'campoLogin', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(25, 148), size=wx.Size(224, 21), style=0, value=u'')

        self.botaoCarregar = wx.BitmapButton(bitmap=wx.Bitmap(u'./Graficos/botao_carregar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEEDICAOFUNCIONARIOBOTAOCARREGAR,
              name=u'botaoCarregar', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(262, 144), size=wx.Size(26, 27),
              style=wx.BU_AUTODRAW)

        self.logoIFPE = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/logo.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEEDICAOFUNCIONARIOLOGOIFPE,
              name=u'logoIFPE', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(8, 8), size=wx.Size(175, 70), style=0)

        self.linhaCadastroFuncionarios = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/LinhaEdicaoFuncionarios.png',
              wx.BITMAP_TYPE_PNG),
              id=wxID_FRAMEEDICAOFUNCIONARIOLINHACADASTROFUNCIONARIOS,
              name=u'linhaCadastroFuncionarios',
              parent=self.painelEdicaoFuncionario, pos=wx.Point(0, 80),
              size=wx.Size(1024, 21), style=0)

        self.nomeCPF = wx.StaticText(id=wxID_FRAMEEDICAOFUNCIONARIONOMECPF,
              label=u'CPF:', name=u'nomeCPF',
              parent=self.painelEdicaoFuncionario, pos=wx.Point(11, 185),
              size=wx.Size(24, 13), style=0)

        self.campoCPF = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRAMEEDICAOFUNCIONARIOCAMPOCPF,
              name=u'campoCPF', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(24, 203), size=wx.Size(104, 21), style=0, value=u'')
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
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEEDICAOFUNCIONARIOCPFINVALIDO,
              name=u'CPFInvalido', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(170, 205), size=wx.Size(14, 14), style=0)
        self.CPFInvalido.Show(False)

        self.validarCPF = wx.BitmapButton(bitmap=wx.Bitmap(u'./Graficos/botao_buscar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEEDICAOFUNCIONARIOVALIDARCPF,
              name=u'validarCPF', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(134, 199), size=wx.Size(26, 26),
              style=wx.BU_AUTODRAW)
        self.validarCPF.Bind(wx.EVT_BUTTON, self.OnValidarCPFButton,
              id=wxID_FRAMEEDICAOFUNCIONARIOVALIDARCPF)

        self.dataNascimento = wx.StaticText(id=wxID_FRAMEEDICAOFUNCIONARIODATANASCIMENTO,
              label=u'Data de nascimento:', name=u'dataNascimento',
              parent=self.painelEdicaoFuncionario, pos=wx.Point(202, 183),
              size=wx.Size(100, 13), style=0)

        self.campoAniversario = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRAMEEDICAOFUNCIONARIOCAMPOANIVERSARIO,
              name=u'campoAniversario', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(215, 202), size=wx.Size(104, 21), style=0,
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
              id=wxID_FRAMEEDICAOFUNCIONARIOSELECIONASEXO, label=u'Sexo:',
              majorDimension=1, name=u'selecionaSexo',
              parent=self.painelEdicaoFuncionario, pos=wx.Point(342, 183),
              size=wx.Size(176, 43), style=wx.RA_SPECIFY_ROWS)
        self.selecionaSexo.SetStringSelection(u'Feminino')

        self.nomeNomeAluno = wx.StaticText(id=wxID_FRAMEEDICAOFUNCIONARIONOMENOMEALUNO,
              label=u'Nome Completo:', name=u'nomeNomeAluno',
              parent=self.painelEdicaoFuncionario, pos=wx.Point(11, 239),
              size=wx.Size(80, 13), style=0)

        self.campoNomeFuncionario = wx.TextCtrl(id=wxID_FRAMEEDICAOFUNCIONARIOCAMPONOMEFUNCIONARIO,
              name=u'campoNomeFuncionario', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(24, 258), size=wx.Size(496, 21), style=0, value=u'')
        self.campoNomeFuncionario.SetMaxLength(50)
        self.campoNomeFuncionario.SetToolTipString(u'campoNomeFuncionario')

        self.nomeCEP = wx.StaticText(id=wxID_FRAMEEDICAOFUNCIONARIONOMECEP,
              label=u'CEP:', name=u'nomeCEP',
              parent=self.painelEdicaoFuncionario, pos=wx.Point(11, 293),
              size=wx.Size(24, 13), style=0)

        self.campoCEP = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRAMEEDICAOFUNCIONARIOCAMPOCEP,
              name=u'campoCEP', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(24, 312), size=wx.Size(104, 21), style=0,
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
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEEDICAOFUNCIONARIOBOTAOBUSCARCEP,
              name=u'botaoBuscarCEP', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(136, 309), size=wx.Size(26, 26),
              style=wx.BU_AUTODRAW)
        self.botaoBuscarCEP.Bind(wx.EVT_BUTTON, self.OnBotaoBuscarCEPButton,
              id=wxID_FRAMEEDICAOFUNCIONARIOBOTAOBUSCARCEP)

        self.nomeNumero = wx.StaticText(id=wxID_FRAMEEDICAOFUNCIONARIONOMENUMERO,
              label=u'N\xfamero:', name=u'nomeNumero',
              parent=self.painelEdicaoFuncionario, pos=wx.Point(160, 293),
              size=wx.Size(42, 13), style=0)

        self.campoNumero = wx.TextCtrl(id=wxID_FRAMEEDICAOFUNCIONARIOCAMPONUMERO,
              name=u'campoNumero', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(173, 312), size=wx.Size(100, 21), style=0,
              value=u'')

        self.nomeComplemento = wx.StaticText(id=wxID_FRAMEEDICAOFUNCIONARIONOMECOMPLEMENTO,
              label=u'Complemento:', name=u'nomeComplemento',
              parent=self.painelEdicaoFuncionario, pos=wx.Point(293, 293),
              size=wx.Size(70, 13), style=0)

        self.campoComplemento = wx.TextCtrl(id=wxID_FRAMEEDICAOFUNCIONARIOCAMPOCOMPLEMENTO,
              name=u'campoComplemento', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(306, 312), size=wx.Size(214, 21), style=0,
              value=u'')
        self.campoComplemento.SetToolTipString(u'campoComplemento')

        self.nomeEndereco = wx.StaticText(id=wxID_FRAMEEDICAOFUNCIONARIONOMEENDERECO,
              label=u'Endere\xe7o:', name=u'nomeEndereco',
              parent=self.painelEdicaoFuncionario, pos=wx.Point(11, 348),
              size=wx.Size(50, 13), style=0)

        self.campoEndereco = wx.TextCtrl(id=wxID_FRAMEEDICAOFUNCIONARIOCAMPOENDERECO,
              name=u'campoEndereco', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(24, 369), size=wx.Size(496, 21), style=0, value=u'')

        self.nomeBairro = wx.StaticText(id=wxID_FRAMEEDICAOFUNCIONARIONOMEBAIRRO,
              label=u'Bairro:', name=u'nomeBairro',
              parent=self.painelEdicaoFuncionario, pos=wx.Point(11, 402),
              size=wx.Size(33, 13), style=0)

        self.campoBairro = wx.TextCtrl(id=wxID_FRAMEEDICAOFUNCIONARIOCAMPOBAIRRO,
              name=u'campoBairro', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(24, 421), size=wx.Size(224, 21), style=0, value=u'')

        self.nomeCidade = wx.StaticText(id=wxID_FRAMEEDICAOFUNCIONARIONOMECIDADE,
              label=u'Cidade:', name=u'nomeCidade',
              parent=self.painelEdicaoFuncionario, pos=wx.Point(265, 402),
              size=wx.Size(38, 13), style=0)

        self.campoCidade = wx.TextCtrl(id=wxID_FRAMEEDICAOFUNCIONARIOCAMPOCIDADE,
              name=u'campoCidade', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(278, 421), size=wx.Size(186, 21), style=0,
              value=u'')

        self.nomeUF = wx.StaticText(id=wxID_FRAMEEDICAOFUNCIONARIONOMEUF,
              label=u'UF:', name=u'nomeUF', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(480, 402), size=wx.Size(18, 13), style=0)

        self.campoUF = wx.TextCtrl(id=wxID_FRAMEEDICAOFUNCIONARIOCAMPOUF,
              name=u'campoUF', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(493, 421), size=wx.Size(27, 21), style=0, value=u'')
        self.campoUF.SetMaxLength(2)

        self.nomeTelefone = wx.StaticText(id=wxID_FRAMEEDICAOFUNCIONARIONOMETELEFONE,
              label=u'Telefone:', name=u'nomeTelefone',
              parent=self.painelEdicaoFuncionario, pos=wx.Point(11, 449),
              size=wx.Size(47, 13), style=0)

        self.campoTelefone = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRAMEEDICAOFUNCIONARIOCAMPOTELEFONE,
              name=u'campoTelefone', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(24, 468), size=wx.Size(136, 21), style=0,
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

        self.nomeCelular = wx.StaticText(id=wxID_FRAMEEDICAOFUNCIONARIONOMECELULAR,
              label=u'Celular:', name=u'nomeCelular',
              parent=self.painelEdicaoFuncionario, pos=wx.Point(175, 451),
              size=wx.Size(38, 13), style=0)

        self.campoCelular = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRAMEEDICAOFUNCIONARIOCAMPOCELULAR,
              name=u'campoCelular', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(188, 470), size=wx.Size(136, 21), style=0,
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

        self.selecionaTipoUsuario = wx.RadioBox(choices=['Administrador',
              'Operador'], id=wxID_FRAMEEDICAOFUNCIONARIOSELECIONATIPOUSUARIO,
              label=u'Tipo de Usu\xe1rio:', majorDimension=1,
              name=u'selecionaTipoUsuario', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(335, 449), size=wx.Size(184, 43),
              style=wx.RA_SPECIFY_ROWS)
        self.selecionaTipoUsuario.SetStringSelection(u'Operador')

        self.nomeSenha = wx.StaticText(id=wxID_FRAMEEDICAOFUNCIONARIONOMESENHA,
              label=u'Senha:', name=u'nomeSenha',
              parent=self.painelEdicaoFuncionario, pos=wx.Point(11, 499),
              size=wx.Size(35, 13), style=0)

        self.campoSenha = wx.TextCtrl(id=wxID_FRAMEEDICAOFUNCIONARIOCAMPOSENHA,
              name=u'campoSenha', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(24, 520), size=wx.Size(224, 21),
              style=wx.TE_PASSWORD, value=u'')

        self.nomeConfimarSenha = wx.StaticText(id=wxID_FRAMEEDICAOFUNCIONARIONOMECONFIMARSENHA,
              label=u'Confirmar Senha:', name=u'nomeConfimarSenha',
              parent=self.painelEdicaoFuncionario, pos=wx.Point(282, 499),
              size=wx.Size(85, 13), style=0)

        self.campoConfirmarSenha = wx.TextCtrl(id=wxID_FRAMEEDICAOFUNCIONARIOCAMPOCONFIRMARSENHA,
              name=u'campoConfirmarSenha', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(296, 520), size=wx.Size(224, 21),
              style=wx.TE_PASSWORD, value=u'')

        self.botaoSalvar = wx.Button(id=wxID_FRAMEEDICAOFUNCIONARIOBOTAOSALVAR,
              label=u'Salvar', name=u'botaoSalvar',
              parent=self.painelEdicaoFuncionario, pos=wx.Point(920, 536),
              size=wx.Size(75, 23), style=0)
        self.botaoSalvar.Bind(wx.EVT_BUTTON, self.OnBotaoSalvarButton,
              id=wxID_FRAMEEDICAOFUNCIONARIOBOTAOSALVAR)

        self.cpfValido = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/botao_valido.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEEDICAOFUNCIONARIOCPFVALIDO,
              name=u'cpfValido', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(170, 205), size=wx.Size(14, 14), style=0)
        self.cpfValido.Show(False)

        self.botaoVoltar = wx.BitmapButton(bitmap=wx.Bitmap(u'./Graficos/botao_voltar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEEDICAOFUNCIONARIOBOTAOVOLTAR,
              name=u'botaoVoltar', parent=self.painelEdicaoFuncionario,
              pos=wx.Point(952, 13), size=wx.Size(57, 57),
              style=wx.BU_AUTODRAW)
        self.botaoVoltar.Bind(wx.EVT_BUTTON, self.OnBotaoVoltarButton,
              id=wxID_FRAMEEDICAOFUNCIONARIOBOTAOVOLTAR)

        self.botaoLimparFuncionario = wx.Button(id=wxID_FRAMEEDICAOFUNCIONARIOBOTAOLIMPARFUNCIONARIO,
              label=u'Limpar', name=u'botaoLimparFuncionario',
              parent=self.painelEdicaoFuncionario, pos=wx.Point(880, 129),
              size=wx.Size(75, 23), style=0)
        self.botaoLimparFuncionario.Bind(wx.EVT_BUTTON,
              self.OnBotaoLimparFuncionarioButton,
              id=wxID_FRAMEEDICAOFUNCIONARIOBOTAOLIMPARFUNCIONARIO)

        self.nomeErro = wx.StaticText(id=wxID_FRAMEEDICAOFUNCIONARIONOMEERRO,
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

