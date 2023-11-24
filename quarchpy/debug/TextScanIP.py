from quarchpy.device.scanDevices import scanDevices, lookupDevice
import socket
from quarchpy._version import __version__ as quarchpyVersion

print("Testing with quarchpy version v"+str(quarchpyVersion))

myScan=scanDevices(target_conn="TCP",ipAddressLookup="192.168.1.167")
print("Scan with IP lookup:  "+ str(myScan))

# myScan=scanDevices(target_conn="TCP")
# print("Scan with NO IP lookup:  "+ str(myScan))
