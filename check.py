import os
import requests

webhook = os.environ["DISCORD_WEBHOOK"]

requests.post(
    webhook,
    json={
        "content": "✅ Shark Valley monitor is connected! Discord alerts are working."
    }
)

print("Discord message sent!")
