#Boa:Frame:frameEdicaoAluno
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
    return frameEdicaoAluno(parent)

[wxID_FRAMEEDICAOALUNO, wxID_FRAMEEDICAOALUNOABACONTATO, 
 wxID_FRAMEEDICAOALUNOABAPESSOAL, wxID_FRAMEEDICAOALUNOABAPROFISSIONAL, 
 wxID_FRAMEEDICAOALUNOBOTAOBUSCARCEP, wxID_FRAMEEDICAOALUNOBOTAOLIMPARCONTATO, 
 wxID_FRAMEEDICAOALUNOBOTAOLIMPARPESSOAL, 
 wxID_FRAMEEDICAOALUNOBOTAOLIMPARPROFISSIONAL, 
 wxID_FRAMEEDICAOALUNOBOTAOSALVAR, wxID_FRAMEEDICAOALUNOBOTAOVOLTAR, 
 wxID_FRAMEEDICAOALUNOBUSCARCPF, wxID_FRAMEEDICAOALUNOCAMPOANIVERSARIO, 
 wxID_FRAMEEDICAOALUNOCAMPOANOCONCLUSAO, wxID_FRAMEEDICAOALUNOCAMPOBAIRRO, 
 wxID_FRAMEEDICAOALUNOCAMPOCELULAR, wxID_FRAMEEDICAOALUNOCAMPOCEP, 
 wxID_FRAMEEDICAOALUNOCAMPOCIDADE, wxID_FRAMEEDICAOALUNOCAMPOCOMPLEMENTO, 
 wxID_FRAMEEDICAOALUNOCAMPOCONFIRMARSENHA, wxID_FRAMEEDICAOALUNOCAMPOCPF, 
 wxID_FRAMEEDICAOALUNOCAMPOEMAIL, wxID_FRAMEEDICAOALUNOCAMPOENDERECO, 
 wxID_FRAMEEDICAOALUNOCAMPOMATRICULA, wxID_FRAMEEDICAOALUNOCAMPONOMEALUNO, 
 wxID_FRAMEEDICAOALUNOCAMPONOMEMAE, wxID_FRAMEEDICAOALUNOCAMPONOMEPAI, 
 wxID_FRAMEEDICAOALUNOCAMPONUMERO, wxID_FRAMEEDICAOALUNOCAMPOSENHA, 
 wxID_FRAMEEDICAOALUNOCAMPOTELEFONE, wxID_FRAMEEDICAOALUNOCAMPOUF, 
 wxID_FRAMEEDICAOALUNOCOMBOBOXCURSOS, 
 wxID_FRAMEEDICAOALUNOCOMBOBOXDEPARTAMENTO, 
 wxID_FRAMEEDICAOALUNOCPFENCONTRADO, wxID_FRAMEEDICAOALUNOCPFNAOENCONTRADO, 
 wxID_FRAMEEDICAOALUNODADOSDOSALUNOS, wxID_FRAMEEDICAOALUNODATANASCIMENTO, 
 wxID_FRAMEEDICAOALUNOLINHAEDICAOALUNOS, wxID_FRAMEEDICAOALUNOLOGOIFPE, 
 wxID_FRAMEEDICAOALUNONOMEANOCONCLUSAO, wxID_FRAMEEDICAOALUNONOMEBAIRRO, 
 wxID_FRAMEEDICAOALUNONOMECELULAR, wxID_FRAMEEDICAOALUNONOMECEP, 
 wxID_FRAMEEDICAOALUNONOMECIDADE, wxID_FRAMEEDICAOALUNONOMECOMPLEMENTO, 
 wxID_FRAMEEDICAOALUNONOMECONFIRMARSENHA, wxID_FRAMEEDICAOALUNONOMECPF, 
 wxID_FRAMEEDICAOALUNONOMECURSO, wxID_FRAMEEDICAOALUNONOMEDEPARTAMENTO, 
 wxID_FRAMEEDICAOALUNONOMEDISPONIBILIDADE, wxID_FRAMEEDICAOALUNONOMEEMAIL, 
 wxID_FRAMEEDICAOALUNONOMEENDERECO, wxID_FRAMEEDICAOALUNONOMEERRO, 
 wxID_FRAMEEDICAOALUNONOMEMATRICULA, wxID_FRAMEEDICAOALUNONOMENOMEALUNO, 
 wxID_FRAMEEDICAOALUNONOMENOMEMAE, wxID_FRAMEEDICAOALUNONOMENOMEPAI, 
 wxID_FRAMEEDICAOALUNONOMENUMERO, wxID_FRAMEEDICAOALUNONOMESENHA, 
 wxID_FRAMEEDICAOALUNONOMETELEFONE, wxID_FRAMEEDICAOALUNONOMEUF, 
 wxID_FRAMEEDICAOALUNOOPCAOMANHA, wxID_FRAMEEDICAOALUNOOPCAONOITE, 
 wxID_FRAMEEDICAOALUNOOPCAOTARDE, wxID_FRAMEEDICAOALUNOPAINELEDICAO, 
 wxID_FRAMEEDICAOALUNOSELECIONASEXO, wxID_FRAMEEDICAOALUNOVERIFICARESTAGIO, 
] = [wx.NewId() for _init_ctrls in range(66)]

