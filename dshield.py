import urllib2
import re

def get_page(url):        
        headers = {'User-Agent' : 'Mozilla 5.10'}
        request = urllib2.Request(url,None,headers)
        response = urllib2.urlopen(request)
        text = response.read()
        response.close()
        return text
 
def extractIPS(text):
        pattern = r'(([0-9]+\.){3}[0])'
        ips = [each[0] for each in re.findall(pattern, text)]   
        return ips

def write_to_file(IPs):
        if len(IPs) != 0:                
                file = open('ips_cidr_blocked.txt', 'a')
                for ips in IPs:
                        file.write(ips + '/24\n')
                file.close()


text = get_page('http://feeds.dshield.org/block.txt')
IPs = extractIPS(text)
write_to_file(IPs)



