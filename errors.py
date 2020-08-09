# -*- coding: utf-8 -*-
import json

from tornado.web import HTTPError


class AppException(HTTPError):
    """
    统一错误码处理
    status_code
    """

    def __init__(self, status_code, err_code, err_msg, error_info=None):
        self.err_obj = {
            'errcode': err_code,
            'errmsg': err_msg
        }
        if error_info:
            self.err_obj["error_info"] = error_info
        self.status_code = status_code
        self.err_code = err_code
        self.err_msg = err_msg
        self.log_message = json.dumps(self.err_obj)

        HTTPError.__init__(self, status_code, self.log_message)

    def add_info(self, key, value):
        self.err_obj[key] = value
        return self

    def description(self, _desc):
        self.add_info('description', _desc)
        return self

    def __str__(self):
        return '{}：{}({})'.format(
            self.err_obj['errcode'],
            self.err_obj['errmsg'],
            self.err_obj.get("description")
        )


# AUTH 类错误返回
AUTH_PASSWORD_ERROR = AppException(401, 11002, '密码错误')
AUTH_VALID_CODE_ERROR = AppException(401, 11006, '验证码错误')
AUTH_TOKEN_INVALID = AppException(401, 10001, '登录信息错误')
AUTH_COMPANY_INVALID = AppException(401, 10001, '访问信息与登录公司不符')
AUTH_TOKEN_NOT_COMPACT = AppException(401, 10001, '访问令牌不合法')
NO_PERMISSION_LOGIN = AppException(401, 11011, '没有权限登录')
LOGIN_CODE_EXPIRE = AppException(401, 11012, '登录信息已过期')
LOGIN_SIGNATURE_NOT_COMPACT = AppException(401, 11013, '签名不符')
LOGIN_SSO_PHONE_NOT_NULL = AppException(401, 11014, '单点登录手机号不能为空')
LOGIN_BLACK_LIST = AppException(401, 11015, '系统黑名单用户')
USER_NOT_EXIST = AppException(401, 11023, '用户不存在')
USER_PASSWORD_NOT_EFFECT = AppException(401, 11024, '密码不符合规则')
LOGIN_ACCESS_CONTROL = AppException(401, 11016, '该企业已启用接入限制')
AUTH_PASSWORD_ERROR_MAX_TIME = AppException(401, 11018, '密码错误超过最大次数,帐号锁定十分钟')
AUTH_IMG_CODE_ERROR = AppException(401, 11019, '图片验证码错误')
UPLOAD_FORBIDDEN_FILE_EXTEND = AppException(401, 11020, '不被允许的上传文件扩展名')
USER_SOURCE_MODEL_NOT_EXIST = AppException(401, 11021, '未找到用户载体')
USER_ACCESS_URL_ERROR = AppException(401, 11022, '用户接入域名错误')

# 绑定关系类
BINDING_USER_EMP_NOT_EXIST = AppException(404, 11003, '用户无法绑定职员：信息不符')
BINDING_WE_CHAT_NOT_BINDING = AppException(401, 11008, '微信用户未绑定')
BINDING_THIRD_NO_OPEN_APP = AppException(401, 11009, '当前应用还未开通')
NOT_BIND_MODIFY_META_USER = AppException(401, 11051, '还未填写元数据更改者')
NOT_BIND_MODIFY_ROLE_USER = AppException(401, 11051, '还未填写权限操作者')

# Token 验证
COMPANY_KEY_INVALID = AppException(401, 10002, 'Company Key Invalid')

# 微信服务类
SERVICE_NOT_AVAILABLE = AppException(400, 20001, '服务发生故障')
MAP_SERVICE_NOT_AVAILABLE = AppException(400, 20002, 'QQ地图服务故障')
USER_NOT_SUBSCRIBE = AppException(400, 20002, '用户未关注')

