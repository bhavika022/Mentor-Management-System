from tkinter import *
import os
from b import Session, Login, Schedule, Update_, Request
from time_ import DateEntry

session = Session()
creds = 'tempfile.temp'

def Signup(): 			#function for signup page
	global pwordE 
	global nameE
	global studentE
	global roots
	
	roots = Tk() 
	roots.title('Signup') 
	roots.geometry("1900x1500")

	intruction = Label(roots, text='Please Enter new Credidentials\n') 
	intruction.grid(row=0, column=0, sticky=E)
	intruction.config(font=("Courier", 44))

	nameL = Label(roots, text='New Username: ')
	pwordL = Label(roots, text='New Password: ') 
	nameL.grid(row=1, column=0, sticky=W) 
	pwordL.grid(row=3, column=0, sticky=W)
	studentL = Label(roots, text='Admin/Student: ') 
	studentL.grid(row=5, column=0, sticky=W)
	nameL.config(font=("Courier", 44))
	pwordL.config(font=("Courier", 44))
	studentL.config(font=("Courier", 44))

	emptyL = Label(roots, text=' ')
	emptyL.grid(row=2, sticky=W)
	emptyL1 = Label(roots, text=' ')
	emptyL1.grid(row=4, sticky=W)
	emptyL2 = Label(roots, text=' ')
	emptyL2.grid(row=6, sticky=W)
	emptyL2.config(font=("Courier", 44))	

	nameE = Entry(roots) 
	pwordE = Entry(roots, show='*')
	nameE.grid(row=1,column=1)
	pwordE.grid(row=3, column=1) 
	studentE = Entry(roots)
	studentE.grid(row=5,column=1)
	nameE.config(font=("Courier", 44))
	pwordE.config(font=("Courier", 44))
	studentE.config(font=("Courier", 44))

	signupButton = Button(roots, text='Signup', command=FSSignup)
	signupButton.grid(column=1,columnspan=2, sticky=W)
	signupButton.config(font=("Courier", 44))
	roots.mainloop() 

def FSSignup():			#function to store the new entry (new user) in the database
	user = Login(nameE.get(), pwordE.get(), studentE.get())
	session.add(user)
	session.commit()
	LoginPage() 

def LoginPage():		#to login into the function
	global nameEL
	global pwordEL
	global studentEL 
	global rootA

	rootA = Tk()
	rootA.title('Login')
	rootA.geometry("1900x1500") 

	intruction = Label(rootA, text='Please Login\n')
	intruction.grid(sticky=E)
	intruction.config(font=("Courier", 38))	

	nameL = Label(rootA, text='Username: ') 
	pwordL = Label(rootA, text='Password: ')
	nameL.grid(row=1, column=1, sticky=W)
	nameL.config(font=("Courier", 44))
	pwordL.config(font=("Courier", 44))
	pwordL.grid(row=3, column=1, sticky=W)
	studL = Label(rootA, text='Admin/Student: ') 
	studL.grid(row=5, column=1, sticky=W)
	studL.config(font=("Courier", 44))

	emptyL = Label(rootA, text=' ')
	emptyL.grid(row=2, sticky=W)
	emptyL1 = Label(rootA, text=' ')
	emptyL1.grid(row=4, sticky=W)
	emptyL2 = Label(rootA, text=' ')
	emptyL2.grid(row=6, sticky=W)
	emptyL2.config(font=("Courier", 40))
	emptyL3 = Label(rootA, text=' ')
	emptyL3.grid(row=8, sticky=W)
	emptyL4 = Label(rootA, text=' ')
	emptyL4.grid(row=10, sticky=W)	

	nameEL = Entry(rootA)
	nameEL.config(font=("Courier", 44)) 
	pwordEL = Entry(rootA, show='*')
	pwordEL.config(font=("Courier", 44))
	nameEL.grid(row=1, column=2)
	pwordEL.grid(row=3, column=2)
	studentEL = Entry(rootA)
	studentEL.grid(row=5,column=2)
	studentEL.config(font=("Courier", 44))

	loginB = Button(rootA, text='   Login   ', command=CheckLogin) 
	loginB.grid(row=7,column=2,columnspan=4, sticky=W)
	loginB.config(font=("Courier", 44))

	signup1B = Button(rootA, text='   Signup  ', command=Signup) 
	signup1B.grid(row=9,column=2,columnspan=4, sticky=W)
	signup1B.config(font=("Courier", 44))

	rmuser = Button(rootA, text='Delete User', fg='red', command=lambda: DelUser(nameEL)) 
	rmuser.grid(row=11,column=2,columnspan=4, sticky=W)
	rmuser.config(font=("Courier", 44))
	
	rootA.mainloop()

