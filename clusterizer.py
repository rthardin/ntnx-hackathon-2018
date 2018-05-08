import requests
import time

CLOUDALIZER_IP = "35.196.167.141"
CLUSTER_IP = "10.21.55.37"
VM_UUID = "314cecaf-03cc-437d-9828-32e99fd474a9"


def toggle_vm_power():
  s = requests.Session()
  s.auth = ('admin', 'techX2018!')

  url = "https://%s:9440/api/nutanix/v2.0/vms/%s" % (
    CLUSTER_IP, VM_UUID)
  response = s.get(url, verify=False)
  vm_info = response.json()
  if vm_info.get("power_state", "").lower() == "on":
    print "VM is ON,  and will be powered OFF"
    response = s.post(url + "/set_power_state",
                      json={"transition": "ON"},
                      verify=False)
    task_info = response.json()
  else:
    print "VM is OFF, and nwill be powered ON"
    response = s.post(url + "/set_power_state",
                      json={"transition": "OFF"},
                      verify=False)
    task_info = response.json()


if __name__ == '__main__':
  while True:
    response = requests.get("http://%s/cmd" % CLOUDALIZER_IP)
    if response.status_code == 200:
      print "Something to do - cycling VM power"
      toggle_vm_power()
    else:
      time.sleep(5)
