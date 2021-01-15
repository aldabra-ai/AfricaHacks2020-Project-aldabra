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
    
    HOSPITALITY_RANK = [
        ('ONE', 1),
        ('TWO', 2),
        ('THREE', 3),
        ('FOUR', 4),
        ('FIVE', 5),
    ]

    name = models.CharField(max_length=300, help_text='Enter hospital name')
    address = models.CharField(max_length=450, help_text='hospital address')
    hospital_type = models.CharField(max_length=30, choices=HOSPITAL_TYPE)
    rank = models.CharField(max_length=20, choices=HOSPITALITY_RANK)
    #slug = models.SlugField()
    objects = models.Manager()
    special_clinics = SpecialClinicManager()
    traditional_hospitals = TraditionalHospitalManager()
    #rooms  = models.IntegerField()
    #blocks = models.IntegerField()

    

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
    block_name = models.CharField(max_length=100, blank=True)
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
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    availability = models.CharField(max_length=15, choices=AVAILABILITY)
    slug = models.SlugField()
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

   # class Department(models.Model):
   #     name = models.CharField(max_length=250)
   #    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
   #     hod = models.ForeignKey(Physician, on_delete=models.CASCADE)
   #     department_id = models.BigIntegerField()
   #
   #     def __str__(self):
   #         return self.name



    



