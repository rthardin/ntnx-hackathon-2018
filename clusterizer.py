import requests


CLUSTER_IP = "10.21.55.37"


if __name__ == '__main__':
  url = "https://%s:9440/api/nutanix/v2.0/vms/" % CLUSTER_IP
  print requests.get(url)
