from django.db import models
from django.core.validators import validate_ipv4_address

###########################################################################################################################################

CHOICE_STATUS = [
    ('Em uso', 'Em uso'),
    ('Descartado', 'Descartado'),
    ('Não Localizado', 'Não Localizado'),
]

###########################################################################################################################################

CHOICE_LOCAL_DESKTOP = [
    ('Antas Norte', 'Antas Norte'),
    ('Pedra Branca', 'Pedra Branca'),
    ('Centro Gold', 'Centro Gold'),
    ('Pantera', 'Pantera'),
    ('Ourilândia do Norte', 'Ourilândia do Norte'),
]

###########################################################################################################################################

CHOICE_PAIS = [
    ('Brasil', 'Brasil'),
    ('Austrália', 'Austrália'),
]

###########################################################################################################################################

CHOICE_FABRICANTE_DESKTOP = [
    ('DELL', 'DELL'),
    ('Acer', 'Acer'),
    ('ASUS', 'ASUS'),
    ('HP', 'HP'),
    ('Positivo', 'Positivo'),
    ('Samsung', 'Samsung'),
    ('Sony VAIO', 'Sony VAIO'),
]    

###########################################################################################################################################

CHOICE_RAM = [
    ('12GB', '12GB'),
    ('8GB', '8GB'),
    ('6GB', '6GB'),
    ('4GB', '4GB'),
    ('2GB', '2GB'),
] 

###########################################################################################################################################

CHOICE_RAM_DESKTOP = [
    ('128GB', '128GB'),
    ('64GB', '64GB'),
    ('32GB', '32GB'),
    ('16GB', '16GB'),
    ('8GB', '8GB'),
    ('6GB', '6GB'),
    ('4GB', '4GB'),
    ('2GB', '2GB'),
] 

###########################################################################################################################################

CHOICE_ARMAZENAMENTO = [
    ('16GB', '16GB'),
    ('32GB', '32GB'),
    ('64GB', '64GB'),
    ('128GB', '128GB'),
    ('256GB', '256GB'),
    ('512GB', '512GB'),
    ('1TB', '1TB'),
    ('2TB', '2TB'),
]

###########################################################################################################################################

CHOICE_DEPARTAMENTO = [
    ('Tecnologia da Informação', 'Tecnologia da Informação'),
    ('Armazem', 'Armazem'),
    ('Suprimentos', 'Suprimentos'),
    ('Segurança', 'Segurança'),
    ('Medicina', 'Medicina'),
    ('Planta', 'Planta'),
    ('Operação', 'Operação'),
    ('Recursos Humanos', 'Recursos Humanos'),
    ('Administração', 'Administração'),
]

###########################################################################################################################################

CHOICE_TIPO = [
    ('Laptop', 'Laptop'),
    ('Desktop', 'Desktop'),
    ('Rádio', 'Rádio'),
    ('Celular', 'Celular'),
    ('Network', 'Network'),
    ('Periféricos', 'Periféricos'),
]

###########################################################################################################################################

CHOICE_OPERADORA = [
    ('VIVO', 'VIVO'),
    ('TIM', 'TIM'),
    ('CLARO', 'CLARO'),
]

###########################################################################################################################################

CHOICE_STATUS_CELULAR = [
    ('Em uso', 'Em uso'),
    ('Em estoque', 'Em estoque'),
    ('Desativado', 'Desativado'),
    ('Devolvido', 'Devolvido'),

]

###########################################################################################################################################

CHOICE_ARMAZENAMENTO_DESKTOP = [
    ('HD 320GB', 'HD 320GB'),
    ('HD 500GB', 'HD 500GB'),
    ('HD 1TB', 'HD 1TB'),
    ('HD 2TB', 'HD 2TB'),
    ('HD 4TB', 'HD 4TB'),
    ('SSD Sata 256GB', 'SSD Sata 256GB'),
    ('SSD Sata 512GB', 'SSD Sata 512GB'),
    ('SSD Sata 1TB', 'SSD Sata 1TB'),
    ('SSD Sata 2TB', 'SSD Sata 2TB'),
    ('SSD Sata 4TB', 'SSD Sata 4TB'),
    ('SSD NVMe 128GB', 'SSD NVMe 128GB'),
    ('SSD NVMe 256GB', 'SSD NVMe 256GB'),
    ('SSD NVMe 512GB', 'SSD NVMe 512GB'),
    ('SSD NVMe 1TB', 'SSD NVMe 1TB'),
    ('SSD NVMe 2TB', 'SSD NVMe 2TB'),
]

