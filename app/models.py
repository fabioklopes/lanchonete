from django.db import models

def gerar_codigo_cliente(tamanho=10): 
    caracteres = string.ascii_uppercase + string.digits 
    return ''.join(secrets.choice(caracteres) for _ in range(tamanho))

class Customer(models.Model):
    """
    Customer
    @description: Representação da entidade Cliente, contendo informações pessoais e de contato dos clientes da loja.
    @author: Fábio Klevinskas Lopes
    @since: 2026-03-02
    @version: 1.0
    """
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        
    customer_code = models.CharField(max_length=10, null=False, blank=False, unique=True, verbose_name='Código de Cliente')
    first_name = models.CharField(max_length=20, null=False, blank=False, verbose_name='Primeiro Nome')
    last_name = models.CharField(max_length=30, null=False, blank=False, verbose_name='Restante do nome')
    email = models.EmailField(max_length=50, null=False, blank=False, verbose_name='E-mail')
    phone_number = models.CharField(max_length=11, null=False, blank=False, verbose_name='WhatsApp')
    address = models.CharField(max_length=100, null=False, blank=False, verbose_name='Endereço')
    neighborhood = models.CharField(max_length=50, null=False, blank=False, verbose_name='Bairro')
    registration_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, verbose_name='Cliente Ativo')
    
    def save(self, *args, **kwargs): 
        if not self.customer_code: 
            self.customer_code = gerar_codigo_cliente(10)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.customer_code})'


class Group(models.Model):
    """
    Group
    @description: Representação da entidade Grupo, contendo informações sobre os grupos de produtos da loja.
    @author: Fábio Klevinskas Lopes
    @since: 2026-03-02
    @version: 1.0
    """
    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'
        
    name = models.CharField(max_length=25, null=False, blank=False, unique=True, verbose_name='Nome do Grupo')

    def __str__(self):
        return self.name


class Input(models.Model):
    """
    Input
    @description: Representação da entidade Insumo, contendo informações sobre os insumos da loja.
    @author: Fábio Klevinskas Lopes
    @since: 2026-03-02
    @version: 1.0
    """
    class Meta:
        verbose_name = 'Insumo'
        verbose_name_plural = 'Insumos'
        
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=False, blank=False, verbose_name='Grupo')
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nome do Insumo')
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, verbose_name='Valor de Compra')
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, verbose_name='Valor de Venda')
    stock_quantity = models.PositiveIntegerField(null=False, blank=False, verbose_name='Quantidade em Estoque')
    minimum_stock = models.PositiveIntegerField(null=False, blank=False, verbose_name='Estoque Mínimo')

    def __str__(self):
        return self.name


class Menu(models.Model):
    """
    Menu
    @description: Representação da entidade Cardápio, contendo informações sobre os itens do cardápio da loja.
    @author: Fábio Klevinskas Lopes
    @since: 2026-03-02
    @version: 1.0
    """
    class Meta:
        verbose_name = 'Cardápio'
        verbose_name_plural = 'Cardápios'
    
    TYPE = (
        ('A', 'Acompanhamento'),
        ('B', 'Bebida'),
        ('L', 'Lanche'),
        ('S', 'Sobremesa'),
        ('R', 'Refeição'),
        ('P', 'Porção'),
    )

    KIND = (
        ('Q', 'Quente'),
        ('F', 'Frio'),
        ('G', 'Gelado'),
    )
    
    name = models.CharField(max_length=35, null=False, blank=False, unique=True, verbose_name='Nome do Produto')
    type = models.CharField(max_length=1, choices=TYPE, null=False, blank=False, verbose_name='Tipo do Produto')
    description = models.TextField(max_length=200, null=False, blank=False, verbose_name='Descrição do Produto')
    kind = models.CharField(max_length=1, choices=KIND, null=False, blank=False, verbose_name='Forma de servir')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, verbose_name='Valor do Produto')
    photo = models.ImageField(upload_to='', null=True, blank=True, verbose_name='Foto do Produto')
    yeld_servings = models.PositiveIntegerField(null=False, blank=False, verbose_name='Rendimento do Produto')

    def __str__(self):
        return self.name


class Order(models.Model):
    """
    Order
    @description: Representação da entidade Pedido, contendo informações sobre os pedidos realizados pelos clientes da loja.
    @author: Fábio Klevinskas Lopes
    @since: 2026-03-02
    @version: 1.0
    """
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    PAYMENT_METHODS = (
        ('CC', 'Cartão de Crédito'),
        ('CD', 'Cartão de Débito'),
        ('C', 'Dinheiro'),
        ('P', 'Pix'),
    )

    order_number = models.CharField(max_length=10, null=False, blank=False, unique=True, verbose_name='Número do Pedido')
    order_date = models.DateTimeField(auto_now_add=True, verbose_name='Data do Pedido')
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE, null=False, blank=False, verbose_name='Item do Cardápio')
    quantity = models.PositiveIntegerField(null=False, blank=False, verbose_name='Quantidade')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, verbose_name='Valor Total')
    payment_method = models.CharField(max_length=2, choices=PAYMENT_METHODS, null=False, blank=False, verbose_name='Forma de Pagamento')
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, verbose_name='Valor Pago')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, blank=False, verbose_name='Cliente')

    def __str__(self):
        return f'#{self.order_number} - {self.quantity}x {self.menu_item.name} - R$ {self.total_price:.2f}'


