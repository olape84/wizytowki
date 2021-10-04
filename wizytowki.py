import random

class Card:
    def __init__ (self, name, surname, company_name, occupation, email):
        self.name=name
        self.surname=surname
        self.company_name=company_name
        self.occupation=occupation
        self.email=email
    
    def __str__(self) -> str:
        return f'{self.name} {self.surname} {self.email}'

    __repr__ = __str__
    
    def get_label_length (self):
        return len(self.name) + len(self.surname) +1

    @property  
    def label_length (self):
        return get_label_length
    
    def contact():
        random.choice([BaseContact, BusinessContact])() 

names= [
    Card(  
        name="Edward A.",
        surname="Copland", 
        company_name= "Food Barn", 
        occupation= "bill and account collector", 
        email= "EdwardACopland@armyspy.com "
        ),
    Card(
        name="Maria P.", 
        surname="Grant",
        company_name="ManCharm", 
        occupation="Foreign language interpreter", 
        email="MariaPGrant@teleworm.us"
        ),
    Card(
        name="Debra A.", 
        surname="Johnson", 
        company_name="Netstars Matrix Design",
        occupation="Meteorologist", 
        email="DebraAJohnson@rhyta.com "
        ),
    Card(
        name="Joseph D.", 
        surname="Hague", 
        company_name="Stratabiz",
        occupation= "Telecommunications equipment installer", 
        email="JosephDHague@jourrapide.com "
        ),
    Card(
        name="Ronald D.", 
        surname="Hogan", 
        company_name="Sky High Financial Advice",
        occupation= "Bench technician",
        email="RonaldDHogan@armyspy.com"
        )
        ]

for c in names:
    print(c.name, c.surname, c.email)
by_name = sorted(names,key=lambda c: c.name)
by_surname = sorted(names,key=lambda c: c.surname)
by_email = sorted(names,key=lambda c: c.email)
print(by_name)
print(by_surname)
print(by_email)
from faker import Faker
fake= Faker()
for i in range (10):
    print(fake.name())
    print(fake.email()) 
class BaseContact(Card):
    def __init__(self, private_phone_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.private_phone_number=private_phone_number
    print("Wybieram prywatny numer telefonu: ",  fake.phone_number(), "i kontaktuje się z ", fake.name())

class BusinessContact(Card):
    def __init__(self,business_phone_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.business_phone_number=business_phone_number
    print("Wybieram służbowy numer telefonu: ",  fake.phone_number(), "i kontaktuje się z ", fake.name())
    
Card.contact()
Card.label_length() 