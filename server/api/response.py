def responseAccount(account):
    '''
    Generates a response object based on the given "account"
    '''
    return {
        'id': account.id,
        'email': account.email,
        'image': account.image.url if(account.image) else None,
        'name': account.name,
        'phone': account.phone,
        'dateOfBirth': account.dateOfBirth,
        'created': account.created
    }


def responseSeller(seller):
    '''
    Generates a response object based on the given "seller"
    '''
    return {
        'id': seller.id,
        'account': responseAccount(seller.account),
        'paymentID': seller.paymentID,
        'billing': seller.billing,
        'revenue': seller.revenue
    }


def responseProduct(product):
    '''
    Generates a response object based on the given "product"
    '''
    return {
        'id': product.id,
        'seller': {
            'id': product.seller.id,
            'account': {
                'id': product.seller.account.id,
                'name': product.seller.account.name
            }
        },
        'image': product.image.url if(product.image) else None,
        'name': product.name,
        'mrp': product.mrp,
        'discount': product.discount,
        'category': product.category,
        'inStock': product.inStock,
        'rating': product.rating
    }


def responseCustomer(customer):
    '''
    Generates a response object based on the given "customer"
    '''
    return {
        'id': customer.id,
        'account': responseAccount(customer.account),
        'credit': customer.credit
    }


def responseAddress(address):
    '''
    Generates a response object based on the given "address"
    '''
    return {
        'id': address.id,
        'locality': address.locality,
        'city': address.city,
        'state': address.state,
        'pincode': address.pincode,
    }


def responseCartItem(cartItem):
    '''
    Generates a response object based on the given "cartItem"
    '''
    return {
        'id': cartItem.id,
        'product': {
            'id': cartItem.product.id,
            'image': cartItem.product.image.url if(cartItem.product.image) else None,
            'name': cartItem.product.name,
            'mrp': cartItem.product.mrp,
            'discount': cartItem.product.discount,
            'inStock': cartItem.product.inStock
        },
        'quantity': cartItem.quantity
    }


def responseOrder(order):
    '''
    Generates a response object based on the given "order"
    '''
    return {
        'id': order.id,
        'product': {
            'id': order.product.id,
            'image': order.product.image.url if(order.product.image) else None,
            'name': order.product.name
        },
        'amount': order.amount,
        'quantity': order.quantity,
        'time': order.time,
        'address': order.address,
        'status': order.status
    }


def responseReview(review):
    '''
    Generates a response object based on the given "review"
    '''
    return {
        'id': review.id,
        'customer': {
            'id': review.customer.id,
            'account': {
                'id': review.customer.account.id,
                'image': review.customer.account.image.url if(review.customer.account.image) else None,
                'name': review.customer.account.name
            }
        },
        'rating': review.rating,
        'message': review.message,
        'date': review.date
    }
