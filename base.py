from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, Float, Date , Time

engine = create_engine("mysql+pymysql://root:987654321@192.168.43.83/cse2")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Login(Base):
	__tablename__ = 'login'
	username = Column(String, primary_key=True)
	password = Column(String)
	admin = Column(String)
	def __init__(self, uname, passw, ad):
		self.username = uname
		self.password = passw
		self.admin = ad

#class Login_admin(Base):
#	__tablename__ = 'login_admin'
#	username_admin = Column(String, primary_key=True)
#	password_admin = Column(String)
#	def __init__(self, uname, passw):
#		self.username_admin = uname
#		self.password_admin = passw
		
		
#isha = Login('lautrey', '1234')
#session.add(isha)



class Schedule(Base):
	__tablename__ = 'schedule'
	date = Column(Date, primary_key=True)
	time = Column(Time)
	topic = Column(String)
	seen = Column(Integer,default=0)
	def __init__(self, da, top, ti=None):
		self.date = da
		self.topic = top
		self.time = None

class Request(Base):
	__tablename__ = 'request'
	date = Column(Date, primary_key=True)
	topic = Column(String)
	accept = Column(Integer,default=0)
	admin = Column(String)
	def __init__(self, dd, tt, aa):
		self.date = dd
		self.topic = tt
		self.admin = aa


	#sch = Schedule( '2018-09-12' , '12:46:09')
	#session.add(sch)


#class Agenda(Base):
#	__tablename__ = 'agenda'
#	topic = Column(String, primary_key=True)
#	def __init__(self, top):
#		self.topic = top
	



class Update_(Base):
	__tablename__ = 'update_'
	date = Column(Date, primary_key=True)
	time = Column(Time)
	number_of_presentees = Column(Float)
	topic = Column(String)
	conclusion = Column(String)
	def __init__(self, da, nop, top, ti=None, cncl=None):
		self.date = da
		self.time = None
		self.number_of_presentees = nop
		self.topic = top
		self.conclusion = cncl





session.commit()
session.close()


