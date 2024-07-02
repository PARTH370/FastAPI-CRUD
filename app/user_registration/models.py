from sqlalchemy import Column, Integer, String, Date, func, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, nullable=True, comment="Name of the company associated with the user")
    first_name = Column(String, index=True, nullable=True, comment="First name of the user")
    last_name = Column(String, index=True, nullable=True, comment="Last name of the user")
    email = Column(String, index=True, nullable=True, comment="Email address of the user")
    password = Column(String, nullable=True, comment="Password of the user")
    mobile = Column(String, nullable=True, comment="Mobile number of the user")
    hashtag = Column(String, nullable=True, comment="Hashtag associated with the user")
    date_of_birth = Column(Date, nullable=True, comment="Date of birth of the user")
    created_at = Column(DateTime, default=func.now(), nullable=True, comment="Timestamp of when the user was created")
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=True, comment="Timestamp of when the user was last updated")
    is_active = Column(Integer, default=1, nullable=True, comment="Flag to indicate if the user is active or not")