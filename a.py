import mysql.connector

con=mysql.connector.connect(host='localhost',user='root',password='root')
cur=con.cursor()
cur.execute('create database if not exists items')
cur.execute('use items')
cur.execute('create table if not exist cs(sno int,products varchar(20),cost int)')
sql='select * from cs'
cur.execute(sql)
res=cur.fetchall()
if res==[]:
	cur.execute("insert into cs values(1,'cake',50)")
	cur.execute("insert into cs values(2,'pastry',20)")
	cur.execute("insert into cs values(3,'milk',60)")
	cur.execute("insert into cs values(4,'butter',20)")
	cur.execute("insert into cs values(5,'cheese',30)")
	con.commit()
	
cur.execute('create table if not exists vip(sno int, varieties varchar(20))')
sql='select * from vip'
cur.execute(sql)
res=cur.fetchall()
if res==[]:
	cur.execute('insert into vip values(1,"Vaniela")')
	cur.execute('insert into vip values(2,"Chocolate")')
	cur.execute('insert into vip values(3,"Strawberry")')
	cur.execute('insert into vip values(4,"Butter_Scotch")')
	con.commit()
	
cur.execute('create table if not exists worker(sno int,Name varchar(20),Salary int)')
sql='select * from worker'
cur.execute(sql)
res=cur.fetchall()
if res==[]:
	cur.execute('insert into worker values(1,"Anuj",12364')
	cur.execute('insert into worker values(2,"Rahul",12364')
	cur.execute('insert into worker values(3,"Mukesh",12364')
	cur.execute('insert into worker values(4,"Brijesh",12364')
	con.commit()
	
	
	
	
	
print('CLASS 12 CS PROJECT')
print('Welcome')
print('To')
print('BAKERY MANAGEMENT SYSTEM')
print('MADE BY: KUSHAL AGARWAL')
print('SUBMITTED TO:MR. BIRBAL JAT SIR')
print('Session: 2022-23')

