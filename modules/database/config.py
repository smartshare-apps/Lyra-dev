import sqlite3
from functools import partial

ERROR_CODES = {
    "NO_DB": "There was an issue connecting to the store database. Please verify your configuration below."
}


def admin_names():
    return ["admin", "joe"]


sessionPrefixList = [
    "cart:", "auth:"

]

generalSettings = {
    "default_tableName": "products",
    "default_templateDir": "templates"
}

productColumnMappings = [
    "product_id", "stripe_id", "VariantSKU", "VariantPrice", "VariantCompareAtPrice", "VariantInventoryQty",
    "VariantTaxable", "VariantWeightUnit", "VariantGrams", "Title", "BodyHTML", "Vendor", "Type", "Tags", "Published",
    "ImageSrc", "ImageAltText", "VariantTypes", "resources"
]

variantColumnMappings = [
    "variant_id", "VariantSKU", "product_id", "VariantData", "VariantPrice", "VariantCompareAtPrice", "VariantGrams",
    "VariantWeightUnit",
    "VariantInventoryQty", "VariantImg", "VariantTaxCode", "VariantTaxable", "VariantBarcode", "VariantRequiresShipping"
]

orderColumnMappings = [
    "order_id", "Date", "customer_id", "PaymentInfo", "PaymentStatus", "FulfillmentStatus", "SKU_List", "OrderTotal",
    "TaxTotal", "ShippingTotal", "SubTotal", "OrderEvents", "Currency", "ShippingAddress", "ShippingAddress2",
    "ShippingCity",
    "ShippingPostalCode", "ShippingCountry", "Company", "ShippingFirstName", "ShippingLastName", "Email",
    "ShippingState", "PhoneNumber", "Note", "BillingAddress", "BillingAddress2", "BillingCity",
    "BillingPostalCode", "BillingCountry", "BillingFirstName", "BillingLastName", "BillingState", "token_id",
    "charge_id", "order_creation_method"
]

shipmentColumnMappings = [
    "shipment_id", "order_id", "TrackingNumber", "LabelURL", "ShipmentDate", "Carrier", "SKU_List", "FulfillmentMethod"
]

customerColumnMappings = [
    "customer_id", "user_id", "Email", "Phone", "ShippingFirstName", "ShippingLastName", "ShippingAddress1",
    "ShippingAddress2", "ShippingCity", "ShippingState", "ShippingPostalCode", "ShippingCountry", "BillingFirstName",
    "BillingLastName",
    "BillingAddress1", "BillingAddress2", "BillingCity", "BillingState", "BillingPostalCode", "BillingCountry",
    "Company", "TotalSpent", "LastOrder", "accepts_marketing"]

vendorColumnMappings = [
    "vendor_id", "Name", "URL", "Phone", "Email"

]

collectionColumnMappings = [
    "collection_id", "Title", "BodyHTML", "CollectionImageSrc", "Published", "Conditions", "Strict", "URL", "Meta",
    "PageTitle", "Template", "resources"
]

pluginColumnMappings = [
    "plugin_id", "plugin_name", "plugin_icon", "plugin_type", "uri", "description"
]

eventColumnMappings = [
    "event_id", "Time", "Type", "Message", "Data"
]

userColumnMappings = [
    "user_id", "customer_id", "username", "level", "is_active", "last_login", "created_on", "order_list"
]

dashboardColumnMappings = [
    "tile_id", "tile_type", "requirements", "resources"
]

collectionRuleMappings = {
    ">": ">",
    "<": "<",
    ">=": ">=",
    "<=": "<=",
    "c": " LIKE ",
    "=": "=",
    "!=": "!=",
    "dc": " NOT LIKE "

}

# these field mappings are for structuring dynamic queries
productFieldMapping = {
    "VariantSKU": "TEXT",
    "VariantPrice": "REAL",
    "VariantWeightUnit": "TEXT",
    "VariantCompareAtPrice": "REAL",
    "VariantTaxable": "INTEGER",
    "VariantInventoryPolicy": "TEXT",
    "VariantGrams": "REAL",
    "VariantRequiresShipping": "INTEGER",
    "VariantTaxCode": "INTEGER",
    "VariantFulfillmentService": "TEXT",
    "product_id": "INTEGER",
    "VariantInventoryQty": "INTEGER",
    "Published": "TEXT",
    "Tags": "TEXT",
    "Title": "TEXT",
    "Type": "TEXT",
    "BodyHTML": "TEXT",
    "ImageSrc": "TEXT"
}

