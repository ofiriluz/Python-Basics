import urlparse
import socket

class DNSRecord:
    def __init__(self, ip, hosts=None):
        self.__ip = None
        self.set_ip(ip)
        self.__hosts = []
        self.add_hosts(hosts)
        self.__hosts_iter = 0

    def __is_valid_ip(self, ip):
        try:
            socket.inet_aton(ip)
            return True
        except:
            return False

    def __is_valid_host(self, host):
        try:
            urlparse.urlparse(host)
            return True
        except:
            return False

    def add_host(self, host):
        # Try and parse the given the host to see if its a valid url, if not raise an exception
        if not self.__is_valid_host(host):
            raise Exception("Invalid Host given")
        self.__hosts.append(host)

    def add_hosts(self, hosts):
        if type(hosts) == list:
            for host in hosts:
                self.add_host(host)

    def get_ip(self):
        return self.__ip

    def set_ip(self, ip):
        # Check if its a valid ip, if not raise an exception
        if not self.__is_valid_ip(ip):
            raise Exception("Invalid IP given")
        self.__ip = ip

    def get_hosts(self):
        return self.__hosts

    def clear_hosts(self):
        self.__hosts.clear()

    def remove_host(self, host):
        # Will learn more about in the next parts
        self.__hosts = filter(lambda h: h != host, self.__hosts)

    def __iter__(self):
        return self

    def __next__(self):
        if self.__hosts_iter == len(self.__hosts):
            raise StopIteration
        self.__hosts_iter += 1
        return self.__hosts[self.__hosts_iter-1]

    def __str__(self):
        return self.__ip + " " + " ".join(self.__hosts)