WE_CHAT_API_LIMITED_REACHED = AppException(400, 20005, '微信API调用次数超限')
WE_CHAT_DECRYPT_VALIDATE_ERROR = AppException(400, 20006, '微信消息解密错误')
WE_CHAT_SERVICE_ERROR = AppException(400, 20007, '服务发生错误')
WE_CHAT_REFRESH_TOKEN_ERROR = AppException(400, 20008, '微信Refresh Token失效')
WE_CHAT_NOT_REGISTER = AppException(400, 20008, '微信公众号未注册')
WE_CHAT_PERIPHERAL_EQUIPMENT_TICKET_EXPIRE = AppException(400, 20010, '周边地址ticket过期')
WE_CHAT_PERIPHERAL_EQUIPMENT_TIME_EXPIRE = AppException(400, 20011, '周边地址信息已过期，请重新摇一摇')
WE_CHATAPP_NOT_REGISTER = AppException(400, 20012, '小程序在系统中还未注册')

WE_CHAT_IP_RESTRICT_ERROR = AppException(400, 20009, '微信服务IP访问限制')

# openid服务类
SERVICE_OPENID_NOT_AVAILABLE = AppException(400, 20001, 'openid服务故障')

# 数据校验
DATA_JSON_CONVERT_ERROR = AppException(400, 40001, 'JSON格式转换错误，无法转换')
DATA_FIELD_NOT_FOUND = AppException(400, 40002, '数据字段不完整')
COMPANY_IS_NOT_REGISTER = AppException(400, 40003, '企业未注册')
ARTICLE_CONTENT_TOO_LONG = AppException(400, 40004, '圈子消息超长')
META_DATA_REPEAT = AppException(400, 40005, "元数据包含和上一层级重复内容")

DATA_CONVERT_ERROR = AppException(400, 40005, 'Data Convert Error')
USER_PHONE_NOT_VALID = AppException(403, 40006, '手机号不合法')
ALREADY_SEND_PHONE_CODE = AppException(403, 40007, '已发送过验证码，还未过期')
USER_PHONE_VALID_CODE_ERROR = AppException(403, 40006, '手机号不合法')
ALREADY_SEND_SSC_CONTENT = AppException(403, 40008, '请勿频繁发送消息')
ALREADY_SEND_EXCEED_MAX_TIMES = AppException(403, 40009, '今天这个号码已超过最大发送次数')
# 权限
PERMISSION_USER_NOT_LOGIN = AppException(403, 50001, '用户未登录')
PERMISSION_EMP_ROLE_ERROR = AppException(403, 51002, '用户没有绑定职员')
PERMISSION_COMMON_ROLE_ERROR = AppException(403, 51002, '用户没有操作所需要的业务权限')
PERMISSION_ADMIN_ROLE_ERROR = AppException(403, 51002, '用户没有系统管理员权限')
HCM_PERMISSION_ADMIN_ROLE_ERROR = AppException(403, 51002, '用户没有HCM系统管理员权限')
PERMISSION_COMPANY_ADMIN_ROLE_ERROR = AppException(403, 51003, '用户没有公司管理员权限')
PERMISSION_NOT_ACCESS_METHOD = AppException(403, 51005, '当前帐号无权限访问此方法')
CURRENT_CONTEXT_IS_NULL = AppException(403, 51006, '当前登陆信息已失效')

# CONFIG
CONFIG_KEY_NOT_EXISTS = AppException(401, 61001, 'Config Not Exists')
TEMPLATE_NOT_EXISTS = AppException(401, 61002, 'Template Not Exists')
ES_CONNECTION_ERROR = AppException(401, 61003, 'es链接错误, 请检查es部署情况以及相关配置')

# REST
DATA_NOT_FOUND = AppException(500, 80001, '您请求的数据不存在')
DATA_RULE_ERROR = AppException(500, 80002, '数据规则错误')
NO_PERMISSION_VIEW_DATA = AppException(500, 80003, '您没有权限查看该数据')
ACCOUNT_IS_PERMISSION = AppException(500, 80011, '您的账号被禁用')
API_NOT_PERMIT = AppException(500, 80002, 'API未授权，不允许访问')
NUMBER_DUP_ERROR = AppException(500, 80005, '编码重复')
DATA_FILE_PATH_NOT_EXIST = AppException(500, 61002, 'Data File Path Not Exist')
DATA_HAS_DELETED = AppException(500, 61003, 'Data Has Deleted')
TEMP_DATA_HAS_DELETED = AppException(500, 61004, '您的链接数据已失效')