vendorFieldMapping = {
    "vendor_id": "INTEGER",
    "Name": "TEXT",
    "URL": "TEXT",
    "Phone": "TEXT",
    "Email": "TEXT"
}

variantFieldMapping = {
    "VariantSKU": "TEXT",
    "VariantPrice": "REAL",
    "VariantCompareAtPrice": "REAL",
    "VariantTaxable": "INTEGER",
    "VariantInventoryPolicy": "TEXT",
    "VariantWeightUnit": "TEXT",
    "VariantGrams": "REAL",
    "VariantRequiresShipping": "TEXT",
    "VariantTaxCode": "INTEGER",
    "VariantFulfillmentService": "TEXT",
    "variant_id": "INTEGER",
    "VariantInventoryQty": "INTEGER",
}

collectionFieldMapping = {
    "collection_id": "INTEGER",
    "Title": "TEXT",
    "Meta": "TEXT",
    "URL": "TEXT",
    "Published": "INTEGER",
    "PageTitle": "TEXT",
    "Template": "TEXT",
    "BodyHTML": "TEXT",
    "CollectionImageSrc": "TEXT",
    "Strict": "INTEGER",
    "Conditions": "TEXT"

}

orderFieldMapping = {
    "order_id": "INTEGER",
    "customer_id": "INTEGER",
    "Email": "TEXT",
    "PhoneNumber": "TEXT",
    "Date": "TEXT",
    "ShippingFirstName": "TEXT",
    "ShippingLastName": "TEXT",
    "ShippingAddress": "TEXT",
    "ShippingAddress2": "TEXT",
    "ShippingCity": "TEXT",
    "ShippingState": "TEXT",
    "ShippingPostalCode": "TEXT",
    "ShippingCountry": "TEXT",
    "BillingFirstName": "TEXT",
    "BillingLastName": "TEXT",
    "BillingAddress": "TEXT",
    "BillingAddress2": "TEXT",
    "BillingCity": "TEXT",
    "BillingState": "TEXT",
    "BillingPostalCode": "TEXT",
    "BillingCountry": "TEXT",
    "Company": "TEXT",
    "PaymentInfo": "TEXT",
    "PaymentStatus": "TEXT",
    "FulfillmentStatus": "TEXT",
    "SKU_List": "TEXT",
    "OrderTotal": "REAL",
    "TaxTotal": "REAL",
    "ShippingTotal": "REAL",
    "SubTotal": "REAL",
    "OrderEvents": "TEXT",
    "Currency": "TEXT",
    "TotalSpent": "REAL",
    "LastOrder": "INTEGER",
    "accepts_marketing": "TEXT",
    "order_creation_method": "TEXT",
    "token_id": "TEXT",
    "charge_id": "TEXT"
}

shipmentFieldMapping = {
    "shipment_id": "INTEGER",
    "order_id": "INTEGER",
    "TrackingNumber": "TEXT",
    "LabelURL": "TEXT",
    "ShipmentDate": "TEXT",
    "Carrier": "TEXT",
    "SKU_List": "TEXT",
    "FulfillmentMethod": "TEXT"
}

dashboardFieldMapping = {
    "tile_id": "INTEGER",
    "tile_type": "TEXT",
    "requirements": "TEXT",
    "resources": "TEXT"
}

customerFieldMapping = {
    "customer_id": "INTEGER",
    "user_id": "INTEGER",
    "Email": "TEXT",
    "Phone": "TEXT",
    "ShippingFirstName": "TEXT",
    "ShippingLastName": "TEXT",
    "ShippingAddress1": "TEXT",
    "ShippingAddress2": "TEXT",
    "ShippingCity": "TEXT",
    "ShippingState": "TEXT",
    "ShippingPostalCode": "TEXT",
    "ShippingCountry": "TEXT",
    "BillingFirstName": "TEXT",
    "BillingLastName": "TEXT",
    "BillingAddress1": "TEXT",
    "BillingAddress2": "TEXT",
    "BillingCity": "TEXT",
    "BillingState": "TEXT",
    "BillingPostalCode": "TEXT",
    "BillingCountry": "TEXT",
    "TotalSpent": "REAL",
    "LastOrder": "INTEGER",
    "Company": "TEXT",
    "accepts_marketing": "TEXT"
}

pluginFieldMapping = {
    "plugin_id": "INTEGER",
    "plugin_name": "TEXT",
    "plugin_type": "TEXT",
    "plugin_icon": "INTEGER",
    "description": "TEXT",
    "uri": "TEXT"
}

