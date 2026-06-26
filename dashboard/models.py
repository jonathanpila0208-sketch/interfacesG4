from django.db import models

class OrdenTrabajo(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado'),
    ]

    numero_orden = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    clave = models.CharField(max_length=50, blank=True)
    pais = models.CharField(max_length=50, default='Ecuador')
    anio = models.CharField(max_length=4)
    tipo_vehiculo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    placas = models.CharField(max_length=20)
    color = models.CharField(max_length=30)
    telefono = models.CharField(max_length=20)
    
    # Servicios
    alin_automovil = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    alin_camioneta = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    alin_furgoneta = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    alin_camion = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    bal_automovil = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    bal_camioneta = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    bal_furgoneta = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    bal_camion = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    combo_automovil = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    combo_camioneta = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    combo_furgoneta = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    combo_camion = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    enllantaje = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    nitrogeno = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    parches = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    
    # Correcciones
    corr_del_izq = models.CharField(max_length=100, blank=True)
    corr_del_der = models.CharField(max_length=100, blank=True)
    corr_post_izq = models.CharField(max_length=100, blank=True)
    corr_post_der = models.CharField(max_length=100, blank=True)
    
    otros = models.TextField(blank=True)
    llamadas = models.CharField(max_length=100, blank=True)
    valor_transferencia = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def total(self):
        return (
            self.alin_automovil + self.alin_camioneta + self.alin_furgoneta + self.alin_camion +
            self.bal_automovil + self.bal_camioneta + self.bal_furgoneta + self.bal_camion +
            self.combo_automovil + self.combo_camioneta + self.combo_furgoneta + self.combo_camion +
            self.enllantaje + self.nitrogeno + self.parches + self.valor_transferencia
        )

    def __str__(self):
        return self.numero_orden