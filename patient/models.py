import time
from django.db import models
# from django.contrib.postgres.fields import models.JSONField
from django.contrib.auth.models import User
from village.models import Village
from mandal.models import Mandal
from PHC.models import PHC
from village_sec.models import Village_sec


class Patient (models.Model):
    pkid = models.CharField(max_length=32,
                            primary_key=True
                            )
# BASIC DETAILS
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone = models.CharField(max_length=10,blank = True,null = True)
    adhaar = models.CharField(max_length=256, blank=True)  #hashedData
    relation = models.CharField(max_length=30)  # SonOf/DaughterOf/WifeOf
    gaurdian_name = models.CharField(max_length=50)
    age = models.SmallIntegerField(default=0)
    # M=> Male/F=>Female/NB=>NonBinary
    gender = models.CharField(default='NaN', max_length=3)
    address = models.CharField(max_length=500)
    weight = models.DecimalField(
        default=0.0, decimal_places=3, max_digits=6, blank=True)
    height = models.DecimalField(
        default=0.0, decimal_places=2, max_digits=5, blank=True)
    bloodgroup = models.CharField(default=None, max_length=4)
    PVTG = models.CharField(default=None, max_length=5)
    # Foreign Keys
    mandal = models.ForeignKey(
        Mandal, on_delete=models.CASCADE, default=None, null=True)
    phc = models.ForeignKey(
        PHC, on_delete=models.CASCADE, default=None, null=True)
    villagesec = models.ForeignKey(  
        Village_sec, on_delete=models.CASCADE, default=None, null=True)
    village = models.ForeignKey(
        Village, on_delete=models.CASCADE, default=None, null=True)
    # single/married/separated/divorced/widowed
    maritalstatus = models.CharField(default=None, max_length=15, null=True)
    habits = models.JSONField(null=True)
    # FORMAT =
    # {
    #    smoking : bool,
    #    drinking : bool
    # }



    def __str__(self):
        return self.name

class PatientReport (models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
        # Basic Vitals
    BasicVitals = models.JSONField(null=True)

    # FORMAT =
    # {
    # Fever : "xC" for Celcius and "xF",
    # BP : "x",
    # HR : "x",
    # Pulse: "x",
    # RespRate : "x",
    # }

    BasicSymptoms = models.JSONField(null=True)

    # FORMAT =
    # {
    # Temperature : True or False,
    # Aches :  True or False,
    # Fatigue :  True or False,
    # Cold:  True or False,
    # Cough :  True or False,
    # Diarrhoea :  True or False,
    # Bleeding :  True or False,
    # Infection : True or False,
    # others : "Text"
    # }

    # Pedal Fields
    pedalEdema = models.CharField(max_length=2, blank=True)
    # if above is yes then ask single/bilateral

    pedal_profile = models.JSONField(null=True)

    # FORMAT =
    # {
    # pedaltype = models.CharField(max_length=50, blank=True)
    # dateoftesting = models.CharField(blank=True, max_length=10)
    # serumCreatinine = models.DecimalField(
    #     max_digits=5, decimal_places=1, blank=True)
    # bloodUrea = models.DecimalField(max_digits=5, decimal_places=1, blank=True)
    # uricAcid = models.DecimalField(max_digits=5, decimal_places=1, blank=True)
    # electrolytes_sodium = models.DecimalField(
    #     max_digits=5, decimal_places=1, blank=True)
    # electrolytes_potassium = models.DecimalField(
    #     max_digits=5, decimal_places=1, blank=True)
    # bun = models.DecimalField(max_digits=5, decimal_places=1, blank=True)
    # }

    KidneyProfile = models.JSONField(null=True)

    # FORMAT =
    {
        # in case abnormal ask following
        # ailments = models.TextField(max_length=100,blank=True)
        # dialysis = models.BooleanField(default = False)
    }

    doctorreq = models.BooleanField(default=False)
    # if above is yes then ask refer to the following hospital
    hospitalAdmit = models.CharField(max_length=50, blank=True)
    opd = models.BooleanField(default=False)
    dateOfAdmit = models.CharField(blank=True, max_length=10)  # YYYY-MM-DD
    refered = models.BooleanField(default=False)
    # case:yes
    referredto = models.CharField(max_length=50, blank=True)
    ref_status = models.TextField(max_length=300, blank=True)
    treatmentDone = models.TextField(max_length=300, blank=True)
    DischargeDetails = models.JSONField(null = True)
    #FORMAT = 
    # {
    #     discharged = models.BooleanField()
    # }

    deceased = models.BooleanField(default=False,null = True)
    # if above is answered yes

    DetailsDeath = models.JSONField(null=True)
    # FORMAT =
    {
        # deathDate = models.CharField(blank = True, max_length=10)
        # placeOfDeath = models.CharField(max_length=50,blank=True)
        # causeOfDeath = models.TextField(max_length=300,blank=True)
    }
    AnemiaProfile = models.JSONField(null=True)
    PatientHealthStatus = models.JSONField(null = True)
    # What it will look like:
    # {
    #    wbc_count = models.DecimalField(max_digits=5, decimal_places=2,blank = True)
    #    diffrential_count = models.JSONField(null = True)
    #    hb = models.DecimalField(max_digits=5, decimal_places=2,blank = True)
    #    plat_count = models.DecimalField( max_digits=5, decimal_places=2,blank=True)
    # }
    type_data = models.CharField(max_length=50,blank = True,null = True)
    