###########################################################################################################################################

class PEDRABRANCA(models.Model):
    # Descrevendo o nome da class
    class Meta:
        verbose_name = "PEDRA BRANCA"
        verbose_name_plural = "PEDRA BRANCA"

    VLAN = models.CharField("VLAN", max_length=50, null=True, blank=True)
    SERIAL = models.CharField("N. Série", max_length=50, null=True, blank=True)
    SERVICE_TAG = models.CharField("Service Tag", max_length=50, null=True, blank=True)
    MODEL_HOST = models.CharField("MODEL / HOST", max_length=50, null=True, blank=True)
    NAME = models.CharField("Nome", max_length=50, null=True, blank=True)
    IP = models.CharField("IP Address", max_length=50, null=True, blank=True)
    HOSTNAME = models.CharField("Hostname", max_length=50, null=True, blank=True)
    MAC = models.CharField("MAC", max_length=50, null=True, blank=True)
    LOCAL = models.CharField("Local", max_length=50, null=True, blank=True)
    SWITCH_PORT = models.CharField("Porta do Switch", max_length=50, null=True, blank=True)

###########################################################################################################################################

class PANTERA(models.Model):
    # Descrevendo o nome da class
    class Meta:
        verbose_name = "PANTERA"
        verbose_name_plural = "PANTERA"

    VLAN = models.CharField("VLAN", max_length=50, null=True, blank=True)
    SERIAL = models.CharField("SERIAL", max_length=50, null=True, blank=True)
    SERVICE_TAG = models.CharField("SERVICE TAG", max_length=50, null=True, blank=True)
    MODEL_HOST = models.CharField("MODEL / HOST", max_length=50, null=True, blank=True)
    TYPE = models.CharField("TYPE", max_length=50, null=True, blank=True)  
    NAME = models.CharField("NAME", max_length=50, null=True, blank=True)
    IP = models.CharField("IP ADDRESS", max_length=50, null=True, blank=True)
    HOSTNAME = models.CharField("HOSTNAME", max_length=50, null=True, blank=True)
    MAC = models.CharField("M.A.C", max_length=50, null=True, blank=True)
    LOCAL_COMMENT = models.CharField("LOCAL (COMMENT)", max_length=50, null=True, blank=True)
    SWITCH_PORT = models.CharField("SWITCH PORT", max_length=50, null=True, blank=True)
    DHCP_OPTION = models.CharField("DHCP OPTION", max_length=50, null=True, blank=True)

###########################################################################################################################################

class EXTERNAL_IPS(models.Model):
    # Descrevendo o nome da class
    class Meta:
        verbose_name = "EXTERNAL IPs"
        verbose_name_plural = "EXTERNAL IPs"

    Site = models.CharField("Site", max_length=50, null=True, blank=True)
    Provedor = models.CharField("Provedor", max_length=50, null=True, blank=True)
    Tipo = models.CharField("Tipo", max_length=50, null=True, blank=True)
    IP_01 = models.CharField("IP", max_length=50, null=True, blank=True)
    Rota_2 = models.CharField(" Rota 2", max_length=50, null=True, blank=True)  
    IP_02 = models.CharField("IP", max_length=50, null=True, blank=True)
    Gateway = models.CharField("Gateway", max_length=50, null=True, blank=True)
    Vlan = models.CharField("Vlan", max_length=50, null=True, blank=True)

###########################################################################################################################################

