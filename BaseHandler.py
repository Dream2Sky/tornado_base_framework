import json

import tornado
import tornado.web


class BaseHandler(tornado.web.RequestHandler):

    def post(self, *args, **kwargs):
        """
        open api 通用请求
        首先解析请求的地址， 解析出对应的服务，
        然后反序列请求参数，作为对应服务方法的参数
        最后序列化返回结果作为结果返回
        :param args:
        :param kwargs:
        :return:
        """
        service_name, method_name = self.resolve_service(self.request)
        executor = getattr(self.service_initialize(service_name), method_name)
        param = json.loads(self.request.body.decode("utf-8", "ignore"))
        result = executor(param)
        result = self.deserialize_result(result)
        self.write(result)

    def resolve_service(self, request):
        """
        请求解析
        :param request:
        :return: 返回解析出来的服务路径，服务对应执行的方法名
        """
        return "", ""

    def service_initialize(self, service_name):
        pass

    def deserialize_result(self, result):
        return ""
