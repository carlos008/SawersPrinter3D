import platform
import glob
from util import profile


def serialList(forAutoDetect=False):
    baselist=[]
    if platform.system() == "Windows":
        try:
            key=_winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,"HARDWARE\\DEVICEMAP\\SERIALCOMM")
            i=0
            while True:
                values = _winreg.EnumValue(key, i)
                if not forAutoDetect or 'USBSER' in values[0]:
                    baselist+=[values[1]]
                i+=1
        except:
            pass
    if forAutoDetect:
        baselist = baselist + glob.glob('/dev/ttyUSB*') + glob.glob('/dev/ttyACM*') + glob.glob("/dev/cu.usb*")
        baselist = filter(lambda s: not 'Bluetooth' in s, baselist)
        prev = profile.getMachineSetting('serial_port_auto')
        if prev in baselist:
            baselist.remove(prev)
            baselist.insert(0, prev)
    else:
        baselist = baselist + glob.glob('/dev/ttyUSB*') + glob.glob('/dev/ttyACM*') + glob.glob("/dev/cu.*") + glob.glob("/dev/tty.usb*") + glob.glob("/dev/rfcomm*")
    if version.isDevVersion() and not forAutoDetect:
        baselist.append('VIRTUAL')
    return baselist
serialList(True)