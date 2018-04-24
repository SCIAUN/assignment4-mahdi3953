import nmap


def port_scanner():
    All_Hosts = {'192.168.1.1','192.168.1.2','192.168.1.3','192.168.1.4'
        ,'192.168.1.5','192.168.1.6','192.168.1.7',
        '192.168.1.8','192.168.1.9','192.168.1.10'}
    nm =  nmap.PortScanner()
    for h in All_Hosts:
        nm.scan(h,'21-1000')
        content = "Host : %s = %s"%(h,nm.scaninfo()) + '\n'
        write_to_file(content)


def write_to_file(content):
    file = open('Result.txt','a')
    file.write(content)
    file.close()

def main():
    port_scanner()

main()
