# Location of vpncli in windows system.
vpndir = "C:\Program Files (x86)\Cisco\Cisco AnyConnect Secure Mobility Client"
config = {
        'dc': {
            'host': '<hostNameURL>',
            'uname': '<userName>',
            'pw': '<pwd>'
            },
        'prod': {
            # If hostname is not url then enclose in quotes
            'host': '"<hostName>"',
            'uname': '<userName>',
            'pw': '<pwd>'
            }
        }