# OpenAPI
OPEN_API_NOT_FOUND = AppException(400, 90001, '您请求的OpenAPI不存在')
PARAMS_IS_NONE = AppException(400, 90002, 'params没有配置描述')
PARAMS_IS_INVALID = AppException(400, 90003, '您传递的参数无法匹配')
SOURCES_IS_NONE = AppException(400, 90004, 'sources没有配置描述')
RESULT_IS_NONE = AppException(400, 90005, 'result没有配置描述')
SOURCE_NAME_NOT_FOUND = AppException(400, 90006, 'source的name配置为空')
SOURCE_PARAMS_NOT_FOUND = AppException(400, 90007, 'source的params配置为空')
SOURCE_SERVICE_NOT_FOUND = AppException(400, 90008, 'source的service配置为空')
SOURCE_SERVICE_TYPE_NOT_FOUND = AppException(400, 90009, 'source中service的type设置为空')
SOURCE_SERVICE_TYPE_IS_INVALID = AppException(400, 90010, 'source中service的type设置无效，type只能为self_sercie或hcm_cloud或expand')
SOURCE_SERVICE_MODULE_NOT_FOUND = AppException(400, 90011, 'source中service的module设置为空')
SOURCE_SERVICE_CLASS_NOT_FOUND = AppException(400, 90012, 'source中service的class设置为空')
SOURCE_HANDLER_CLASS_NOT_FOUND = AppException(400, 90013, 'source中service的handler设置为空')
FETCH_OFFLINE_ERROR = AppException(400, 90014, '访问线下API报错')
OFFLINE_LOGIN_MAX_ERROR = AppException(400, 90017, '访问线下API报错')

# 系统授信
SYS_AUTH_ERROR = AppException(400, 90014, '系统授信失败')
SYS_INVOKE_API_ERROR = AppException(400, 90014, '系统间调用接口失败')

SYS_OUTER_AUTH_TOKEN_EXPIRE = AppException(400, 90019, 'token不合法')
SYS_OUTER_AUTH_FAILD = AppException(400, 90020, '系统间授信登陆失败')

# Channel
PRIVATE_CHANNEL = AppException(400, 80001, '私人频道，禁止关注')
SYSTEM_CHANNEL = AppException(400, 80002, '系统频道，不能进行操作')
OWNER_CHANNEL = AppException(400, 80003, '您本人的频道，无需操作')
CHANNEL_PERMISSION = AppException(400, 80004, '您无权查看该频道')
CHANNEL_MESSAGE_PERMISSION = AppException(400, 80005, '您无权查看该消息')
LOGIN_OFFLINE_ERROR = AppException(400, 90015, '登录线下系统出错')
OFFLINE_SERVICE_NAME_ERROR = AppException(400, 90018, '服务名称不合法')
TASK_EXEC_ERROR = AppException(400, 80015, '任务执行错误')

ONLY_CLOSE_SELFSERVICE_CAN_BE_DELETE = AppException(401, 11002, '只有关闭状态的服务才能删除')
ONLY_CUSTOMER_CAN_BE_DELETE = AppException(401, 11003, '只有个性化定制内容才能删除')

SEND_MOBILE_MSG_ERROR = AppException(500, 12001, '发送短信消息失败')

JOIN_FIELD_NOT_EXIST = AppException(500, 12011, 'table join field not exist')

# setting
HAVE_SUB_INFO_NOT_DELETE = AppException(500, 13001, '还有下级信息不能删除')
HAVE_NO_PERMISSION_TO_DELETE = AppException(500, 13003, '您没有权限删除这个信息')
HAVE_NO_PERMISSION_TO_VIEW = AppException(500, 13004, '您没有权限查看这个信息')
HAVE_NO_PERMISSION_TO_MODIFY = AppException(500, 13002, '您没有权限修改这个信息')
INFOMATION_NOT_VALID = AppException(500, 13003, '信息不合法')

