import requests

class AdaOtp:
    def __init__(self):
        self.get = requests.Session()
        self.apikey = ""
        self.service_otp_id = 00

    def get_info_account(self):
        response = self.get(f"https://turbootp.com/api/get-profile/{self.apikey}")
        return response.json()
    
    def set_order(self):
        response = self.get(f"https://turbootp.com/api/set-orders/{self.apikey}/{self.service_otp_id}")
        return response.json()
    
    def get_order(self, order_id):
        response = self.gett(f"https://turbootp.com/api/get-orders/{self.apikey}/{order_id}")
        return response.json()
    
    def cancle_order(self, order_id):
        response = self.get(f"https://turbootp.com/api/cancle-orders/{self.apikey}/{order_id}")
        return response.json()

    def finish_order(self, order_id):
        response = self.get(f"https://turbootp.com/api/finish-orders/{self.apikey}/{order_id}")
        return response.json()
