class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        res = {
    "id": self.current_id,
    "name": name,
    "phone": phone,
    "email": email,
    "favorite": favorite}
        print(res)
        self.contacts.append(res)
        Contacts.current_id += 1
        
            
                
                
                
                
                
            
        
        
