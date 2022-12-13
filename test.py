import sys
from steam.client import SteamClient

client = SteamClient()
client.anonymous_login()
appID = int(sys.argv[1])


def main():
    result = client.get_product_info(apps=[appID])
    result = result['apps']
    result = result[appID]
    if "config" not in result:
        return "none"
    result = result["config"]
    if "launch" not in result:
        return "none"
    result = result["launch"]
    result = result["0"]
    result = result["executable"]
    result = result.split(".")[0]

    return result

print(main())