# employee_history
JOB_NOT_EXIST = AppException(500, 14001, '对应的岗位不存在')
PART_JOB_ERROR = AppException(500, 14007, '兼职岗位信息出错')
EMPLOYEE_NOT_EXIST = AppException(500, 14004, '对应的人员不存在')
JOB_INFO_NOT_VALID = AppException(500, 14002, '岗位信息不合法')
EXIST_PRIMARY_JOB_NOT_TERMINATE = AppException(500, 14003, '存在未终止的主岗位')
ACTION_TARGET_NOT_EXIST = AppException(500, 14005, '变动目标参数不存在')
ACTION_EMPLOYEE_NOT_EXIST = AppException(500, 14006, '变动员工不存在')
DEPARTMENT_NOT_EXIST = AppException(500, 14007, '组织不存在')
POSITION_NOT_EXIST = AppException(500, 14008, '职位不存在')
ACTION_JOB_NOT_EXIST = AppException(500, 14009, '职务不存在')
ACTION_JOBGRADE_NOT_EXIST = AppException(500, 14010, '职等不存在')
ACTION_JOBLEVEL_NOT_EXIST = AppException(500, 14011, '职级不存在')
ACTION_JOBTYPE_NOT_EXIST = AppException(500, 14012, '任职类型不能为空')
ACTION_POSITION_STATUS_NOT_EXIST = AppException(500, 14013, '职级不存在')
ACTION_EMPLOYEECATEGORY_NOT_EXIST = AppException(500, 14014, '用工类型不能为空')
MODIFY_JOB_NOT_EXIST = AppException(500, 14015, '指定业务日期对应岗位上的任职不存在')
MODIFY_JOB_ALREADY_EXIST = AppException(500, 14016, '系统已存在岗位的任职')
ACTION_EMPLOYEE_NOT_EXIST = AppException(500, 14017, '员工不存在')
ACTION_SOURCE_EMPLOYEE_CATEGPRY_NOT_VALID = AppException(500, 14018, '原用工类型不合法')
ACTION_SOURCE_POSITIONSTATUS_NOT_VALID = AppException(500, 14018, '原岗位状态不合法')
ACTION_TARGET_EMPLOYEE_CATEGPRY_NOT_VALID = AppException(500, 14018, '目标用工类型不合法')
ACTION_TARGET_POSITIONSTATUS_NOT_VALID = AppException(500, 14018, '目标岗位状态不合法')
ACTION_SOURCE_POSITIONTYPE_NOT_VALID = AppException(500, 14019, '原岗位类别不合法')
ACTION_PRIMARY_JOB_NOT_EXIST = AppException(500, 14020, '兼职的任职时间需晚于主职任职时间')
ACTION_PRIMARY_JOB_NOT_TERMINATE = AppException(500, 14021, '主任职还未结束')
ORG_HAS_MODIFY_NOT_MODIFY = AppException(500, 14022, '已做过变更,不能再变更')
ORG_NO_PERMISSION = AppException(500, 14023, '没有权限查看组织')
ACTION_ALREADY_BUSINESS_NOT_REBACK = AppException(500, 14024, '后续已经做过业务了,不能撤消')
ACTION_BUSINESS_ALREADY_MODIFY_NOT_REBACK = AppException(500, 14025, '业务已发生变化,不能撤消')

BUSINESS_SOURCE_EMPLOYEE_CATEGPRY_NOT_VALID = AppException(500, 14022, '入口用工类型不合法')
BUSINESS_SOURCE_POSITIONSTATUS_NOT_VALID = AppException(500, 14023, '入口岗位状态不合法')
BUSINESS_TARGET_NOT_EXIST = AppException(500, 14024, '业务目标参数不存在')
BUSINESS_IN_NOT_EXIST = AppException(500, 14025, '业务入口参数不存在')
ALREADY_BUSINESS_NOT_REBACK = AppException(500, 14026, '后续已做过业务，不允许回退')
ID_CARD_NOT_VALID = AppException(500, 14027, '身份证号不合法')
BUSINESS_TARGET_EMPLOYEE_CATEGPRY_NOT_VALID = AppException(500, 14028, '出口用工类型不匹配')
BUSINESS_TARGET_POSITIONSTATUS_NOT_VALID = AppException(500, 14029, '出口岗位状态不匹配')
BUSINESS_TARGET_POSITIONTYPE_NOT_VALID = AppException(500, 14030, '出口任职类型不匹配')
PRIMARY_JOB_NOT_DELETE = AppException(500, 14031, "主任职不允许删除")
RULE_UNDEFINED = AppException(500, 14033, "顺序号规则未预置")
ID_CARD_DUPLICATE = AppException(500, 14034, '身份证号重复')
FUTURE_MANY_BUSINESS = AppException(500, 14032, '不允许多版本回退')
PRE_EMPLOYEE_ID_DUPLICATE = AppException(500, 14035, '人员重复导入')
PARTTIME_JOB_NOT_TERMINATE = AppException(500, 14036, '存在未终止的非主岗位')
PRIMARY_JOB_ONLY_ONE = AppException(500, 14037, '主岗位必须唯一')
NOT_REVISE_TWO_VERSION = AppException(500, 14038, '不能跨两个业务做修订业务')
COMMON_TIPS_ERROR = AppException(500, 14039, '')

