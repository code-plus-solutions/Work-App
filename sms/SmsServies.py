import random

from kavenegar import *


def random_code():
    code = ''
    for i in range(4):
        code += str(random.randint(0, 9))
    return code


def sendSms(phone):
    try:
        code = random_code()
        api = KavenegarAPI(apikey='335A2F4979756B556B4B53616B424958717539744555653067342F483130486F574F31784E7136504534633D')
        params = {'sender': '10008663', 'receptor': f'{phone}', 'message': f'{code}'}
        response = api.sms_send(params)
        print(response)
        return code
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)