ch=''
while ch!='N' or ch!='n':
	print('\n\n PLEASE CHOOSE\n1 FOR ADMIN\n3 For EXIT:\n')
	choice=int(input("ENTER YOUR CHOICE:"))
	if choice==3:
		break
	if choice==1:
		admin=input("USERNAME")
		password=int(input('ENTER PASSWORD:'))
		if password==1234:
			print('Hi Sir, You Logged in as Admin successfully')
			print('press 1 to add items in a shop')
			print('press 2 see items in the shop')
			print('press 3 to update cost of any item')
			print('press 4 to add varieties of cake in the shop')
			print('press 5 to add workers in the shop')
			print('press 6 to see workers')
			print('press 7 to update salary of any worker')
			
			c=int(input('Enter any choice'))
			if c==1:
				def add():
					sno=int(input('Enter Sno:'))
					product1=input('Enter product name:')
					cost=int(input('Enter the cost'))
					d1=(sno,product1,cost)
					s1'insert into cs values(%s,%s,%s)'
					cur.execute(s1,d1)
					con.commit()
					print('item added successfully')
				add()
			elif c==2:
				def items():
					print('Items in the shop')
					sql='select * from cs'
					cur.execute(sql)
					res=cur.fetchall()
					t=(['serial_no','products','cost'])
					for serial_no,products,cost in res:
						print(serial_no,':','\t',products,':\t\t','cost',cost)
				items()
			elif c==3:
				def money():
					sno=input('enter the sno of the product:')
					n_cost=input('enter the rupees to be added')
					cur.execute('update cs set cost=cost+'+n_cost+'where sno='+sno+';')
					con.commit()
					print('Table after updation')
					sq='select * from cs'
					cur.execute(sq)
					res=cur.fetchall()
					t=(['sno','products','cost'])
					for sno,products,cost in res:
						print(':','\t',products,':','\t','cost',cost)
				money()
			elif c==4:
					def variety():
						sno=input("Enter sno.:")
						varieties=input("Enter Variety:")
						d2=(sno,varieties)
						s2='insert into vip vapues(%s,%s)'
						cur.execute(s2,d2)
						con.commit()
					variety()
				elif c==5:
					def ad():
						sno=int(input("Enter Sno.:"))
						emp=input("Enter Name:")
						salary=int(input("Enter the salary"))
						dx=(sno,emp,salary)
						sy="insert into worker values(%s,%s,%s)"
						cur.execute(sy,dx)
						con.commit()
						print("Done")
					ad()
				elif c==6:
					def workers():
						print("Workers in the Shop:")
						sql="select * from worker"
						cur.execute(sql)
						res=cur.fetchall()
						t=(['serial_no','name','salary'])
						for serial_no,name,salary in res:
							print(serial_no,':',"\t",name,":",'cost',salary)
					worker()
				elif c==7:
					def up():
						print("Choose 1 to increase the salary:")
						print("Choose to decrease:")
						name=input("Enter the name of the employee")
						n_salary=input("Enter the rupees to be added")
						
						sig=int(input("Enter Choice(1/2):"))
						if sig==1:
							cur.execute("update worker set salary=salary+"+n_salary"where name="+name+':')
							con.commit()
							print("Table after updation")
							sq="select * from worker"
							cur.execute(sq)
							res=cur.fetchall()
							t=(['sno','name','salary'])
							for sno,name,salary in res:
								print(sno,":","\t",name,":","\t",salary)
						if sig==2:
							cur.execute("update worker set salary=salary-"+n_salary+"where name="+name+':')
							con.commit()
							print("Table after updation:")
							sq="select * from worker"
							cur.execute(sq)
							res=cur.fetchall()
							t=(['sno','name','salary'])
							for sno,name,salary in res:
								print(sno,":","\t",name,":","\t",salary)
					up()
				
				else:
						print("Sorey you have entered the wrong input")
				else:
						print("Wrong Password")
			elif choice==2:
					name=input("Enter Your Name")
					phone=int(input("Enter your Phone Number:"))
					print("Press 1 to see the menu",sep='.....')
					print("press 2 to order an item")
					c=int(input('Enter your choice:'))
					if c==1:
						def items():
							print("Items in the shop")
							sql="select * from cs"
							cur.execute(sql)
							res=cur.fetchall()
							t=(['serial_no','products','cost'])
							for serial_no,products,cost in res:
							 print(serial_no,":","\t",products,":","cost",cost)
						items()
					elif c==2:
							 print("What do you order")
							 sql="select * from cs"
							 cur.execute(sql)
							 res=cur.fetchall()
							t=(['serial_no','products','cost'])
							for serial_no,products,cost in res:
							 print(serial_no,":","\t",products,":","cost",cost)
							sql="select sno from cs"
							cur.execute(sql)
							res=cur.fetchall()
							print(res)
							l=[]
							for i in range(len(res)):
							 l.append(res[i][0])
							 
							d=int(input("Enter your serial no of the item to buy"))
							if d==1:
							 def items():
							 	print("Which cake do you want")
							 	kl="select * from vip"
							 	cur.execute(kl)
							 	srh=cur.fetchall()
							 	f=(["sno","varieties"])
							 	for sno,varieties in srh:
							 		print(sno,":","\t\t",varieties)
							 	print("Which cake do you want")
							 	ck=int(input("Enter Choice:"))
							 	if ck==1:
							 		print("How much Vaniella Cake Quantity you want?")
							 		qty=int(input('Enter qty.'))
							 		print("You Ordered Succesfully")
							 		cur.execute("select *  from cs where product='cake'")
							 		for i in cur:
							 			c=i[2]
							 			con.commit()
							 		print("Total Amount:",qty*c)
							 		print("\n")
							 		print("Your Bill")
							 		print("Customers Name:",name)
							 		print("Contact no.:",phone)
							 		print("Cake type:Vaniella")
							 		print("No. of cakes:",qty)
							 		print("Total amount",qty*c)
							 		print("Thank you for ordering the item")
							 		print("Date:"datetime.now())
							 	if ck==2:
							 		print("How much Chocalte cake Quantity you want?")
							 		qty=int(input('Enter qty.'))
							 		print("You Ordered Succesfully")
							 		cur.execute("select *  from cs where product='cake'")
							 		for i in cur:
							 			L=i[2]
							 			con.commit()
							 		print("Total Amount:",qty*L)
							 		print("\n")
							 		print("Your Bill")
							 		print("Customers Name:",name)
							 		print("Contact no.:",phone)
							 		print("Cake type:Chocolate")
							 		print("No. of cakes:",qty)
							 		print("Total amount",qty*L)
							 		print("Thank you for ordering the item")
							 		print("Date:"datetime.now())
							 	if ck==3:
							 		
							 		print("How much Strawberry cake Quantity you want?")
							 		qty=int(input('Enter qty.'))
							 		print("You Ordered Succesfully")
							 		cur.execute("select *  from cs where product='cake'")
							 		for i in cur:
							 			N=i[2]
							 			con.commit()
							 		print("Total Amount:",qty*N)
							 		print("\n")
							 		print("Your Bill")
							 		print("Customers Name:",name)
							 		print("Contact no.:",phone)
							 		print("Cake type:Strawberry")
							 		print("No. of cakes:",qty)
							 		print("Total amount",qty*N)
							 		print("Thank you for ordering the item")
							 		print("Date:"datetime.now())
							 	if ck==4:
							 		print("How much Butterscotch Cake Quantity you want?")
							 		qty=int(input('Enter qty.'))
							 		print("You Ordered Succesfully")
							 		cur.execute("select *  from cs where product='cake'")
							 		for i in cur:
							 			M=i[2]
							 			con.commit()
							 		print("Total Amount:",qty*M)
							 		print("\n")
							 		print("Your Bill")
							 		print("Customers Name:",name)
							 		print("Contact no.:",phone)
							 		print("Cake type:Vaniella")
							 		print("No. of cakes:",qty)
							 		print("Total amount",qty*M)
							 		print("Thank you for ordering the item")
							 		print("Date:"datetime.now())
							 items()
							elif d==2:
								print("How much Pastry you want?")
							 	qty=int(input('Enter qty.'))
							 	print("You Ordered Succesfully")
							 	cur.execute("select *  from cs where product='pastry'")
							 	for i in cur:
							 			c=i[2]
							 			con.commit()
							       print("Total Amount:",qty*c)
	                             print("\n")
							 	print("Your Bill")
							 	print("Customers Name:",name)
							 	print("Contact no.:",phone)
							 	print("Cake type:Vaniella")
							 	print("No. of cakes:",qty)
							 	print("Total amount",qty*c)
							 	print("Thank you for ordering the item")
							 	print("Date:"datetime.now())
							 elif d==3:
							 	print("How much litre of milk Quantity you want?")
							 	qty=int(input('Enter qty.'))
							 	print("You Ordered Succesfully")
							 	cur.execute("select *  from cs where product='milk'")
							 	for i in cur:
							 			c=i[2]
							 			con.commit()
							 	print("Total Amount:",qty*c)
							 	print("\n")
							 	print("Your Bill")
							 	print("Customers Name:",name)
							 	print("Contact no.:",phone)
							 	print("Milk")
							 	print("No. of cakes:",qty)
							 	print("Total amount",qty*c)
							 	print("Thank you for ordering the item")
							 	print("Date:"datetime.now())
							 if d==4:
							 	print("How much Quantity of butter you want?")
							 	qty=int(input('Enter qty.'))
							 	print("You Ordered Succesfully")
							 	cur.execute("select *  from cs where product='butter'")
							 	for i in cur:
							 			c=i[2]
							 			con.commit()
							 	print("Total Amount:",qty*c)
							 	print("\n")
							 	print("Your Bill")
							 	print("Customers Name:",name)
							 	print("Contact no.:",phone)
							 	print("Cake type:Vaniella")
							 	print("No. of cakes:",qty)
							 	print("Total amount",qty*c)
							 	print("Thank you for ordering the item")
							 	print("Date:"datetime.now())
							 if d==5:
							 		print("How much Quantity of cheese you want?")
							 		qty=int(input('Enter qty.'))
							 		print("You Ordered Succesfully")
							 		cur.execute("select *  from cs where product='cheese'")
							 		for i in cur:
							 			c=i[2]
							 			con.commit()
							 		print("Total Amount:",qty*c)
							 		print("\n")
							 		print("Your Bill")
							 		print("Customers Name:",name)
							 		print("Contact no.:",phone)
							 		print("Cheese")
							 		print("No. of cakes:",qty)
							 		print("Total amount",qty*c)
							 		print("Thank you for ordering the item")
							 		print("Date:"datetime.now())
							 	elif d in l:
							 		qty=int(input("Enter qty:"))
							 		print("you have succesfully order your selected item")
							 		cur.execute("select * from cs where sno="+str(d))
							 		for i cur:
							 			L=i[2]
							 		print("Total Amount",qty*L)
							 		print("\n")
							 		print("Your Bill")
							 		print("Customers name:",name)
							 		print("Mobile no,:",phone)
							 		print("Quantity",qty)
							 		print("Total amount",qty*)
							 		print("Thank you for ordering the item")
							 		print("Date:"datetime.now())
							 	else:
							 		print("Wrong Input")
							 else:
							 	print("Wrong Password")
ch=input("Do you want to continue(y/n)")
if ch=='n' or ch=="N":
			exit()
			
			
			
			
							 	
			
								
			
			
			
							 		
							 		
							 
							 
							 
							 
							 
							 
							 
					
					
					
					
				
					
			
	
	
	
	




