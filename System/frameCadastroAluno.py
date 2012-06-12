# -*- coding: cp1252 -*-
#Boa:Frame:frameCadastroAluno
#! /usr/bin/env python
#-*-coding: latin1-*-
#-*-coding: iso-8859-1-*-

import wx
import wx.lib.masked.textctrl
import urllib
import cgi
import bridge
import Db #IMPORTA O BANCO

def create(parent):
    return frameCadastroAluno(parent)

[wxID_FRAMECADASTROALUNO, wxID_FRAMECADASTROALUNOABACONTATO, 
 wxID_FRAMECADASTROALUNOABAPESSOAL, wxID_FRAMECADASTROALUNOABAPROFISSIONAL, 
 wxID_FRAMECADASTROALUNOBOTAOBUSCARCEP, 
 wxID_FRAMECADASTROALUNOBOTAOLIMPARCONTATO, 
 wxID_FRAMECADASTROALUNOBOTAOLIMPARPESSOAL, 
 wxID_FRAMECADASTROALUNOBOTAOLIMPARPROFISSIONAL, 
 wxID_FRAMECADASTROALUNOBOTAOSALVAR, wxID_FRAMECADASTROALUNOBOTAOVOLTAR, 
 wxID_FRAMECADASTROALUNOCAMPOANIVERSARIO, 
 wxID_FRAMECADASTROALUNOCAMPOANOCONCLUSAO, wxID_FRAMECADASTROALUNOCAMPOBAIRRO, 
 wxID_FRAMECADASTROALUNOCAMPOCELULAR, wxID_FRAMECADASTROALUNOCAMPOCEP, 
 wxID_FRAMECADASTROALUNOCAMPOCIDADE, wxID_FRAMECADASTROALUNOCAMPOCOMPLEMENTO, 
 wxID_FRAMECADASTROALUNOCAMPOCONFIRMARSENHA, wxID_FRAMECADASTROALUNOCAMPOCPF, 
 wxID_FRAMECADASTROALUNOCAMPOEMAIL, wxID_FRAMECADASTROALUNOCAMPOENDERECO, 
 wxID_FRAMECADASTROALUNOCAMPOMATRICULA, wxID_FRAMECADASTROALUNOCAMPONOMEALUNO, 
 wxID_FRAMECADASTROALUNOCAMPONOMEMAE, wxID_FRAMECADASTROALUNOCAMPONOMEPAI, 
 wxID_FRAMECADASTROALUNOCAMPONUMERO, wxID_FRAMECADASTROALUNOCAMPOSENHA, 
 wxID_FRAMECADASTROALUNOCAMPOTELEFONE, wxID_FRAMECADASTROALUNOCAMPOUF, 
 wxID_FRAMECADASTROALUNOCOMBOBOXCURSOS, 
 wxID_FRAMECADASTROALUNOCOMBOBOXDEPARTAMENTO, 
 wxID_FRAMECADASTROALUNOCPFINVALIDO, wxID_FRAMECADASTROALUNOCPFVALIDO, 
 wxID_FRAMECADASTROALUNODADOSDOSALUNOS, wxID_FRAMECADASTROALUNODATANASCIMENTO, 
 wxID_FRAMECADASTROALUNOLINHACADASTROALUNOS, wxID_FRAMECADASTROALUNOLOGOIFPE, 
 wxID_FRAMECADASTROALUNONOMEANOCONCLUSAO, wxID_FRAMECADASTROALUNONOMEBAIRRO, 
 wxID_FRAMECADASTROALUNONOMECELULAR, wxID_FRAMECADASTROALUNONOMECEP, 
 wxID_FRAMECADASTROALUNONOMECIDADE, wxID_FRAMECADASTROALUNONOMECOMPLEMENTO, 
 wxID_FRAMECADASTROALUNONOMECONFIRMARSENHA, wxID_FRAMECADASTROALUNONOMECPF, 
 wxID_FRAMECADASTROALUNONOMECURSO, wxID_FRAMECADASTROALUNONOMEDEPARTAMENTO, 
 wxID_FRAMECADASTROALUNONOMEDISPONIBILIDADE, wxID_FRAMECADASTROALUNONOMEEMAIL, 
 wxID_FRAMECADASTROALUNONOMEENDERECO, wxID_FRAMECADASTROALUNONOMEERRO, 
 wxID_FRAMECADASTROALUNONOMEMATRICULA, wxID_FRAMECADASTROALUNONOMENOMEALUNO, 
 wxID_FRAMECADASTROALUNONOMENOMEMAE, wxID_FRAMECADASTROALUNONOMENOMEPAI, 
 wxID_FRAMECADASTROALUNONOMENUMERO, wxID_FRAMECADASTROALUNONOMESENHA, 
 wxID_FRAMECADASTROALUNONOMETELEFONE, wxID_FRAMECADASTROALUNONOMEUF, 
 wxID_FRAMECADASTROALUNOOPCAOMANHA, wxID_FRAMECADASTROALUNOOPCAONOITE, 
 wxID_FRAMECADASTROALUNOOPCAOTARDE, wxID_FRAMECADASTROALUNOPAINELCADASTRO, 
 wxID_FRAMECADASTROALUNOSELECIONASEXO, wxID_FRAMECADASTROALUNOVALIDARCPF, 
 wxID_FRAMECADASTROALUNOVERIFICARESTAGIO, 
] = [wx.NewId() for _init_ctrls in range(66)]

