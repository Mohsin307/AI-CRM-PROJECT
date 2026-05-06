from sqlalchemy import Column, Integer, String, Text
from db import Base

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    hcp_name = Column(String)
    summary = Column(Text)
    product = Column(String)
    sentiment = Column(String)
    follow_up = Column(String)