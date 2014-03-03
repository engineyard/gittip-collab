#!/usr/bin/env python3

# Licensed to the public under the Apache License 2.0.

import base64

from urllib import request
from urllib import parse

import json
import yaml

API_URL = "https://www.gittip.com/%s/tips.json?%s"

config = yaml.load(open("config.yaml"))

giver_max = config["account"]["max_total"] / len(config["tips"])

recipients = {}

for giver in config["tips"].keys():
    giver_total = 0
    giver_recipients = config["tips"][giver]
    for recipient in giver_recipients.keys():
        recipient_tip = recipients.get(recipient, 0)
        tip_amount = giver_recipients[recipient]
        recipient_tip += tip_amount
        recipients[recipient] = recipient_tip
        giver_total += tip_amount
    if giver_total > giver_max:
        raise Exception(
            "%s wants to give %s in total" % (giver, giver_total))

tips = []

for recipient, tip_amount in recipients.items():
    tips.append({
        "username": recipient,
        "platform": "gittip",
        "amount": "%.2f" % round(tip_amount, 2)
    })

data = json.dumps(tips).encode("utf-8")

url = API_URL % (
    config["account"]["username"],
    parse.urlencode({"also_prune": 1})
)

req = request.Request(url)
req.add_header("Content-Type", "application/json")
req.add_header('Authorization',
    "Basic " + base64.urlsafe_b64encode(
        bytes("%s:" % config["account"]["api_key"], "utf-8")
    ).decode("utf-8"))

print(request.urlopen(req, data).read().decode('utf-8'))