def CheckLogin():		# to validate the login
	
	
	
	users = session.query(Login).filter(Login.username == nameEL.get()).all()
	if len(users) > 0:
		user = users[0]
		if studentEL.get() == 'Admin':		#to check if whether the user that just logged in a mentor or a student
			if nameEL.get() == user.username and pwordEL.get() == user.password and studentEL.get() == user.admin:
				
					
				r = Tk()
				r.title('Home')
				r.geometry("1900x1500")
				v=IntVar()
				
				emptyL = Label(r, text=' ')
				emptyL.grid(row=2, sticky=W)
				emptyL.config(font=("Courier", 44))
				emptyL1 = Label(r, text=' ')
				emptyL1.grid(row=4, sticky=W)
				emptyL2 = Label(r, text=' ')
				emptyL2.grid(row=6, sticky=W)
				emptyL3 = Label(r, text=' ')
				emptyL3.grid(row=8, sticky=W)
				emptyL4 = Label(r, text=' ')
				emptyL4.grid(row=10, sticky=W)
			
				rlbl = Label(r, text='\n Enter choice')
				rlbl.grid(row=1,column=0)
				rlbl.config(font=("Courier", 44))
				scheduleButton = Button(r, text='  Call Meeting  ', command=EnterDateTime)
				scheduleButton.grid(row=3,column=4,columnspan=7, sticky=W)
				scheduleButton.config(font=("Courier", 44))
			
				ConclusionButton = Button(r, text=' Update Records ', command=EnterConclusion)
				ConclusionButton.grid(row=5,column=4,columnspan=7, sticky=W)
				ConclusionButton.config(font=("Courier", 44))
			
				
				
				RButton = Button(r, text=' Requests ', command=stu_req)
				RButton.grid(row=7,column=4,columnspan=7, sticky=W)
				RButton.config(font=("Courier", 44))

				HistoryButton = Button(r, text='  View History  ', command=meet_history)
				HistoryButton.grid(row=9,column=4,columnspan=7, sticky=W)
				HistoryButton.config(font=("Courier", 44))
	
				r.mainloop()
		
			else:
				r = Tk()
				r.title('D:')
				r.geometry('150x50')
				rlbl = Label(r, text='\n[!] Invalid Login')
				rlbl.pack()
				r.mainloop()

		elif studentEL.get() == 'Student':		#to check if whether the user that just logged in a mentor or a student
			if nameEL.get() == user.username and pwordEL.get() == user.password and studentEL.get() == user.admin:
		
				r = Tk()
				r.title('Home')
				r.geometry("1900x1500")
				v=IntVar()
			
				rlbl = Label(r, text='Please Enter Choice')
				rlbl.grid(row=0,column=0,sticky=E)

				rlbl.config(font=("Courier", 44))
				
				reqButton = Button(r, text='Request for Meeting', command=Req)
				reqButton.grid(row=3,column=1,columnspan=2, sticky=W)
				
				emptyL = Label(r, text=' ')
				emptyL.grid(row=1, sticky=W)
				emptyL.config(font=("Courier", 35))

				emptyL1 = Label(r, text=' ')
				emptyL1.grid(row=2, sticky=W)
				emptyL1.config(font=("Courier", 35))

				emptyL2 = Label(r, text=' ')
				emptyL2.grid(row=4, sticky=W)
				emptyL2.config(font=("Courier", 35))

				emptyL2 = Label(r, text=' ')
				emptyL2.grid(row=6, sticky=W)
				emptyL2.config(font=("Courier", 35))
				
				notificationButton = Button(r, text=' See Notifications ', command=Notes)
				notificationButton.grid(row=5,column=1,columnspan=2, sticky=W)
				
				reqButton.config(font=("Courier", 44))
				notificationButton.config(font=("Courier", 44))

				LogOutButton = Button(r, text='      Log Out      ', fg='red',command=ExitAll)
				LogOutButton.grid(row=7,column=1,columnspan=2, sticky=W)
				LogOutButton.config(font=("Courier", 44))

				r.mainloop()


			else:
				r = Tk()
				r.title('D:')
				r.geometry('150x50')
				rlbl = Label(r, text='\n[!] Invalid Login')
				rlbl.pack()
				r.mainloop()

	else:
		r = Tk()
		r.title('D:')
		r.geometry('150x50')
		rlbl = Label(r, text='\n[!] Invalid Login')
		rlbl.pack()
		r.mainloop()

