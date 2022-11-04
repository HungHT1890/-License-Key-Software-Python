from subprocess import check_output
from requests import session
def get_product_id():
    data_key = check_output('systeminfo').decode("utf-8").split("\n")
    Product_ID = ''
    for x in data_key:
        if 'Product ID' in x:
            Product_ID = (x.split('Product ID:')[1].strip())
            break
    return Product_ID

def get_bios_number():
    data_key = check_output('wmic diskdrive get SerialNumber').decode().split("\n")[1].strip().strip('\r')
    return data_key

def get_ip_v4():
    return session().get('https://api.ipify.org?format=json').json()['ip']

def creat_key_soft(key_name):
    main_key = get_bios_number()
    ip_key = get_ip_v4()
    if main_key == '':
        back_up_key = get_product_id()+f'_{ip_key}_{key_name}'
        return back_up_key
    else:
        return main_key+f'_{key_name}'


# contact: t.me/hunght1890
# email: hungsaki2003@gmail.com

