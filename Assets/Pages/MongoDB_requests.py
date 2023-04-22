from pymongo import MongoClient
from Assets.Secrets.Mong_password import mongo_connection


class MongoCommons(object):
    def __init__(self):
        self.client = MongoClient(mongo_connection)
        self.db = self.client['trado_qa']
        self.users = self.db['users']
        self.products = self.db['products']
        self.departments = self.db['departments']


class MongoRequests(MongoCommons):
    def find_login_code(self, registered_num):
        for user in self.users.find({'phone': registered_num}):
            existing_user = user
            login_code = existing_user.get('loginCode')
            return login_code, existing_user

    def find_existing_branch(self, branch_name):
        for department in self.departments.find({'name': branch_name}):
            cur_department = department
            dep_name = cur_department.get('name')
            return dep_name
    def find_existing_image_branch(self, branch_name):
        for department in self.departments.find({'name': branch_name}):
            cur_department = department
            dep_name = cur_department.get('image')
            return dep_name

    def find_existing_background_image_branch(self, branch_name):
        for department in self.departments.find({'name': branch_name}):
            cur_department = department
            dep_name = cur_department.get('coverImage')
            return dep_name

    def get_mailing_list_status(self, registered_num):
        for user in self.users.find({'phone': registered_num}):
            existing_user = user
            mailing_list = existing_user.get('marketingList')
            return mailing_list

    def get_product_count(self):
        doc_count = self.products.estimated_document_count()
        return doc_count

    def get_product_info(self, product_id):
        for product in self.products.find({'barcode': product_id}):
            current_product = product
            units = current_product.get('units')
            units_in_carton = units.get('unitsInCarton')
            stock = current_product.get('productStock')
            price = current_product.get('price')
            return int(stock), float(price), int(units_in_carton)