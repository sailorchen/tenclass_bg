from locust import task,HttpUser,between,HttpLocust,TaskSet


class MyHome(TaskSet):

    @task(1)
    def get_sale(self):
        # header = { "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
        #            "x-shop-code":"00001",
        #            "content-type":"application/json",
        #            "authorization":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjdXJyZW50LXVzZXIiOiIwOjExODrpmYjomY4iLCJleHAiOjE2MjUxMjc5NDl9.3qbgr5HF4GTyDJRZlN0DQ9ClSHAZS95OlbZiimz5lnc"}

        req = self.client.get("/bbg-crm/admin/api/v1/admin_user.self",headers = self.user.header, name="获取销售")
        # print(req.text)

    def get_real(self):
        req = self.client.get("/bbg-crm/admin/api/v1/admin_user.self",headers = self.user.header, name="获取真直播")

    def get_fake(self):
        pass


class websitUser(HttpUser):
    tasks = [MyHome]
    min_wait = 1000
    max_wait = 3000
    host = r"https://pichu-stage.tenclass.com"
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
        "x-shop-code": "00001",
        "content-type": "application/json",
        "authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjdXJyZW50LXVzZXIiOiIwOjExODrpmYjomY4iLCJleHAiOjE2MjUxMjc5NDl9.3qbgr5HF4GTyDJRZlN0DQ9ClSHAZS95OlbZiimz5lnc"}