def EnterDateTime():			#to call for a new meeting
	
	
	r1 = Tk()
	r1.title('Enter Date and Topic')
	r1.geometry("1900x1500")
	
	namL1 = Label(r1, text='Schedule\n') 
	namL1.grid(row=0,column=0,sticky=W)
	namL1.config(font=("Courier", 44))

	namL = Label(r1, text='Enter date:') 
	namL.grid(row=1,column=0,sticky=W)
	namL.config(font=("Courier", 44))
	d = DateEntry(r1)
	d.grid(row=1,column=1,sticky=W)

	emptyL2 = Label(r1, text=' ')
	emptyL2.grid(row=2,column=0, sticky=W)
	emptyL2.config(font=("Courier", 35))

	nameL = Label(r1, text='Enter Agenda:') 
	nameL.grid(row=3,column=0,sticky=W)
	nameL.config(font=("Courier", 44))
	nameE = Entry(r1) 
	nameE.grid(row=3,column=1)
	nameE.config(font=("Courier", 44))	
	
	emptyL2 = Label(r1, text=' ')
	emptyL2.grid(row=4,column=0, sticky=W)
	emptyL2.config(font=("Courier", 35))

	okButton = Button(r1, text='   OK   ', command=lambda: Exit_(d,nameE))
	okButton.grid(row=5,column=1, sticky=W)
	okButton.config(font=("Courier", 44))
	
	r1.mainloop()


def EnterConclusion():			#to maintain the records of the meeting that has alredy taken place

	r3 = Tk()
	r3.title('Enter Conclusion')
	r3.geometry("1900x1500")

	rlbl = Label(r3, text='Enter Updates:\n')
	rlbl.grid(row=0,column=0,sticky=E)
	rlbl.config(font=("Courier", 44))
	
	
	dateL = Label(r3, text='Enter date: ') 
	dateL.grid(row=1, column=0, sticky=W)
	dateL.config(font=("Courier", 44))
	d = DateEntry(r3)
	d.grid(row=1, column=1, sticky=W)
	dateL.config(font=("Courier", 44))

	empty2 = Label(r3, text=' ')
	empty2.grid(row=2,column=0)
	empty2.config(font=("Courier", 30))
	
	studL = Label(r3, text='No. of students present:')
	studL.grid(row=3, column=0, sticky=W)
	studE = Entry(r3) 
	studE.grid(row=3,column=1)
	studL.config(font=("Courier", 44))
	studE.config(font=("Courier", 44))
	
	empty3 = Label(r3, text=' ')
	empty3.grid(row=4,column=0)
	empty3.config(font=("Courier", 30))	

	empty4 = Label(r3, text=' ')
	empty4.grid(row=6,column=0)
	empty4.config(font=("Courier", 30))	
	
	topicL = Label(r3, text='Topic Disscussed:')
	topicL.grid(row=5, column=0, sticky=W)
	topicE = Entry(r3) 
	topicE.grid(row=5,column=1)
	
	topicL.config(font=("Courier", 44))
	topicE.config(font=("Courier", 44))
	
	okButton = Button(r3, text='   OK   ', command=lambda: Exit2_(d,studE,topicE,g=None))
	okButton.grid(row=7,column=1,columnspan=2, sticky=W)
	okButton.config(font=("Courier", 44))
	
	r3.mainloop()