class ROUTES(models.Model):
    # Descrevendo o nome da class
    class Meta:
        verbose_name = "ROUTES"
        verbose_name_plural = "ROUTES"

    VLAN01 = models.CharField("VLAN", max_length=50, null=True, blank=True)
    NAME = models.CharField("NAME", max_length=50, null=True, blank=True)
    VLAN02 = models.CharField("VLAN", max_length=50, null=True, blank=True)
    VLAN_10 = models.CharField("10", max_length=50, null=True, blank=True)
    VLAN_20 = models.CharField("20", max_length=50, null=True, blank=True)  
    VLAN_30 = models.CharField("30", max_length=50, null=True, blank=True)
    VLAN_31 = models.CharField("31", max_length=50, null=True, blank=True)
    VLAN_32 = models.CharField("32", max_length=50, null=True, blank=True)
    VLAN_42 = models.CharField("42", max_length=50, null=True, blank=True)
    VLAN_44 = models.CharField("44", max_length=50, null=True, blank=True)
    VLAN_132 = models.CharField("132", max_length=50, null=True, blank=True)
    VLAN_224 = models.CharField("224", max_length=50, null=True, blank=True)
    VLAN_226 = models.CharField("226", max_length=50, null=True, blank=True)
    VLAN_228 = models.CharField("228", max_length=50, null=True, blank=True)
    VLAN_236 = models.CharField("236", max_length=50, null=True, blank=True)
    VLAN_250 = models.CharField("250", max_length=50, null=True, blank=True)
    VLAN_251 = models.CharField("251", max_length=50, null=True, blank=True)
    INTERNET = models.CharField("INTERNET", max_length=50, null=True, blank=True)
    COMENTARIOS = models.CharField("COMENTÁRIOS", max_length=50, null=True, blank=True)

###########################################################################################################################################

class MATERIAL(models.Model):
    # Descrevendo o nome da class
    class Meta:
        verbose_name = "MATERIAL"
        verbose_name_plural = "MATERIAL"

    MATERIAL = models.CharField("MATERIAL", max_length=50, null=True, blank=True)
    QTD = models.CharField("QTD", max_length=50, null=True, blank=True)
    VENDOR = models.CharField("VENDOR", max_length=50, null=True, blank=True)
    MODELO = models.CharField("MODELO", max_length=50, null=True, blank=True)
    N_SERIE = models.CharField("N/S", max_length=50, null=True, blank=True)  

###########################################################################################################################################

class ANTAS_NORTE(models.Model):
    # Descrevendo o nome da class
    class Meta:
        verbose_name = "ANTAS NORTE"
        verbose_name_plural = "ANTAS NORTE"

    VLAN = models.CharField("VLAN", max_length=50, null=True, blank=True)
    SERIAL = models.CharField("SERIAL", max_length=50, null=True, blank=True)
    SERVICE_TAG = models.CharField("SERVICE TAG", max_length=50, null=True, blank=True)
    MODELO = models.CharField("MODELO", max_length=50, null=True, blank=True)
    NAME = models.CharField("NAME", max_length=50, null=True, blank=True)  
    IP = models.CharField("IP", max_length=50, null=True, blank=True)
    HOSTNAME = models.CharField("HOSTNAME", max_length=50, null=True, blank=True)
    MAC = models.CharField("MAC", max_length=50, null=True, blank=True)
    LOCAL = models.CharField("LOCAL", max_length=50, null=True, blank=True)
    SWITCH_PORT = models.CharField("SWITCH PORT", max_length=50, null=True, blank=True)
    COMMENTS = models.CharField("COMMENTS", max_length=50, null=True, blank=True)
    DHCP = models.CharField("DHCP", max_length=50, null=True, blank=True)

###########################################################################################################################################

class VLANs(models.Model):
    # Descrevendo o nome da class
    class Meta:
        verbose_name = "VLANs"
        verbose_name_plural = "VLANs"

    VLAN = models.CharField("VLAN", max_length=50, null=True, blank=True)
    NAME = models.CharField("NAME", max_length=50, null=True, blank=True)
    NAME_OBS = models.CharField("NAME-OBS", max_length=50, null=True, blank=True)
    OUTROS = models.CharField("OUTROS", max_length=50, null=True, blank=True)
    OUTROS_OBS = models.CharField("OUTROS-OBS", max_length=50, null=True, blank=True)

###########################################################################################################################################

