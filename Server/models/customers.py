from app import db

class Customer(db.Model):
  __tablename__='customers'
  customer_id = db.Column('customer_id',db.Integer,primary_key=True)
  customer_name = db.Column('customer_name', db.String())
  
