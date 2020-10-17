#!usr/bin/env python
import subprocess
import optparse


def args():
    parser = optparse.OptionParser()
    parser.add_option("-i", help="specify the interface", dest="interface")
    parser.add_option("-m", help="specify a mac address of your choice", dest="new_mac")
    (options, argument) = parser.parse_args()
    if not options.interface:
        parser.error("--> specify a interface (or) use --help for more info")
    elif not options.new_mac:
        parser.error("--> specify a mac address (or) use --help for more info")
    return options


def mac(interface, new_mac):
    print(">>> changing mac address for " + interface + " to new mac address " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    print(">>> DONE")


options = args()
mac(options.interface, options.new_mac)