class frameEdicaoAluno(wx.Frame):
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
        wx.Frame.__init__(self, id=wxID_FRAMEEDICAOALUNO,
              name=u'frameEdicaoAluno', parent=prnt, pos=wx.Point(700, 273),
              size=wx.Size(1040, 614), style=wx.DEFAULT_FRAME_STYLE,
              title=u'Est\xe1gio Curricular - Edi\xe7\xe3o Cadastral de Alunos')
        self.SetClientSize(wx.Size(1024, 576))
        self.Center(wx.BOTH)
        self.SetIcon(wx.Icon(u'./Graficos/icone.ico',wx.BITMAP_TYPE_ICO))
        self.SetMaxSize(wx.Size(1040, 614))
        self.SetMinSize(wx.Size(1040, 614))

        self.painelEdicao = wx.Panel(id=wxID_FRAMEEDICAOALUNOPAINELEDICAO,
              name=u'painelEdicao', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(1024, 576), style=wx.TAB_TRAVERSAL)
        self.painelEdicao.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.logoIFPE = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/logo.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEEDICAOALUNOLOGOIFPE,
              name=u'logoIFPE', parent=self.painelEdicao, pos=wx.Point(8, 8),
              size=wx.Size(175, 70), style=0)

        self.linhaEdicaoAlunos = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/LinhaEdicaoAlunos.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEEDICAOALUNOLINHAEDICAOALUNOS,
              name=u'linhaEdicaoAlunos', parent=self.painelEdicao,
              pos=wx.Point(0, 80), size=wx.Size(1024, 25), style=0)

        self.dadosDosAlunos = wx.Notebook(id=wxID_FRAMEEDICAOALUNODADOSDOSALUNOS,
              name=u'dadosDosAlunos', parent=self.painelEdicao, pos=wx.Point(20,
              120), size=wx.Size(984, 424), style=0)
        self.dadosDosAlunos.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.dadosDosAlunos.SetForegroundColour(wx.Colour(255, 255, 255))
        self.dadosDosAlunos.SetThemeEnabled(True)

        self.abaPessoal = wx.Window(id=wxID_FRAMEEDICAOALUNOABAPESSOAL,
              name=u'abaPessoal', parent=self.dadosDosAlunos, pos=wx.Point(0,
              0), size=wx.Size(976, 398), style=wx.TAB_TRAVERSAL)

        self.campoCPF = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRAMEEDICAOALUNOCAMPOCPF,
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

        self.nomeCPF = wx.StaticText(id=wxID_FRAMEEDICAOALUNONOMECPF,
              label=u'CPF:', name=u'nomeCPF', parent=self.abaPessoal,
              pos=wx.Point(11, 15), size=wx.Size(24, 13), style=0)

        self.cpfNaoEncontrado = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/botao_invalido.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEEDICAOALUNOCPFNAOENCONTRADO,
              name=u'cpfNaoEncontrado', parent=self.abaPessoal,
              pos=wx.Point(170, 36), size=wx.Size(14, 14), style=0)
        self.cpfNaoEncontrado.Show(False)

        self.cpfEncontrado = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/botao_valido.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEEDICAOALUNOCPFENCONTRADO,
              name=u'cpfEncontrado', parent=self.abaPessoal, pos=wx.Point(170,
              36), size=wx.Size(14, 14), style=0)
        self.cpfEncontrado.Show(False)

        self.BuscarCPF = wx.BitmapButton(bitmap=wx.Bitmap(u'./Graficos/botao_carregar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEEDICAOALUNOBUSCARCPF,
              name=u'BuscarCPF', parent=self.abaPessoal, pos=wx.Point(134, 30),
              size=wx.Size(26, 26), style=wx.BU_AUTODRAW)
        self.BuscarCPF.Bind(wx.EVT_BUTTON, self.OnBuscarCPFButton,
              id=wxID_FRAMEEDICAOALUNOBUSCARCPF)

        self.dataNascimento = wx.StaticText(id=wxID_FRAMEEDICAOALUNODATANASCIMENTO,
              label=u'Data de nascimento:', name=u'dataNascimento',
              parent=self.abaPessoal, pos=wx.Point(196, 14), size=wx.Size(100,
              13), style=0)

        self.campoAniversario = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRAMEEDICAOALUNOCAMPOANIVERSARIO,
              name=u'campoAniversario', parent=self.abaPessoal,
              pos=wx.Point(209, 33), size=wx.Size(104, 21), style=0, value=u'')
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
              id=wxID_FRAMEEDICAOALUNOSELECIONASEXO, label=u'Sexo:',
              majorDimension=1, name=u'selecionaSexo', parent=self.abaPessoal,
              pos=wx.Point(338, 14), size=wx.Size(176, 41),
              style=wx.RA_SPECIFY_ROWS)

        self.nomeNomeAluno = wx.StaticText(id=wxID_FRAMEEDICAOALUNONOMENOMEALUNO,
              label=u'Nome Completo:', name=u'nomeNomeAluno',
              parent=self.abaPessoal, pos=wx.Point(11, 70), size=wx.Size(80,
              13), style=0)

        self.campoNomeAluno = wx.TextCtrl(id=wxID_FRAMEEDICAOALUNOCAMPONOMEALUNO,
              name=u'campoNomeAluno', parent=self.abaPessoal, pos=wx.Point(24,
              89), size=wx.Size(496, 21), style=0, value=u'')
        self.campoNomeAluno.SetMaxLength(50)

        self.nomeNomeMae = wx.StaticText(id=wxID_FRAMEEDICAOALUNONOMENOMEMAE,
              label=u'Nome da M\xe3e:', name=u'nomeNomeMae',
              parent=self.abaPessoal, pos=wx.Point(11, 125), size=wx.Size(70,
              14), style=0)

        self.campoNomeMae = wx.TextCtrl(id=wxID_FRAMEEDICAOALUNOCAMPONOMEMAE,
              name=u'campoNomeMae', parent=self.abaPessoal, pos=wx.Point(24,
              145), size=wx.Size(496, 21), style=0, value=u'')
        self.campoNomeMae.SetMaxLength(50)

        self.nomeNomePai = wx.StaticText(id=wxID_FRAMEEDICAOALUNONOMENOMEPAI,
              label=u'Nome do Pai:', name=u'nomeNomePai',
              parent=self.abaPessoal, pos=wx.Point(11, 181), size=wx.Size(64,
              13), style=0)

        self.campoNomePai = wx.TextCtrl(id=wxID_FRAMEEDICAOALUNOCAMPONOMEPAI,
              name=u'campoNomePai', parent=self.abaPessoal, pos=wx.Point(24,
              202), size=wx.Size(496, 21), style=0, value=u'')
        self.campoNomePai.SetMaxLength(50)

        self.nomeCEP = wx.StaticText(id=wxID_FRAMEEDICAOALUNONOMECEP,
              label=u'CEP:', name=u'nomeCEP', parent=self.abaPessoal,
              pos=wx.Point(11, 237), size=wx.Size(24, 13), style=0)

        self.campoCEP = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRAMEEDICAOALUNOCAMPOCEP,
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
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEEDICAOALUNOBOTAOBUSCARCEP,
              name=u'botaoBuscarCEP', parent=self.abaPessoal, pos=wx.Point(136,
              253), size=wx.Size(26, 26), style=wx.BU_AUTODRAW)
        self.botaoBuscarCEP.Bind(wx.EVT_BUTTON, self.OnBotaoBuscarCEPButton,
              id=wxID_FRAMEEDICAOALUNOBOTAOBUSCARCEP)

        self.nomeNumero = wx.StaticText(id=wxID_FRAMEEDICAOALUNONOMENUMERO,
              label=u'N\xfamero:', name=u'nomeNumero', parent=self.abaPessoal,
              pos=wx.Point(160, 237), size=wx.Size(42, 13), style=0)

        self.campoNumero = wx.TextCtrl(id=wxID_FRAMEEDICAOALUNOCAMPONUMERO,
              name=u'campoNumero', parent=self.abaPessoal, pos=wx.Point(173,
              256), size=wx.Size(100, 21), style=0, value=u'')

        self.nomeComplemento = wx.StaticText(id=wxID_FRAMEEDICAOALUNONOMECOMPLEMENTO,
              label=u'Complemento:', name=u'nomeComplemento',
              parent=self.abaPessoal, pos=wx.Point(293, 237), size=wx.Size(70,
              13), style=0)

        self.campoComplemento = wx.TextCtrl(id=wxID_FRAMEEDICAOALUNOCAMPOCOMPLEMENTO,
              name=u'campoComplemento', parent=self.abaPessoal,
              pos=wx.Point(306, 256), size=wx.Size(214, 21), style=0,
              value=u'')

        self.nomeEndereco = wx.StaticText(id=wxID_FRAMEEDICAOALUNONOMEENDERECO,
              label=u'Endere\xe7o:', name=u'nomeEndereco',
              parent=self.abaPessoal, pos=wx.Point(11, 292), size=wx.Size(50,
              13), style=0)

        self.campoEndereco = wx.TextCtrl(id=wxID_FRAMEEDICAOALUNOCAMPOENDERECO,
              name=u'campoEndereco', parent=self.abaPessoal, pos=wx.Point(24,
              313), size=wx.Size(496, 21), style=0, value=u'')

        self.abaProfissional = wx.Window(id=wxID_FRAMEEDICAOALUNOABAPROFISSIONAL,
              name=u'abaProfissional', parent=self.dadosDosAlunos,
              pos=wx.Point(0, 0), size=wx.Size(976, 398),
              style=wx.TAB_TRAVERSAL)

        self.nomeMatricula = wx.StaticText(id=wxID_FRAMEEDICAOALUNONOMEMATRICULA,
              label=u'Matr\xedcula:', name=u'nomeMatricula',
              parent=self.abaProfissional, pos=wx.Point(16, 15),
              size=wx.Size(48, 13), style=0)

        self.campoMatricula = wx.TextCtrl(id=wxID_FRAMEEDICAOALUNOCAMPOMATRICULA,
              name=u'campoMatricula', parent=self.abaProfissional,
              pos=wx.Point(29, 34), size=wx.Size(144, 21), style=0, value=u'')

        self.abaContato = wx.Window(id=wxID_FRAMEEDICAOALUNOABACONTATO,
              name=u'abaContato', parent=self.dadosDosAlunos, pos=wx.Point(0,
              0), size=wx.Size(976, 398), style=wx.TAB_TRAVERSAL)

        self.campoEmail = wx.TextCtrl(id=wxID_FRAMEEDICAOALUNOCAMPOEMAIL,
              name=u'campoEmail', parent=self.abaContato, pos=wx.Point(24, 35),
              size=wx.Size(312, 21), style=0, value=u'')
        self.campoEmail.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))

        self.nomeEmail = wx.StaticText(id=wxID_FRAMEEDICAOALUNONOMEEMAIL,
              label=u'E-Mail:', name=u'nomeEmail', parent=self.abaContato,
              pos=wx.Point(11, 16), size=wx.Size(33, 13), style=0)

        self.nomeTelefone = wx.StaticText(id=wxID_FRAMEEDICAOALUNONOMETELEFONE,
              label=u'Telefone:', name=u'nomeTelefone', parent=self.abaContato,
              pos=wx.Point(11, 68), size=wx.Size(47, 13), style=0)

        self.campoTelefone = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRAMEEDICAOALUNOCAMPOTELEFONE,
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

        self.campoCelular = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRAMEEDICAOALUNOCAMPOCELULAR,
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

        self.nomeBairro = wx.StaticText(id=wxID_FRAMEEDICAOALUNONOMEBAIRRO,
              label=u'Bairro:', name=u'nomeBairro', parent=self.abaPessoal,
              pos=wx.Point(11, 346), size=wx.Size(33, 13), style=0)

        self.nomeDepartamento = wx.StaticText(id=wxID_FRAMEEDICAOALUNONOMEDEPARTAMENTO,
              label=u'Departamento:', name=u'nomeDepartamento',
              parent=self.abaProfissional, pos=wx.Point(200, 15),
              size=wx.Size(74, 13), style=0)

        self.nomeCelular = wx.StaticText(id=wxID_FRAMEEDICAOALUNONOMECELULAR,
              label=u'Celular:', name=u'nomeCelular', parent=self.abaContato,
              pos=wx.Point(11, 125), size=wx.Size(38, 13), style=0)

        self.nomeCidade = wx.StaticText(id=wxID_FRAMEEDICAOALUNONOMECIDADE,
              label=u'Cidade:', name=u'nomeCidade', parent=self.abaPessoal,
              pos=wx.Point(265, 346), size=wx.Size(38, 13), style=0)

        self.campoBairro = wx.TextCtrl(id=wxID_FRAMEEDICAOALUNOCAMPOBAIRRO,
              name=u'campoBairro', parent=self.abaPessoal, pos=wx.Point(24,
              365), size=wx.Size(224, 21), style=0, value=u'')

        self.campoCidade = wx.TextCtrl(id=wxID_FRAMEEDICAOALUNOCAMPOCIDADE,
              name=u'campoCidade', parent=self.abaPessoal, pos=wx.Point(278,
              365), size=wx.Size(186, 21), style=0, value=u'')

        self.nomeUF = wx.StaticText(id=wxID_FRAMEEDICAOALUNONOMEUF,
              label=u'UF:', name=u'nomeUF', parent=self.abaPessoal,
              pos=wx.Point(480, 346), size=wx.Size(18, 13), style=0)

        self.campoUF = wx.TextCtrl(id=wxID_FRAMEEDICAOALUNOCAMPOUF,
              name=u'campoUF', parent=self.abaPessoal, pos=wx.Point(493, 365),
              size=wx.Size(27, 21), style=0, value=u'')

        self.botaoLimparPessoal = wx.Button(id=wxID_FRAMEEDICAOALUNOBOTAOLIMPARPESSOAL,
              label=u'Limpar', name=u'botaoLimparPessoal',
              parent=self.abaPessoal, pos=wx.Point(880, 20), size=wx.Size(75,
              23), style=0)
        self.botaoLimparPessoal.Bind(wx.EVT_BUTTON,
              self.OnBotaoLimparPessoalButton,
              id=wxID_FRAMEEDICAOALUNOBOTAOLIMPARPESSOAL)

        self.comboBoxDepartamento = wx.ComboBox(choices=[],
              id=wxID_FRAMEEDICAOALUNOCOMBOBOXDEPARTAMENTO,
              name=u'comboBoxDepartamento', parent=self.abaProfissional,
              pos=wx.Point(217, 34), size=wx.Size(130, 21),
              style=wx.CB_READONLY, value=u'Selecione o Departamento')
        self.comboBoxDepartamento.SetLabel(u'')
        self.comboBoxDepartamento.SetStringSelection(u'Selecione o departamento')

        self.nomeCurso = wx.StaticText(id=wxID_FRAMEEDICAOALUNONOMECURSO,
              label=u'Curso:', name=u'nomeCurso', parent=self.abaProfissional,
              pos=wx.Point(373, 15), size=wx.Size(33, 13), style=0)

        self.comboBoxCursos = wx.ComboBox(choices=[],
              id=wxID_FRAMEEDICAOALUNOCOMBOBOXCURSOS, name=u'comboBoxCursos',
              parent=self.abaProfissional, pos=wx.Point(390, 34),
              size=wx.Size(130, 21), style=wx.CB_READONLY, value=u'')
        self.comboBoxCursos.SetLabel(u'Selecione o Curso')

        self.nomeAnoConclusao = wx.StaticText(id=wxID_FRAMEEDICAOALUNONOMEANOCONCLUSAO,
              label=u'Ano que concluiu (ou concluir\xe1) o curso:',
              name=u'nomeAnoConclusao', parent=self.abaProfissional,
              pos=wx.Point(16, 75), size=wx.Size(192, 13), style=0)

        self.campoAnoConclusao = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRAMEEDICAOALUNOCAMPOANOCONCLUSAO,
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

        self.botaoLimparProfissional = wx.Button(id=wxID_FRAMEEDICAOALUNOBOTAOLIMPARPROFISSIONAL,
              label=u'Limpar', name=u'botaoLimparProfissional',
              parent=self.abaProfissional, pos=wx.Point(880, 20),
              size=wx.Size(75, 23), style=0)
        self.botaoLimparProfissional.Bind(wx.EVT_BUTTON,
              self.OnBotaoLimparProfissionalButton,
              id=wxID_FRAMEEDICAOALUNOBOTAOLIMPARPROFISSIONAL)

        self.botaoVoltar = wx.BitmapButton(bitmap=wx.Bitmap(u'./Graficos/botao_voltar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMEEDICAOALUNOBOTAOVOLTAR,
              name=u'botaoVoltar', parent=self.painelEdicao, pos=wx.Point(952,
              13), size=wx.Size(57, 57), style=wx.BU_AUTODRAW)
        self.botaoVoltar.Bind(wx.EVT_BUTTON, self.OnBotaoVoltarButton,
              id=wxID_FRAMEEDICAOALUNOBOTAOVOLTAR)

        self.botaoSalvar = wx.Button(id=wxID_FRAMEEDICAOALUNOBOTAOSALVAR,
              label=u'Salvar', name=u'botaoSalvar', parent=self.abaContato,
              pos=wx.Point(885, 360), size=wx.Size(75, 23), style=0)
        self.botaoSalvar.Bind(wx.EVT_BUTTON, self.OnBotaoSalvarButton,
              id=wxID_FRAMEEDICAOALUNOBOTAOSALVAR)

        self.campoSenha = wx.TextCtrl(id=wxID_FRAMEEDICAOALUNOCAMPOSENHA,
              name=u'campoSenha', parent=self.abaContato, pos=wx.Point(24, 197),
              size=wx.Size(312, 21), style=wx.TE_PASSWORD, value=u'')

        self.nomeErro = wx.StaticText(id=wxID_FRAMEEDICAOALUNONOMEERRO,
              label=u'', name=u'nomeErro', parent=self.abaPessoal,
              pos=wx.Point(456, 40), size=wx.Size(0, 13),
              style=wx.ALIGN_CENTRE)
        self.nomeErro.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, True,
              u'Tahoma'))
        self.nomeErro.SetAutoLayout(True)

        self.verificarEstagio = wx.RadioBox(choices=['Sim', 'N\xe3o'],
              id=wxID_FRAMEEDICAOALUNOVERIFICARESTAGIO, label=u'Estagiando:',
              majorDimension=1, name=u'verificarEstagio',
              parent=self.abaProfissional, pos=wx.Point(234, 75),
              size=wx.Size(94, 44), style=wx.RA_SPECIFY_ROWS)
        self.verificarEstagio.SetStringSelection(u'N\xe3o')
        self.verificarEstagio.Bind(wx.EVT_RADIOBOX,
              self.OnVerificarEstagioRadiobox,
              id=wxID_FRAMEEDICAOALUNOVERIFICARESTAGIO)

        self.nomeDisponibilidade = wx.StaticText(id=wxID_FRAMEEDICAOALUNONOMEDISPONIBILIDADE,
              label=u'Disponibilidade:', name=u'nomeDisponibilidade',
              parent=self.abaProfissional, pos=wx.Point(351, 76),
              size=wx.Size(75, 13), style=0)

        self.opcaoManha = wx.CheckBox(id=wxID_FRAMEEDICAOALUNOOPCAOMANHA,
              label=u'Manh\xe3', name=u'opcaoManha',
              parent=self.abaProfissional, pos=wx.Point(372, 98),
              size=wx.Size(53, 13), style=0)
        self.opcaoManha.SetValue(False)

        self.opcaoTarde = wx.CheckBox(id=wxID_FRAMEEDICAOALUNOOPCAOTARDE,
              label=u'Tarde', name=u'opcaoTarde', parent=self.abaProfissional,
              pos=wx.Point(428, 98), size=wx.Size(49, 13), style=0)
        self.opcaoTarde.SetValue(False)
        self.opcaoTarde.SetToolTipString(u'opcaoTarde')

        self.opcaoNoite = wx.CheckBox(id=wxID_FRAMEEDICAOALUNOOPCAONOITE,
              label=u'Noite', name=u'opcaoNoite', parent=self.abaProfissional,
              pos=wx.Point(479, 98), size=wx.Size(40, 13), style=0)
        self.opcaoNoite.SetValue(False)

        self.nomeConfirmarSenha = wx.StaticText(id=wxID_FRAMEEDICAOALUNONOMECONFIRMARSENHA,
              label=u'Confirmar Senha:', name=u'nomeConfirmarSenha',
              parent=self.abaContato, pos=wx.Point(11, 231), size=wx.Size(85,
              13), style=0)

        self.campoConfirmarSenha = wx.TextCtrl(id=wxID_FRAMEEDICAOALUNOCAMPOCONFIRMARSENHA,
              name=u'campoConfirmarSenha', parent=self.abaContato,
              pos=wx.Point(24, 250), size=wx.Size(312, 21),
              style=wx.TE_PASSWORD, value=u'')

        self.botaoLimparContato = wx.Button(id=wxID_FRAMEEDICAOALUNOBOTAOLIMPARCONTATO,
              label=u'Limpar', name=u'botaoLimparContato',
              parent=self.abaContato, pos=wx.Point(880, 20), size=wx.Size(75,
              23), style=0)
        self.botaoLimparContato.Bind(wx.EVT_BUTTON,
              self.OnBotaoLimparContatoButton,
              id=wxID_FRAMEEDICAOALUNOBOTAOLIMPARCONTATO)

        self.nomeSenha = wx.StaticText(id=wxID_FRAMEEDICAOALUNONOMESENHA,
              label=u'Senha:', name=u'nomeSenha', parent=self.abaContato,
              pos=wx.Point(11, 178), size=wx.Size(35, 13), style=0)

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



