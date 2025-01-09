import requests

#封装requests库
class ApiRequest(object):

    def send_request(self, method,url, data=None ,headers=None,cookies=None,
                     auth=None,timeout=None,allow_redirects=None,proxies=None,
                     verify=None,stream=None,cert=None ,json=None,params=None,files=None):
        self.r=requests.request(method,url, data=data, headers=headers, cookies=cookies,
                                auth=auth, timeout=timeout, allow_redirects=allow_redirects,
                                verify=verify, stream=stream, cert=cert, json=json, params=params, files=files)
        return self.r