from django.db import models

# Create your models here.

class UF(models.Model):

    nome = models.CharField(max_length=2)

    class Meta:
        
        verbose_name_plural = 'UFs'

    def __str__(self):

        return self.nome

class Cidade(models.Model):

    nome = models.CharField(max_length=100)
    uf = models.ForeignKey(UF)

    class Meta:

        verbose_name_plural = "Cidades"

    def __str__(self):

        return f'{self.nome} - {self.uf}'
    
class Bairro(models.Model):

    nome = models.CharField(max_length=50)

    class Meta:
        
        verbose_name_plural = 'Bairros'

    def __str__(self):

        return self.nome
    
class TipoLogradouro(models.Model):

    nome = models.CharField(max_length=100)

    class Meta:

        verbose_name_plural = "Tipos de Logradouros"

    def __str__(self):

        return self.nome
    
class TipoImovel(models.Model):

    nome = models.CharField(max_length=100)

    class Meta:

        verbose_name_plural = "Tipos de Imóveis"

    def __str__(self):

        return self.nome
    
class Cargo(models.Model):

    nome = models.CharField(max_length=100)

    class Meta:

        verbose_name_plural = "Cargos"

    def __str__(self):

        return self.nome

class Pessoa(models.Model):

    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=15)
    rg = models.CharField(max_length=20)
    data_nasc = models.DateField()
    email = models.CharField(max_length=80)
    cidade = models.ForeignKey(Cidade)

    class Meta:

        verbose_name_plural = "Pessoas"

    def __str__(self):

        return self.nome
    
class Logradouro(models.Model):

    tipo = models.ForeignKey(TipoLogradouro)
    nome = models.CharField(max_length=100)
    numero = models.PositiveIntegerField()
    complemento = models.CharField(max_length=100)
    bairro = models.ForeignKey(Bairro)
    cep = models.ForeignKey(max_length=20)

    class Meta:

        verbose_name_plural = "Logradouros"

    def __str__(self):

        return f'{self.tipo}, {self.nome}, {self.numero}'

class Imoveis(models.Model):

    nome = models.CharField(max_length=100)
    tipo_imovel = models.ForeignKey(TipoImovel)
    descricao = models.CharField(max_length=500)
    area_construida = models.CharField(max_length=50)
    n_comodos = models.PositiveIntegerField()
    cor = models.CharField(max_length=40)
    n_vagas = models.PositiveIntegerField()
    tipo_logradouro = models.ForeignKey(TipoLogradouro, on_delete = models.CASCADE)
    logradouro = models.ForeignKey(Logradouro)
    bairro = models.ForeignKey(Bairro)
    cidade = models.ForeignKey(Cidade)
    uf = models.ForeignKey(UF)
    cep = models.CharField(max_length=20)
    valor = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:

        verbose_name_plural = "Imóveis"

    def __str__(self):

        return f'{self.tipo_imovel} - {self.nome}'
    
# Comprador
# Estado do Imóvel
# Formas de pagamento
# Nível de qualidade