def meet_history ():			#displaying records from database of the meetings that has already takken place

	r3 = Tk()
	r3.title('History')
	r3.geometry("1900x1500")

	updateEls = []
	updates = session.query(Update_).all()
	topicL = Label(r3, text='Date')
	topicL.grid(row=0,column=1)
	topicL1 = Label(r3, text='Attendence')
	topicL1.grid(row=0,column=3)
	topicL2 = Label(r3, text='Topic')
	topicL2.grid(row=0,column=5)
	topicL.config(font=("Courier", 20))
	topicL1.config(font=("Courier", 20))
	topicL2.config(font=("Courier", 20))
	empty1 = Label(r3, text=' ')
	empty2 = Label(r3, text=' ')
	empty1.grid(column=2)
	empty2.grid(column=4)
	for x in updates :
		c=1
		str_ = str(x.date)
		str_1= str(x.number_of_presentees)
		str_2= str(x.topic)
		print(str_)
		z = Label(r3, text=str_)	
		z.grid(column=1)
		z.config(font=("Courier", 20))
		updateEls.append(z)
		z1 = Label(r3, text=str_1)	
		z1.grid(column=3)
		z1.config(font=("Courier", 20))
		updateEls.append(z1)
		z2 = Label(r3, text=str_2)	
		z2.grid(column=5)
		z2.config(font=("Courier", 20))
		++c
		updateEls.append(z2)
	
	empty2 = Label(r3, text=' ')
	empty2.grid(column=1,columnspan=2)
	empty2.config(font=("Courier",20))
	
	HomeButton = Button(r3, text='   Home    ',fg='red', command=CheckLogin)
	HomeButton.grid(column=1,columnspan=2, sticky=W)
	HomeButton.config(font=("Courier", 20))
	
	empty1 = Label(r3, text=' ')
	empty1.grid(column=1,columnspan=2)
	empty1.config(font=("Courier",20))

	LogOutButton = Button(r3, text='  Log Out  ', fg='red',command=ExitAll)
	LogOutButton.grid(column=1,columnspan=2, sticky=W)
	LogOutButton.config(font=("Courier", 20))

	r3.mainloop()

def stu_req():		#student requesting the mentor for a meeting

	r3 = Tk()
	r3.title('Requests')
	r3.geometry("1900x1500")

	nL = Label(r3, text='             \n')
	nL.grid(row=0,column=0)
	nL.config(font=("Courier", 20))

	nameL = Label(r3, text='Enter Name:')
	nameL.grid(row=1,column=1)
	nameL.config(font=("Courier", 44))

	nameE = Entry(r3) 
	nameE.grid(row=1,column=2)
	nameE.config(font=("Courier", 44))
	
	nL1 = Label(r3, text='             \n')
	nL1.grid(row=2,column=0,columnspan=2)
	nL1.config(font=("Courier", 20))

	okButton = Button(r3, text='   OK   ', command=lambda: namecon(nameE))
	okButton.grid(column=2, sticky=W)
	okButton.config(font=("Courier", 44))

	r3.mainloop()

def namecon(a):			#displaying requests in the mentors see requests page

	r3 = Tk()
	r3.title('Requests')
	r3.geometry("1900x1500")
	
	topicL = Label(r3, text='Date')
	topicL.grid(row=0,column=1)
	topicL1 = Label(r3, text='topic')
	topicL1.grid(row=0,column=2)
	topicL.config(font=("Courier", 35))
	topicL1.config(font=("Courier", 35))

	usersEle = []
	users2 = session.query(Request).filter(Request.admin == a.get()).all()
	if len(users2) > 0:
		for x in users2:
			st_ = str(x.date)
			st_1 = str(x.topic)
			print(st_)
			q = Label(r3, text=st_)
			z = Label(r3, text=st_1)
			z.grid(column=1)
			z.config(font=("Courier", 35))
			q.config(font=("Courier", 35))
			q.grid(column=2)
			usersEle.append(q)
			usersEle.append(z)
		session.query(Request).filter(Request.admin == a.get()).update({"accept":1})
		session.commit()
	
		
	SButton = Button(r3, text='  Schedule ',fg='red', command=EnterDateTime)
	SButton.grid(column=1, sticky=W)
	SButton.config(font=("Courier", 35))
	
	empty1 = Label(r3, text=' ')
	empty1.grid(column=1,columnspan=2)
	empty1.config(font=("Courier",20))

	HomeButton = Button(r3, text='   Home    ',fg='red', command=CheckLogin)
	HomeButton.grid(column=1)
	HomeButton.config(font=("Courier", 35))
	
	empty1 = Label(r3, text=' ')
	empty1.grid(column=1,columnspan=2)
	empty1.config(font=("Courier",20))

	LogOutButton = Button(r3, text='  Log Out  ', fg='red',command=ExitAll)
	LogOutButton.grid(column=1)
	LogOutButton.config(font=("Courier", 35))

	r3.mainloop()

	

	

