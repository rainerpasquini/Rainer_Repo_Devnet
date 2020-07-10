from ncclient import manager
import xmltodict
import xml.dom.minidom

m = manager.connect(host='ios-xe-mgmt.cisco.com', port=10000, username='developer',
                    password='C1sco12345', device_params={'name': 'csr'})

running_config = m.get_config('running')
print(xml.dom.minidom.parseString(str(running_config)).toprettyxml())
