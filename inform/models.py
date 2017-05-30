from __future__ import unicode_literals

from django.db import models

class Univs(models.Model):
    uni_number = models.CharField(max_length=6)
    
    uni_nation = models.CharField(max_length=10, blank=True)
    uni_location = models.CharField(max_length=10, blank=True)
    uni_name = models.TextField()
    uni_language = models.TextField(blank=True)
    uni_people = models.CharField(max_length=1, blank=True) # 왜 maxlength가 1인가요?
    uni_term = models.CharField(max_length=1, blank=True)# 왜 maxlength가 1인가요?
    # 파견인원과 파견기간이 숫자 하나면 충분해서 그랬습니다. 다른 유용한 필드가 있나요?
    
    uni_logo = models.URLField(blank=True) #왜 이미지 필드가 아닌가요?
    # 링크를 가져와서 쓸 때에도 이미지 필드가 가능한가요?
    # 아니면 이 경우도 URL필드를 쓰는게 나을까요? 일단 URL로 수정해 놓겠습니다.
    uni_map = models.TextField(blank=True)
    uni_site = models.URLField(blank=True)# 왜 URL필드가 아닌가요?
    # URL필드의 존재를 몰랐습니다. 고치겠습니다.
    uni_address = models.TextField(blank=True)
    uni_found = models.TextField(blank=True)
    uni_area = models.TextField(blank=True)
    uni_nos = models.TextField(blank=True)
    
    uni_major = models.TextField(blank=True)
    uni_qualification = models.TextField(blank=True)
    
    uni_etc = models.TextField(blank=True)
