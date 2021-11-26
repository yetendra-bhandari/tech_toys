from datetime import date, datetime
import time
import hashlib
from django import forms
from django.core.exceptions import ValidationError
import jwt
from tech_toys.settings import SECRET_KEY
from .models import Account

emailField = forms.EmailField()


def validEmail(email):
    '''
    Check whether the given email address is valid or not.
    '''
    try:
        emailField.clean(email)
    except(ValidationError):
        return False
    return True


def validName(name):
    '''
    Check whether the given name is valid or not.
    '''
    return len(name) > 0 and len(name) <= 32 and not name.isspace() and all(char.isalpha() or char == ' ' for char in name)


def validDateOfBirth(dateOfBirth):
    '''
    Checks whether the given date of birth is valid or not.
    '''
    try:
        dob = datetime.strptime(dateOfBirth, '%Y-%m-%d').date()
        temp = date.today()
        temp = temp.replace(year=temp.year - 18)
        return dob <= temp
    except(ValueError):
        return False


def validAccount(account):
    '''
    Checks whether the given account details are valid or not.
    '''
    try:
        return validEmail(account['email']) and validName(account['name']) and len(account['phone']) == 10 and account['phone'].isdigit() and validDateOfBirth(account['dateOfBirth'])
    except(KeyError):
        return False


def validSeller(seller):
    '''
    Checks whether the given seller details are valid or not.
    '''
    try:
        return validAccount(seller['account']) and len(seller['paymentID']) <= 12 and len(seller['billing']) <= 256
    except(KeyError):
        return False


def validCustomer(customer):
    '''
    Checks whether the given customer details are valid or not.
    '''
    try:
        return validAccount(customer['account'])
    except(KeyError):
        return False


def validProduct(product):
    '''
    Checks whether the given product details are valid or not.
    '''
    PRODUCT_CATAGORY = {'EARP', 'HEAD', 'LAPT', 'VIRT'}
    try:
        return (product['image'].size <= 2500000 if('image' in product) else True) and len(product['name']) <= 64 and len(product['description']) <= 4096 and len(product['specifications']) <= 4096 and product['mrp'] > 0 and product['mrp'] <= 500000 and product['discount'] >= 0 and product['discount'] <= 100 and product['category'] in PRODUCT_CATAGORY
    except(KeyError):
        return False


def validAddress(address):
    '''
    Checks whether the given address is valid or not.
    '''
    try:
        return len(address['locality']) <= 256 and len(address['city']) <= 64 and len(address['state']) <= 64 and address['pincode'] >= 100000 and address['pincode'] < 1000000
    except(KeyError):
        return False


def validReview(review):
    '''
    Checks whether the given review is valid or not.
    '''
    RATINGS = {10, 20, 30, 40, 50}
    try:
        return review['rating'] in RATINGS and len(review['message']) <= 512
    except(KeyError):
        return False


def strongPassword(password):
    '''
    Checks whether the given password is strong or not.
    '''
    return 8 <= len(password) <= 20


def saltedHash(password):
    '''
    Generates the 'SHA-256' salted-hash of the given password.
    '''
    return hashlib.sha256((SECRET_KEY + password).encode()).hexdigest()


def generateToken(remember, account):
    '''
    Generates the JWT token from the given parameters.
    '''
    exp = int(time.time()) + (604800 if(remember) else 86400)
    return (jwt.encode({'exp': exp, 'email': account.email, 'password': account.password}, SECRET_KEY, algorithm='HS256'))


def readToken(header):
    '''
    Reads the given JWT token and returns the payload.
    '''
    try:
        token = header.split()
        if(token[0] == 'Bearer'):
            payload = jwt.decode(token[1], SECRET_KEY, algorithms='HS256')
            return Account.objects.get(email=payload['email'], password=payload['password'])
    except(IndexError, KeyError, jwt.InvalidTokenError, jwt.ExpiredSignatureError, Account.DoesNotExist):
        pass
    return None
