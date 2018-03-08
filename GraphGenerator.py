import sys
import json
import re
import config

if __name__ == "__main__":
    line_generator = open(config.datafilename)
    graph_file = open(config.filegraph, "w")

    for line in line_generator:
        line_object = json.loads(line)
        try:
            source = line_object["user"]["screen_name"]
            tweet = line_object["text"]
            re.sub("[\w]+@[\w]+\.[c][o][m]", "", tweet)
            targets = re.findall("@([a-zA-Z0-9]{1,15})", tweet)
            for target in targets:
                line="{0:20s},{1:20s}".format(source,target)
                graph_file.write(line)
                graph_file.write("\n")
                print(line)
        except KeyError:
            source = ""
            target=""
    graph_file.close()