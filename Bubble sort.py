def bsearch(list,low,high,item):
    if low>high:
        return None
    else:
        mid=(int(low)+int(high))//2
        if list[mid]>item:
            return bsearch(list,low,mid-1,item)
        elif list[mid]<item:
            return bsearch(list,mid+1,high,item)
        elif list[mid]==item:
            return mid
        else:
            return -1
l=eval(input('enter the list'))
n=len(l)
r=int(input('enter the item to be found'))
s=bsearch(l,0,n-1,r)
if (s==-1):
    print('item not found')
else:
    print('element  found at the index',s)