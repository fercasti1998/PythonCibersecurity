from scapy.all import *   #para conceder permisos de todo tipo a scapy

packet = rdpcap('http.cap')
packet

p= packet[0]
p.show()

p[TCP].dport = 8080
p.show()

p = IP()/TCP()
p.show()

p[TCP].dport = 35
p.show()
p = IP(dst="8.8.8.8")/TCP(dport=53)


p = IP(dst="8.8.8.8")/TCP(dport=53)/DNS()
p.show()