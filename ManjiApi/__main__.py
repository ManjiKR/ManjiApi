import argparse
from ManjiApi.server import manjiapi

parser = argparse.ArgumentParser("ManjiApi")

parser.add_argument("--host", "-H", default="0.0.0.0")
parser.add_argument("--post", "-P", default=80)

args = parser.parse_args()
manjiapi.run(args.host, args.post)
