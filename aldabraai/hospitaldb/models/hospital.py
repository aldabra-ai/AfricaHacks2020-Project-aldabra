from django.db import models

class TraditionalHospitalManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(hospital_type='TH')

class SpecialClinicManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(hospital_type='SC')

class AvailableRoomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(availability='AV')

class Hospital(models.Model):

    HOSPITAL_TYPE = [
        ('SC', 'Special Clinic'),
        ('TH', 'Tranditional Hospital')
    ]


    name = models.CharField(max_length=300, help_text='Enter hospital name')
    address = models.CharField(max_length=450, help_text='hospital address')
    hospital_type = models.CharField(max_length=30, choices=HOSPITAL_TYPE, default=HOSPITAL_TYPE[1])
    rank = models.FloatField(max_length=5)
    objects = models.Manager()
    special_clinics = SpecialClinicManager()
    traditional_hospitals = TraditionalHospitalManager()
    slug = models.SlugField(unique=True)

    

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("aldabra-hospital-dashboard", kwargs={"pk": self.pk})
    

    class Meta:
        ordering = ['-rank']
        verbose_name = 'Hospital'
        verbose_name_plural = 'Hospitals'

class Block(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    block_floor = models.IntegerField()
    block_code = models.IntegerField()

    def __str__(self):
        return self.block_name


class Room(models.Model):

    AVAILABILITY = [
        ('AV', 'Available'),
        ('UA', 'Unavailable')
    ]

    
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    room_name = models.CharField(max_length=250, blank=True)
    room_number = models.IntegerField(primary_key=True)
    room_type = models.CharField(max_length=100)
    block = models.ForeignKey(Block, on_delete=models.PROTECT)
    availability = models.CharField(max_length=15, choices=AVAILABILITY)
    objects = models.Manager()
    available_rooms = AvailableRoomManager()

    def __str__(self):
        return self.room_number

    # def get_absolute_url(self):
    #     return reverse('room-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['availability']
        verbose_name = 'Hospital Room'
        verbose_name_plural = 'Hospital Rooms'







    



