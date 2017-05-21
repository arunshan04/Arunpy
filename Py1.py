import mysql.connector
class Truck(object):
    def __init__(self, wheels, miles, make, model, year, sold_on):
        self.wheels = wheels
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on
        cnx=mysql.connector.connect(user='Arun',password='123',host='127.0.0.1',database='ARUN')
        cursor = cnx.cursor()
        data_employee = (self.wheels, self.miles,self.make, self.model, self.year, self.sold_on)
        add_truck = ("INSERT INTO trucks (wheels ,miles ,make ,model , year ,sold_on ) VALUES (%s, %s, %s, %s, %s, %s)")
        print (add_truck,data_employee)
        cursor.execute(add_truck,data_employee);
        cnx.commit()
        cursor.close()
        cnx.close()
    def sale_price(self):
        if self.sold_on is not None:
            return 0.0  # Already sold
        return 5000.0 * self.wheels
    def purchase_price(self):
        if self.sold_on is None:
            return 0.0  # Not yet sold
        return 10000 - (.10 * self.miles)

jef=Truck(4,100,2010,2008,2012,2015)