def is_valid_ipv4(self, IP):
    parts = IP.split('.')

    if len(parts) != 4:
        return False

    for part in parts:
        if not part:
            return False

        if len(part) > 1 and part[0] == '0':
            return False

        for char in part:
            if not char.isdigit():
                return False

        num = int(part)

        if not 0 <= num <= 255:
            return False

    return True


def is_valid_ipv6(IP):
    chars = set(['A', 'B', 'C', 'D', 'E', 'F'])
    nums = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

    parts = IP.split(':')

    if len(parts) != 8:
        return False

    for part in parts:
        if not 0 < len(part) <= 4:
            return False

        for char in part:
            if char.isdigit():
                if char not in nums:
                    return False
            elif char.isalpha():
                if char.upper() not in chars:
                    return False
            else:
                return False

    return True


def validIPAddress(self, IP: str) -> str:
    if '.' in IP:
        if self.is_valid_ipv4(IP):
            return 'IPv4'
    elif ':' in IP:
        if self.is_valid_ipv6(IP):
            return 'IPv6'

    return 'Neither'
