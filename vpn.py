'''
Usage python [command] [environment]
command:
    c - connect
    d - disconnect
environment:
    dev - development
    prod - production
'''
import os
import getpass
import fire
import env


def disconnect():
    '''
    Disconnect form vpn
    '''
    os.chdir(env.vpndir)
    os.system("vpncli disconnect")


def connect(to='dev'):
    '''
    Connect to VPN
    '''
    cwd = os.getcwd()
    if to not in env.config.keys():
        print('Invalid environment')
        raise ValueError
    acceptMessage = ''
    yubiKey = ''
    if to == 'prod':
        yubiKey = getpass.getpass('Touch the yubikey : ') if to == 'prod' else ''
        acceptMessage = 'y'
    with open(f'{cwd}\\creds.txt', 'w') as f:
        f.write(f"connect {env.config[to]['host']}\n")
        f.write(f"{env.config[to]['uname']}\n{env.config[to]['pw']}{yubiKey}\n{acceptMessage}")

    os.chdir(env.vpndir)
    try:
        os.system(f"vpncli -s < {cwd}\\creds.txt")
    finally:
        os.remove(f"{cwd}\\creds.txt")


if __name__ == "__main__":
    fire.Fire({"d": disconnect, "c": connect})
