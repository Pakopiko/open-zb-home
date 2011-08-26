################################################################################
# Set up your parameters:
################################################################################
TCP_PORT = 4321

import hashlib
WEBSITE_PASSWORD = hashlib.md5("mypass").hexdigest() 
WEBSITE_ROOT = "/Users/ruzz/open-zb-home/Site"
WEBSITE_PORT = 8880
WEBSOCKET_PORT = 8881

ZB_PORT = '/dev/tty.usbserial-A800czWn'
ZB_SPEED = 57600

#Change with values shown on the back of your XBee Modules.


ZB={
        "2":'\x00\x13\xA2\x00\x40\x7A\x38\x58',
        "4":'\x00\x13\xA2\x00\x40\x76\x47\xB6',
        "BC":'\x00\x00\x00\x00\x00\x00\xFF\xFF'
}

############################
# To create key and certificate:
# openssl genrsa > privkey.pem
# Then:
# openssl req -new -x509 -key privkey.pem -out cacert.pem -days 1000
# feel free to comment these out if you dont want to use ssl, also update the main script accordingly.
###############################
SSL_PRIVKEY = '/Users/ruzz/open-zb-home/privkey.pem'
SSL_CERT = '/Users/ruzz/open-zb-home/cacert.pem'
