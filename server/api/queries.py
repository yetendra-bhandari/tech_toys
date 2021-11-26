from django.db.models import Avg
from .models import Account, Address, CartItem, Customer, Order, Product, Review, Seller
from .authentication import validSeller, validCustomer, validProduct, validAddress, validReview, saltedHash, generateToken, readToken
from .response import responseAccount, responseSeller, responseProduct, responseCustomer, responseAddress, responseCartItem, responseOrder, responseReview
from PIL import Image


# Queries


def sellerExists(email):
    if(email):
        return Seller.objects.filter(account__email=email).exists()
    return None


def customerExists(email):
    if(email):
        return Customer.objects.filter(account__email=email).exists()
    return None


def getSellerById(sellerID):
    if(sellerID):
        try:
            seller = Seller.objects.get(id=sellerID)
            return responseSeller(seller)
        except(Seller.DoesNotExist):
            pass
    return None


def getSeller(header):
    account = readToken(header)
    if(account):
        try:
            return responseSeller(account.seller)
        except(Seller.DoesNotExist):
            pass
    return None


def getSellerProducts(header):
    account = readToken(header)
    if(account):
        try:
            products = Product.objects.filter(seller=account.seller)
            response = []
            for product in products:
                response.append(responseProduct(product))
            return response
        except(Seller.DoesNotExist):
            pass
    return None


def getSellerPendingOrders(header):
    account = readToken(header)
    if(account):
        try:
            orders = Order.objects.filter(product__seller=account.seller, status='PEN')
            response = []
            for order in orders:
                response.append(responseOrder(order))
            return response
        except(Seller.DoesNotExist):
            pass
    return None


def getCustomer(header):
    account = readToken(header)
    if(account):
        try:
            return responseCustomer(account.customer)
        except(Customer.DoesNotExist):
            pass
    return None


def getCustomerAddresses(header):
    account = readToken(header)
    if(account):
        addresses = Address.objects.filter(customer__account=account)
        response = []
        for address in addresses:
            response.append(responseAddress(address))
        return response
    return None


def getCustomerCartItems(header):
    account = readToken(header)
    if(account):
        cartItems = CartItem.objects.filter(customer__account=account)
        response = []
        for cartItem in cartItems:
            response.append(responseCartItem(cartItem))
        return response
    return None


def getCustomerOrders(header):
    account = readToken(header)
    if(account):
        orders = Order.objects.filter(customer__account=account)
        response = []
        for order in orders:
            response.append(responseOrder(order))
        return response
    return None


def getProductsByCategory(category):
    products = None
    if(category):
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()
    response = []
    for product in products:
        response.append(responseProduct(product))
    return response


def getProductById(productID):
    if(productID):
        try:
            product = Product.objects.get(id=productID)
            response = responseProduct(product)
            response['description'] = product.description
            response['specifications'] = product.specifications
            return response
        except(Product.DoesNotExist):
            pass
    return None


def getProductReviews(productID):
    if(productID):
        reviews = Review.objects.filter(product__id=productID)
        response = []
        for review in reviews:
            response.append(responseReview(review))
        return response
    return None


# Mutations


def refreshToken(header):
    account = readToken(header)
    if(account):
        return generateToken(True, account)
    return None


