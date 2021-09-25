class Card:
    def __init__ (self, name, surname, company_name, occupation, email):
        self.name=name
        self.surname=surname
        self.company_name=company_name
        self.occupation=occupation
        self.email=email
    
    def __str__(self) -> str:
        return f'{self.name} {self.surname} {self.email}'

    @property #nie wiem czemu ale ten atrybut nie chce działać. robiłam na czuja - nie rozumiem całej tej koncepcji 
    def label_length (self):
        return self.label_length
    
    @label_length.setter
    def label_length (self):
        return len(fake.name())
        
names= [
    Card( #nie rozumiem czemu wszystkie elementy z listy nazywaja sie tak samo tj Card- to są instancje klasy? dotrzeć można po atrybutach? 
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
print(by_name) #drukuje miejsce w pamięci nie imię i nie wiem dlaczego, czy rozwiązaniem jest metoda __str__?
print(by_surname)
print(by_email)
from faker import Faker
fake= Faker()
for i in range (10):
    print(fake.name())
    print(fake.email()) #tu email nie zgadza się z imieniem. to ma znaczenie przy generowaniu przypadkowych danych? czy trzeba do pliku dodać?
class BaseContact(Card):
    def __init__(self, private_phone_number, *args, **kwargs): #numery tel sa dziwne
        super().__init__(*args, **kwargs)
        self.private_phone_number=private_phone_number
class BusinessContact(Card):
    def __init__(self,business_phone_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.business_phone_number=business_phone_number
print("Wybieram numer telefonu: ",  fake.phone_number(), "i kontaktuje się z ", fake.name())
class Card: 
    def contact():
        for i in range (10): #te warunki są chyba złe ale się zafiksowałam i nie widzę innego podejścia
            if BaseContact:
                print("Wybieram numer telefonu: ", fake.phone_number(), "i kontaktuje się z ", fake.name())
            elif BusinessContact:
                print("Wybieram numer telefonu: ", fake.phone_number(), "i kontaktuje się z ", fake.name())
Card.contact()
Card.label_length(fake.name()) #card nie ma atrubutu label_length, nie rozumiem dlaczego skoro powyżej go ustawiłam.. 