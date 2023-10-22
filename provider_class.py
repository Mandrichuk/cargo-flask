class Provider:
    def __init__(self, id, name, phone):
        self.id = id
        self.name = name
        self.phone = phone
        self.product_list = []

    def __str__(self):
        return f"{self.id=}, {self.name=}, {self.phone=}, {self.product_list=}" 
    