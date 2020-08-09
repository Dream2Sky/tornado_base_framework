import traceback
from typing import Union

import tornado.web

from errors import AppException


class BaseHandler(tornado.web.RequestHandler):

    def __init__(self, application, request, **kwargs) -> None:
        super().__init__(application, request, **kwargs)
        self.err_code = 0
        self.err_msg = ""
        self.trace_info = ""
        self.base_result = dict(
            err_code=self.err_code,
            err_msg=self.err_msg,
            data=None
        )

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
        service_result = dict()
        try:
            service_name, method_name = self.resolve_service(self.request)
            dynamic_service = self.service_initialize(service_name)
            # if not hasattr(dynamic_service, method_name):
            #     raise Exception("invalid open api url")
            #
            # executor = getattr(dynamic_service, method_name)
            # param = json.loads(self.request.body.decode("utf-8", "ignore"))
            # result = executor(param)
            # result = self.deserialize_result(result)
            # service_result = self.deserialize_result(dict())
            service_result = dict()

        except AppException as ex:
            self.set_status(ex.status_code)
            self.err_code = ex.err_code
            self.err_msg = ex.err_msg
        except Exception as ex:
            self.set_status(500)
            self.err_msg = str(ex)
            self.trace_info = traceback.format_exc()

        self.write(service_result)

    def write(self, chunk: Union[str, bytes, dict]) -> None:
        self.base_result.update(dict(err_code=self.err_code, err_msg=self.err_msg, data=chunk))
        if self.trace_info:
            self.base_result["trace_info"] = self.trace_info
        chunk = self.base_result
        super().write(chunk)

    def resolve_service(self, request):
        """
        请求解析
        :param request:
        :return: 返回解析出来的服务路径，服务对应执行的方法名
        """
        return "", ""

    def service_initialize(self, service_name):
        return object()

    def deserialize_result(self, result):
        return ""