def Notes():		#to display notifications on the student page
	
	r3 = Tk()
	r3.title('Notifications')
	r3.geometry("1900x1500")

	usersEle = []
	users2 = session.query(Schedule).filter(Schedule.seen == 0).all()
	if len(users2) > 0:
		for x in users2:
			st_ = str(x.date)
			st_1 = str(x.topic)
			print(st_)
			q = Label(r3, text=st_)
			z = Label(r3, text=st_1)
			z.grid(column=1)
			q.grid(column=2)
			z.config(font=("Courier",25))
			q.config(font=("Courier",25))
			usersEle.append(q)
			usersEle.append(z)
		session.query(Schedule).update({"seen":0})
		session.commit()
	else:
		nameL = Label(r3, text='No new notifications ')
		nameL.grid(column=1)
		nameL.config(font=("Courier",30))
	
	empty1 = Label(r3, text=' ')
	empty1.grid(column=1,columnspan=2)
	empty1.config(font=("Courier",20))

	HomeButton = Button(r3, text='   Home    ',fg='red', command=CheckLogin)
	HomeButton.grid(column=1)
	HomeButton.config(font=("Courier", 35))
	
	empty1 = Label(r3, text=' ')
	empty1.grid(column=1,columnspan=2)
	empty1.config(font=("Courier",20))

	LogOutButton = Button(r3, text='  Log Out  ', fg='red',command=ExitAll)
	LogOutButton.grid(column=1)
	LogOutButton.config(font=("Courier", 35))
	
	r3.mainloop()

def Req():
	r3 = Tk()
	r3.title('Request')
	r3.geometry("1900x1500")

	rlbl = Label(r3, text='Enter Details')
	rlbl.grid(row=0,column=0,sticky=E)
	rlbl.config(font=("Courier", 44))
	
	topicL = Label(r3, text='Date:  ')
	topicL.grid(row=3,column=1,sticky=W)
	topicL1 = Label(r3, text='Topic: ')
	topicL1.grid(row=5,column=1,sticky=W)
	topicL2 = Label(r3, text='Mentor:')
	topicL2.grid(row=7,column=1,sticky=W)

	empty = Label(r3, text=' ')
	empty.grid(row=1,column=1,columnspan=2)
	empty.config(font=("Courier",20))

	empty1 = Label(r3, text=' ')
	empty1.grid(row=2,column=1,columnspan=2)
	empty1.config(font=("Courier",20))

	empty2 = Label(r3, text=' ')
	empty2.grid(row=4,column=1,columnspan=2)
	empty2.config(font=("Courier",20))

	empty3 = Label(r3, text=' ')
	empty3.grid(column=1,columnspan=2)
	empty3.config(font=("Courier",20))

	empty4 = Label(r3, text=' ')
	empty4.grid(row=6,column=1,columnspan=2)
	empty4.config(font=("Courier",20))

	topicL.config(font=("Courier", 44))
	topicL1.config(font=("Courier", 44))
	topicL2.config(font=("Courier", 44))
	
	studE = Entry(r3)
	studE1 = Entry(r3)
	
	studE.grid(row=5,column=2)
	studE1.grid(row=7,column=2)

	studE.config(font=("Courier", 44))
	studE1.config(font=("Courier", 44))	
	
	d = DateEntry(r3)
	d.grid(row=3,column=2)

	empty5 = Label(r3, text=' ')
	empty5.grid(row=8,column=1,columnspan=2)
	empty5.config(font=("Courier",20))

	okButton = Button(r3, text='   OK   ', command=lambda: Exit3_(d,studE,studE1))
	okButton.grid(row=9,column=1,columnspan=2)
	okButton.config(font=("Courier", 44))

	r3.mainloop()
	
	
	
	

