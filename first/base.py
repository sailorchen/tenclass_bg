import requests
from operator import methodcaller
class Base(object):

    #创建引流录播课
    def create_yinliu(self,token=None,env=None,shop=None,**kwargs):
        '''
        可变参数:course_name
        '''
        url="{}/study-center/admin/api/v2/course".format(env)
        course_name= '文学' if not kwargs.get("course_name") else kwargs.get("course_name")
        if 'stage' in env:
            data = {"base":{"name":course_name,"cover":"https://stage-1300403833.cos.ap-guangzhou.myqcloud.com/28271626486980349.jpg","course_way":"drainage","course_type":"ordinary","detail":{"days":10},"buy_notice_status":"off"},"payment":{"origin_price":10,"sale_price":0,"paid_type":1},"boot":{"boot_type":"personal","assigned":True,"assign_id":1257},"share":{"icon":"https://stage-1300403833.cos.ap-guangzhou.myqcloud.com/68561626487028126.jpg","description":"3454"}}
        else:
            data = {"base":{"name":course_name,"cover":"https://stage-1300403833.cos.ap-guangzhou.myqcloud.com/28271626486980349.jpg","course_way":"drainage","course_type":"ordinary","detail":{"days":10},"buy_notice_status":"off"},"payment":{"origin_price":10,"sale_price":0,"paid_type":1},"boot":{"boot_type":"personal","assigned":True,"assign_id":1257},"share":{"icon":"https://stage-1300403833.cos.ap-guangzhou.myqcloud.com/68561626487028126.jpg","description":"3454"}}
        headers = {'x-shop-code':shop,'authorization':token,'content-type':'application/json'}
        course_id = requests.post(url=url,json=data,headers=headers)
        print('创建引流录播课')

    def create_camp(self,**kwargs):
        if kwargs:
            for key,value in kwargs.items():
                print(key,value)
        print('创建引流训练课')


    def create_jiaofu(self):
        print('创建交付课')

if __name__ == '__main__':
    b = Base()
    methodcaller("create_camp",key1="333")(b)