def editAccountImage(header, image):
    account = readToken(header)
    try:
        if(account and image.size <= 2500000):
            account.image = image
            account.save()
            canvas = Image.open(account.image.url[1:])
            canvas = canvas.crop(((account.image.width - account.image.height) // 2, 0, (account.image.width + account.image.height) // 2, account.image.height) if(account.image.width > account.image.height) else (0, (account.image.height - account.image.width) // 2, account.image.width, (account.image.height + account.image.width) // 2))
            canvas = canvas.resize((500, 500))
            canvas.save(account.image.url[1:])
            return responseAccount(account)
    except(AttributeError):
        pass
    return None


def addSeller(remember, sellerInput):
    if(validSeller(sellerInput)):
        account, created = Account.objects.get_or_create(
            email=sellerInput['account']['email'],
            defaults={
                'name': sellerInput['account']['name'],
                'phone': sellerInput['account']['phone'],
                'password': saltedHash(sellerInput['account']['password']),
                'dateOfBirth': sellerInput['account']['dateOfBirth']
            })
        if(created):
            seller = Seller.objects.create(
                account=account, paymentID=sellerInput['paymentID'], billing=sellerInput['billing'])
            return {
                'authToken': generateToken(remember, seller.account),
                'seller': responseSeller(seller)
            }
    return None


def loginSeller(remember, accountInput):
    if(accountInput):
        try:
            seller = Seller.objects.get(
                account__email=accountInput['email'], account__password=saltedHash(accountInput['password']))
            return {
                'authToken': generateToken(remember, seller.account),
                'seller': responseSeller(seller)
            }
        except(Seller.DoesNotExist):
            pass
    return None


def editSeller(header, sellerInput, password):
    account = readToken(header)
    if(account and validSeller(sellerInput)):
        try:
            seller = account.seller
            if((saltedHash(password) == seller.account.password) and (seller.account.email == sellerInput['account']['email'] or not Seller.objects.filter(email=sellerInput['account']['email']).exists())):
                seller.account.email = sellerInput['account']['email']
                seller.account.name = sellerInput['account']['name']
                seller.account.phone = sellerInput['account']['phone']
                if('password' in sellerInput['account']):
                    seller.account.password = saltedHash(
                        sellerInput['account']['password'])
                seller.account.dateOfBirth = sellerInput['account']['dateOfBirth']
                seller.paymentID = sellerInput['paymentID']
                seller.billing = sellerInput['billing']
                seller.account.save()
                seller.save()
                return responseSeller(seller)
        except(Seller.DoesNotExist):
            pass
    return None


def addSellerProduct(header, productInput):
    account = readToken(header)
    if(account and validProduct(productInput)):
        try:
            seller = account.seller
            product = Product.objects.create(seller=seller, name=productInput['name'], description=productInput['description'], specifications=productInput['specifications'],
                                             mrp=productInput['mrp'], discount=productInput['discount'], category=productInput['category'], inStock=productInput['inStock'])
            if('image' in productInput):
                product.image = productInput['image']
                product.save()
                canvas = Image.open(product.image.url[1:])
                canvas.thumbnail((800, 800))
                canvas.save(product.image.url[1:])
            return responseProduct(product)
        except(Seller.DoesNotExist):
            pass
    return None


def addCustomer(remember, customerInput):
    if(validCustomer(customerInput)):
        account, created = Account.objects.get_or_create(
            email=customerInput['account']['email'],
            defaults={
                'name': customerInput['account']['name'],
                'phone': customerInput['account']['phone'],
                'password': saltedHash(customerInput['account']['password']),
                'dateOfBirth': customerInput['account']['dateOfBirth']
            })
        if(created):
            customer = Customer.objects.create(account=account)
            return {
                'authToken': generateToken(remember, customer.account),
                'customer': responseCustomer(customer)
            }
    return None


def loginCustomer(remember, accountInput):
    if(accountInput):
        try:
            customer = Customer.objects.get(
                account__email=accountInput['email'], account__password=saltedHash(accountInput['password']))
            return {
                'authToken': generateToken(remember, customer.account),
                'customer': responseCustomer(customer)
            }
        except(Customer.DoesNotExist):
            pass
    return None


def editCustomer(header, customerInput, password):
    account = readToken(header)
    if(account and validCustomer(customerInput)):
        try:
            customer = account.customer
            if((saltedHash(password) == customer.account.password) and (customer.account.email == customerInput['account']['email'] or not Account.objects.filter(email=customerInput['account']['email']).exists())):
                customer.account.email = customerInput['account']['email']
                customer.account.name = customerInput['account']['name']
                customer.account.phone = customerInput['account']['phone']
                if('password' in customerInput['account']):
                    customer.account.password = saltedHash(
                        customerInput['account']['password'])
                customer.account.dateOfBirth = customerInput['account']['dateOfBirth']
                customer.account.save()
                customer.save()
                return responseCustomer(customer)
        except(Customer.DoesNotExist):
            pass
    return None


def addCustomerAddress(header, addressInput):
    account = readToken(header)
    if(account and validAddress(addressInput)):
        try:
            customer = account.customer
            address = Address.objects.create(
                customer=customer, locality=addressInput['locality'], city=addressInput['city'], state=addressInput['state'], pincode=addressInput['pincode'])
            return responseAddress(address)
        except(Customer.DoesNotExist):
            pass
    return None


def addCustomerCartItem(header, productID, quantity):
    account = readToken(header)
    if(account and quantity <= 10):
        try:
            customer = account.customer
            product = Product.objects.get(id=productID)
            cartItem = CartItem.objects.create(
                customer=customer, product=product, quantity=quantity)
            return responseCartItem(cartItem)
        except(Customer.DoesNotExist, Product.DoesNotExist):
            pass
    return None


def deleteCustomerCartItem(header, cartItemID):
    account = readToken(header)
    if(account):
        try:
            CartItem.objects.get(id=cartItemID, customer=account.customer).delete()
            return True
        except(Customer.DoesNotExist, CartItem.DoesNotExist):
            pass
    return None


def addCustomerOrders(header, cartItemIDs, addressID):
    account = readToken(header)
    if(account):
        try:
            customer = account.customer
            address = Address.objects.get(
                id=addressID, customer=customer)
            cartItems = []
            itemAmounts = []
            for cartItemID in cartItemIDs:
                cartItem = CartItem.objects.get(
                    id=cartItemID, customer=customer)
                cartItems.append(cartItem)
                itemAmounts.append(
                    cartItem.product.mrp * cartItem.quantity * (100 - cartItem.product.discount) // 100)
            totalAmount = sum(itemAmounts)
            if(all(cartItem.product.inStock for cartItem in cartItems) and customer.credit >= totalAmount):
                for cartItem, itemAmount in zip(cartItems, itemAmounts):
                    order = Order.objects.create(
                        customer=customer, product=cartItem.product, amount=itemAmount,  quantity=cartItem.quantity, address=address)
                    order.product.seller.revenue += itemAmount
                    order.product.seller.save()
                    cartItem.delete()
                customer.credit -= totalAmount
                customer.save()
                return True
        except(Customer.DoesNotExist, Address.DoesNotExist, CartItem.DoesNotExist):
            pass
    return None


def editCustomerOrderStatus(header, orderID, status):
    ORDER_STATUS = {'DEL', 'CNL'}
    account = readToken(header)
    if(account and status in ORDER_STATUS):
        try:
            customer = account.customer
            order = Order.objects.get(
                id=orderID, customer=customer)
            if(order.status == 'PEN'):
                order.status = status
                order.save()
                if(status == 'CNL'):
                    order.product.seller.revenue -= order.amount
                    customer.credit += order.amount
                    order.product.seller.save()
                    customer.save()
                return True
        except(Customer.DoesNotExist, Order.DoesNotExist):
            pass
    return None


def editProductDiscount(header, productID, discount):
    account = readToken(header)
    if(account and discount in range(100)):
        try:
            product = Product.objects.get(
                id=productID, seller__account=account)
            product.discount = discount
            product.save()
            return responseProduct(product)
        except(Product.DoesNotExist):
            pass
    return None


def editProductStock(header, productID, inStock):
    account = readToken(header)
    if(account):
        try:
            product = Product.objects.get(
                id=productID, seller__account=account)
            product.inStock = inStock
            product.save()
            return responseProduct(product)
        except(Product.DoesNotExist):
            pass
    return None


def addProductReview(header, productID, reviewInput):
    account = readToken(header)
    if(account and validReview(reviewInput)):
        try:
            product = Product.objects.get(id=productID)
            customer = Customer.objects.get(account=account)
            Review.objects.create(product=product, customer=customer,
                                  rating=reviewInput['rating'], message=reviewInput['message'])
            reviews = Review.objects.filter(product=product)
            product.rating = int(reviews.aggregate(
                Avg('rating'))['rating__avg'])
            product.save()
            return product.rating
        except(Customer.DoesNotExist, Product.DoesNotExist):
            pass
    return None


def deleteProductReview(header, reviewID):
    account = readToken(header)
    if(account):
        try:
            review = Review.objects.get(id=reviewID, customer__account=account)
            product = review.product
            review.delete()
            reviews = Review.objects.filter(product=product)
            product.rating = int(reviews.aggregate(
                Avg('rating'))['rating__avg'])
            product.save()
            return product.rating
        except(Review.DoesNotExist):
            pass
    return None
