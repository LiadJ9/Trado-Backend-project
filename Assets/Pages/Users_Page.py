import Assets.Pages.Backend_utils as U
from Assets.Pages.Commons import Commons


class UsersPage(Commons):
    def search_first_name_to_search(self):
        search = Commons(self.driver).wait_for(Commons.SEARCH_BAR)
        search.send_keys(Commons.FIRST_NAME)
        search.send_keys(Keys.ENTER)

    def search_partial_name_to_search(self):
        search = Commons(self.driver).wait_for(Commons.SEARCH_BAR)
        search.send_keys('jac')
        search.send_keys(Keys.ENTER)

    def insert_first_name_into_user_details(self):
        search = Commons(self.driver).wait_for(Commons.first_name_box)
        search.send_keys(Commons.FIRST_NAME)

    def insert_last_name_into_user_details(self):
        search = Commons(self.driver).wait_for(Commons.last_name_box)
        search.send_keys(Commons.LAST_NAME)

    def insert_id_into_user_details(self):
        search = Commons(self.driver).wait_for(Commons.id_box)
        search.send_keys(Commons.ID)

    def insert_email_into_user_details(self):
        search = Commons(self.driver).wait_for(Commons.email_box)
        search.send_keys(Commons.EMAIL)

    def insert_phone_number_into_user_details(self):
        search = Commons(self.driver).wait_for(Commons.phone_number_box)
        search.send_keys(Commons.PHONE)

    def insert_additional_phone_number_into_user_details(self):
        search = Commons(self.driver).wait_for(Commons.additional_phone_number_box)
        search.send_keys(Commons.PHONE)

    def insert_city_into_user_details(self):
        search = Commons(self.driver).wait_for(Commons.city_box)
        search.send_keys(Commons.CITY)

    def insert_street_into_user_details(self):
        search = Commons(self.driver).wait_for(Commons.street_box)
        search.send_keys(Commons.STREET)

    def insert_building_into_user_details(self):
        search = Commons(self.driver).wait_for(Commons.building_box)
        search.send_keys(Commons.BUILDING)

    def insert_apartment_into_user_details(self):
        search = Commons(self.driver).wait_for(Commons.apartment_box)
        search.send_keys(Commons.APARTMENT)

    def insert_floor_into_user_details(self):
        search = Commons(self.driver).wait_for(Commons.floor_box)
        search.send_keys(Commons.FLOOR)

    def insert_comment_into_user_details(self):
        search = Commons(self.driver).wait_for(Commons.comment_box)
        search.send_keys(Commons.COMMENT)

    def insert_account_owner_into_user_details(self):
        search = Commons(self.driver).wait_for(Commons.account_owner_box)
        search.send_keys(Commons.ACCOUNT_OWNER)

    def insert_number_account_into_user_details(self):
        search = Commons(self.driver).wait_for(Commons.number_account_box)
        search.send_keys(Commons.NUMBER_ACCOUNT)

    def insert_number_branch_into_user_details(self):
        search = Commons(self.driver).wait_for(Commons.number_branch_box)
        search.send_keys(Commons.NUMBER_BRANCH)

    def insert_bank_name_into_user_details(self):
        search = Commons(self.driver).wait_for(Commons.bank_name_box)
        search.send_keys(Commons.BANK_NAME)

    def insert_credit_score_into_user_details(self):
        search = Commons(self.driver).wait_for(Commons.credit_score)
        search.send_keys(Commons.CREDIT_SCORE)

    def insert_balance_into_user_details(self):
        search = Commons(self.driver).wait_for(Commons.balance_box)
        search.send_keys(Commons.BALANCE)

    def insert_income_into_user_details(self):
        search = Commons(self.driver).wait_for(Commons.income_box)
        search.send_keys(Commons.INCOME)

    def insert_outcome_into_user_details(self):
        search = Commons(self.driver).wait_for(Commons.outcome_box)
        search.send_keys(Commons.OUTCOME)

    pass
