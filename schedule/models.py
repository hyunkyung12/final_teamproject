# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Post(models.Model):
	#author = models.ForeignKey('auth.User') 외부키 충돌이 나서 일단 주석처리 했습니다, djangogirls 튜토리얼 그대로 가져오신것 같은데
	#										 은정님도 그대로 가져오셔서 충돌이 나네요.. 일정에 author는 필요 없으니 지우셔도 될것같고 schedule 앱 안에서
	#										 적당하게 수정해서 해주세요!
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
			default=timezone.now)
	published_date = models.DateTimeField(
			blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title



# Create your models here.
