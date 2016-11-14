import sys
from SOAPpy import SOAPProxy
import xml.etree.ElementTree as ET
#serverUrl='localhost:8081'#
serverUrl='54.212.246.204:8081'
namespace='xml'
server = SOAPProxy(serverUrl, namespace) 
#server.update_xml('testa',["Adventure"],["asdasd"],'asasd','1','May','1999')
#response = server.test()
server.movieRemove("testa")
response = server.movieNameFromeType("Adventure")
print response