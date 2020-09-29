# winciscovpncli
Update env.py with the correct values of dev and prod credentials and hostnames

    NAME
        vpn
    
    DESCRIPTION
        Usage python [command] [environment]
        command:
            c - connect
            d - disconnect
        environment:
            dev - development
            prod - production
    
    FUNCTIONS
        connect(to='dc')
            Connect to VPN
    
        disconnect()
            Disconnect form vpn
    

## Create a run command for the cli
    
    Create a shortcut to the vpn.py file.
    Copy the shortcut to C:\Windows\
        Run command 
            "vpn c dev" connects to development environment.
            "vpn c prod" connects to production environment.
            "vpn d" disconnects the vpn
