#Boa:Frame:frameCadastro
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
    return frameCadastro(parent)

[wxID_FRAMECADASTRO, wxID_FRAMECADASTROABACONTATO, 
 wxID_FRAMECADASTROABAPESSOAL, wxID_FRAMECADASTROABAPROFISSIONAL, 
 wxID_FRAMECADASTROBOTAOBUSCARCEP, wxID_FRAMECADASTROBOTAOLIMPARCONTATO, 
 wxID_FRAMECADASTROBOTAOLIMPARPESSOAL, 
 wxID_FRAMECADASTROBOTAOLIMPARPROFISSIONAL, wxID_FRAMECADASTROBOTAOSALVAR, 
 wxID_FRAMECADASTROBOTAOVOLTAR, wxID_FRAMECADASTROCAMPOANIVERSARIO, 
 wxID_FRAMECADASTROCAMPOANOCONCLUSAO, wxID_FRAMECADASTROCAMPOBAIRRO, 
 wxID_FRAMECADASTROCAMPOCELULAR, wxID_FRAMECADASTROCAMPOCEP, 
 wxID_FRAMECADASTROCAMPOCIDADE, wxID_FRAMECADASTROCAMPOCOMPLEMENTO, 
 wxID_FRAMECADASTROCAMPOCPF, wxID_FRAMECADASTROCAMPOEMAIL, 
 wxID_FRAMECADASTROCAMPOENDERECO, wxID_FRAMECADASTROCAMPOMATRICULA, 
 wxID_FRAMECADASTROCAMPONOMEALUNO, wxID_FRAMECADASTROCAMPONOMEMAE, 
 wxID_FRAMECADASTROCAMPONOMEPAI, wxID_FRAMECADASTROCAMPONUMERO, 
 wxID_FRAMECADASTROCAMPOTELEFONE, wxID_FRAMECADASTROCAMPOUF, 
 wxID_FRAMECADASTROCOMBOBOXCURSOS, wxID_FRAMECADASTROCOMBOBOXDEPARTAMENTO, 
 wxID_FRAMECADASTROCPFINVALIDO, wxID_FRAMECADASTROCPFVALIDO, 
 wxID_FRAMECADASTRODADOSDOSALUNOS, wxID_FRAMECADASTRODATANASCIMENTO, 
 wxID_FRAMECADASTROLINHACADASTROALUNOS, wxID_FRAMECADASTROLOGOIFPE, 
 wxID_FRAMECADASTRONOMEANOCONCLUSAO, wxID_FRAMECADASTRONOMEBAIRRO, 
 wxID_FRAMECADASTRONOMECELULAR, wxID_FRAMECADASTRONOMECEP, 
 wxID_FRAMECADASTRONOMECIDADE, wxID_FRAMECADASTRONOMECOMPLEMENTO, 
 wxID_FRAMECADASTRONOMECPF, wxID_FRAMECADASTRONOMECURSO, 
 wxID_FRAMECADASTRONOMEDEPARTAMENTO, wxID_FRAMECADASTRONOMEDISPONIBILIDADE, 
 wxID_FRAMECADASTRONOMEEMAIL, wxID_FRAMECADASTRONOMEENDERECO, 
 wxID_FRAMECADASTRONOMEERRO, wxID_FRAMECADASTRONOMEMATRICULA, 
 wxID_FRAMECADASTRONOMENOMEALUNO, wxID_FRAMECADASTRONOMENOMEMAE, 
 wxID_FRAMECADASTRONOMENOMEPAI, wxID_FRAMECADASTRONOMENUMERO, 
 wxID_FRAMECADASTRONOMETELEFONE, wxID_FRAMECADASTRONOMEUF, 
 wxID_FRAMECADASTROOPCAOMANHA, wxID_FRAMECADASTROOPCAONOITE, 
 wxID_FRAMECADASTROOPCAOTARDE, wxID_FRAMECADASTROPAINELCADASTRO, 
 wxID_FRAMECADASTROSELECIONASEXO, wxID_FRAMECADASTROVALIDARCPF, 
 wxID_FRAMECADASTROVERIFICARESTAGIO, 
] = [wx.NewId() for _init_ctrls in range(62)]

