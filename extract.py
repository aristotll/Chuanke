import re

import time
import webbrowser

reStr = '/(.{1,20})-(.{1,20}).html'
extractRe = re.compile(reStr)
i = 0
numLists = []
with open('test.txt') as f:
    for line in f:
        # print(extractRe.search(line).group(1))
        reMath = (extractRe.search(line).group(1), extractRe.search(line).group(2))
        if reMath in numLists:
            continue
        else:
            numLists.append(reMath)
        # http://stackoverflow.com/questions/29186844/how-to-close-an-internet-tab-with-cmd-python

            # command = 'http://www.chuanke.com/?mod=student&act=study&courseid={0}'.format(reMath)
            # this is study

        # http://stackoverflow.com/questions/10987453/how-to-use-chromes-network-debugger-with-redirects

        command = 'http://www.chuanke.com/?mod=order&act=create&do=freebuy&sid={}&courseid={}&r=0.8422734711305542'.format(
            *reMath)
        webbrowser.open(command)
        time.sleep(5)
        # pid = subprocess.Popen(command,shell=True)
        # i += 1
        # if i > 10:
        #     time.sleep(100)
        #     i -= 10
# subprocess.check_call(['taskkill', '/F', '/T', '/PID', str(pid)])