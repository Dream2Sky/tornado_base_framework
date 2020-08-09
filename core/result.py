class BaseResult():
    def __call__(cls, *args, **kwargs):
        return dict(
            state_code=200,
            errcode=0,
            errmsg=""
        )

    def __init__(self, data):
        print(type(self))
        print(isinstance(self, dict))