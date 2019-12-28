import abc

class BaseDNSRequest(object):
    def __init__(self):
        pass

    @abc.abstractmethod
    def method(self):
        pass

    @abc.abstractmethod
    def api_path(self):
        pass

    @abc.abstractmethod
    def data(self):
        pass

class ListDNSRecordsRequest(BaseDNSRequest):
    def __init__(self):
        super(ListDNSRecordsRequest, self).__init__()

    def method(self):
        return "GET"

    def api_path(self):
        return "dns_records"

    def data(self):
        return {}

class ListDNSRecordsByIPRequest(BaseDNSRequest):
    def __init__(self, ip):
        self.__ip = ip
        super(ListDNSRecordsByIPRequest, self).__init__()

    def method(self):
        return "GET"

    def api_path(self):
        return "dns_records/{ip}".format(ip=self.__ip)

    def data(self):
        return {}

class AddDNSRecordRequest(BaseDNSRequest):
    def __init__(self, ip, hosts):
        self.__ip = ip
        self.__hosts = hosts
        super(AddDNSRecordRequest, self).__init__()

    def method(self):
        return "POST"

    def api_path(self):
        return "add_dns_record"

    def data(self):
        return {
            "ip": self.__ip,
            "hosts": self.__hosts
        }

class AddDNSRecordHostsRequest(BaseDNSRequest):
    def __init__(self, ip, hosts):
        self.__ip = ip
        self.__hosts = hosts
        super(AddDNSRecordHostsRequest, self).__init__()

    def method(self):
        return "POST"

    def api_path(self):
        return "add_dns_record_hosts"

    def data(self):
        return {
            "ip": self.__ip,
            "hosts": self.__hosts
        }

class RemoveDNSRecordRequest(BaseDNSRequest):
    def __init__(self, ip):
        self.__ip = ip
        super(RemoveDNSRecordRequest, self).__init__()

    def method(self):
        return "DELETE"

    def api_path(self):
        return "remove_dns_record/{ip}".format(ip=self.__ip)

    def data(self):
        return {}

class RemoveDNSRecordHostRequest(BaseDNSRequest):
    def __init__(self, host):
        self.__host = host
        super(RemoveDNSRecordHostRequest, self).__init__()

    def method(self):
        return "DELETE"

    def api_path(self):
        return "remove_dns_record_host/{host}".format(host=self.__host)

    def data(self):
        return {}

class ClearDNSRecordsRequest(BaseDNSRequest):
    def __init__(self):
        super(ClearDNSRecordsRequest, self).__init__()

    def method(self):
        return "DELETE"

    def api_path(self):
        return "clear_dns_records"

    def data(self):
        return {}