class CAN(models.Model):
    # Descrevendo o nome da class
    class Meta:
        verbose_name = "CAN"
        verbose_name_plural = "CAN"

    VLAN = models.CharField("VLAN", max_length=50, null=True, blank=True)
    SERIAL = models.CharField("SERIAL", max_length=50, null=True, blank=True)
    SERVICE_TAG = models.CharField("SERVICE TAG", max_length=50, null=True, blank=True)
    MODEL_HOST = models.CharField("MODEL / HOST", max_length=50, null=True, blank=True)
    TYPE = models.CharField("TYPE", max_length=50, null=True, blank=True)  
    NAME = models.CharField("NAME", max_length=50, null=True, blank=True)
    IP = models.CharField("IP Address", max_length=50, null=True, blank=True)
    HOSTNAME = models.CharField("HOSTNAME", max_length=50, null=True, blank=True)
    MAC = models.CharField("MAC", max_length=50, null=True, blank=True)
    LOCAL_COMENT = models.CharField("LOCAL (COMENT)", max_length=50, null=True, blank=True)
    SWITCH_PORT = models.CharField("SWITCH PORT", max_length=50, null=True, blank=True)
    DHCP_OPTION = models.CharField("DHCP OPTION", max_length=50, null=True, blank=True)

###########################################################################################################################################

class BHZ(models.Model):
    # Descrevendo o nome da class
    class Meta:
        verbose_name = "BELORIZONTE"
        verbose_name_plural = "BELORIZONTE"

    VLAN = models.CharField("VLAN", max_length=50, null=True, blank=True)
    SERIAL = models.CharField("SERIAL", max_length=50, null=True, blank=True)
    SERVICE_TAG = models.CharField("SERVICE TAG", max_length=50, null=True, blank=True)
    MODEL_HOST = models.CharField("MODEL / HOST", max_length=50, null=True, blank=True)    
    TYPE = models.CharField("TYPE", max_length=50, null=True, blank=True)  
    NAME = models.CharField("NAME", max_length=50, null=True, blank=True)
    IP = models.CharField("IP ADDRESS", max_length=50, null=True, blank=True)
    HOSTNAME = models.CharField("HOSNAME", max_length=50, null=True, blank=True)
    MAC = models.CharField("M.A.C", max_length=50, null=True, blank=True)
    LOCAL_COMENT = models.CharField("LOCAL (COMENT)", max_length=50, null=True, blank=True)
    SWITCH_PORT = models.CharField("SWITCH PORT", max_length=50, null=True, blank=True)
    DHCP_OPTION = models.CharField("DHCP OPTION", max_length=50, null=True, blank=True)

###########################################################################################################################################

# class Laptop(models.Model):
#   # Descrevendo o nome da class
#    class Meta:
#        verbose_name = "Laptop"
#        verbose_name_plural = "Laptop"
#
#    hostname = models.CharField('N. Hostname', max_length=20, null=True, blank=True)
#    patrimonio = models.CharField('Patrimônio', max_length=20, null=True, blank=True)
#    local = models.CharField('Local', max_length=50, null=True, blank=True, choices=CHOICE_LOCAL_DESKTOP)
#    utilizador = models.CharField('Utilizador', max_length=35, null=True, blank=True,)
#    departamento = models.CharField('Departamento', max_length=50, null=True, blank=True, choices=CHOICE_DEPARTAMENTO)
#    cargo = models.CharField('Cargo', max_length=30, null=True, blank=True)
#    datarecebimento = models.DateTimeField('Data Recebimento', max_length=10, null=True, blank=True)
#    fabricante = models.CharField('Fabricante', max_length=50, null=True, blank=True, choices=CHOICE_FABRICANTE_DESKTOP)
#    modelo = models.CharField('Modelo', max_length=35, null=True, blank=True)
#    memoriaram = models.CharField('M. RAM', max_length=10, null=True, blank=True, choices=CHOICE_RAM_DESKTOP)
#    armazenamento = models.CharField('Armazenamento', max_length=50, null=True, blank=True, choices=CHOICE_ARMAZENAMENTO_DESKTOP)
#    numerodeserie = models.CharField('N. Série', max_length=30, null=True, blank=True)
#    observacoes = models.TextField('Observações', max_length=800, null=True, blank=True)

