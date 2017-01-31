from django.db import models

class Category(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

class Ingredient(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)
    quantity = models.DecimalField('Quantidade', decimal_places=2, max_length=10)
    buy_price = models.DecimalField('Preço de Compra', decimal_places=2, max_digits=6)
    sell_price = models.DecimalField('Preço de venda', decimal_places=2, max_digits=6)
    quantity = models.DecimalField('Quantidade', decimal_places=2, max_digits=10)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Ingrediente'
        verbose_name_plural = 'Ingredientes'
        ordering = ['name']

class Product(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)
    category = models.ForeignKey('catalog.Category', verbose_name='Categoria')
    ingredient = models.ForeignKey('catalog.Ingredient', verbose_name='Ingredientes')
    quantity = models.DecimalField('Quantidade', decimal_places=2, max_digits=10)
    description = models.TextField('Descrição', blank=True)
    buy_price = models.DecimalField('Preço de compra', decimal_places=2, max_digits=6)
    sell_price = models.DecimalField('Preço', decimal_places=2, max_digits=6)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']
