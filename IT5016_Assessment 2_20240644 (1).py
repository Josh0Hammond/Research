class Ticket:
    def __init__(self,staffid,name,email,desc):
        self.staffid=staffid
        self.staus="open"
        self.ticketid=0
    def generateid(self,counter):
        self.ticketid=counter+2000
    def changepass(self):
        pass


class Helpdesk:
    def __init__(self):
        self.counter=0
        self.helpdesk=[]
    def createticket(self,staffid,name,email,desc):
        self.counter=self.counter+1
        ticket=Ticket(staffid,name,email,desc)
        ticket.generateid(self.counter)
        self.helpdesk.append(ticket)
        password
    #Generate new password#
    def desc = input("Password Change"):
        generatePassword():
        password = ""
        count = 0
        while count < PasswordLength:
            password += random.choice(passwordChars)
            count += 1
            print("New Password: ", password)
            generatePassword()
    #If this isn't right then I don't understand the assignment and I don't understand how to do the rest of it#