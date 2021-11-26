from ariadne import QueryType, MutationType, make_executable_schema, upload_scalar
from . import queries


type_defs = """
    scalar Date
    scalar Time
    scalar URL
    scalar AuthToken
    scalar Upload
    type Account {
        id: ID
        email: String
        image: URL
        name: String
        phone: String
        dateOfBirth: Date
        created: Date
    }
    type Seller {
        id: ID
        account: Account
        paymentID: String
        billing: String
        revenue: Int
    }
    type Customer {
        id: ID
        account: Account
        credit: Int
    }
    type Product {
        id: ID
        seller: Seller
        image: URL
        name: String
        description: String
        specifications: String
        mrp: Int
        discount: Int
        category: String
        inStock: Boolean
        rating: Int
    }
    type CartItem {
        id: ID
        product: Product
        quantity: Int
    }
    type Address {
        id: ID
        locality: String
        city: String
        state: String
        pincode: Int
    }
    type Order {
        id: ID
        product: Product
        amount: Int
        quantity: Int
        time: Time
        address: Address
        status: String
    }
    type Review {
        id: ID
        customer: Customer
        rating: Int
        message: String
        date: Date
    }
    type SellerToken {
        authToken: AuthToken
        seller: Seller
    }
    type CustomerToken {
        authToken: AuthToken
        customer: Customer
    }
    input AccountInput {
        email: String
        name: String
        phone: String
        password: String
        dateOfBirth: Date
    }
    input SellerInput {
        account: AccountInput
        paymentID: String
        billing: String
    }
    input ProductInput {
        image: Upload
        name: String
        description: String
        specifications: String
        mrp: Int
        discount: Int
        category: String
        inStock: Boolean
    }
    input CustomerInput {
        account: AccountInput
    }
    input AddressInput {
        locality: String
        city: String
        state: String
        pincode: Int
    }
    input ReviewInput {
        rating: Int
        message: String
    }
    type Query {
        sellerExists(email: String): Boolean
        customerExists(email: String): Boolean
        getSellerById(sellerID: ID): Seller
        getSeller: Seller
        getSellerProducts: [Product]
        getSellerPendingOrders: [Order]
        getCustomer: Customer
        getCustomerAddresses: [Address]
        getCustomerCartItems: [CartItem]
        getCustomerOrders: [Order]
        getProductsByCategory(category: String): [Product]
        getProductById(productID: ID): Product
        getProductReviews(productID: ID): [Review]
    }
    type Mutation {
        refreshToken: AuthToken
        editAccountImage(image: Upload): Account
        addSeller(remember: Boolean, sellerInput: SellerInput): SellerToken
        loginSeller(remember: Boolean, accountInput: AccountInput): SellerToken
        editSeller(sellerInput: SellerInput, password: String): Seller
        addSellerProduct(productInput: ProductInput): Product
        addCustomer(remember: Boolean, customerInput: CustomerInput): CustomerToken
        loginCustomer(remember: Boolean, accountInput: AccountInput): CustomerToken
        editCustomer(customerInput: CustomerInput, password: String): Customer
        addCustomerAddress(addressInput: AddressInput): Address
        addCustomerCartItem(productID: ID, quantity: Int): CartItem
        deleteCustomerCartItem(cartItemID: ID): Boolean
        addCustomerOrders(cartItemIDs: [ID], addressID: ID): Boolean
        editCustomerOrderStatus(orderID: ID, status: String): Boolean
        editProductDiscount(productID: ID, discount: Int): Product
        editProductStock(productID: ID, inStock: Boolean): Product
        addProductReview(productID: ID, reviewInput: ReviewInput): Int
        deleteProductReview(reviewID: ID): Int
    }
"""

query = QueryType()
mutation = MutationType()


@query.field("sellerExists")
def resolve_sellerExists(_, info, email=None):
    return queries.sellerExists(email)


@query.field("customerExists")
def resolve_customerExists(_, info, email=None):
    return queries.customerExists(email)


@query.field("getSellerById")
def resolve_getSellerById(_, info, sellerID=None):
    return queries.getSellerById(sellerID)


@query.field("getSeller")
def resolve_getSeller(_, info):
    if('Authorization' in info.context["request"].headers):
        return queries.getSeller(info.context["request"].headers['Authorization'])
    return None


@query.field("getSellerProducts")
def resolve_getSellerProducts(_, info):
    if('Authorization' in info.context["request"].headers):
        return queries.getSellerProducts(info.context["request"].headers['Authorization'])
    return None


@query.field("getSellerPendingOrders")
def resolve_getSellerPendingOrders(_, info):
    if('Authorization' in info.context["request"].headers):
        return queries.getSellerPendingOrders(info.context["request"].headers['Authorization'])
    return None


@query.field("getCustomer")
def resolve_getCustomer(_, info):
    if('Authorization' in info.context["request"].headers):
        return queries.getCustomer(info.context["request"].headers['Authorization'])
    return None


@query.field("getCustomerAddresses")
def resolve_getCustomerAddresses(_, info):
    if('Authorization' in info.context["request"].headers):
        return queries.getCustomerAddresses(info.context["request"].headers['Authorization'])
    return None