class Inventory(models.Model):
    """
    Inventory
    @description: Representação da entidade Estoque, contendo informações sobre o estoque dos insumos da loja.
    @author: Fábio Klevinskas Lopes
    @since: 2026-03-02
    @version: 1.0
    """
    class Meta:
        verbose_name = 'Estoque'
        verbose_name_plural = 'Estoques'
        
    input = models.ForeignKey(Input, on_delete=models.CASCADE, null=False, blank=False, verbose_name='Insumo')
    quantity = models.PositiveIntegerField(null=False, blank=False, verbose_name='Quantidade em Estoque')
    last_updated = models.DateTimeField(auto_now=True, verbose_name='Última Atualização')

    def __str__(self):
        return f'{self.input.name}'


class Employee(models.Model):
    """
    Employee
    @description: Representação da entidade Funcionário, contendo informações sobre os funcionários da loja.
    @author: Fábio Klevinskas Lopes
    @since: 2026-03-02
    @version: 1.0
    """
    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
        
    first_name = models.CharField(max_length=20, null=False, blank=False, verbose_name='Primeiro Nome')
    last_name = models.CharField(max_length=30, null=False, blank=False, verbose_name='Restante do nome')
    phone_number = models.CharField(max_length=11, null=False, blank=False, verbose_name='WhatsApp')
    address = models.CharField(max_length=100, null=False, blank=False, verbose_name='Endereço')
    neighborhood = models.CharField(max_length=50, null=False, blank=False, verbose_name='Bairro')
    registration_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, verbose_name='Funcionário Ativo')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Financial(models.Model):
    """
    Financial
    @description: Representação da entidade Financeiro, contendo informações sobre as finanças da loja.
    @author: Fábio Klevinskas Lopes
    @since: 2026-03-02
    @version: 1.0
    """
    class Meta:
        verbose_name = 'Financeiro'
        verbose_name_plural = 'Financeiros'
        
    TRANSACTION_TYPES = (
        ('E', 'Entrada'),
        ('S', 'Saída'),
    )

    date = models.DateTimeField(auto_now_add=True, verbose_name='Data da Transação')
    description = models.CharField(max_length=100, null=False, blank=False, verbose_name='Descrição da Transação')
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, verbose_name='Valor da Transação')
    transaction_type = models.CharField(max_length=1, choices=TRANSACTION_TYPES, null=False, blank=False, verbose_name='Tipo de Transação')
    invoice_number = models.CharField(max_length=50, null=True, blank=True, verbose_name='Número da Nota Fiscal')

    def __str__(self):
        return f'{self.get_transaction_type_display()} - R$ {self.amount:.2f} - {self.description}'


class Delivery_Driver(models.Model):
    """
    Delivery Driver
    @description: Representação da entidade Motorista de Entrega, contendo informações sobre os motoristas responsáveis pelas entregas da loja.
    @author: Fábio Klevinskas Lopes
    @since: 2026-03-02
    @version: 1.0
    """
    class Meta:
        verbose_name = 'Entregador'
        verbose_name_plural = 'Entregadores'
        
    full_name = models.CharField(max_length=20, null=False, blank=False, verbose_name='Nome Completo')
    identity_number = models.CharField(max_length=20, null=False, blank=False, unique=True, verbose_name='Identificação (CPF)')
    plate_number = models.CharField(max_length=8, null=False, blank=False, unique=True, verbose_name='Placa do Veículo', help_text='Formato: ABC-1234')
    phone_number = models.CharField(max_length=11, null=False, blank=False, verbose_name='WhatsApp')
    active = models.BooleanField(default=True, verbose_name='Entregador Ativo')

    def __str__(self):
        return f'{self.full_name}'


class Delivery(models.Model):
    """
    Delivery
    @description: Representação da entidade Delivery, contendo informações sobre as entregas realizadas pela loja.
    @author: Fábio Klevinskas Lopes
    @since: 2026-03-02
    @version: 1.0
    """
    class Meta:
        verbose_name = 'Delivery'
        verbose_name_plural = 'Deliveries'

    STATUS_CHOICES = (
        ('P', 'Pendente'),
        ('A', 'Andamento'),
        ('C', 'Concluída'),
        ('X', 'Cancelada'),
    )

    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False, blank=False, verbose_name='Pedido')
    delivery_start = models.DateTimeField(auto_now_add=True, verbose_name='Início da Entrega')
    delivery_end = models.DateTimeField(null=True, blank=True, verbose_name='Fim da Entrega')
    delivery_status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P', verbose_name='Status da Entrega')
    delivery_driver = models.ForeignKey(Delivery_Driver, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Entregador')

    def __str__(self):
        return f'Entrega do Pedido #{self.order.order_number} - {self.delivery_status}'


# 