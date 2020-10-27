#!/usr/bin/env python
# coding: utf-8

# In[3]:


from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import sqlalchemy
sqlalchemy.__version__


# In[4]:


engine = create_engine('sqlite:///:memory:', echo=True)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name, self.fullname, self.nickname)


# In[5]:


User.__table__


# In[6]:


Base.metadata.create_all(engine)


# In[7]:


ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')


# In[8]:


ed_user.name


# In[9]:


ed_user.nickname


# In[10]:


str(ed_user.id)


# In[12]:


ed_user


# In[13]:


Session = sessionmaker(bind=engine)


# In[14]:


session = Session()
session.add(ed_user)


# In[15]:


our_user = session.query(User).filter_by(name='ed').first()
our_user


# In[16]:


ed_user is our_user


# In[17]:


our_user


# In[18]:


ed_user


# In[19]:


session.add_all([
    User(name='wendy', fullname='Wendy Williams', nickname='windy'),
    User(name='mary', fullname='Mary Contrary', nickname='mary'),
    User(name='fred', fullname='Fred Flintstone', nickname='freddy')])


# In[20]:


ed_user.nickname = 'eddie'


# In[21]:


session.dirty


# In[22]:


session.new


# In[23]:


session.commit()


# In[24]:


ed_user.id


# In[32]:


session.query(User).all()


# In[33]:


ed_user.name = 'Edwardo'


# In[34]:


fake_user = User(name='fakeuser', fullname='Invalid', nickname='12345')
session.add(fake_user)


# In[35]:


session.query(User).all()


# In[36]:


session.query(User).filter(User.name.in_(['Edwardo', 'fakeuser'])).all()


# In[37]:


session.rollback()


# In[38]:


ed_user.name


# In[39]:


fake_user in session


# In[40]:


session.query(User).all()


# In[41]:


for instance in session.query(User).order_by(User.id):
    print(instance.name, instance.fullname, instance.id)


# In[42]:


for name, fullname in session.query(User.name, User.fullname):
    print(name, fullname)


# In[ ]:
