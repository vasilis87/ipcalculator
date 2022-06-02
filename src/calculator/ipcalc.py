def ipcalculator(prefix: str):
    """
    This function gets prefix in format 10.255.5.1/26 and calculates network address,mask,wildcard mask,
    broadcast address firs host ip and last host ip. And returns this values as string in dot decimal format
    :param prefix: str
            prefix ipaddress/prefixlenght
    :return: list of strings
            (network,mask,wildcard_mask,broadcast , first hop , last hop )
            ex.('10.255.5.0', '255.255.255.248', '0.0.0.7', '10.255.5.7', '10.255.5.1', '10.255.5.6')
    """
    ipaddress, prefix_lenght = prefix.split(sep='/')

    prefix_lenght = int(prefix_lenght)
    if prefix_lenght > 32:
        raise ValueError("Preffic lenght cant be more than 32")

    maskpattern = ('1' * prefix_lenght) + ('0' * (32 - prefix_lenght))
    inversemaskpattern = ('0' * prefix_lenght) + ('1' * (32 - prefix_lenght))

    maskbinary = [maskpattern[0:8], maskpattern[8:16], maskpattern[16:24], maskpattern[24:32]]
    inversemaskbinary = [inversemaskpattern[0:8], inversemaskpattern[8:16], inversemaskpattern[16:24],
                         inversemaskpattern[24:32]]

    maskdecimary = ['0b' + value for value in maskbinary]
    maskdecimary = [int(value, 2) for value in maskdecimary]

    wildcard = ['0b' + value for value in inversemaskbinary]
    wildcard = [int(value, 2) for value in wildcard]

    ipaddresstr = ipaddress.split(sep='.')

    networkaddress = [(int(ipaddresstr[i]) & maskdecimary[i]) for i in range(4)]
    broadcast = [int(ipaddresstr[i]) | wildcard[i] for i in range(4)]

    first = [networkaddress[i] if i != 3 else int(networkaddress[i]) + 1 for i in range(4)]
    last = [broadcast[i] if i != 3 else int(broadcast[i]) - 1 for i in range(4)]

    networkaddress = [str(value) for value in networkaddress]
    maskdecimary = [str(value) for value in maskdecimary]
    wildcard = [str(value) for value in wildcard]
    broadcast = [str(value) for value in broadcast]
    first = [str(value) for value in first]
    last = [str(value) for value in last]

    return '.'.join(networkaddress), '.'.join(maskdecimary), '.'.join(wildcard), '.'.join(broadcast), '.'.join(
        first), '.'.join(last)



if __name__ == '__main__':
    print(ipcalculator('10.12.19.65/30'))