###########################################################################################################################################

# class Celular(models.Model):
#    # Descrevendo o nome da class
#    class Meta:
#        verbose_name = "Celular"
#        verbose_name_plural = "Celular"    
#
#    utilizador = models.CharField('Utilizador', max_length=100, null=True, blank=True)
#    matricula = models.CharField('Matrícula', max_length=100, null=True, blank=True)
#    status = models.CharField('Status', max_length=100, null=True, blank=True, choices=CHOICE_STATUS_CELULAR)
#    departamento = models.CharField('Departamento', max_length=100, null=True, blank=True, choices=CHOICE_DEPARTAMENTO)
#    email = models.CharField('E-mail', max_length=100, null=True, blank=True)
#    datacompra = models.DateField('Data da Compra', max_length=100, null=True, blank=True)
#    datarecebimento = models.DateTimeField('Data Recebimento', max_length=100, null=True, blank=True)
#    telefone = models.CharField('N. Telefone', max_length=11, null=True, blank=True)
#    imeidochip = models.CharField('IMEI do CHIP', max_length=100, null=True, blank=True)
#    operadora = models.CharField('Operadora', max_length=100, null=True, blank=True, choices=CHOICE_OPERADORA)
#    fabricante = models.CharField('Fabricante', max_length=100, null=True, blank=True,)
#    modelo = models.CharField('Modelo', max_length=100, null=True, blank=True)
#    memoriaram = models.CharField('M. RAM', max_length=100, null=True, blank=True, choices=CHOICE_RAM)
#    armazenamento = models.CharField('Armazenamento', max_length=30, null=True, blank=True)
#    numerodeserie = models.CharField('N. Série', max_length=30, null=True, blank=True)
#    observacoes = models.TextField('Observações', max_length=800, null=True, blank=True)

###########################################################################################################################################
   
# class Rede(models.Model):
#    # Descrevendo o nome da class
#    class Meta:
#        verbose_name = "Rede"
#        verbose_name_plural = "Rede"
#
#   utilizador = models.CharField('Utilizador', max_length=100, null=True, blank=True)
#    matricula = models.CharField('Matrícula', max_length=100, null=True, blank=True)
#    departamento = models.CharField('Departamento', max_length=100, null=True, blank=True, choices=CHOICE_DEPARTAMENTO)
#    email = models.CharField('E-mail', max_length=100, null=True, blank=True)
#    datacompra = models.DateField('Data da Compra', max_length=100, null=True, blank=True)
#    datarecebimento = models.DateTimeField('Data Recebimento', max_length=100, null=True, blank=True)
#    telefone = models.CharField('N. Telefone', max_length=100, null=True, blank=True)
#    imeidochip = models.CharField('IMEI do CHIP', max_length=100, null=True, blank=True)
#    fabricante = models.CharField('Fabricante', max_length=100, null=True, blank=True,)
#    modelo = models.CharField('Modelo', max_length=100, null=True, blank=True)
#    memoriaram = models.CharField('M. RAM', max_length=100, null=True, blank=True, choices=CHOICE_RAM)
#    armazenamento = models.CharField('Armazenamento', max_length=30, null=True, blank=True)
#    numerodeserie = models.CharField('N. Série', max_length=30, null=True, blank=True)

###########################################################################################################################################
   
# class Radio(models.Model):
#    # Descrevendo o nome da class
#    class Meta:
#        verbose_name = "Rádio"
#        verbose_name_plural = "Rádio"
#
#    utilizador = models.CharField('Utilizador', max_length=100, null=True, blank=True)
#    matricula = models.CharField('Matrícula', max_length=100, null=True, blank=True)
#    departamento = models.CharField('Departamento', max_length=100, null=True, blank=True, choices=CHOICE_DEPARTAMENTO)
#    email = models.CharField('E-mail', max_length=100, null=True, blank=True)
#    datacompra = models.DateField('Data da Compra', max_length=100, null=True, blank=True)
#    datarecebimento = models.DateTimeField('Data Recebimento', max_length=100, null=True, blank=True)
#    telefone = models.CharField('N. Telefone', max_length=100, null=True, blank=True)
#    imeidochip = models.CharField('IMEI do CHIP', max_length=100, null=True, blank=True)
#    fabricante = models.CharField('Fabricante', max_length=100, null=True, blank=True,)
#    modelo = models.CharField('Modelo', max_length=100, null=True, blank=True)
#    memoriaram = models.CharField('M. RAM', max_length=100, null=True, blank=True, choices=CHOICE_RAM_DESKTOP)
#    armazenamento = models.CharField('Armazenamento', max_length=30, null=True, blank=True)
#    numerodeserie = models.CharField('N. Série', max_length=30, null=True, blank=True)

