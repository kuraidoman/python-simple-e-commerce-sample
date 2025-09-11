# Domain Layer (Entities)
class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


# Infrastructure Layer (Repository)
class ProductRepository:
    def __init__(self, products):
        self.products = products
    
    def findById(self, id):
        for product in self.products:
            if product.id == id:
                return product
        return None


# Application Layer (Use Cases)
class OrderService:
    def __init__(self, productRepository):
        self.productRepository = productRepository
    
    def placeOrder(self, productId, quantity):
        product = self.productRepository.findById(productId)
        if not product:
            raise Exception("Product not found")
        else:
            totalPrice = product.price * quantity
            return {
                "product": product.name,
                "quantity": quantity,
                "totalPrice": totalPrice
            }


def placeOrderController(req, res):
    productId = req['body']['productId']
    quantity = req['body']['quantity']
    orderService = OrderService(ProductRepository(products))
    order = orderService.placeOrder(productId, quantity)
    res.send(order)


products = [
    Product(1, "Laptop", 1200),
    Product(2, "Mouse", 25),
    Product(3, "Keyboard", 75),
    Product(4, "Monitor", 300),
    Product(5, "Webcam", 50),
]


def display_products(product_list):
    for product in product_list:
        print(f"ID: {product.id}, Name: {product.name}, Price ${product.price}")


class Response:
    def send(self, data):
        print("Response:", data)


display_products(products)

req = {"body": {"productId": 2, "quantity": 3}}
res = Response()
placeOrderController(req, res)