class frameCadastro(wx.Frame):
    def _init_coll_dadosDosAlunos_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.abaPessoal, select=True,
              text=u'Dados Pessoais')
        parent.AddPage(imageId=-1, page=self.abaProfissional, select=False,
              text=u'Dados Profissionais')
        parent.AddPage(imageId=-1, page=self.abaContato, select=False,
              text=u'Contato')

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMECADASTRO, name=u'frameCadastro',
              parent=prnt, pos=wx.Point(700, 273), size=wx.Size(1040, 614),
              style=wx.DEFAULT_FRAME_STYLE,
              title=u'Est\xe1gio Curricular - Cadastro de Alunos')
        self.SetClientSize(wx.Size(1024, 576))
        self.Center(wx.BOTH)
        self.SetIcon(wx.Icon(u'./Graficos/icone.ico',
              wx.BITMAP_TYPE_ICO))
        self.SetMaxSize(wx.Size(1040, 614))
        self.SetMinSize(wx.Size(1040, 614))

        self.painelCadastro = wx.Panel(id=wxID_FRAMECADASTROPAINELCADASTRO,
              name=u'painelCadastro', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(1024, 576), style=wx.TAB_TRAVERSAL)
        self.painelCadastro.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.logoIFPE = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/logo.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMECADASTROLOGOIFPE,
              name=u'logoIFPE', parent=self.painelCadastro, pos=wx.Point(8, 8),
              size=wx.Size(175, 70), style=0)

        self.linhaCadastroAlunos = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/LinhaCAdastroAlunos.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMECADASTROLINHACADASTROALUNOS,
              name=u'linhaCadastroAlunos', parent=self.painelCadastro,
              pos=wx.Point(0, 80), size=wx.Size(1024, 21), style=0)

        self.dadosDosAlunos = wx.Notebook(id=wxID_FRAMECADASTRODADOSDOSALUNOS,
              name=u'dadosDosAlunos', parent=self.painelCadastro,
              pos=wx.Point(20, 120), size=wx.Size(984, 424), style=0)
        self.dadosDosAlunos.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.dadosDosAlunos.SetForegroundColour(wx.Colour(255, 255, 255))
        self.dadosDosAlunos.SetThemeEnabled(True)

        self.abaPessoal = wx.Window(id=wxID_FRAMECADASTROABAPESSOAL,
              name=u'abaPessoal', parent=self.dadosDosAlunos, pos=wx.Point(0,
              0), size=wx.Size(976, 398), style=wx.TAB_TRAVERSAL)

        self.campoCPF = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRAMECADASTROCAMPOCPF,
              name=u'campoCPF', parent=self.abaPessoal, pos=wx.Point(24, 34),
              size=wx.Size(104, 21), style=0, value=u'')
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

        self.nomeCPF = wx.StaticText(id=wxID_FRAMECADASTRONOMECPF,
              label=u'CPF:', name=u'nomeCPF', parent=self.abaPessoal,
              pos=wx.Point(11, 15), size=wx.Size(24, 13), style=0)

        self.CPFInvalido = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/botao_invalido.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMECADASTROCPFINVALIDO,
              name=u'CPFInvalido', parent=self.abaPessoal, pos=wx.Point(170,
              36), size=wx.Size(14, 14), style=0)
        self.CPFInvalido.Show(False)

        self.cpfValido = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/botao_valido.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMECADASTROCPFVALIDO,
              name=u'cpfValido', parent=self.abaPessoal, pos=wx.Point(170, 36),
              size=wx.Size(14, 14), style=0)
        self.cpfValido.Show(False)

        self.validarCPF = wx.BitmapButton(bitmap=wx.Bitmap(u'./Graficos/botao_buscar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMECADASTROVALIDARCPF,
              name=u'validarCPF', parent=self.abaPessoal, pos=wx.Point(134, 30),
              size=wx.Size(26, 26), style=wx.BU_AUTODRAW)
        self.validarCPF.Bind(wx.EVT_BUTTON, self.OnValidarCPFButton,
              id=wxID_FRAMECADASTROVALIDARCPF)

        self.dataNascimento = wx.StaticText(id=wxID_FRAMECADASTRODATANASCIMENTO,
              label=u'Data de nascimento:', name=u'dataNascimento',
              parent=self.abaPessoal, pos=wx.Point(202, 14), size=wx.Size(100,
              13), style=0)

        self.campoAniversario = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRAMECADASTROCAMPOANIVERSARIO,
              name=u'campoAniversario', parent=self.abaPessoal,
              pos=wx.Point(215, 33), size=wx.Size(104, 21), style=0, value=u'')
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
              id=wxID_FRAMECADASTROSELECIONASEXO, label=u'Sexo:',
              majorDimension=1, name=u'selecionaSexo', parent=self.abaPessoal,
              pos=wx.Point(342, 14), size=wx.Size(176, 43),
              style=wx.RA_SPECIFY_ROWS)

        self.nomeNomeAluno = wx.StaticText(id=wxID_FRAMECADASTRONOMENOMEALUNO,
              label=u'Nome Completo:', name=u'nomeNomeAluno',
              parent=self.abaPessoal, pos=wx.Point(11, 70), size=wx.Size(80,
              13), style=0)

        self.campoNomeAluno = wx.TextCtrl(id=wxID_FRAMECADASTROCAMPONOMEALUNO,
              name=u'campoNomeAluno', parent=self.abaPessoal, pos=wx.Point(24,
              89), size=wx.Size(496, 21), style=0, value=u'')
        self.campoNomeAluno.SetMaxLength(50)

        self.nomeNomeMae = wx.StaticText(id=wxID_FRAMECADASTRONOMENOMEMAE,
              label=u'Nome da M\xe3e:', name=u'nomeNomeMae',
              parent=self.abaPessoal, pos=wx.Point(11, 125), size=wx.Size(70,
              14), style=0)

        self.campoNomeMae = wx.TextCtrl(id=wxID_FRAMECADASTROCAMPONOMEMAE,
              name=u'campoNomeMae', parent=self.abaPessoal, pos=wx.Point(24,
              145), size=wx.Size(496, 21), style=0, value=u'')
        self.campoNomeMae.SetMaxLength(50)

        self.nomeNomePai = wx.StaticText(id=wxID_FRAMECADASTRONOMENOMEPAI,
              label=u'Nome do Pai:', name=u'nomeNomePai',
              parent=self.abaPessoal, pos=wx.Point(11, 181), size=wx.Size(64,
              13), style=0)

        self.campoNomePai = wx.TextCtrl(id=wxID_FRAMECADASTROCAMPONOMEPAI,
              name=u'campoNomePai', parent=self.abaPessoal, pos=wx.Point(24,
              202), size=wx.Size(496, 21), style=0, value=u'')
        self.campoNomePai.SetMaxLength(50)

        self.nomeCEP = wx.StaticText(id=wxID_FRAMECADASTRONOMECEP,
              label=u'CEP:', name=u'nomeCEP', parent=self.abaPessoal,
              pos=wx.Point(11, 237), size=wx.Size(24, 13), style=0)

        self.campoCEP = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRAMECADASTROCAMPOCEP,
              name=u'campoCEP', parent=self.abaPessoal, pos=wx.Point(24, 256),
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
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMECADASTROBOTAOBUSCARCEP,
              name=u'botaoBuscarCEP', parent=self.abaPessoal, pos=wx.Point(136,
              253), size=wx.Size(26, 26), style=wx.BU_AUTODRAW)
        self.botaoBuscarCEP.Bind(wx.EVT_BUTTON, self.OnBotaoBuscarCEPButton,
              id=wxID_FRAMECADASTROBOTAOBUSCARCEP)

        self.nomeNumero = wx.StaticText(id=wxID_FRAMECADASTRONOMENUMERO,
              label=u'N\xfamero:', name=u'nomeNumero', parent=self.abaPessoal,
              pos=wx.Point(160, 237), size=wx.Size(42, 13), style=0)

        self.campoNumero = wx.TextCtrl(id=wxID_FRAMECADASTROCAMPONUMERO,
              name=u'campoNumero', parent=self.abaPessoal, pos=wx.Point(173,
              256), size=wx.Size(100, 21), style=0, value=u'')

        self.nomeComplemento = wx.StaticText(id=wxID_FRAMECADASTRONOMECOMPLEMENTO,
              label=u'Complemento:', name=u'nomeComplemento',
              parent=self.abaPessoal, pos=wx.Point(293, 237), size=wx.Size(70,
              13), style=0)

        self.abaProfissional = wx.Window(id=wxID_FRAMECADASTROABAPROFISSIONAL,
              name=u'abaProfissional', parent=self.dadosDosAlunos,
              pos=wx.Point(0, 0), size=wx.Size(976, 398),
              style=wx.TAB_TRAVERSAL)

        self.nomeMatricula = wx.StaticText(id=wxID_FRAMECADASTRONOMEMATRICULA,
              label=u'Matr\xedcula:', name=u'nomeMatricula',
              parent=self.abaProfissional, pos=wx.Point(16, 15),
              size=wx.Size(48, 13), style=0)

        self.campoMatricula = wx.TextCtrl(id=wxID_FRAMECADASTROCAMPOMATRICULA,
              name=u'campoMatricula', parent=self.abaProfissional,
              pos=wx.Point(29, 34), size=wx.Size(144, 21), style=0, value=u'')

        self.abaContato = wx.Window(id=wxID_FRAMECADASTROABACONTATO,
              name=u'abaContato', parent=self.dadosDosAlunos, pos=wx.Point(0,
              0), size=wx.Size(976, 398), style=wx.TAB_TRAVERSAL)

        self.campoEmail = wx.TextCtrl(id=wxID_FRAMECADASTROCAMPOEMAIL,
              name=u'campoEmail', parent=self.abaContato, pos=wx.Point(24, 35),
              size=wx.Size(312, 21), style=0, value=u'')

        self.nomeEmail = wx.StaticText(id=wxID_FRAMECADASTRONOMEEMAIL,
              label=u'E-Mail:', name=u'nomeEmail', parent=self.abaContato,
              pos=wx.Point(11, 16), size=wx.Size(33, 13), style=0)

        self.nomeTelefone = wx.StaticText(id=wxID_FRAMECADASTRONOMETELEFONE,
              label=u'Telefone:', name=u'nomeTelefone', parent=self.abaContato,
              pos=wx.Point(11, 68), size=wx.Size(47, 13), style=0)

        self.campoTelefone = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRAMECADASTROCAMPOTELEFONE,
              name=u'campoTelefone', parent=self.abaContato, pos=wx.Point(24,
              87), size=wx.Size(136, 21), style=0, value=u'(  )    -    ')
        self.campoTelefone.SetAutoformat('')
        self.campoTelefone.SetMask(u'(XX)XXXX-XXXX')
        self.campoTelefone.SetFormatcodes('')
        self.campoTelefone.SetDescription('')
        self.campoTelefone.SetExcludeChars('')
        self.campoTelefone.SetValidRegex('')
        self.campoTelefone.SetMaxLength(13)
        self.campoTelefone.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))

        self.nomeCelular = wx.StaticText(id=wxID_FRAMECADASTRONOMECELULAR,
              label=u'Celular:', name=u'nomeCelular', parent=self.abaContato,
              pos=wx.Point(11, 125), size=wx.Size(38, 13), style=0)

        self.campoCelular = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRAMECADASTROCAMPOCELULAR,
              name=u'campoCelular', parent=self.abaContato, pos=wx.Point(24,
              144), size=wx.Size(136, 21), style=0, value=u'')
        self.campoCelular.SetAutoformat('')
        self.campoCelular.SetMask(u'(XX)XXXX-XXXX')
        self.campoCelular.SetFormatcodes('')
        self.campoCelular.SetDescription('')
        self.campoCelular.SetExcludeChars('')
        self.campoCelular.SetValidRegex('')
        self.campoCelular.SetMaxLength(13)
        self.campoCelular.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))

        self.botaoSalvar = wx.Button(id=wxID_FRAMECADASTROBOTAOSALVAR,
              label=u'Salvar', name=u'botaoSalvar', parent=self.abaContato,
              pos=wx.Point(885, 360), size=wx.Size(75, 23), style=0)

        self.campoComplemento = wx.TextCtrl(id=wxID_FRAMECADASTROCAMPOCOMPLEMENTO,
              name=u'campoComplemento', parent=self.abaPessoal,
              pos=wx.Point(306, 256), size=wx.Size(214, 21), style=0,
              value=u'')

        self.nomeDepartamento = wx.StaticText(id=wxID_FRAMECADASTRONOMEDEPARTAMENTO,
              label=u'Departamento:', name=u'nomeDepartamento',
              parent=self.abaProfissional, pos=wx.Point(200, 15),
              size=wx.Size(74, 13), style=0)

        self.botaoLimparContato = wx.Button(id=wxID_FRAMECADASTROBOTAOLIMPARCONTATO,
              label=u'Limpar', name=u'botaoLimparContato',
              parent=self.abaContato, pos=wx.Point(880, 20), size=wx.Size(75,
              23), style=0)

        self.nomeEndereco = wx.StaticText(id=wxID_FRAMECADASTRONOMEENDERECO,
              label=u'Endere\xe7o:', name=u'nomeEndereco',
              parent=self.abaPessoal, pos=wx.Point(11, 292), size=wx.Size(50,
              13), style=0)

        self.campoEndereco = wx.TextCtrl(id=wxID_FRAMECADASTROCAMPOENDERECO,
              name=u'campoEndereco', parent=self.abaPessoal, pos=wx.Point(24,
              313), size=wx.Size(496, 21), style=0, value=u'')

        self.nomeBairro = wx.StaticText(id=wxID_FRAMECADASTRONOMEBAIRRO,
              label=u'Bairro:', name=u'nomeBairro', parent=self.abaPessoal,
              pos=wx.Point(11, 346), size=wx.Size(33, 13), style=0)

        self.nomeCidade = wx.StaticText(id=wxID_FRAMECADASTRONOMECIDADE,
              label=u'Cidade:', name=u'nomeCidade', parent=self.abaPessoal,
              pos=wx.Point(265, 346), size=wx.Size(38, 13), style=0)

        self.campoBairro = wx.TextCtrl(id=wxID_FRAMECADASTROCAMPOBAIRRO,
              name=u'campoBairro', parent=self.abaPessoal, pos=wx.Point(24,
              365), size=wx.Size(224, 21), style=0, value=u'')

        self.campoCidade = wx.TextCtrl(id=wxID_FRAMECADASTROCAMPOCIDADE,
              name=u'campoCidade', parent=self.abaPessoal, pos=wx.Point(278,
              365), size=wx.Size(186, 21), style=0, value=u'')

        self.comboBoxDepartamento = wx.ComboBox(choices=[],
              id=wxID_FRAMECADASTROCOMBOBOXDEPARTAMENTO,
              name=u'comboBoxDepartamento', parent=self.abaProfissional,
              pos=wx.Point(217, 34), size=wx.Size(130, 21),
              style=wx.CB_READONLY, value=u'Selecione o Departamento')
        self.comboBoxDepartamento.SetLabel(u'')
        self.comboBoxDepartamento.SetStringSelection(u'Selecione o departamento')

        self.nomeCurso = wx.StaticText(id=wxID_FRAMECADASTRONOMECURSO,
              label=u'Curso:', name=u'nomeCurso', parent=self.abaProfissional,
              pos=wx.Point(373, 15), size=wx.Size(33, 13), style=0)

        self.comboBoxCursos = wx.ComboBox(choices=[],
              id=wxID_FRAMECADASTROCOMBOBOXCURSOS, name=u'comboBoxCursos',
              parent=self.abaProfissional, pos=wx.Point(390, 34),
              size=wx.Size(130, 21), style=wx.CB_READONLY, value=u'')
        self.comboBoxCursos.SetLabel(u'Selecione o Curso')

        self.nomeAnoConclusao = wx.StaticText(id=wxID_FRAMECADASTRONOMEANOCONCLUSAO,
              label=u'Ano que concluiu (ou concluir\xe1) o curso:',
              name=u'nomeAnoConclusao', parent=self.abaProfissional,
              pos=wx.Point(16, 75), size=wx.Size(192, 13), style=0)

        self.campoAnoConclusao = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRAMECADASTROCAMPOANOCONCLUSAO,
              name=u'campoAnoConclusao', parent=self.abaProfissional,
              pos=wx.Point(40, 96), size=wx.Size(56, 21), style=0,
              value=u'    . ')
        self.campoAnoConclusao.SetAutoformat('')
        self.campoAnoConclusao.SetMask(u'XXXX.X')
        self.campoAnoConclusao.SetDatestyle('MDY')
        self.campoAnoConclusao.SetFormatcodes('')
        self.campoAnoConclusao.SetDescription('')
        self.campoAnoConclusao.SetExcludeChars('')
        self.campoAnoConclusao.SetValidRegex('')
        self.campoAnoConclusao.SetMaxLength(6)
        self.campoAnoConclusao.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, u'Tahoma'))

        self.botaoLimparProfissional = wx.Button(id=wxID_FRAMECADASTROBOTAOLIMPARPROFISSIONAL,
              label=u'Limpar', name=u'botaoLimparProfissional',
              parent=self.abaProfissional, pos=wx.Point(880, 20),
              size=wx.Size(75, 23), style=0)
        self.botaoLimparProfissional.Bind(wx.EVT_BUTTON,
              self.OnBotaoLimparProfissionalButton,
              id=wxID_FRAMECADASTROBOTAOLIMPARPROFISSIONAL)

        self.botaoVoltar = wx.BitmapButton(bitmap=wx.Bitmap(u'./Graficos/botao_voltar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMECADASTROBOTAOVOLTAR,
              name=u'botaoVoltar', parent=self.painelCadastro, pos=wx.Point(952,
              13), size=wx.Size(57, 57), style=wx.BU_AUTODRAW)
        self.botaoVoltar.Bind(wx.EVT_BUTTON, self.OnBotaoVoltarButton,
              id=wxID_FRAMECADASTROBOTAOVOLTAR)

        self.nomeUF = wx.StaticText(id=wxID_FRAMECADASTRONOMEUF, label=u'UF:',
              name=u'nomeUF', parent=self.abaPessoal, pos=wx.Point(480, 346),
              size=wx.Size(18, 13), style=0)

        self.campoUF = wx.TextCtrl(id=wxID_FRAMECADASTROCAMPOUF,
              name=u'campoUF', parent=self.abaPessoal, pos=wx.Point(493, 365),
              size=wx.Size(27, 21), style=0, value=u'')

        self.botaoLimparPessoal = wx.Button(id=wxID_FRAMECADASTROBOTAOLIMPARPESSOAL,
              label=u'Limpar', name=u'botaoLimparPessoal',
              parent=self.abaPessoal, pos=wx.Point(880, 20), size=wx.Size(75,
              23), style=0)
        self.botaoLimparPessoal.Bind(wx.EVT_BUTTON,
              self.OnBotaoLimparPessoalButton,
              id=wxID_FRAMECADASTROBOTAOLIMPARPESSOAL)

        self.nomeErro = wx.StaticText(id=wxID_FRAMECADASTRONOMEERRO, label=u'',
              name=u'nomeErro', parent=self.abaPessoal, pos=wx.Point(541, 36),
              size=wx.Size(0, 13), style=wx.ALIGN_CENTRE)
        self.nomeErro.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, True,
              u'Tahoma'))
        self.nomeErro.SetAutoLayout(True)

        self.verificarEstagio = wx.RadioBox(choices=['Sim', 'N\xe3o'],
              id=wxID_FRAMECADASTROVERIFICARESTAGIO, label=u'Estagiando:',
              majorDimension=1, name=u'verificarEstagio',
              parent=self.abaProfissional, pos=wx.Point(234, 75),
              size=wx.Size(94, 44), style=wx.RA_SPECIFY_ROWS)
        self.verificarEstagio.SetStringSelection(u'N\xe3o')
        self.verificarEstagio.Bind(wx.EVT_RADIOBOX,
              self.OnVerificarEstagioRadiobox,
              id=wxID_FRAMECADASTROVERIFICARESTAGIO)

        self.nomeDisponibilidade = wx.StaticText(id=wxID_FRAMECADASTRONOMEDISPONIBILIDADE,
              label=u'Disponibilidade:', name=u'nomeDisponibilidade',
              parent=self.abaProfissional, pos=wx.Point(351, 76),
              size=wx.Size(75, 13), style=0)

        self.opcaoManha = wx.CheckBox(id=wxID_FRAMECADASTROOPCAOMANHA,
              label=u'Manh\xe3', name=u'opcaoManha',
              parent=self.abaProfissional, pos=wx.Point(372, 98),
              size=wx.Size(53, 13), style=0)
        self.opcaoManha.SetValue(False)

        self.opcaoTarde = wx.CheckBox(id=wxID_FRAMECADASTROOPCAOTARDE,
              label=u'Tarde', name=u'opcaoTarde', parent=self.abaProfissional,
              pos=wx.Point(428, 98), size=wx.Size(49, 13), style=0)
        self.opcaoTarde.SetValue(False)
        self.opcaoTarde.SetToolTipString(u'opcaoTarde')

        self.opcaoNoite = wx.CheckBox(id=wxID_FRAMECADASTROOPCAONOITE,
              label=u'Noite', name=u'opcaoNoite', parent=self.abaProfissional,
              pos=wx.Point(479, 98), size=wx.Size(40, 13), style=0)
        self.opcaoNoite.SetValue(False)

        self._init_coll_dadosDosAlunos_Pages(self.dadosDosAlunos)

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
        self.CPFInvalido.Show(False)
        self.cpfValido.Show(False)
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


    def OnBotaoLimparProfissionalButton(self, event):
        self.campoMatricula.SetValue('')
        
        self.campoAnoConclusao.SetValue('')
        event.Skip()

    def OnBotaoVoltarButton(self, event):
        event.Skip()

    def OnVerificarEstagioRadiobox(self, event):
        event.Skip()

