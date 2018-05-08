import requests


CLUSTER_IP = "10.21.55.37"
VM_UUID = "314cecaf-03cc-437d-9828-32e99fd474a9"


if __name__ == '__main__':
  s = requests.Session()
  s.auth = ('admin', 'techX2018!')

  url = "https://%s:9440/api/nutanix/v2.0/vms/%s" % (
    CLUSTER_IP, VM_UUID)
  response = s.get(url)
  print response
  vm_info = response.json()
  if vm_info.get("power_state", "").lower() == "on":
    print "VM is ON"
  else:
    print "VM is OFF"