# security
NOT_MANAGER_NOT_OPERATE = AppException(500, 15001, '您不是管理员，不能操作')
NOT_ONLYOWNER_NOT_OPERATE = AppException(500, 15001, '您不是系统拥有者，不能操作')
NOT_VALID_GRANTINFO = AppException(500, 15001, '非法的授权数据')
INVALID_OPERATION = AppException(500, 15001, '无效操作')
MANAGER_NOT_GRANT_SELF = AppException(500, 15015, '管理员不能给自己授权')

NO_PERMISSION_NEED_GRANT = AppException(500, 15005, '无合法授权信息，需要进行授权')

AUTH_CODE_EXPIRE = AppException(500, 16001, '授权信息已过期')

EXECUTE_OPEN_API_ERROR = AppException(500, 17003, '执行OpenApi报错')

EMP_CACHE_NOT_EXIST = AppException(500, 18001, '员工缓存信息不存在')
DEPT_CACHE_NOT_EXIST = AppException(500, 18002, '部门缓存信息不存在')
COMMON_BASIC_CACHE_NOT_EXIST = AppException(500, 18004, '辅助信息缓存不存在')
REDIS_QUEUE_IS_FULL = AppException(500, 19001, 'redis queue is full')

NO_PERMISSION_TO_ACCESS_DATA = AppException(500, 18003, '无权限访问数据')

GEO_SECRETVALUE_OVERDUE = AppException(500, 21001, 'geo坐标加密的时间戳已过期')

MOBILE_ATTEND_SOURCE_NOT_WX = AppException(500, 21002, '移动签到异常，需从微信登录')

MOBILE_ATTEND_SOURCE_NOT_APP = AppException(500, 21004, '移动打卡异常，需从微信或app登录')

MOBILE_ATTEND_SOURCE_VIRTUAL = AppException(500, 21003, '不允许使用虚拟机打卡')

REMOTE_INVOKE_ERROR = AppException(500, 22001, '远程调用服务报错')

ATTEND_BALANCE_NOT_SUFFICIENT = AppException(500, 21005, '假期余额不足')

PERMISSION_DB_TABLE_ERROR = AppException(500, 21007, '无权操作指定数据表')

# cadre vote
NAME_DUP_ERROR = AppException(500, 30001, '名称重复')
PARENT_DATA_FOUND = AppException(500, 30002, '上级数据不存在')
NEED_GROUP = AppException(500, 30003, '必须指定分组')
HAS_VOTED = AppException(500, 30004, '已经投过票了')
HAS_DATA_UNDER_GROUP = AppException(500, 30005, '分组下还有投票人')

# donation
HAS_DONATION = AppException(400, 30001, '你已经捐过款了')

# Handler
USER_AGENT_ERROR = AppException(400, 70001, 'User Agent Error')
BROWSER_NOT_ACCEPT_ERROR = AppException(400, 70002, 'Browser Not Accept Error')
NEED_WE_CHAT_ERROR = AppException(400, 70003, 'Need WeChat')
DOMAIN_NOT_EXIST_ERROR = AppException(400, 70004, 'Domain not Exists')

WE_CHAT_SETTING_ERROR = AppException(400, 70005, 'We Chat Setting Error')

APPLY_JOB_NOT_EXIST = AppException(400, 23001, '投递的岗位不存在')

SECURITY_LEVEL_NOT_ALLOW = AppException(400, 24001, '您的密级没有权限查看')

SYN_USER_NOT_VALID = AppException(400, 25001, '同步用户名与密码不正确')
SYN_DATA_NOT_VALID_JSON = AppException(400, 25002, '同步数据')

DICTIONARY_ONLY_ONE_OBJECT = AppException(400, 26002, '一次只允许一个对象的值')
DICTIONARY_FIELD_NOT_EXIST = AppException(400, 26003, '字段不存在')

