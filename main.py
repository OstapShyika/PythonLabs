import re
from zipfile import ZipFile

with ZipFile("access_log_Jul95.zip") as zip_manager:
    zip_manager.extractall()

logfile = open("access_log_Jul95", "r")
logs_list = logfile.read().split("\n")

machine_pattern = ' - - \\[| '

successful_logs_pattern = re.compile(".*(\\[08/Jul/1995:(07:11:3[7-9]|[4-5][0-9]|"
                                     "0[8-9]:[0-5][0-9]:[0-5][0-9]|"
                                     "1[0-9]:[0-5][0-9]:[0-5][0-9]|2[0-3]:[0-5][0-9]:[0-5][0-9])|"
                                     "\\[[8-9]/Jul/1995:([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]|"
                                     "\\[10/Jul/1995:(0[0-7]:[0-5][0-9]:[0-5][0-9]|08:([0-1][0-2]:[0-5]"
                                     "[0-9]|13:([0-2][0-9]|3[0-7])))).*(200).*")
successful_logs_dict = {}
for line in logs_list:
    separated_log = re.split(machine_pattern, line)
    machine_name = separated_log[0]
    request_matches = re.match(successful_logs_pattern, line)
    if request_matches:
        successful_logs_dict[machine_name] = successful_logs_dict.get(machine_name, 0) + 1

for k, v in successful_logs_dict.items():
    print(f'{k} - {v} successful logs')