###########################################################################################################################################

CHOICE_VLAN_PBA = [
    ('VLAN 10 - FORMATAÇÃO', 'VLAN 10 - FORMATAÇÃO'),
    ('VLAN 20 - CORPORATIVO', 'VLAN 20 - CORPORATIVO'),
    ('VLAN 42 - PBAPDV', 'VLAN 42 - PBAPDV'),
    ('VLAN 136 - CATRACA E R. DE PONTO', 'VLAN 136 - CATRACA E R. DE PONTO'),
    ('VLAN 132 - CÂMERA', 'VLAN 132 - CÂMERA'),
    ('VLAN 226 - SWITCH', 'VLAN 226 - SWITCH'),
    ('VLAN 228 - PTP - ACSSES POINT', 'VLAN 228 - PTP - ACSSES POINT'),
]

CHOICE_FABRICANTE_PBA = [
    ('CISCO',  'CISCO'),
    ('DELL', 'DELL'),
    ('UBIQUITI', 'UBIQUITI'),
    ('DATACON', 'DATACON'),
]

CHOICE_LOCAL_INFRA_REDE = [
    ('ANTAS NORTE', 'ANTAS NORTE'),
    ('PEDRA BRANCA', 'PEDRA BRANCA'),
    ('CENTRO GOLD', 'CENTRO GOLD'),
    ('PANTERA', 'PANTERA'),
    ('OURILÂNDIA DO NORTE', 'OURILÂNDIA DO NORTE'),
    ('SANTA LUCIA', 'SANTA LUCIA'),
]

CHOICE_CATEGORIA_PBA = [
    ('REDE', 'REDE'),
    ('MONITORAMENTO', 'MONITORAMENTO'),
    ('COMUNICAÇÃO', 'COMUNICAÇÃO'),
]

CHOICE_TIPO_PBA = [
    ('SWITCH', 'SWITCH'),
    ('ACSSES POINT', 'ACSSES POINT'),
    ('NVR / DVR', 'NVR / DVR'),

]

class ativosgeral(models.Model):
    # Descrevendo o nome da class
    class Meta:
        verbose_name = "Ativos de Rede em Geral"
        verbose_name_plural = "Ativos de Rede em Geral"

    hostname = models.CharField("Hostname", max_length=50,)
    vlan = models.CharField("VLAN", max_length=40, choices=CHOICE_VLAN_PBA)
    ip = models.CharField("IP Address", max_length=15, unique=True)
    mac = models.CharField("MAC", max_length=50,)
    nserie = models.CharField("N. Série", max_length=50,)
    fabricante = models.CharField("Fabricante", max_length=50, choices=CHOICE_FABRICANTE_PBA)
    modelo = models.CharField("Modelo", max_length=35, null=True, blank=True,)
    instaladoem = models.CharField("Instalado em", max_length=50,)
    localidade = models.CharField("Localidade", max_length=50, null=True, blank=True, choices=CHOICE_LOCAL_INFRA_REDE)
    categoria = models.CharField("Categoria", max_length=50, choices=CHOICE_CATEGORIA_PBA)
    tipo = models.CharField("Tipo", max_length=50, choices=CHOICE_TIPO_PBA)
    tipogestao = models.CharField("Tipo de Acesso", max_length=50,)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)
    usuario = models.CharField("Usuário:", max_length=20,)
    senha = models.CharField("Senha:", max_length=20,)
    obs = models.TextField("Observações:", max_length=400, null=True, blank=True,)

    # Obrigatoriedade para ficar tudo em Maiúsculo
    def clean(self):
        self.hostname = self.hostname.upper()
        self.vlan = self.vlan.upper()
        self.ip = self.ip.upper()
        self.mac = self.mac.upper()
        self.nserie = self.nserie.upper()
        self.fabricante = self.fabricante.upper()
        self.modelo = self.modelo.upper() if self.modelo else None
        self.instaladoem = self.instaladoem.upper()
        self.localidade = self.localidade.upper() if self.localidade else None
        self.categoria = self.categoria.upper()
        self.tipo = self.tipo.upper()
        self.tipogestao = self.tipogestao.upper() if self.tipogestao else None
        # self.usuario = self.usuario.upper()
        # self.senha = self.senha.upper()
        self.obs = self.obs.upper() if self.obs else None

