def func1(*args ,**kwargs):
	print(args,kwargs)
	
l=[1,2,3]
t =(4,5,6)
d = {'a':7,'b':8}

func1()
func1(1,2)
func1(3,4,"ankit")
func1("prachi",a=3,b=9)
func1(*l)
func1(*l ,**d)
func1(*t)
func1(*t, **d)
func1(1,2,3,*l,name='kumrawat',**d)
func1(1,2,3,'abc')

def func2(arg1,*arg2,**kwargs):
	print(arg1,arg2,kwargs)


func2(1)
func2(4,7,8,'anku',key=2)
func2(4,arg=1,ab='c',pq='hr',oo='st')
func2(*l)
func2(*t,**d)
func2(2,**d)
func2(3,5,*t,age = 23,**d)

