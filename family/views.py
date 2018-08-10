from django.shortcuts import get_object_or_404, render

from .models import Pool, ImmFamily, Member

# Create your views here.
def OpenPools(request):
  pools = Pool.objects.order_by('sort_order')
  members = Member.objects.order_by('birthday')
  membersByPool = [{},{}]
  membersByPool[0][0] = []
  membersByPool[1][0] = []
  for pool in pools:
    membersByPool[0][pool.id] = []
    membersByPool[1][pool.id] = []
  for member in members:
    if member.pool:
      membersByPool[member.participation][member.pool.id].append(member)
    else:
      membersByPool[member.participation][0].append(member)
  numOfCols = len(pools) + int((len(membersByPool[0][0]) + len(membersByPool[1][0]))>0)
  context = {
    'pools': pools,
    'membersByPool': membersByPool,
    'numOfCols': numOfCols,
  }
  return render(request, 'openpools.html', context)

def EditMember(request, member_id):
  member = get_object_or_404(Member, id = member_id)
  context = {
    'member': member,
  }
  return render(request, 'editmember.html', context)