productDisplayOptions = {
    "recordsPerPage": 10,
    "confirmDelete": True
}


# payment settings functions


def getDefaultShippingAddress(database):
    currentQuery = """SELECT FieldList FROM settings WHERE setting_id="DefaultShippingAddress";"""

    try:
        database.execute(currentQuery)
    except Exception as e:
        print "Error: ", e

    address = database.fetchone()
    if address:
        address = filter(lambda a: a != "", address[0].split(';'))
        formattedAddress = {}

        print address
        for field in address:
            field = field.split(':')
            formattedAddress[field[0]] = field[1]

        return formattedAddress
    else:
        return None


def setDefaultShippingAddress(default_address, database):
    currentQuery = """UPDATE settings SET FieldList=? WHERE setting_id="DefaultShippingAddress";"""

    try:
        database.execute(currentQuery, (default_address,))
    except Exception as e:
        print e
        return False

    return True


def getPackageTypes(database):
    currentQuery = """SELECT FieldList FROM settings WHERE setting_id="PackageTypes";"""

    try:
        database.execute(currentQuery)
    except Exception as e:
        print "Error: ", e

    packages = database.fetchone()

    if packages:
        packages = filter(lambda p: p != "", packages[0].split('<package_split>'))
        packageList = []

        for idx, package in enumerate(packages):
            package = filter(lambda p: p != "", package.split(';'))

            packageList.append({})

            packageList[idx] = {}

            for field in package:
                key, value = field.split('=')
                packageList[idx][key] = value

        formattedPackages = {}

        for package in packageList:
            formattedPackages[package['title']] = {}
            formattedPackages[package['title']] = package
            formattedPackages[package['title']].pop('title', None)

        return formattedPackages
    else:
        return None


def setPackageTypes(package_type_string, database):
    currentQuery = """UPDATE settings SET FieldList=? WHERE setting_id="PackageTypes";"""

    try:
        database.execute(currentQuery, (package_type_string,))
    except Exception as e:
        print e
        return False

    return True


# template to retreive api keys
def getAPIKeys(database, setting_id):
    currentQuery = """SELECT FieldList FROM settings WHERE setting_id=?;"""

    try:
        database.execute(currentQuery, (setting_id,))
    except Exception as e:
        print "Error: ", e

    api_keys = database.fetchone()
    if api_keys:
        api_keys = api_keys[0].split(',')

        formatted_api_keys = {}

        for key in api_keys:
            key = key.split(':')
            formatted_api_keys[key[0]] = key[1]

        return formatted_api_keys


# template function to set api keys
def setAPIKeys(setting_id, api_keys, database):
    currentQuery = """UPDATE settings SET FieldList=? WHERE setting_id=?;"""

    try:
        database.execute(currentQuery, (api_keys, setting_id,))
    except Exception as e:
        print e
        return False

    return True


setStripeAPIKeys = partial(setAPIKeys, setting_id='stripe_api_keys')
getStripeAPIKeys = partial(getAPIKeys, setting_id='stripe_api_keys')

setShippoAPIKeys = partial(setAPIKeys, setting_id='shippo_api_keys')
getShippoAPIKeys = partial(getAPIKeys, setting_id='shippo_api_keys')


def getGoogleAnalyticsScript(database):
    currentQuery = """SELECT FieldList FROM settings WHERE setting_id="GoogleAnalyticsScript";"""
    try:
        database.execute(currentQuery)
    except Exception as e:
        print e
        return None

    analytics_script = database.fetchone()
    if analytics_script:
        return analytics_script[0]


def setGoogleAnalyticsScript(analytics_script, database):
    currentQuery = """UPDATE settings SET FieldList=? WHERE setting_id="GoogleAnalyticsScript";"""

    try:
        database.execute(currentQuery, (analytics_script,))
    except Exception as e:
        print "Error saving google analytics script:", e
        return False

    return True


def BulkProductEditorSettings(database):
    currentQuery = """SELECT FieldList FROM settings WHERE setting_id="BulkProductEditorFields";"""

    try:
        database.execute(currentQuery)
    except Exception as e:
        print e

    settings = database.fetchone()
    if settings:
        return settings[0]
    else:
        return None


def setBulkProductEditorSettings(selectedFields, database):
    currentQuery = """UPDATE settings SET FieldList=? WHERE setting_id="BulkProductEditorFields";"""

    try:
        database.execute(currentQuery, (selectedFields,))
    except Exception as e:
        print "Error saving bulk editor settings:", e
        return False

    return True