@query.field("getCustomerCartItems")
def resolve_getCustomerCartItems(_, info):
    if('Authorization' in info.context["request"].headers):
        return queries.getCustomerCartItems(info.context["request"].headers['Authorization'])
    return None


@query.field("getCustomerOrders")
def resolve_getCustomerOrders(_, info):
    if('Authorization' in info.context["request"].headers):
        return queries.getCustomerOrders(info.context["request"].headers['Authorization'])
    return None


@query.field("getProductsByCategory")
def resolve_getProductsByCategory(_, info, category=None):
    return queries.getProductsByCategory(category)


@query.field("getProductById")
def resolve_getProductById(_, info, productID=None):
    return queries.getProductById(productID)


@query.field("getProductReviews")
def resolve_getProductReviews(_, info, productID=None):
    return queries.getProductReviews(productID)


@mutation.field("refreshToken")
def resolve_refreshToken(_, info):
    if('Authorization' in info.context["request"].headers):
        return queries.refreshToken(info.context["request"].headers['Authorization'])
    return None


@mutation.field("editAccountImage")
def resolve_editAccountImage(_, info, image=None):
    if('Authorization' in info.context["request"].headers):
        return queries.editAccountImage(info.context["request"].headers['Authorization'], image)
    return None


@mutation.field("addSeller")
def resolve_addSeller(_, info, remember=None, sellerInput=None):
    return queries.addSeller(remember, sellerInput)


@mutation.field("loginSeller")
def resolve_loginSeller(_, info, remember=None, accountInput=None):
    return queries.loginSeller(remember, accountInput)


@mutation.field("editSeller")
def resolve_editSeller(_, info, sellerInput, password):
    if('Authorization' in info.context["request"].headers):
        return queries.editSeller(info.context["request"].headers['Authorization'], sellerInput, password)
    return None


@mutation.field("addSellerProduct")
def resolve_addSellerProduct(_, info, productInput):
    if('Authorization' in info.context["request"].headers):
        return queries.addSellerProduct(info.context["request"].headers['Authorization'], productInput)
    return None


@mutation.field("addCustomer")
def resolve_addCustomer(_, info, remember=None, customerInput=None):
    return queries.addCustomer(remember, customerInput)


@mutation.field("loginCustomer")
def resolve_loginCustomer(_, info, remember=None, accountInput=None):
    return queries.loginCustomer(remember, accountInput)


@mutation.field("editCustomer")
def resolve_editCustomer(_, info, customerInput, password):
    if('Authorization' in info.context["request"].headers):
        return queries.editCustomer(info.context["request"].headers['Authorization'], customerInput, password)
    return None


@mutation.field("addCustomerAddress")
def resolve_addCustomerAddress(_, info, addressInput):
    if('Authorization' in info.context["request"].headers):
        return queries.addCustomerAddress(info.context["request"].headers['Authorization'], addressInput)
    return None


@mutation.field("addCustomerCartItem")
def resolve_addCustomerCartItem(_, info, productID, quantity):
    if('Authorization' in info.context["request"].headers):
        return queries.addCustomerCartItem(info.context["request"].headers['Authorization'],  productID, quantity)
    return None


@mutation.field("deleteCustomerCartItem")
def resolve_deleteCustomerCartItem(_, info, cartItemID):
    if('Authorization' in info.context["request"].headers):
        return queries.deleteCustomerCartItem(info.context["request"].headers['Authorization'],  cartItemID)
    return None


@mutation.field("addCustomerOrders")
def resolve_addCustomerOrders(_, info, cartItemIDs, addressID):
    if('Authorization' in info.context["request"].headers):
        return queries.addCustomerOrders(info.context["request"].headers['Authorization'],  cartItemIDs, addressID)
    return None


@mutation.field("editCustomerOrderStatus")
def resolve_editCustomerOrderStatus(_, info, orderID, status):
    if('Authorization' in info.context["request"].headers):
        return queries.editCustomerOrderStatus(info.context["request"].headers['Authorization'],  orderID, status)
    return None


@mutation.field("editProductDiscount")
def resolve_editProductDiscount(_, info, productID, discount):
    if('Authorization' in info.context["request"].headers):
        return queries.editProductDiscount(info.context["request"].headers['Authorization'],  productID, discount)
    return None


@mutation.field("editProductStock")
def resolve_editProductStock(_, info, productID, inStock):
    if('Authorization' in info.context["request"].headers):
        return queries.editProductStock(info.context["request"].headers['Authorization'],  productID, inStock)
    return None


@mutation.field("addProductReview")
def resolve_addProductReview(_, info, productID, reviewInput):
    if('Authorization' in info.context["request"].headers):
        return queries.addProductReview(info.context["request"].headers['Authorization'],  productID, reviewInput)
    return None


@mutation.field("deleteProductReview")
def resolve_deleteProductReview(_, info, reviewID):
    if('Authorization' in info.context["request"].headers):
        return queries.deleteProductReview(info.context["request"].headers['Authorization'],  reviewID)
    return None


schema = make_executable_schema(type_defs, query, mutation, upload_scalar)