###########################################################################################################################################

class Cisco(models.Model):
    # Descrevendo o nome da class
    class Meta:
        verbose_name = "CISCO"
        verbose_name_plural = "CISCO"

    hostname = models.CharField("Hostname", max_length=50,)
    vlan = models.CharField("VLAN", max_length=40)
    ip = models.CharField("IP Address", max_length=15, null=True, blank=True)
    mac = models.CharField("MAC", max_length=50, null=True, blank=True)
    nserie = models.CharField("N. Série", max_length=50, null=True, blank=True)
    fabricante = models.CharField("Fabricante", max_length=50)
    modelo = models.CharField("Modelo", max_length=35, null=True, blank=True,)
    instaladoem = models.CharField("Instalado em", max_length=50, null=True, blank=True,)
    localidade = models.CharField("Localidade", max_length=50)
    categoria = models.CharField("Categoria", max_length=50)
    tipo = models.CharField("Tipo", max_length=50)
    tipogestao = models.CharField("Tipo de Acesso", max_length=50, null=True,)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    usuario = models.CharField("Usuário:", max_length=20,)
    senha = models.CharField("Senha:", max_length=20,)
    obs = models.CharField("Observações:", max_length=60, null=True, blank=True,)

###########################################################################################################################################

class intelbras(models.Model):
    # Descrevendo o nome da class
    class Meta:
        verbose_name = "INTELBRAS"
        verbose_name_plural = "INTELBRAS"

    hostname = models.CharField("Hostname", max_length=50,)
    vlan = models.CharField("VLAN", max_length=40)
    ip = models.CharField("IP Address", max_length=15, null=True, blank=True)
    mac = models.CharField("MAC", max_length=50, null=True, blank=True)
    nserie = models.CharField("N. Série", max_length=50, null=True, blank=True)
    fabricante = models.CharField("Fabricante", max_length=50)
    modelo = models.CharField("Modelo", max_length=35, null=True, blank=True,)
    instaladoem = models.CharField("Instalado em", max_length=50, null=True, blank=True,)
    localidade = models.CharField("Localidade", max_length=50)
    categoria = models.CharField("Categoria", max_length=50)
    tipo = models.CharField("Tipo", max_length=50)
    tipogestao = models.CharField("Tipo de Acesso", max_length=50, null=True,)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em', auto_now=True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)
    usuario = models.CharField("Usuário:", max_length=20,)
    senha = models.CharField("Senha:", max_length=20,)
    obs = models.CharField("Observações:", max_length=60, null=True, blank=True,)

###########################################################################################################################################

class Message(models.Model):
    class Meta:
        verbose_name = "Anotações"
        verbose_name_plural = "Anotações"

    title = models.CharField('Título', max_length=40)
    content = models.TextField('Insira suas Anotações', max_length=800)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    def __str__(self):
        return self.title

###########################################################################################################################################

CHOICE_FABRICANTE_ACSSES_POINT = [
    ('UBIQUITI', 'UBIQUITI'),
    ('CISCO', 'CISCO'),
    ('TP-LINK', 'TP-LINK'),
    ('D-LINK', 'D-LINK'),

]

CHOICE_TIPO_ACSSES_POINT = [
    ('ACSSES POINT', 'ACSSES POINT'),
    ('PTP', 'PTP'),
]