def BulkInventoryEditorSettings(database):
    currentQuery = """SELECT FieldList FROM settings WHERE setting_id="BulkInventoryEditorFields";"""

    try:
        database.execute(currentQuery)
    except Exception as e:
        print e

    settings = database.fetchone()
    if settings:
        return settings[0]
    else:
        return None


def setBulkInventoryEditorSettings(selectedFields, database):
    currentQuery = """UPDATE settings SET FieldList=? WHERE setting_id="BulkInventoryEditorFields";"""

    try:
        database.execute(currentQuery, (selectedFields,))
    except Exception as e:
        print e
        return False

    return True


def BulkCollectionEditorSettings(database):
    currentQuery = """SELECT FieldList FROM settings WHERE setting_id="BulkCollectionEditorFields";"""

    try:
        database.execute(currentQuery)
    except Exception as e:
        print e

    settings = database.fetchone()
    if settings:
        return settings[0]
    else:
        return None


def setBulkCollectionEditorSettings(selectedFields, database):
    currentQuery = """UPDATE settings SET FieldList=? WHERE setting_id="BulkCollectionEditorFields";"""

    try:
        database.execute(currentQuery, (selectedFields,))
    except Exception as e:
        print "Error: ", e
        return False

    return True


def CountryList(database):
    currentQuery = """SELECT FieldList FROM settings WHERE setting_id="CountryList";"""

    try:
        database.execute(currentQuery)
    except Exception as e:
        print "Error: ", e

    countryList = database.fetchone()

    if countryList:
        countryList = [country.split(':') for country in countryList[0].split(',')]
        return countryList


def getRedisSettings(database):
    currentQuery = """SELECT FieldList FROM settings WHERE setting_id="RedisConfig";"""
    try:
        database.execute(currentQuery)
    except Exception as e:
        print "Error: ", e
        return None

    redisConfig = database.fetchone()

    if redisConfig:
        redisConfig = [field.split('=') for field in filter(lambda i: i != '', redisConfig[0].split('<redis_split>'))]

        formattedRedisConfig = {}

        for field in redisConfig:
            formattedRedisConfig[field[0]] = field[1]

        return formattedRedisConfig


def setRedisConfig(redis_config, database):
    currentQuery = """UPDATE settings SET FieldList=? WHERE setting_id="RedisConfig";"""

    print currentQuery

    print "REDIS CONFIG:", redis_config

    try:
        database.execute(currentQuery, (redis_config,))
    except Exception as e:
        print "Error: ", e
        return None

    return True


def getDatabaseSettings(database):
    currentQuery = """SELECT FieldList FROM settings WHERE setting_id="DatabaseConfig";"""

    try:
        database.execute(currentQuery)
    except Exception as e:
        print "Error: ", e
        return None

    databaseConfig = database.fetchone()

    if databaseConfig:
        databaseConfig = [field.split('=') for field in
                          filter(lambda i: i != '', databaseConfig[0].split('<database_split>'))]

        formattedDatabaseConfig = {}

        for field in databaseConfig:
            formattedDatabaseConfig[field[0]] = field[1]

        return formattedDatabaseConfig


def setDatabaseConfig(database_config, database):
    currentQuery = """UPDATE settings SET FieldList=? WHERE setting_id="DatabaseConfig";"""

    print "DATABASE CONFIG:", database_config

    try:
        database.execute(currentQuery, (database_config,))
    except Exception as e:
        print "Error: ", e
        return None

    return True


def loadProductTags(productDatabase):
    currentQuery = """SELECT FieldList FROM settings WHERE setting_id="Tags";""";

    try:
        productDatabase.execute(currentQuery);
    except Exception as e:
        print "Error getting product tags: ", e
        return None

    tags = productDatabase.fetchone()
    if tags:
        tags = set(filter(lambda t: t != '', sorted(tags[0].split(','))))
        print "all:", tags
        return tags


def loadProductTypes(database):
    currentQuery = """SELECT FieldList FROM settings WHERE setting_id="Types";""";
    try:
        database.execute(currentQuery);
    except Exception as e:
        return None

    types = database.fetchone()
    if types:
        types = set(filter(lambda t: t != '', sorted(types[0].split(','))))
        print "all:", types
        return types


def saveProductTypes(product_types, database):
    currentQuery = """UPDATE settings SET FieldList=? WHERE setting_id="Types";"""

    try:
        database.execute(currentQuery, (product_types,))
    except Exception as e:
        print "Error: ", e
        return None

    return True
