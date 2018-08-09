import re
from datetime import timedelta

data_in: str = "Sun 10:00-20:00\nFri 05:00-10:00\nFri 16:30-23:50\nSat 10:00-24:00\nSun 01:00-04:00\n" \
         "Sat 02:00-06:00\nTue 03:30-18:15\nTue 19:00-20:00\nWed 04:25-15:14\nWed 15:14-22:40\n" \
         "Thu 00:00-23:59\nMon 05:00-13:00\nMon 15:00-21:00"

adict = {'Mon': '1', 'Tue': '2', 'Wed': '3', 'Thu': '4', 'Fri': '5', 'Sat': '6', 'Sun': '7'}

cal_entries = [0,]


def multiple_replace(text, adict):
    rx = re.compile('|'.join(map(re.escape, adict)))

    def one_xlat(match):
        return adict[match.group(0)]
    return rx.sub(one_xlat, text)


def get_timedelta(item):
    rx = re.compile("(\d) ((\d\d):(\d\d))-((\d\d):(\d\d))")
    time_d = rx.search(item)
    m_s = ((int(time_d.group(1))-1)*1440)+(int(time_d.group(3))*60+int(time_d.group(4)))
    m_e = ((int(time_d.group(1))-1)*1440)+(int(time_d.group(6))*60+int(time_d.group(7)))
    cal_entries.append(m_s)
    cal_entries.append(m_e)


data_mid = sorted(multiple_replace(data_in, adict).split('\n'))
for i in range(len(data_mid)):
    get_timedelta(data_mid[i])
cal_entries.append(7*24*60)

breaks = [x -y for x, y in zip(cal_entries[1::2], cal_entries[0::2])]
print(max(breaks))


