class Product:
    def __init__(self, id, provider_id, name, price, image):
        self.id = id
        self.provider_id = provider_id
        self.name = name
        self.price = price
        self.image = image

    def __str__(self):
        return f"{self.id=}, {self.provider_id=}, {self.name=}, {self.price=}, {self.image=}" 