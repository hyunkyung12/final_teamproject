from __future__ import unicode_literals

from django.db import models

class Univs(models.Model):
    uni_number = models.CharField(max_length=6)
    
    uni_nation = models.CharField(max_length=10, blank=True)
    uni_location = models.CharField(max_length=10, blank=True)
    uni_name = models.TextField()
    uni_language = models.TextField(blank=True)
    uni_people = models.CharField(max_length=1, blank=True)
    uni_term = models.CharField(max_length=1, blank=True)
    
    uni_logo = models.TextField(blank=True)
    uni_map = models.TextField(blank=True)
    uni_site = models.TextField(blank=True)
    uni_address = models.TextField(blank=True)
    uni_found = models.TextField(blank=True)
    uni_area = models.TextField(blank=True)
    uni_nos = models.TextField(blank=True)
    
    uni_major = models.TextField(blank=True)
    uni_qualification = models.TextField(blank=True)
    
    uni_etc = models.TextField(blank=True)
