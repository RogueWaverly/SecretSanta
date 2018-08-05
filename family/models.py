from django.db import models

# Create your models here.
class Pool(models.Model):
  pool_name = models.CharField(max_length=200, blank=True, unique=True, default=None)
  sort_order = models.IntegerField(default=0)
  def __str__(self):
    return self.pool_name
  class Meta:
    ordering = ['sort_order']

class ImmFamily(models.Model):
  def __str__(self):
    return str(self.id)
  class Meta:
    verbose_name = 'Immediate Family'
    verbose_name_plural = 'Immediate Families' 

class Member(models.Model):
  mem_name = models.CharField(max_length=200, blank=True, unique=True, default=None)
  birthday = models.DateTimeField(null=True)
  participation = models.BooleanField(default=0)
  pool = models.ForeignKey(Pool, on_delete=models.SET_DEFAULT, default=0)
  imm_family = models.ForeignKey(ImmFamily, on_delete=models.SET_NULL, null=True)
  spouse = models.OneToOneField('self', on_delete=models.SET_NULL, null=True, related_name='spouse_of')
  match = models.OneToOneField('self', on_delete=models.SET_NULL, null=True, related_name='match_of')
  prev_match = models.OneToOneField('self', on_delete=models.SET_NULL, null=True, related_name='prev_match_of')
  def __str__(self):
    return self.mem_name
  class Meta:
    ordering = ['birthday','id']
