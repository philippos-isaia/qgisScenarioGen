import os, sys
import argparse
import datetime

parser = argparse.ArgumentParser()
parser.add_argument("--output", help="CSV Output Filename")
args = parser.parse_args()

def coordinate(id,station):
    for st in station:
        if st["id"]==id:
            return(st["coordinates"])



events=[{
    "timestep":"1",
    "mapshow":"True",
    "eventshow":"True",
    "simulator":"MATLAB",
    "id":"substation:34",
    "shape":"Polygon",
    "colourimage":"(149:156:154)",
    "what":"Electricity-blackout",
    "where":"Substation-34",
    "when":"12:00:00"
}]
print()

if args.output:
    f=open(args.output, "a")
    for item in events:
        f.write(item["timestep"]+","+item["mapshow"]+","+item["eventshow"]+","+item["simulator"]+
                ","+item["id"]+","+item["shape"]+","+coordinate(item["id"],substations)+","+item["colourimage"]+
                ","+item["what"]+","+item["where"]+","+item["when"]+"\n")
    f.close()

else:
    print("Please define CSV Output Filename")
