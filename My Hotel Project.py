class MyHotel:	
    def disp(self):
    	print('welcome to Hotel Manasa in Tirupati')
    	print('Please select Items in MENU')
    	a=(int(input('enter number of idly    :')))
    	s=a*5
    	print('idly amount is',s)
    	print()
    	b=int(input('enter number of vada    :'))
    	t=b*10
    	print('vada amount is',t)
    	print()
    	c=int(input('enter number of Dosa	:'))
    	u=c*20
    	print('Dosa amount is',u)
    	print()
    	d=int(input('enter number of chapathi:'))
    	v=d*15
    	print('Chapathi amount is',v)
    	print()
    	e=int(input('enter number of Puri    :'))
    	w=e*20
    	print('Puri amount is',w)
    	print()
    	f=int(input('enter number of Porota  :'))
    	x=f*25
    	print('Porota amount is',x)
    	p=s+t+u+v+w+x
    	print()
    	f=open("morning.txt",'w')
    	f.write('Breakfast Bill is:\n')
    	f.write(str(p))
    	f.write('\n')
    	f.write('supplier collected tip is:')
    	print('The total Hotel bill is:','Rs.',p)
    	print('Thank you for eating breakfast in my Hotel...')
    	print()
    	j=str(input('Do you have to pay tip to supplier yes (or) no:'))
    	if j=='yes':
    		y=int(input('Allow pay tip to supplier:'))
    		print('supplier collected tip is',y,'Rupees')
    	else:
    		print('Not allow to pay tip')
    	print()	
    	z=int(input('How many stars you give for feedback:'))
    	f.write(str(y))
    	f.close()
    	if z==1:
    		print('One star: *')
    		print('very bad maintainence')
    	elif z==2:
    		print('Two stars: **')
    		print('average maintainence')
    	elif z==3:
    		print('Three stars: ***')
    		print('Good maintainence')
    	elif z==4:
    		print('Four stars: ****')
    		print('very Good maintainence')
    	elif z==5:
    		print('Five stars: *****')
    		print('very very Good maintainence.....Thank you')
    	else:
    		print('stars valid for 0 to 5 only')
    		z1=int(input('Please enter a valid star:'))
    		if z1==1:
    			print('One star: *')
    			print('very bad maintainence')
    		elif z1==2:
    			print('Two stars: **')
    			print('average maintainence')
    		elif z1==3:
    			print('Three stars: ***')
    			print('Good maintaintence')
    		elif z1==4:
    			print('Four stars: ****')
    			print('very Good maintainence')
    		elif z1==5:
    			print('Five stars: *****')
    			print('very very Good maintainence.....Thank you')				
    	print()	
    	print('------Thank You to Come------')
    	print()
    	print('---------------Developed by Sai----------------')
    	print()
s12=str(input('Do you want to order Morning Tiffen  [yes (or) no]: '))
if s12=='yes':
	M=MyHotel()
	M.disp()
sr=str(input('Do you want to order afternoon Lunch: [yes (or) no]:'))
print()
if sr=='yes':
    	      print('welcome to Manasa Hotel in tirupati')
    	      print('Please select Atfernoon Items in MENU')
    	      a=int(input('enter mills       :'))
    	      s=a*50
    	      print('mills amount is',s)
    	      print()
    	      b=int(input('enter veg rice    :'))
    	      t=b*40
    	      print('veg rice amount is',t)
    	      print()
    	      c=int(input('enter Gobi	  :'))
    	      u=c*60
    	      print('Gobi  amount is',u)
    	      print()
    	      d=int(input('enter Gobi rice   :'))
    	      v=d*50
    	      print('Gobi rice amount is',v)
    	      print()
    	      e=int(input('enter chapathi    :'))
    	      w=e*10
    	      print('chapthi amount is',w)
    	      print()
    	      f=int(input('enter porota      :'))
    	      x=f*15
    	      print('Porota amount is',x)
    	      p1=s+t+u+v+w+x
    	      print()
    	      print('The total Hotel bill is:','Rs.',p1)
    	      f=open("afternoon.txt",'w')
    	      f.write('Afternoon Lunch Bill is:\n')
    	      f.write(str(p1))
    	      f.write('\n')
    	      print('Thank you for eating lunch in my Hotel...')
    	      j=str(input('Do you have to pay tip to supplier yes (or) no:'))
    	      if j=='yes':
    	      	y=int(input('Allow pay tip to supplier:'))
    	      	print('supplier collected tip is',y,'Rupees')
    	      else:
    	      	print('Not allow to pay tip')
    	      print()
    	      z=int(input('How many stars you give for feedback:'))
    	      f.write('supplier collected tip is: ')
    	      f.write(str(y))
    	      f.close()
    	      if z==1:
    	      	print('One star: *')
    	      	print('very bad maintainence')
    	      elif z==2:
    	      	print('Two stars: **')
    	      	print('average maintainence')
    	      elif z==3:
    	      	print('Three stars: ***')
    	      	print('Good maintainence')
    	      elif z==4:
    	      	print('Four stars: ****')
    	      	print('very Good maintainence')
    	      elif z==5:
    	      	print('Five stars: *****')
    	      	print('very very Good maintainence.....Thank you')
    	      else:
    	      	print('stars valid for 0 to 5 only')
    	      	z1=int(input('Please enter a valid star:'))
    	      	if z1==1:
    	      		print('One star: *')
    	      		print('very bad maintainence')
    	      	elif z1==2:
    	      		print('Two stars: **')
    	      		print('average maintainence')
    	      	elif z1==3:
    	      		print('Three stars: ***')
    	      		print('Good maintaintence')
    	      	elif z1==4:
    	      		print('Four stars: ****')
    	      		print('very Good maintainence')
    	      	elif z1==5:
    	      		print('Five stars: *****')
    	      		print('very very Good maintainence.....Thank you')
print()
print('------Thank You to Come------')
print()
print('---------------Developed by Sai--------------')			             	    
    			         				
    									
	
		