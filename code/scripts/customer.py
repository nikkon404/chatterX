import random
import time


class Customer():

    def __init__(self, name, movieID, seat, contact):
        self.name = name
        self.movieID = movieID
        self.seat = seat
        self.contact = contact
        self.custNo = random.randint(0, 999999)

    def saveCustomerInfo(self):
        f = open("./database/customerInfo.csv", "r+")

        value = str(self.custNo) + "," + self.name + "," + \
            self.movieID + "," + self.seat + "," + self.contact
        count = len(f.readlines())
        if count > 0:
            value = "\n"+value
        f.write(value)
        f.close()
