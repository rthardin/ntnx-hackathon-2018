from flask import Flask, request, Response


app = Flask(__name__)


outstanding_requests = 0


@app.route("/")
def main():
  return "Nutanix Hackathon 2018 - Did It All For The Cookies"


@app.route("/cmd")
def main():
  global outstanding_requests
  if request.method == 'POST':
    outstanding_requests += 1
    return "Request received! Outstanding requests: %d" % outstanding_requests
  elif request.method == 'GET':
    if outstanding_requests > 0:
      outstanding_requests -= 1
      return Response("Time to do work", status=200)
    else:
      return Response("Nothing to do - try again later", status=503)
  else:
    return Response("Method not supported", status=405)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