# workflow_online
WORKFLOW_NODES_NOT_EMPTY = AppException(400, 28001, '流程节点未配置')
WORKFLOW_DATA_DISPLAY_NOT_VALID = AppException(400, 28002, '流程表单展示未配置')
WORKFLOW_DATA_DEFINE_NOT_VALID = AppException(400, 28003, '流程表单数据未配置')
WORKFLOW_EVENT_NOT_EXIST = AppException(400, 28004, '定义时流程事件未配置')
WORKFLOW_EVENT_IS_ERROR = AppException(400, 28004, '流程事件报错')
WORKFLOW_HAS_NO_AUTH_VIEW_DATA = AppException(400, 28005, '身份验证失败')
WORKFLOW_NO_PERMIT_MODIFY = AppException(400, 28006, '插件上的公司验证失败')
WORKFLOW_INST_HAS_START = AppException(400, 28007, '流程实例已启动')
WORKFLOW_INST_EVENT_ERROR = AppException(400, 28008, '运行时找不到事件')
WORKFLOW_RANGE_NOT_FOUND = AppException(400, 28009, '流程适用范围没有找到')
WORKFLOW_RANGE_PARENT_NOT_FOUND = AppException(400, 28010, '流程上级流程没找到')

WORKFLOW_BUSINESS_NOT_EFFECT = AppException(400, 28009, '业务还未定义')
WORKFLOW_NOT_FOUND = AppException(400, 28010, '流程没找到')
WORKFLOW_NO_PERMISSION = AppException(400, 28011, '当前流程没有权限访问')
WORKFLOW_NOT_FOUND_PARENT = AppException(400, 28012, '没有找到上一流程节点')
WORKFLOW_NOT_FOUND_EXECUTOR = AppException(400, 28013, '没有找到下一节点审批人,请联系系统管理员维护审批人!')
WORKFLOW_FORM_DATA_CHECKER = AppException(400, 28014, '数据格式错误')
WORKFLOW_CONFIG_ERROR = AppException(400, 28015, '流程配置错误')

MAX_MESSAGE_SEND_LIMIT = AppException(400, 290001, '单个手机号超过短信发送上限')
RESTRICT_IP_LIMIT = AppException(400, 290002, '发送短信IP限制')
SEND_MSG_SERVICE_NOT_USED = AppException(400, 290003, '短信服务不可用')
SEND_EMAIL_SERVICE_NOT_USED = AppException(400, 290005, '邮件服务不可用')
SEND_VOICE_SERVICE_NOT_USED = AppException(400, 290004, '语音验证码服务不可用')

SCRIPT_NOT_VALID = AppException(400, 300001, '脚本不合法')
FLEX_SCRIPT_NOT_VALID = AppException(400, 300002, '脚本配置错误')

OUTER_REQUEST_FAILED = AppException(500, 300010, '外部请求失败')
SAML_REQUEST_ERROR = AppException(400, 300044, 'SAML请求解析失败')

THIRD_CONTRACT_WF_ERROR = AppException(500, 300033, '电子合同流程异常')
THIRD_CONTRACT_ERROR = AppException(500, 18004, '电子合同异常')

RESUME_FETCH_MOBILE_ERROR = AppException(500, 310034, '解析失败，没有提取到手机号')
RESUME_TRANSLATE_ERROR = AppException(500, 310035, '简历解析失败')
RESUME_INTO_HCM_ERROR = AppException(500, 310036, '简历入库失败')
LANXIN_API_URL_NOT_FOUND = AppException(500, 310037, '蓝信api地址未设置')
LANXIN_REQUEST_ERROR = AppException(500, 310038, '蓝信请求失败')

COMPANY_NOT_FOUND = AppException(500, 310096, "未找到企业信息")
SHORT_URL_INVALIDED = AppException(500, 310097, "短链已失效")


class HandlerIndexException(Exception):
    def __init__(self, title, info, oper_href=None, oper_caption=None):
        self.title = title
        self.info = info
        self.oper_href = oper_href
        self.oper_caption = oper_caption


class BrowserPlugInException(Exception):
    def __init__(self, title, info, oper_href=None, oper_caption=None):
        self.title = title
        self.info = info
        self.oper_href = oper_href
        self.oper_caption = oper_caption