def Exit_(d,d1):		#saving data in database and exitiing 

	
	r3 = Tk()
	r3.title('Exit')
	r3.geometry("1900x1500")
	
	user = Schedule(d.get(),d1.get())
	session.add(user)
	session.commit()
	
	users1 = session.query(Schedule).filter(Schedule.topic == d1.get()).all()
	print (users1)
	for x in users1:
		print(x.topic)
	session.query(Schedule).filter(Schedule.topic == d1.get()).update({"seen":1})
	session.commit()

	empty5 = Label(r3, text='                                                ')
	empty5.grid(row=0,column=0)
	empty5.config(font=("Courier",20))

	LogOutButton = Button(r3, text='Log Out', command=LoginPage)
	LogOutButton.grid(row=3,column=1)
	LogOutButton.config(font=("Courier",44))

	empty6 = Label(r3, text=' ')
	empty6.grid(row=2,column=0)
	empty6.config(font=("Courier",20))

	HomeButton = Button(r3, text='  Home  ', command=CheckLogin)
	HomeButton.grid(row=1,column=1)
	HomeButton.config(font=("Courier",44))
	
	r3.mainloop()
	
def Exit1_(d,d1):		#saving data in database and exitiing

	r3 = Tk()
	r3.title('Exit')
	r3.geometry("1900x1500")

	user = Agenda(d.get())
	session.add(user)
	session.commit()

	empty5 = Label(r3, text='                                                ')
	empty5.grid(row=0,column=0)
	empty5.config(font=("Courier",20))

	LogOutButton = Button(r3, text='Log Out', command=LoginPage)
	LogOutButton.grid(row=3,column=1)
	LogOutButton.config(font=("Courier",44))

	empty6 = Label(r3, text=' ')
	empty6.grid(row=2,column=0)
	empty6.config(font=("Courier",20))

	HomeButton = Button(r3, text='  Home  ', command=CheckLogin)
	HomeButton.grid(row=1,column=1)
	HomeButton.config(font=("Courier",44))

	r3.mainloop()
	
def Exit2_(d,e,f,g):		#saving data in database and exitiing

	r3 = Tk()
	r3.title('Exit')
	r3.geometry("1900x1500")
	
	user = Update_(d.get(),e.get(),f.get())
	session.add(user)
	session.commit()

	empty5 = Label(r3, text='                                                ')
	empty5.grid(row=0,column=0)
	empty5.config(font=("Courier",20))

	LogOutButton = Button(r3, text='Log Out', command=LoginPage)
	LogOutButton.grid(row=3,column=1)
	LogOutButton.config(font=("Courier",44))

	empty6 = Label(r3, text=' ')
	empty6.grid(row=2,column=0)
	empty6.config(font=("Courier",20))

	HomeButton = Button(r3, text='  Home  ', command=CheckLogin)
	HomeButton.grid(row=1,column=1)
	HomeButton.config(font=("Courier",44))

	r3.mainloop()

def Exit3_(d,t,a):			#saving data in database and exitiing
	
	r3 = Tk()
	r3.title('Exit')
	r3.geometry('1900x1500')

	user_ = Request(d.get(),t.get(),a.get())
	session.add(user_)
	session.commit()

	empty5 = Label(r3, text='                                                ')
	empty5.grid(row=0,column=0)
	empty5.config(font=("Courier",20))

	LogOutButton = Button(r3, text='Log Out', command=LoginPage)
	LogOutButton.grid(row=3,column=1)
	LogOutButton.config(font=("Courier",44))

	empty6 = Label(r3, text=' ')
	empty6.grid(row=2,column=0)
	empty6.config(font=("Courier",20))

	HomeButton = Button(r3, text='  Home  ', command=CheckLogin)
	HomeButton.grid(row=1,column=1)
	HomeButton.config(font=("Courier",44))
	
	r3.mainloop()

def ExitAll():

	exit(0)

def DelUser(nameE):		#function to delete a user from the the database
	users = session.query(Login).filter(Login.username == nameE.get()).all()
	if len(users) > 0:
		user = users[0]
		session.delete(user)
		session.commit()
	LoginPage() 
	
LoginPage()






