class frameCadastroAluno(wx.Frame):
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
        wx.Frame.__init__(self, id=wxID_FRAMECADASTROALUNO,
              name=u'frameCadastroAluno', parent=prnt, pos=wx.Point(700, 273),
              size=wx.Size(1040, 614), style=wx.DEFAULT_FRAME_STYLE,
              title=u'Est\xe1gio Curricular - Cadastro de Alunos')
        self.SetClientSize(wx.Size(1024, 576))
        self.Center(wx.BOTH)
        self.SetIcon(wx.Icon(u'./Graficos/icone.ico',wx.BITMAP_TYPE_ICO))
        self.SetMaxSize(wx.Size(1040, 614))
        self.SetMinSize(wx.Size(1040, 614))

        self.painelCadastro = wx.Panel(id=wxID_FRAMECADASTROALUNOPAINELCADASTRO,
              name=u'painelCadastro', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(1024, 576), style=wx.TAB_TRAVERSAL)
        self.painelCadastro.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.logoIFPE = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/logo.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMECADASTROALUNOLOGOIFPE,
              name=u'logoIFPE', parent=self.painelCadastro, pos=wx.Point(8, 8),
              size=wx.Size(175, 70), style=0)

        self.linhaCadastroAlunos = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/LinhaCAdastroAlunos.png',
              wx.BITMAP_TYPE_PNG),
              id=wxID_FRAMECADASTROALUNOLINHACADASTROALUNOS,
              name=u'linhaCadastroAlunos', parent=self.painelCadastro,
              pos=wx.Point(0, 80), size=wx.Size(1024, 21), style=0)

        self.dadosDosAlunos = wx.Notebook(id=wxID_FRAMECADASTROALUNODADOSDOSALUNOS,
              name=u'dadosDosAlunos', parent=self.painelCadastro,
              pos=wx.Point(20, 120), size=wx.Size(984, 424), style=0)
        self.dadosDosAlunos.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.dadosDosAlunos.SetForegroundColour(wx.Colour(255, 255, 255))
        self.dadosDosAlunos.SetThemeEnabled(True)

        self.abaPessoal = wx.Window(id=wxID_FRAMECADASTROALUNOABAPESSOAL,
              name=u'abaPessoal', parent=self.dadosDosAlunos, pos=wx.Point(0,
              0), size=wx.Size(976, 398), style=wx.TAB_TRAVERSAL)

        self.campoCPF = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRAMECADASTROALUNOCAMPOCPF,
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

        self.nomeCPF = wx.StaticText(id=wxID_FRAMECADASTROALUNONOMECPF,
              label=u'CPF:', name=u'nomeCPF', parent=self.abaPessoal,
              pos=wx.Point(11, 15), size=wx.Size(24, 13), style=0)

        self.CPFInvalido = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/botao_invalido.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMECADASTROALUNOCPFINVALIDO,
              name=u'CPFInvalido', parent=self.abaPessoal, pos=wx.Point(170,
              36), size=wx.Size(14, 14), style=0)
        self.CPFInvalido.Show(False)

        self.cpfValido = wx.StaticBitmap(bitmap=wx.Bitmap(u'./Graficos/botao_valido.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMECADASTROALUNOCPFVALIDO,
              name=u'cpfValido', parent=self.abaPessoal, pos=wx.Point(170, 36),
              size=wx.Size(14, 14), style=0)
        self.cpfValido.Show(False)

        self.validarCPF = wx.BitmapButton(bitmap=wx.Bitmap(u'./Graficos/botao_buscar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMECADASTROALUNOVALIDARCPF,
              name=u'validarCPF', parent=self.abaPessoal, pos=wx.Point(134, 30),
              size=wx.Size(26, 26), style=wx.BU_AUTODRAW)
        self.validarCPF.Bind(wx.EVT_BUTTON, self.OnValidarCPFButton,
              id=wxID_FRAMECADASTROALUNOVALIDARCPF)

        self.dataNascimento = wx.StaticText(id=wxID_FRAMECADASTROALUNODATANASCIMENTO,
              label=u'Data de nascimento:', name=u'dataNascimento',
              parent=self.abaPessoal, pos=wx.Point(202, 14), size=wx.Size(100,
              13), style=0)

        self.campoAniversario = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRAMECADASTROALUNOCAMPOANIVERSARIO,
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
              id=wxID_FRAMECADASTROALUNOSELECIONASEXO, label=u'Sexo:',
              majorDimension=1, name=u'selecionaSexo', parent=self.abaPessoal,
              pos=wx.Point(342, 14), size=wx.Size(176, 43),
              style=wx.RA_SPECIFY_ROWS)
        self.selecionaSexo.SetStringSelection(u'Feminino')

        self.nomeNomeAluno = wx.StaticText(id=wxID_FRAMECADASTROALUNONOMENOMEALUNO,
              label=u'Nome Completo:', name=u'nomeNomeAluno',
              parent=self.abaPessoal, pos=wx.Point(11, 70), size=wx.Size(80,
              13), style=0)

        self.campoNomeAluno = wx.TextCtrl(id=wxID_FRAMECADASTROALUNOCAMPONOMEALUNO,
              name=u'campoNomeAluno', parent=self.abaPessoal, pos=wx.Point(24,
              89), size=wx.Size(496, 21), style=0, value=u'')
        self.campoNomeAluno.SetMaxLength(50)

        self.nomeNomeMae = wx.StaticText(id=wxID_FRAMECADASTROALUNONOMENOMEMAE,
              label=u'Nome da M\xe3e:', name=u'nomeNomeMae',
              parent=self.abaPessoal, pos=wx.Point(11, 125), size=wx.Size(70,
              14), style=0)

        self.campoNomeMae = wx.TextCtrl(id=wxID_FRAMECADASTROALUNOCAMPONOMEMAE,
              name=u'campoNomeMae', parent=self.abaPessoal, pos=wx.Point(24,
              145), size=wx.Size(496, 21), style=0, value=u'')
        self.campoNomeMae.SetMaxLength(50)

        self.nomeNomePai = wx.StaticText(id=wxID_FRAMECADASTROALUNONOMENOMEPAI,
              label=u'Nome do Pai:', name=u'nomeNomePai',
              parent=self.abaPessoal, pos=wx.Point(11, 181), size=wx.Size(64,
              13), style=0)

        self.campoNomePai = wx.TextCtrl(id=wxID_FRAMECADASTROALUNOCAMPONOMEPAI,
              name=u'campoNomePai', parent=self.abaPessoal, pos=wx.Point(24,
              202), size=wx.Size(496, 21), style=0, value=u'')
        self.campoNomePai.SetMaxLength(50)

        self.nomeCEP = wx.StaticText(id=wxID_FRAMECADASTROALUNONOMECEP,
              label=u'CEP:', name=u'nomeCEP', parent=self.abaPessoal,
              pos=wx.Point(11, 237), size=wx.Size(24, 13), style=0)

        self.campoCEP = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRAMECADASTROALUNOCAMPOCEP,
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
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMECADASTROALUNOBOTAOBUSCARCEP,
              name=u'botaoBuscarCEP', parent=self.abaPessoal, pos=wx.Point(136,
              253), size=wx.Size(26, 26), style=wx.BU_AUTODRAW)
        self.botaoBuscarCEP.Bind(wx.EVT_BUTTON, self.OnBotaoBuscarCEPButton,
              id=wxID_FRAMECADASTROALUNOBOTAOBUSCARCEP)

        self.nomeNumero = wx.StaticText(id=wxID_FRAMECADASTROALUNONOMENUMERO,
              label=u'N\xfamero:', name=u'nomeNumero', parent=self.abaPessoal,
              pos=wx.Point(160, 237), size=wx.Size(42, 13), style=0)

        self.campoNumero = wx.TextCtrl(id=wxID_FRAMECADASTROALUNOCAMPONUMERO,
              name=u'campoNumero', parent=self.abaPessoal, pos=wx.Point(173,
              256), size=wx.Size(100, 21), style=0, value=u'')

        self.nomeComplemento = wx.StaticText(id=wxID_FRAMECADASTROALUNONOMECOMPLEMENTO,
              label=u'Complemento:', name=u'nomeComplemento',
              parent=self.abaPessoal, pos=wx.Point(293, 237), size=wx.Size(70,
              13), style=0)

        self.abaProfissional = wx.Window(id=wxID_FRAMECADASTROALUNOABAPROFISSIONAL,
              name=u'abaProfissional', parent=self.dadosDosAlunos,
              pos=wx.Point(0, 0), size=wx.Size(976, 398),
              style=wx.TAB_TRAVERSAL)

        self.nomeMatricula = wx.StaticText(id=wxID_FRAMECADASTROALUNONOMEMATRICULA,
              label=u'Matr\xedcula:', name=u'nomeMatricula',
              parent=self.abaProfissional, pos=wx.Point(16, 15),
              size=wx.Size(48, 13), style=0)

        self.campoMatricula = wx.TextCtrl(id=wxID_FRAMECADASTROALUNOCAMPOMATRICULA,
              name=u'campoMatricula', parent=self.abaProfissional,
              pos=wx.Point(29, 34), size=wx.Size(144, 21), style=0, value=u'')

        self.abaContato = wx.Window(id=wxID_FRAMECADASTROALUNOABACONTATO,
              name=u'abaContato', parent=self.dadosDosAlunos, pos=wx.Point(0,
              0), size=wx.Size(976, 398), style=wx.TAB_TRAVERSAL)

        self.campoEmail = wx.TextCtrl(id=wxID_FRAMECADASTROALUNOCAMPOEMAIL,
              name=u'campoEmail', parent=self.abaContato, pos=wx.Point(24, 35),
              size=wx.Size(312, 21), style=0, value=u'')

        self.nomeEmail = wx.StaticText(id=wxID_FRAMECADASTROALUNONOMEEMAIL,
              label=u'E-Mail:', name=u'nomeEmail', parent=self.abaContato,
              pos=wx.Point(11, 16), size=wx.Size(33, 13), style=0)

        self.nomeTelefone = wx.StaticText(id=wxID_FRAMECADASTROALUNONOMETELEFONE,
              label=u'Telefone:', name=u'nomeTelefone', parent=self.abaContato,
              pos=wx.Point(11, 68), size=wx.Size(47, 13), style=0)

        self.campoTelefone = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRAMECADASTROALUNOCAMPOTELEFONE,
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

        self.nomeCelular = wx.StaticText(id=wxID_FRAMECADASTROALUNONOMECELULAR,
              label=u'Celular:', name=u'nomeCelular', parent=self.abaContato,
              pos=wx.Point(11, 125), size=wx.Size(38, 13), style=0)

        self.campoCelular = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRAMECADASTROALUNOCAMPOCELULAR,
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

        self.botaoSalvar = wx.Button(id=wxID_FRAMECADASTROALUNOBOTAOSALVAR,
              label=u'Salvar', name=u'botaoSalvar', parent=self.abaContato,
              pos=wx.Point(885, 360), size=wx.Size(75, 23), style=0)
        self.botaoSalvar.Bind(wx.EVT_BUTTON, self.OnBotaoSalvarButton,
              id=wxID_FRAMECADASTROALUNOBOTAOSALVAR)

        self.campoComplemento = wx.TextCtrl(id=wxID_FRAMECADASTROALUNOCAMPOCOMPLEMENTO,
              name=u'campoComplemento', parent=self.abaPessoal,
              pos=wx.Point(306, 256), size=wx.Size(214, 21), style=0,
              value=u'')

        self.nomeDepartamento = wx.StaticText(id=wxID_FRAMECADASTROALUNONOMEDEPARTAMENTO,
              label=u'Departamento:', name=u'nomeDepartamento',
              parent=self.abaProfissional, pos=wx.Point(200, 15),
              size=wx.Size(74, 13), style=0)

        self.nomeSenha = wx.StaticText(id=wxID_FRAMECADASTROALUNONOMESENHA,
              label=u'Senha:', name=u'nomeSenha', parent=self.abaContato,
              pos=wx.Point(11, 178), size=wx.Size(35, 13), style=0)

        self.nomeEndereco = wx.StaticText(id=wxID_FRAMECADASTROALUNONOMEENDERECO,
              label=u'Endere\xe7o:', name=u'nomeEndereco',
              parent=self.abaPessoal, pos=wx.Point(11, 292), size=wx.Size(50,
              13), style=0)

        self.campoEndereco = wx.TextCtrl(id=wxID_FRAMECADASTROALUNOCAMPOENDERECO,
              name=u'campoEndereco', parent=self.abaPessoal, pos=wx.Point(24,
              313), size=wx.Size(496, 21), style=0, value=u'')

        self.nomeBairro = wx.StaticText(id=wxID_FRAMECADASTROALUNONOMEBAIRRO,
              label=u'Bairro:', name=u'nomeBairro', parent=self.abaPessoal,
              pos=wx.Point(11, 346), size=wx.Size(33, 13), style=0)

        self.nomeCidade = wx.StaticText(id=wxID_FRAMECADASTROALUNONOMECIDADE,
              label=u'Cidade:', name=u'nomeCidade', parent=self.abaPessoal,
              pos=wx.Point(265, 346), size=wx.Size(38, 13), style=0)

        self.campoBairro = wx.TextCtrl(id=wxID_FRAMECADASTROALUNOCAMPOBAIRRO,
              name=u'campoBairro', parent=self.abaPessoal, pos=wx.Point(24,
              365), size=wx.Size(224, 21), style=0, value=u'')

        self.campoCidade = wx.TextCtrl(id=wxID_FRAMECADASTROALUNOCAMPOCIDADE,
              name=u'campoCidade', parent=self.abaPessoal, pos=wx.Point(278,
              365), size=wx.Size(186, 21), style=0, value=u'')

        self.comboBoxDepartamento = wx.ComboBox(choices=['DASE'],
              id=wxID_FRAMECADASTROALUNOCOMBOBOXDEPARTAMENTO,
              name=u'comboBoxDepartamento', parent=self.abaProfissional,
              pos=wx.Point(217, 34), size=wx.Size(130, 21),
              style=wx.CB_READONLY, value=u'Selecione o Departamento')
        self.comboBoxDepartamento.SetLabel(u'')
        self.comboBoxDepartamento.SetStringSelection(u'Selecione o departamento')

        self.nomeCurso = wx.StaticText(id=wxID_FRAMECADASTROALUNONOMECURSO,
              label=u'Curso:', name=u'nomeCurso', parent=self.abaProfissional,
              pos=wx.Point(373, 15), size=wx.Size(33, 13), style=0)

        self.comboBoxCursos = wx.ComboBox(choices=['TELECOMUNICACOES',
              'ELETRONICA', 'ELETROTECNICA'],
              id=wxID_FRAMECADASTROALUNOCOMBOBOXCURSOS, name=u'comboBoxCursos',
              parent=self.abaProfissional, pos=wx.Point(390, 34),
              size=wx.Size(130, 21), style=wx.CB_READONLY, value=u'')
        self.comboBoxCursos.SetLabel(u'Selecione o Curso')

        self.nomeAnoConclusao = wx.StaticText(id=wxID_FRAMECADASTROALUNONOMEANOCONCLUSAO,
              label=u'Ano que concluiu (ou concluir\xe1) o curso:',
              name=u'nomeAnoConclusao', parent=self.abaProfissional,
              pos=wx.Point(16, 75), size=wx.Size(192, 13), style=0)

        self.campoAnoConclusao = wx.lib.masked.textctrl.TextCtrl(id=wxID_FRAMECADASTROALUNOCAMPOANOCONCLUSAO,
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

        self.botaoLimparProfissional = wx.Button(id=wxID_FRAMECADASTROALUNOBOTAOLIMPARPROFISSIONAL,
              label=u'Limpar', name=u'botaoLimparProfissional',
              parent=self.abaProfissional, pos=wx.Point(880, 20),
              size=wx.Size(75, 23), style=0)
        self.botaoLimparProfissional.Bind(wx.EVT_BUTTON,
              self.OnBotaoLimparProfissionalButton,
              id=wxID_FRAMECADASTROALUNOBOTAOLIMPARPROFISSIONAL)

        self.botaoVoltar = wx.BitmapButton(bitmap=wx.Bitmap(u'./Graficos/botao_voltar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAMECADASTROALUNOBOTAOVOLTAR,
              name=u'botaoVoltar', parent=self.painelCadastro, pos=wx.Point(952,
              13), size=wx.Size(57, 57), style=wx.BU_AUTODRAW)
        self.botaoVoltar.Bind(wx.EVT_BUTTON, self.OnBotaoVoltarButton,
              id=wxID_FRAMECADASTROALUNOBOTAOVOLTAR)

        self.nomeUF = wx.StaticText(id=wxID_FRAMECADASTROALUNONOMEUF,
              label=u'UF:', name=u'nomeUF', parent=self.abaPessoal,
              pos=wx.Point(480, 346), size=wx.Size(18, 13), style=0)

        self.campoUF = wx.TextCtrl(id=wxID_FRAMECADASTROALUNOCAMPOUF,
              name=u'campoUF', parent=self.abaPessoal, pos=wx.Point(493, 365),
              size=wx.Size(27, 21), style=0, value=u'')
        self.campoUF.SetMaxLength(2)

        self.botaoLimparPessoal = wx.Button(id=wxID_FRAMECADASTROALUNOBOTAOLIMPARPESSOAL,
              label=u'Limpar', name=u'botaoLimparPessoal',
              parent=self.abaPessoal, pos=wx.Point(880, 20), size=wx.Size(75,
              23), style=0)
        self.botaoLimparPessoal.Bind(wx.EVT_BUTTON,
              self.OnBotaoLimparPessoalButton,
              id=wxID_FRAMECADASTROALUNOBOTAOLIMPARPESSOAL)

        self.nomeErro = wx.StaticText(id=wxID_FRAMECADASTROALUNONOMEERRO,
              label=u'', name=u'nomeErro', parent=self.abaPessoal,
              pos=wx.Point(541, 36), size=wx.Size(0, 13),
              style=wx.ALIGN_CENTRE)
        self.nomeErro.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, True,
              u'Tahoma'))
        self.nomeErro.SetAutoLayout(True)

        self.verificarEstagio = wx.RadioBox(choices=['Sim', 'N\xe3o'],
              id=wxID_FRAMECADASTROALUNOVERIFICARESTAGIO, label=u'Estagiando:',
              majorDimension=1, name=u'verificarEstagio',
              parent=self.abaProfissional, pos=wx.Point(234, 75),
              size=wx.Size(94, 44), style=wx.RA_SPECIFY_ROWS)
        self.verificarEstagio.SetStringSelection(u'N\xe3o')
        self.verificarEstagio.Bind(wx.EVT_RADIOBOX,
              self.OnVerificarEstagioRadiobox,
              id=wxID_FRAMECADASTROALUNOVERIFICARESTAGIO)

        self.nomeDisponibilidade = wx.StaticText(id=wxID_FRAMECADASTROALUNONOMEDISPONIBILIDADE,
              label=u'Disponibilidade:', name=u'nomeDisponibilidade',
              parent=self.abaProfissional, pos=wx.Point(351, 76),
              size=wx.Size(75, 13), style=0)

        self.opcaoManha = wx.CheckBox(id=wxID_FRAMECADASTROALUNOOPCAOMANHA,
              label=u'Manh\xe3', name=u'opcaoManha',
              parent=self.abaProfissional, pos=wx.Point(372, 98),
              size=wx.Size(53, 13), style=0)
        self.opcaoManha.SetValue(False)

        self.opcaoTarde = wx.CheckBox(id=wxID_FRAMECADASTROALUNOOPCAOTARDE,
              label=u'Tarde', name=u'opcaoTarde', parent=self.abaProfissional,
              pos=wx.Point(428, 98), size=wx.Size(49, 13), style=0)
        self.opcaoTarde.SetValue(False)
        self.opcaoTarde.SetToolTipString(u'opcaoTarde')

        self.opcaoNoite = wx.CheckBox(id=wxID_FRAMECADASTROALUNOOPCAONOITE,
              label=u'Noite', name=u'opcaoNoite', parent=self.abaProfissional,
              pos=wx.Point(479, 98), size=wx.Size(40, 13), style=0)
        self.opcaoNoite.SetValue(False)

        self.campoSenha = wx.TextCtrl(id=wxID_FRAMECADASTROALUNOCAMPOSENHA,
              name=u'campoSenha', parent=self.abaContato, pos=wx.Point(24, 197),
              size=wx.Size(312, 21), style=wx.TE_PASSWORD, value=u'')

        self.nomeConfirmarSenha = wx.StaticText(id=wxID_FRAMECADASTROALUNONOMECONFIRMARSENHA,
              label=u'Confirmar Senha:', name=u'nomeConfirmarSenha',
              parent=self.abaContato, pos=wx.Point(11, 231), size=wx.Size(85,
              13), style=0)

        self.botaoLimparContato = wx.Button(id=wxID_FRAMECADASTROALUNOBOTAOLIMPARCONTATO,
              label=u'Limpar', name=u'botaoLimparContato',
              parent=self.abaContato, pos=wx.Point(880, 20), size=wx.Size(75,
              23), style=0)
        self.botaoLimparContato.Bind(wx.EVT_BUTTON,
              self.OnBotaoLimparContatoButton,
              id=wxID_FRAMECADASTROALUNOBOTAOLIMPARCONTATO)

        self.campoConfirmarSenha = wx.TextCtrl(id=wxID_FRAMECADASTROALUNOCAMPOCONFIRMARSENHA,
              name=u'campoConfirmarSenha', parent=self.abaContato,
              pos=wx.Point(24, 250), size=wx.Size(312, 21),
              style=wx.TE_PASSWORD, value=u'')

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
        self.selecionaSexo.SetStringSelection(u'Feminino')
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
        self.verificarEstagio.SetStringSelection(u'N\xe3o')
        self.opcaoManha.SetValue(False)
        self.opcaoTarde.SetValue(False)
        self.opcaoNoite.SetValue(False)

        event.Skip()

    def OnBotaoVoltarButton(self, event):
        event.Skip()

    def OnVerificarEstagioRadiobox(self, event):
        event.Skip()

    def OnBotaoSalvarButton(self, event): #pra já deixar maiusculo
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


        #Inserção no banco
        #Primeiro Declaro todo mundo:
        self.__cpf              =self.campoCPF.GetValue()
        self.__data_nascimento  =self.campoAniversario.GetValue()
        self.__sexo             =self.selecionaSexo #o sexo tem que receber 0 ou 1 mas nao sei como faz com o choice, procura na bibioteca do wx
        self.__nome             =self.campoNomeAluno.GetValue()
        self.__mae              =self.campoNomeMae.GetValue()
        self.__pai              =self.campoNomePai.GetValue()
        if self.__pai=='': #caso seja vazio
            self.pai = None
        self.__cep              =self.campoCEP.GetValue()
        self.__numero           =self.campoNumero.GetValue()
        self.__complemento      =self.campoComplemento.GetValue()
        if self.__complemento=='':
            self.__complemento= None
        self.__endereco         =self.campoEndereco.GetValue()
        self.__bairro           =self.campoBairro.GetValue()
        self.__cidade           =self.campoCidade.GetValue()
        self.__uf               =self.campoUF.GetValue()
        self.__matricula        =self.campoMatricula.GetValue()
        self.__departamento     =self.comboBoxDepartamento.GetValue() #nao sei fazer fazer com esse tambem mas tem que tranformar em alguma string para entrar no banco
        self.__curso            =self.comboBoxCursos.GetValue() #nao sei fazer tambem, mas eh string
        self.__ano_conclusao    =self.campoAnoConclusao.GetValue()
        self.__estagiando       =self.verificarEstagio #nao sei mas eh no mesmo esquema
        self.__manha            =self.opcaoManha #nao sei (0 ou 1)
        self.__tarde            =self.opcaoTarde #nao sei (0 ou 1) tambem
        self.__noite            =self.opcaoNoite #nao sei tambem (0 ou 1)
        self.__email            =self.campoEmail.GetValue()
        if self.__email == '':
            self.__email= None
        self.__telefone         =self.campoTelefone.GetValue()
        self.__celular          =self.campoCelular.GetValue()
        self.__senha            =self.campoSenha.GetValue()
        #DEPOIS DE DECLARAR TODO MUNDO EU INSIRO PELA FUNCAO
        Db.createAluno(self.__cpf , self.__data_nascimento, self.__sexo, self.__nome, self.__mae, self.__cep,\
                self.__numero, self.__endereco, self.__bairro, self.__cidade, self.__uf, self.__matricula, \
                self.__departamento , self.__curso, self.__ano_conclusao,\
                self.__estagiando, self.__telefone, self.__celular, self.__senha, pai = self.__pai, \
                complemento = self.__complemento, email= self.__email, manha = self.__manha, tarde = self.__tarde, noite = self.__noite)

        # e fim... A nao ser que dê algum erro ai vc tem que tratar.






        event.Skip()

    def OnBotaoLimparContatoButton(self, event):
        self.campoEmail.SetValue('')
        self.campoTelefone.SetValue('')
        self.campoCelular.SetValue('')
        self.campoSenha.SetValue('')
        self.campoConfirmarSenha.SetValue('')
        event.Skip()