CHOICE_SITE_CONTROLLER_ACSSES_POINT = [
    ('Oz-Homolog', 'Oz-Homolog'),
    ('PBA-MINA', 'PBA-MINA'),
    ('PBA-PRONTOS', 'PBA-PRONTOS'),
    ('Pedra Branca', 'Pedra Branca'),
    ('Antas Norte', 'Antas Norte'),
    ('Centro Gold', 'Centro Gold'),
    ('CAN - Exploration', 'CAN - Exploration'),
]

CHOICE_MODELOS_ACSSES_POINT = [
    ('UAP-AC-M-Pro', 'UAP-AC-M-Pro'),
    ('UAP-AC-Pro', 'UAP-AC-Pro'),
    ('UAP-AC-HD', 'UAP-AC-HD'),
    ('UAP-AC-Lite', 'UAP-AC-Lite'),
    ('UAP-AC-U6-Lite', 'UAP-AC-U6-Lite'),
    ('UAP-AC-LR', 'UAP-AC-LR'),
    ('UAP-AC-U6-M', 'UAP-AC-U6-M'),
    ('UAP-AC-M', 'UAP-AC-M'),

]

class ACSSES_POINT(models.Model):
    # Descrevendo o nome da class
    class Meta:
        verbose_name = "ACSSES POINT"
        verbose_name_plural = "ACSSES POINT"

    hostname = models.CharField("Hostname", max_length=50, unique=True)
    sitecontroller = models.CharField("Site na Controller", max_length=30, choices=CHOICE_SITE_CONTROLLER_ACSSES_POINT)
    ip = models.CharField("IP Address", max_length=15, unique=True)
    mac = models.CharField("MAC", max_length=50, unique=True)
    vlan = models.CharField("VLAN", max_length=40, choices=CHOICE_VLAN_PBA)
    modelo = models.CharField("Modelo", max_length=50, choices=CHOICE_MODELOS_ACSSES_POINT)
    fabricante = models.CharField("Fabricante", max_length=50, choices=CHOICE_FABRICANTE_ACSSES_POINT)
    instaladoem = models.CharField("Instalado em", max_length=50,)
    localidade = models.CharField("Localidade", max_length=50, null=True, blank=True, choices=CHOICE_LOCAL_INFRA_REDE)
    tipo = models.CharField("Tipo", max_length=50, choices=CHOICE_TIPO_ACSSES_POINT)
    obs = models.TextField("Observações:", max_length=400, null=True, blank=True,)

    ###########################################################################################################################################

CHOICE_LOCAL_CAMERAS = [
    ('ANTAS NORTE', 'ANTAS NORTE'),
    ('PEDRA BRANCA', 'PEDRA BRANCA'),
    ('CENTRO GOLD', 'CENTRO GOLD'),
    ('PANTERA', 'PANTERA'),
    ('OURILÂNDIA DO NORTE', 'OURILÂNDIA DO NORTE'),
    ('SANTA LUCIA', 'SANTA LUCIA'),
]

class CAMERAS(models.Model):
    # Descrevendo o nome da class
    class Meta:
        verbose_name = "CAMERAS"
        verbose_name_plural = "CAMERAS"

    IP_ADDRESS = models.CharField(
        "IP Address", 
        max_length=15, 
        validators=[validate_ipv4_address], 
        error_messages={
            'invalid': 'Por favor, insira um endereço IP válido no formato 111.111.111.111.'
        }, 
        unique=True
    )
    N_CANAL = models.CharField("N. Canal", max_length=30)
    PORTA = models.CharField("Porta", max_length=15)
    DISPOSITIVO_ID_CLOUD = models.CharField("Dispositivo | ID Cloud", max_length=50, unique=True)
    FABRICANTE = models.CharField("Fabricante", max_length=40)
    MODELO = models.CharField("Modelo", max_length=50)
    ADOTADO_EM = models.CharField("Adotado em:", max_length=50)
    LOCAL = models.CharField("Local", max_length=50, choices=CHOICE_LOCAL_CAMERAS)
    OBS = models.TextField("Observações:", max_length=400, null=True, blank=True)


###########################################################################################################################################

# models.py
# from django.db import models

class MakeMessages(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.TextField()
    field3 = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.field1


###########################################################################################################################################