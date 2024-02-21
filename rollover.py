'''
Author: Gulshan Rana
Email: gulshan.rana@nokia.com
Date: 21-02-2024
'''

import json
import os
import csv
import commands
import sys
from datetime import datetime as dtm

def prlogonly(o,logs):
        for r in o.splitlines():
                text=r.strip()
                print >> logs, (text.encode('utf-8'))
        r=""
        text=r.strip()
        print >> logs, (text.encode('utf-8'))
        
def Basic_UCS(sel,choice):
    os.system('cls' if os.name == 'nt' else 'clear')
    if sel:
        print("\033[91mInvalid selection.\033[00m")
    input_file=choice
    if not os.path.isdir("/tmp/ucs_log"):
             os.mkdir('/tmp/ucs_log')
    logs = open("/tmp/ucs_log/BASIC_{}.log".format(dtm.now().strftime("%Y%m%d_%H%M%S")), 'w')
    rollover_backup = open('/tmp/ucs_log/BASIC_{}_rollover_backup.txt'.format(dtm.now().strftime("%Y%m%d_%H%M%S")), 'w') 
    len=50
    
    print("=" *len)
    print("\033[95mWelcome to UCS modification\033[00m".center(len))
    print("=" * len)
    print("")
    # for loop to print weather data for every 3 hours for today
    print("-" * len)
    with open(input_file) as dd:
        df=csv.reader(dd)
        cnt=0
        succ=0
        fail=0
        for i in df:
                cnt=cnt+1
                prlogonly('\n',logs)
                print('\n')
                print("\033[94mFetching data from UCS-{}------------------count:{}\033[00m".format(i,cnt))
                prlogonly("\033[94mFetching data from UCS-{}------------------count:{}\033[00m".format(i,cnt),logs)
                curl_command_0= '''curl -k -X GET "https://labdatanpc01-oam.ncloud.vivacom.bg/services/ServiceManager/getData/UsageControlService?processParams=%7B%22name%22%3A%22{}%22%7D" -H "accept: application/json" -H "Authorization: Basic c21hZG1pbjpTcHMhc20w" -o response.json'''.format(i[0])
                curl_command_0_text= '''curl -k -X GET "https://labdatanpc01-oam.ncloud.vivacom.bg/services/ServiceManager/getData/UsageControlService?processParams=%7B%22name%22%3A%22{}%22%7D" -H "accept: application/json" -H "Authorization: Basic c21hZG1pbjpTcHMhc20w"'''.format(i[0])
                print(curl_command_0)
                prlogonly(curl_command_0_text,logs)
                s,o=commands.getstatusoutput(curl_command_0_text)
                prlogonly(o,logs)
                rollover_backup.write(o)
                rollover_backup.write('\n')
                rollover_backup.write('\n')
                print("")
                if 'error' in o:
                        fail=fail+1
                        prlogonly("\033[91mFAILING FOR UCS-{}\033[00m".format(i),logs)
                        print("\033[91mFAILING FOR UCS-{}\033[00m".format(i))
                        continue
                s,o=commands.getstatusoutput(curl_command_0)
                
                data=json.load(open("response.json",))
                name=data[0]["name"]
                desc=data[0]["desc"]
                ucsType=data[0]["ucsType"]
                sessionKey=data[0]["sessionKey"]
                priority=data[0]["priority"]
                ucsLevel=data[0]["ucsLevel"]
                quotaLimit=data[0]["quotaLimit"]
                quotaType=data[0]["quotaType"]
                quotaUnitType=data[0]["quotaUnitType"]["unitTypeName"]
                shortName=data[0]["quotaUnitType"]["shortName"]
                prlogonly("\033[96mFETCHED BELOW PARAMETERS FROM UCS-{}\033[00m".format(i),logs)
                prlogonly("\033[96mname:{}\033[00m".format(name),logs)
                prlogonly("\033[96mdesc:{}\033[00m".format(desc),logs)
                prlogonly("\033[96mucsType:{}\033[00m".format(ucsType),logs)
                prlogonly("\033[96msessionKey:{}\033[00m".format(sessionKey),logs)
                prlogonly("\033[96mpriority:{}\033[00m".format(priority),logs)
                prlogonly("\033[96mucsLevel:{}\033[00m".format(ucsLevel),logs)
                prlogonly("\033[96mquotaLimit:{}\033[00m".format(quotaLimit),logs)
                prlogonly("\033[96mquotaType:{}\033[00m".format(quotaType),logs)
                prlogonly("\033[96mquotaUnitTypeName:{}\033[00m".format(quotaUnitType),logs)
                prlogonly("\033[96mshortName:{}\033[00m".format(shortName),logs)
                curl_command_1 = '''curl -k -X PUT "https://labdatanpc01-oam.ncloud.vivacom.bg/services/ServiceManager/update/UsageControlService" -H "accept: application/json" -H "Authorization: Basic c21hZG1pbjpTcHMhc20w" -H "Content-Type: application/json" -d "{\\"name\\":\\"%s\\",\\"desc\\":\\"%s\\",\\"ucsType\\":\\"%s\\",\\"sessionKey\\":\\"%s\\",\\"priority\\":%d,\\"ucsLevel\\":\\"%s\\",\\"quotaLimit\\":%d,\\"quotaType\\":\\"%s\\",\\"allowOverage\\":false,\\"baseUnit\\":null,\\"minBaseUnit\\":null,\\"appCond\\":{\\"application\\":\\"PCRF-Rules\\",\\"rules\\":[{\\"description\\":\\"\\",\\"conditionContainer\\":{\\"subContainers\\":[{\\"subContainers\\":[],\\"conditions\\":[{\\"criteria\\":{\\"name\\":\\"Load-Row-1Key\\",\\"sourceContext\\":\\"COMPLEX_MAP\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Key-Value\\",\\"value\\":{\\"type\\":\\"ATTRIBUTE\\",\\"value\\":\\"GX_MSG_SESSION.3GPP-SGSN-Address-String\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Map-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"BG_only\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Row-Label\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"sgsn_ip_list\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"ENUM\\",\\"value\\":\\"BooleanEnum.TRUE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]},{\\"criteria\\":{\\"name\\":\\"Load-Row-1Key\\",\\"sourceContext\\":\\"COMPLEX_MAP\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Key-Value\\",\\"value\\":{\\"type\\":\\"ATTRIBUTE\\",\\"value\\":\\"GX_MSG_SESSION.AN-GW-Address-String\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Map-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"BG_only\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Row-Label\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"sgsn_ip_list\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"ENUM\\",\\"value\\":\\"BooleanEnum.TRUE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]}],\\"operator\\":\\"OR\\"},{\\"subContainers\\":[],\\"conditions\\":[{\\"criteria\\":{\\"name\\":\\"Load-Row-1Key\\",\\"sourceContext\\":\\"COMPLEX_MAP\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Key-Value\\",\\"value\\":{\\"type\\":\\"ATTRIBUTE\\",\\"value\\":\\"GX_MSG_SESSION.3GPP-SGSN-Address-String\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Row-Label\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"EU_roaming_list\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Map-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"EURoaming\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"ENUM\\",\\"value\\":\\"BooleanEnum.TRUE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]},{\\"criteria\\":{\\"name\\":\\"Subscriber-Custom-Attribute\\",\\"sourceContext\\":\\"SPR_DEVICE\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Custom-Attribute-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"CDBaseFUPConsumed\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"FALSE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]}],\\"operator\\":\\"AND\\"},{\\"subContainers\\":[],\\"conditions\\":[{\\"criteria\\":{\\"name\\":\\"Load-Row-1Key\\",\\"sourceContext\\":\\"COMPLEX_MAP\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Key-Value\\",\\"value\\":{\\"type\\":\\"ATTRIBUTE\\",\\"value\\":\\"GX_MSG_SESSION.AN-GW-Address-String\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Row-Label\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"EU_roaming_list\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Map-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"EURoaming\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"ENUM\\",\\"value\\":\\"BooleanEnum.TRUE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]},{\\"criteria\\":{\\"name\\":\\"Subscriber-Custom-Attribute\\",\\"sourceContext\\":\\"SPR_DEVICE\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Custom-Attribute-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"CDBaseFUPConsumed\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"FALSE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]}],\\"operator\\":\\"AND\\"},{\\"subContainers\\":[],\\"conditions\\":[{\\"criteria\\":{\\"name\\":\\"Load-Row-1Key\\",\\"sourceContext\\":\\"COMPLEX_MAP\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Key-Value\\",\\"value\\":{\\"type\\":\\"ATTRIBUTE\\",\\"value\\":\\"GX_MSG_SESSION.3GPP-SGSN-Address-String\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Row-Label\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"EU_roaming_list\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Map-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"EURoaming\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"ENUM\\",\\"value\\":\\"BooleanEnum.TRUE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]},{\\"criteria\\":{\\"name\\":\\"Subscriber-Custom-Attribute\\",\\"sourceContext\\":\\"SPR_DEVICE\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Custom-Attribute-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"CDAllFupsConsumed\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"TRUE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]}],\\"operator\\":\\"AND\\"},{\\"subContainers\\":[],\\"conditions\\":[{\\"criteria\\":{\\"name\\":\\"Load-Row-1Key\\",\\"sourceContext\\":\\"COMPLEX_MAP\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Key-Value\\",\\"value\\":{\\"type\\":\\"ATTRIBUTE\\",\\"value\\":\\"GX_MSG_SESSION.AN-GW-Address-String\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Row-Label\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"EU_roaming_list\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Map-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"EURoaming\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"ENUM\\",\\"value\\":\\"BooleanEnum.TRUE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]},{\\"criteria\\":{\\"name\\":\\"Subscriber-Custom-Attribute\\",\\"sourceContext\\":\\"SPR_DEVICE\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Custom-Attribute-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"CDAllFupsConsumed\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"TRUE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]}],\\"operator\\":\\"AND\\"}],\\"conditions\\":[],\\"operator\\":\\"OR\\"},\\"actions\\":[{\\"attributeInfo\\":{\\"name\\":\\"Is-Service-Applicable\\",\\"resultContext\\":\\"POLICY\\"},\\"parameters\\":[],\\"resultContext\\":\\"POLICY\\",\\"name\\":\\"Is-Service-Applicable\\"}],\\"name\\":\\"applicabilityRule\\"}]},\\"doNotDisconnect\\":null,\\"quotaUnitType\\":{\\"unitTypeName\\":\\"%s\\",\\"kindOfUnit\\":\\"VOLUME\\",\\"shortName\\":\\"%s\\",\\"defaultUnit\\":false,\\"defaultSMUnit\\":false,\\"typeConverter\\":{\\"rightSideUnit\\":\\"Byte\\",\\"leftSideValue\\":1,\\"rightSideValue\\":1048576}},\\"thresholdProfileGroupIdList\\":[\\"test_1\\"],\\"clearPenalty\\":null,\\"resetUsage\\":null,\\"assign\\":null,\\"unAssign\\":null}"''' %(name,desc,ucsType,sessionKey,priority,ucsLevel,quotaLimit,quotaType,quotaUnitType,shortName)
                curl_command_1=str(curl_command_1)
                print('\n')
                print ("\033[94mUpdating UCS-{}:\033[00m".format(i))
                
                prlogonly("Running below command for UCS-{}:".format(i),logs)
                prlogonly(curl_command_1,logs)
                prlogonly('\n',logs)
                s,o=commands.getstatusoutput(curl_command_1)                
                print(o)
                print("")
                prlogonly(o,logs)
                if "Success" not in o:
                        fail=fail+1
                        print("UCS-{} is FAILING".format(i))
                        prlogonly("UCS-{} is FAILING".format(i),logs)
                else: succ=succ+1
                #os.system('rm response.json')
        prlogonly("\033[91mSUCCESS: {}\033[00m".format(succ),logs)
        prlogonly("\033[91mFAIL: {}\033[00m".format(fail),logs)
        print("\033[91mSUCCESS: {}\033[00m".format(succ))
        print("\033[91mFAIL: {}\033[00m".format(fail))
                
    
    
    prlogonly('\n',logs)

    print("\033[92m----------PROCESS COMPLETED--------\033[00m".center(80))
    prlogonly("\033[92m----------PROCESS COMPLETED--------\033[00m",logs)
    logs.close()
    print("")
    print("=" * len)
    print("\033[93m 1. Type 1 to update with another UCS type\033[00m".ljust(len))
    print("\033[93m 2. Type 2 to go back to main menu\033[00m".ljust(len))
    print("\033[93m 0. Type 0 to close the app\033[00m".ljust(len))
    print("=" * len)
    print("")
    choice = input("YOUR SELECTION: >> ")
    if choice == 0:
        sys.exit()
    elif choice == 1:
        sub_menu1(sel=False)
        sys.exit()
    elif choice == 2:
        main_menu(sel=False)
        sys.exit()
    return choice

def FUP_UCS(sel,choice):
    os.system('cls' if os.name == 'nt' else 'clear')
    if sel:
        print("\033[91mInvalid selection.\033[00m")
    input_file=choice
    if not os.path.isdir("/tmp/ucs_log"):
             os.mkdir('/tmp/ucs_log')
    logs = open("/tmp/ucs_log/FUP_{}.log".format(dtm.now().strftime("%Y%m%d_%H%M%S")), 'w')
    rollover_backup = open('/tmp/ucs_log/FUP_{}_rollover_backup.txt'.format(dtm.now().strftime("%Y%m%d_%H%M%S")), 'w') 
    len=50
    
    
    
    print("=" *len)
    print("\033[95mWelcome to UCS modification\033[00m".center(len))
    print("=" * len)
    print("")
    # for loop to print weather data for every 3 hours for today
    print("-" * len)
    with open(input_file) as dd:
        df=csv.reader(dd)
        cnt=0
        succ=0
        fail=0
        for i in df:
                cnt=cnt+1
                prlogonly('\n',logs)
                print('\n')
                print("\033[94mFetching data from UCS-{}------------------count:{}\033[00m".format(i,cnt))
                prlogonly("\033[94mFetching data from UCS-{}------------------count:{}\033[00m".format(i,cnt),logs)
                curl_command_0= '''curl -k -X GET "https://labdatanpc01-oam.ncloud.vivacom.bg/services/ServiceManager/getData/UsageControlService?processParams=%7B%22name%22%3A%22{}%22%7D" -H "accept: application/json" -H "Authorization: Basic c21hZG1pbjpTcHMhc20w" -o response.json'''.format(i[0])
                curl_command_0_text= '''curl -k -X GET "https://labdatanpc01-oam.ncloud.vivacom.bg/services/ServiceManager/getData/UsageControlService?processParams=%7B%22name%22%3A%22{}%22%7D" -H "accept: application/json" -H "Authorization: Basic c21hZG1pbjpTcHMhc20w"'''.format(i[0])
                print(curl_command_0)
                prlogonly(curl_command_0_text,logs)
                s,o=commands.getstatusoutput(curl_command_0_text)
                prlogonly(o,logs)
                rollover_backup.write(o)
                rollover_backup.write('\n')
                rollover_backup.write('\n')
                print("")
                if 'error' in o:
                        fail=fail+1
                        prlogonly("\033[91mFAILING FOR UCS-{}\033[00m".format(i),logs)
                        print("\033[91mFAILING FOR UCS-{}\033[00m".format(i))
                        continue
                s,o=commands.getstatusoutput(curl_command_0)
                
                data=json.load(open("response.json",))
                name=data[0]["name"]
                desc=data[0]["desc"]
                ucsType=data[0]["ucsType"]
                sessionKey=data[0]["sessionKey"]
                priority=data[0]["priority"]
                ucsLevel=data[0]["ucsLevel"]
                quotaLimit=data[0]["quotaLimit"]
                quotaType=data[0]["quotaType"]
                quotaUnitType=data[0]["quotaUnitType"]["unitTypeName"]
                shortName=data[0]["quotaUnitType"]["shortName"]
                prlogonly("\033[96mFETCHED BELOW PARAMETERS FROM UCS-{}\033[00m".format(i),logs)
                prlogonly("\033[96mname:{}\033[00m".format(name),logs)
                prlogonly("\033[96mdesc:{}\033[00m".format(desc),logs)
                prlogonly("\033[96mucsType:{}\033[00m".format(ucsType),logs)
                prlogonly("\033[96msessionKey:{}\033[00m".format(sessionKey),logs)
                prlogonly("\033[96mpriority:{}\033[00m".format(priority),logs)
                prlogonly("\033[96mucsLevel:{}\033[00m".format(ucsLevel),logs)
                prlogonly("\033[96mquotaLimit:{}\033[00m".format(quotaLimit),logs)
                prlogonly("\033[96mquotaType:{}\033[00m".format(quotaType),logs)
                prlogonly("\033[96mquotaUnitTypeName:{}\033[00m".format(quotaUnitType),logs)
                prlogonly("\033[96mshortName:{}\033[00m".format(shortName),logs)
                curl_command_1 = '''curl -k -X PUT "https://labdatanpc01-oam.ncloud.vivacom.bg/services/ServiceManager/update/UsageControlService" -H "accept: application/json" -H "Authorization: Basic c21hZG1pbjpTcHMhc20w" -H "Content-Type: application/json" -d "{\\"name\\":\\"%s\\",\\"desc\\":\\"%s\\",\\"ucsType\\":\\"%s\\",\\"sessionKey\\":\\"%s\\",\\"priority\\":%d,\\"ucsLevel\\":\\"%s\\",\\"quotaLimit\\":%d,\\"quotaType\\":\\"%s\\",\\"allowOverage\\":false,\\"baseUnit\\":null,\\"minBaseUnit\\":null,\\"appCond\\":{\\"application\\":\\"PCRF-Rules\\",\\"rules\\":[{\\"description\\":\\"\\",\\"conditionContainer\\":{\\"subContainers\\":[{\\"subContainers\\":[],\\"conditions\\":[{\\"criteria\\":{\\"name\\":\\"Load-Row-1Key\\",\\"sourceContext\\":\\"COMPLEX_MAP\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Key-Value\\",\\"value\\":{\\"type\\":\\"ATTRIBUTE\\",\\"value\\":\\"GX_MSG_SESSION.3GPP-SGSN-Address-String\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Map-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"BG_only\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Row-Label\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"sgsn_ip_list\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"ENUM\\",\\"value\\":\\"BooleanEnum.TRUE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]},{\\"criteria\\":{\\"name\\":\\"Load-Row-1Key\\",\\"sourceContext\\":\\"COMPLEX_MAP\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Key-Value\\",\\"value\\":{\\"type\\":\\"ATTRIBUTE\\",\\"value\\":\\"GX_MSG_SESSION.AN-GW-Address-String\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Map-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"BG_only\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Row-Label\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"sgsn_ip_list\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"ENUM\\",\\"value\\":\\"BooleanEnum.TRUE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]}],\\"operator\\":\\"OR\\"},{\\"subContainers\\":[],\\"conditions\\":[{\\"criteria\\":{\\"name\\":\\"Load-Row-1Key\\",\\"sourceContext\\":\\"COMPLEX_MAP\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Key-Value\\",\\"value\\":{\\"type\\":\\"ATTRIBUTE\\",\\"value\\":\\"GX_MSG_SESSION.3GPP-SGSN-Address-String\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Row-Label\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"EU_roaming_list\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Map-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"EURoaming\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"ENUM\\",\\"value\\":\\"BooleanEnum.TRUE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]},{\\"criteria\\":{\\"name\\":\\"Subscriber-Custom-Attribute\\",\\"sourceContext\\":\\"SPR_DEVICE\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Custom-Attribute-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"CDBaseFUPConsumed\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"FALSE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]}],\\"operator\\":\\"AND\\"},{\\"subContainers\\":[],\\"conditions\\":[{\\"criteria\\":{\\"name\\":\\"Load-Row-1Key\\",\\"sourceContext\\":\\"COMPLEX_MAP\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Key-Value\\",\\"value\\":{\\"type\\":\\"ATTRIBUTE\\",\\"value\\":\\"GX_MSG_SESSION.AN-GW-Address-String\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Row-Label\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"EU_roaming_list\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Map-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"EURoaming\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"ENUM\\",\\"value\\":\\"BooleanEnum.TRUE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]},{\\"criteria\\":{\\"name\\":\\"Subscriber-Custom-Attribute\\",\\"sourceContext\\":\\"SPR_DEVICE\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Custom-Attribute-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"CDBaseFUPConsumed\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"FALSE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]}],\\"operator\\":\\"AND\\"},{\\"subContainers\\":[],\\"conditions\\":[{\\"criteria\\":{\\"name\\":\\"Load-Row-1Key\\",\\"sourceContext\\":\\"COMPLEX_MAP\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Key-Value\\",\\"value\\":{\\"type\\":\\"ATTRIBUTE\\",\\"value\\":\\"GX_MSG_SESSION.3GPP-SGSN-Address-String\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Row-Label\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"EU_roaming_list\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Map-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"EURoaming\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"ENUM\\",\\"value\\":\\"BooleanEnum.TRUE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]},{\\"criteria\\":{\\"name\\":\\"Subscriber-Custom-Attribute\\",\\"sourceContext\\":\\"SPR_DEVICE\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Custom-Attribute-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"CDAllFupsConsumed\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"TRUE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]}],\\"operator\\":\\"AND\\"},{\\"subContainers\\":[],\\"conditions\\":[{\\"criteria\\":{\\"name\\":\\"Load-Row-1Key\\",\\"sourceContext\\":\\"COMPLEX_MAP\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Key-Value\\",\\"value\\":{\\"type\\":\\"ATTRIBUTE\\",\\"value\\":\\"GX_MSG_SESSION.AN-GW-Address-String\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Row-Label\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"EU_roaming_list\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Map-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"EURoaming\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"ENUM\\",\\"value\\":\\"BooleanEnum.TRUE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]},{\\"criteria\\":{\\"name\\":\\"Subscriber-Custom-Attribute\\",\\"sourceContext\\":\\"SPR_DEVICE\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Custom-Attribute-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"CDAllFupsConsumed\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"TRUE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]}],\\"operator\\":\\"AND\\"}],\\"conditions\\":[],\\"operator\\":\\"OR\\"},\\"actions\\":[{\\"attributeInfo\\":{\\"name\\":\\"Is-Service-Applicable\\",\\"resultContext\\":\\"POLICY\\"},\\"parameters\\":[],\\"resultContext\\":\\"POLICY\\",\\"name\\":\\"Is-Service-Applicable\\"}],\\"name\\":\\"applicabilityRule\\"}]},\\"doNotDisconnect\\":null,\\"quotaUnitType\\":{\\"unitTypeName\\":\\"%s\\",\\"kindOfUnit\\":\\"VOLUME\\",\\"shortName\\":\\"%s\\",\\"defaultUnit\\":false,\\"defaultSMUnit\\":false,\\"typeConverter\\":{\\"rightSideUnit\\":\\"Byte\\",\\"leftSideValue\\":1,\\"rightSideValue\\":1048576}},\\"thresholdProfileGroupIdList\\":[\\"test_1\\"],\\"clearPenalty\\":null,\\"resetUsage\\":null,\\"assign\\":null,\\"unAssign\\":null}"''' %(name,desc,ucsType,sessionKey,priority,ucsLevel,quotaLimit,quotaType,quotaUnitType,shortName)
                curl_command_1=str(curl_command_1)
                print('\n')
                print ("\033[94mUpdating UCS-{}:\033[00m".format(i))
                
                prlogonly("Running below command for UCS-{}:".format(i),logs)
                prlogonly(curl_command_1,logs)
                prlogonly('\n',logs)
                s,o=commands.getstatusoutput(curl_command_1)
                print(o)
                print("")
                prlogonly(o,logs)
                if "Success" not in o:
                        fail=fail+1
                        print("UCS-{} is FAILING".format(i))
                        prlogonly("UCS-{} is FAILING".format(i),logs)
                else: succ=succ+1
                #os.system('rm response.json')
        prlogonly("\033[91mSUCCESS: {}\033[00m".format(succ),logs)
        prlogonly("\033[91mFAIL: {}\033[00m".format(fail),logs)
        print("\033[91mSUCCESS: {}\033[00m".format(succ))
        print("\033[91mFAIL: {}\033[00m".format(fail))
                
    
    
    prlogonly('\n',logs)

    print("\033[92m----------PROCESS COMPLETED--------\033[00m".center(80))
    prlogonly("\033[92m----------PROCESS COMPLETED--------\033[00m",logs)
    logs.close()
    print("")
    print("=" * len)
    print("\033[93m 1. Type 1 to update with another UCS type\033[00m".ljust(len))
    print("\033[93m 2. Type 2 to go back to main menu\033[00m".ljust(len))
    print("\033[93m 0. Type 0 to close the app\033[00m".ljust(len))
    print("=" * len)
    print("")
    choice = input("YOUR SELECTION: >> ")
    if choice == 0:
        sys.exit()
    elif choice == 1:
        sub_menu1(sel=False)
        sys.exit()
    elif choice == 2:
        main_menu(sel=False)
        sys.exit()
    return choice


def ZES_UCS(sel,choice):
    os.system('cls' if os.name == 'nt' else 'clear')
    if sel:
        print("\033[91mInvalid selection.\033[00m")
    input_file=choice
    if not os.path.isdir("/tmp/ucs_log"):
             os.mkdir('/tmp/ucs_log')
    logs = open("/tmp/ucs_log/ZES_{}.log".format(dtm.now().strftime("%Y%m%d_%H%M%S")), 'w')
    rollover_backup = open('/tmp/ucs_log/ZES_{}_rollover_backup.txt'.format(dtm.now().strftime("%Y%m%d_%H%M%S")), 'w') 
    len=50
    
    
    
    print("=" *len)
    print("\033[95mWelcome to UCS modification\033[00m".center(len))
    print("=" * len)
    print("")
    # for loop to print weather data for every 3 hours for today
    print("-" * len)
    with open(input_file) as dd:
        df=csv.reader(dd)
        cnt=0
        succ=0
        fail=0
        for i in df:
                cnt=cnt+1
                prlogonly('\n',logs)
                print('\n')
                print("\033[94mFetching data from UCS-{}------------------count:{}\033[00m".format(i,cnt))
                prlogonly("\033[94mFetching data from UCS-{}------------------count:{}\033[00m".format(i,cnt),logs)
                curl_command_0= '''curl -k -X GET "https://labdatanpc01-oam.ncloud.vivacom.bg/services/ServiceManager/getData/UsageControlService?processParams=%7B%22name%22%3A%22{}%22%7D" -H "accept: application/json" -H "Authorization: Basic c21hZG1pbjpTcHMhc20w" -o response.json'''.format(i[0])
                curl_command_0_text= '''curl -k -X GET "https://labdatanpc01-oam.ncloud.vivacom.bg/services/ServiceManager/getData/UsageControlService?processParams=%7B%22name%22%3A%22{}%22%7D" -H "accept: application/json" -H "Authorization: Basic c21hZG1pbjpTcHMhc20w"'''.format(i[0])
                print(curl_command_0)
                prlogonly(curl_command_0_text,logs)
                s,o=commands.getstatusoutput(curl_command_0_text)
                prlogonly(o,logs)
                rollover_backup.write(o)
                rollover_backup.write('\n')
                rollover_backup.write('\n')
                print("")
                if 'error' in o:
                        fail=fail+1
                        prlogonly("\033[91mFAILING FOR UCS-{}\033[00m".format(i),logs)
                        print("\033[91mFAILING FOR UCS-{}\033[00m".format(i))
                        continue
                s,o=commands.getstatusoutput(curl_command_0)
                
                data=json.load(open("response.json",))
                name=data[0]["name"]
                desc=data[0]["desc"]
                ucsType=data[0]["ucsType"]
                sessionKey=data[0]["sessionKey"]
                priority=data[0]["priority"]
                ucsLevel=data[0]["ucsLevel"]
                quotaLimit=data[0]["quotaLimit"]
                quotaType=data[0]["quotaType"]
                quotaUnitType=data[0]["quotaUnitType"]["unitTypeName"]
                shortName=data[0]["quotaUnitType"]["shortName"]
                prlogonly("\033[96mFETCHED BELOW PARAMETERS FROM UCS-{}\033[00m".format(i),logs)
                prlogonly("\033[96mname:{}\033[00m".format(name),logs)
                prlogonly("\033[96mdesc:{}\033[00m".format(desc),logs)
                prlogonly("\033[96mucsType:{}\033[00m".format(ucsType),logs)
                prlogonly("\033[96msessionKey:{}\033[00m".format(sessionKey),logs)
                prlogonly("\033[96mpriority:{}\033[00m".format(priority),logs)
                prlogonly("\033[96mucsLevel:{}\033[00m".format(ucsLevel),logs)
                prlogonly("\033[96mquotaLimit:{}\033[00m".format(quotaLimit),logs)
                prlogonly("\033[96mquotaType:{}\033[00m".format(quotaType),logs)
                prlogonly("\033[96mquotaUnitTypeName:{}\033[00m".format(quotaUnitType),logs)
                prlogonly("\033[96mshortName:{}\033[00m".format(shortName),logs)
                curl_command_1 = '''curl -k -X PUT "https://labdatanpc01-oam.ncloud.vivacom.bg/services/ServiceManager/update/UsageControlService" -H "accept: application/json" -H "Authorization: Basic c21hZG1pbjpTcHMhc20w" -H "Content-Type: application/json" -d "{\\"name\\":\\"%s\\",\\"desc\\":\\"%s\\",\\"ucsType\\":\\"%s\\",\\"sessionKey\\":\\"%s\\",\\"priority\\":%d,\\"ucsLevel\\":\\"%s\\",\\"quotaLimit\\":%d,\\"quotaType\\":\\"%s\\",\\"allowOverage\\":false,\\"baseUnit\\":null,\\"minBaseUnit\\":null,\\"appCond\\":{\\"application\\":\\"PCRF-Rules\\",\\"rules\\":[{\\"description\\":\\"\\",\\"conditionContainer\\":{\\"subContainers\\":[{\\"subContainers\\":[],\\"conditions\\":[{\\"criteria\\":{\\"name\\":\\"Load-Row-1Key\\",\\"sourceContext\\":\\"COMPLEX_MAP\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Key-Value\\",\\"value\\":{\\"type\\":\\"ATTRIBUTE\\",\\"value\\":\\"GX_MSG_SESSION.3GPP-SGSN-Address-String\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Map-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"BG_only\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Row-Label\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"sgsn_ip_list\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"ENUM\\",\\"value\\":\\"BooleanEnum.TRUE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]},{\\"criteria\\":{\\"name\\":\\"Load-Row-1Key\\",\\"sourceContext\\":\\"COMPLEX_MAP\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Key-Value\\",\\"value\\":{\\"type\\":\\"ATTRIBUTE\\",\\"value\\":\\"GX_MSG_SESSION.AN-GW-Address-String\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Map-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"BG_only\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Row-Label\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"sgsn_ip_list\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"ENUM\\",\\"value\\":\\"BooleanEnum.TRUE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]}],\\"operator\\":\\"OR\\"},{\\"subContainers\\":[],\\"conditions\\":[{\\"criteria\\":{\\"name\\":\\"Load-Row-1Key\\",\\"sourceContext\\":\\"COMPLEX_MAP\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Key-Value\\",\\"value\\":{\\"type\\":\\"ATTRIBUTE\\",\\"value\\":\\"GX_MSG_SESSION.3GPP-SGSN-Address-String\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Row-Label\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"EU_roaming_list\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Map-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"EURoaming\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"ENUM\\",\\"value\\":\\"BooleanEnum.TRUE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]},{\\"criteria\\":{\\"name\\":\\"Subscriber-Custom-Attribute\\",\\"sourceContext\\":\\"SPR_DEVICE\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Custom-Attribute-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"CDBaseFUPConsumed\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"FALSE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]}],\\"operator\\":\\"AND\\"},{\\"subContainers\\":[],\\"conditions\\":[{\\"criteria\\":{\\"name\\":\\"Load-Row-1Key\\",\\"sourceContext\\":\\"COMPLEX_MAP\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Key-Value\\",\\"value\\":{\\"type\\":\\"ATTRIBUTE\\",\\"value\\":\\"GX_MSG_SESSION.AN-GW-Address-String\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Row-Label\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"EU_roaming_list\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Map-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"EURoaming\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"ENUM\\",\\"value\\":\\"BooleanEnum.TRUE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]},{\\"criteria\\":{\\"name\\":\\"Subscriber-Custom-Attribute\\",\\"sourceContext\\":\\"SPR_DEVICE\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Custom-Attribute-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"CDBaseFUPConsumed\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"FALSE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]}],\\"operator\\":\\"AND\\"},{\\"subContainers\\":[],\\"conditions\\":[{\\"criteria\\":{\\"name\\":\\"Load-Row-1Key\\",\\"sourceContext\\":\\"COMPLEX_MAP\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Key-Value\\",\\"value\\":{\\"type\\":\\"ATTRIBUTE\\",\\"value\\":\\"GX_MSG_SESSION.3GPP-SGSN-Address-String\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Row-Label\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"EU_roaming_list\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Map-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"EURoaming\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"ENUM\\",\\"value\\":\\"BooleanEnum.TRUE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]},{\\"criteria\\":{\\"name\\":\\"Subscriber-Custom-Attribute\\",\\"sourceContext\\":\\"SPR_DEVICE\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Custom-Attribute-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"CDAllFupsConsumed\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"TRUE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]}],\\"operator\\":\\"AND\\"},{\\"subContainers\\":[],\\"conditions\\":[{\\"criteria\\":{\\"name\\":\\"Load-Row-1Key\\",\\"sourceContext\\":\\"COMPLEX_MAP\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Key-Value\\",\\"value\\":{\\"type\\":\\"ATTRIBUTE\\",\\"value\\":\\"GX_MSG_SESSION.AN-GW-Address-String\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Row-Label\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"EU_roaming_list\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Map-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"EURoaming\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"ENUM\\",\\"value\\":\\"BooleanEnum.TRUE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]},{\\"criteria\\":{\\"name\\":\\"Subscriber-Custom-Attribute\\",\\"sourceContext\\":\\"SPR_DEVICE\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Custom-Attribute-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"CDAllFupsConsumed\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"TRUE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]}],\\"operator\\":\\"AND\\"}],\\"conditions\\":[],\\"operator\\":\\"OR\\"},\\"actions\\":[{\\"attributeInfo\\":{\\"name\\":\\"Is-Service-Applicable\\",\\"resultContext\\":\\"POLICY\\"},\\"parameters\\":[],\\"resultContext\\":\\"POLICY\\",\\"name\\":\\"Is-Service-Applicable\\"}],\\"name\\":\\"applicabilityRule\\"}]},\\"doNotDisconnect\\":null,\\"quotaUnitType\\":{\\"unitTypeName\\":\\"%s\\",\\"kindOfUnit\\":\\"VOLUME\\",\\"shortName\\":\\"%s\\",\\"defaultUnit\\":false,\\"defaultSMUnit\\":false,\\"typeConverter\\":{\\"rightSideUnit\\":\\"Byte\\",\\"leftSideValue\\":1,\\"rightSideValue\\":1048576}},\\"thresholdProfileGroupIdList\\":[\\"test_1\\"],\\"clearPenalty\\":null,\\"resetUsage\\":null,\\"assign\\":null,\\"unAssign\\":null}"''' %(name,desc,ucsType,sessionKey,priority,ucsLevel,quotaLimit,quotaType,quotaUnitType,shortName)
                curl_command_1=str(curl_command_1)
                print('\n')
                print ("\033[94mUpdating UCS-{}:\033[00m".format(i))
                
                prlogonly("Running below command for UCS-{}:".format(i),logs)
                prlogonly(curl_command_1,logs)
                prlogonly('\n',logs)
                s,o=commands.getstatusoutput(curl_command_1)
                print(o)
                print("")
                prlogonly(o,logs)
                if "Success" not in o:
                        fail=fail+1
                        print("UCS-{} is FAILING".format(i))
                        prlogonly("UCS-{} is FAILING".format(i),logs)
                else: succ=succ+1
                #os.system('rm response.json')
        prlogonly("\033[91mSUCCESS: {}\033[00m".format(succ),logs)
        prlogonly("\033[91mFAIL: {}\033[00m".format(fail),logs)
        print("\033[91mSUCCESS: {}\033[00m".format(succ))
        print("\033[91mFAIL: {}\033[00m".format(fail))
                
    
    
    prlogonly('\n',logs)

    print("\033[92m----------PROCESS COMPLETED--------\033[00m".center(80))
    prlogonly("\033[92m----------PROCESS COMPLETED--------\033[00m",logs)
    logs.close()
    print("")
    print("=" * len)
    print("\033[93m 1. Type 1 to update with another UCS type\033[00m".ljust(len))
    print("\033[93m 2. Type 2 to go back to main menu\033[00m".ljust(len))
    print("\033[93m 0. Type 0 to close the app\033[00m".ljust(len))
    print("=" * len)
    print("")
    choice = input("YOUR SELECTION: >> ")
    if choice == 0:
        sys.exit()
    elif choice == 1:
        sub_menu1(sel=False)
        sys.exit()
    elif choice == 2:
        main_menu(sel=False)
        sys.exit()
    return choice


def HYBRID_UCS(sel,choice):
    os.system('cls' if os.name == 'nt' else 'clear')
    if sel:
        print("\033[91mInvalid selection.\033[00m")
    input_file=choice
    if not os.path.isdir("/tmp/ucs_log"):
             os.mkdir('/tmp/ucs_log')
    logs = open("/tmp/ucs_log/HYBRID_{}.log".format(dtm.now().strftime("%Y%m%d_%H%M%S")), 'w')
    rollover_backup = open('/tmp/ucs_log/ZES_{}_rollover_backup.txt'.format(dtm.now().strftime("%Y%m%d_%H%M%S")), 'w') 
    len=50
    
    
    
    print("=" *len)
    print("\033[95mWelcome to UCS modification\033[00m".center(len))
    print("=" * len)
    print("")
    # for loop to print weather data for every 3 hours for today
    print("-" * len)
    with open(input_file) as dd:
        df=csv.reader(dd)
        cnt=0
        succ=0
        fail=0
        for i in df:
                cnt=cnt+1
                prlogonly('\n',logs)
                print('\n')
                print("\033[94mFetching data from UCS-{}------------------count:{}\033[00m".format(i,cnt))
                prlogonly("\033[94mFetching data from UCS-{}------------------count:{}\033[00m".format(i,cnt),logs)
                curl_command_0= '''curl -k -X GET "https://labdatanpc01-oam.ncloud.vivacom.bg/services/ServiceManager/getData/UsageControlService?processParams=%7B%22name%22%3A%22{}%22%7D" -H "accept: application/json" -H "Authorization: Basic c21hZG1pbjpTcHMhc20w" -o response.json'''.format(i[0])
                curl_command_0_text= '''curl -k -X GET "https://labdatanpc01-oam.ncloud.vivacom.bg/services/ServiceManager/getData/UsageControlService?processParams=%7B%22name%22%3A%22{}%22%7D" -H "accept: application/json" -H "Authorization: Basic c21hZG1pbjpTcHMhc20w"'''.format(i[0])
                print(curl_command_0)
                prlogonly(curl_command_0_text,logs)
                s,o=commands.getstatusoutput(curl_command_0_text)
                prlogonly(o,logs)
                rollover_backup.write(o)
                rollover_backup.write('\n')
                rollover_backup.write('\n')
                print("")
                if 'error' in o:
                        fail=fail+1
                        prlogonly("\033[91mFAILING FOR UCS-{}\033[00m".format(i),logs)
                        print("\033[91mFAILING FOR UCS-{}\033[00m".format(i))
                        continue
                s,o=commands.getstatusoutput(curl_command_0)
                
                data=json.load(open("response.json",))
                name=data[0]["name"]
                desc=data[0]["desc"]
                ucsType=data[0]["ucsType"]
                sessionKey=data[0]["sessionKey"]
                priority=data[0]["priority"]
                ucsLevel=data[0]["ucsLevel"]
                quotaLimit=data[0]["quotaLimit"]
                quotaType=data[0]["quotaType"]
                quotaUnitType=data[0]["quotaUnitType"]["unitTypeName"]
                shortName=data[0]["quotaUnitType"]["shortName"]
                prlogonly("\033[96mFETCHED BELOW PARAMETERS FROM UCS-{}\033[00m".format(i),logs)
                prlogonly("\033[96mname:{}\033[00m".format(name),logs)
                prlogonly("\033[96mdesc:{}\033[00m".format(desc),logs)
                prlogonly("\033[96mucsType:{}\033[00m".format(ucsType),logs)
                prlogonly("\033[96msessionKey:{}\033[00m".format(sessionKey),logs)
                prlogonly("\033[96mpriority:{}\033[00m".format(priority),logs)
                prlogonly("\033[96mucsLevel:{}\033[00m".format(ucsLevel),logs)
                prlogonly("\033[96mquotaLimit:{}\033[00m".format(quotaLimit),logs)
                prlogonly("\033[96mquotaType:{}\033[00m".format(quotaType),logs)
                prlogonly("\033[96mquotaUnitTypeName:{}\033[00m".format(quotaUnitType),logs)
                prlogonly("\033[96mshortName:{}\033[00m".format(shortName),logs)
                curl_command_1 = '''curl -k -X PUT "https://labdatanpc01-oam.ncloud.vivacom.bg/services/ServiceManager/update/UsageControlService" -H "accept: application/json" -H "Authorization: Basic c21hZG1pbjpTcHMhc20w" -H "Content-Type: application/json" -d "{\\"name\\":\\"%s\\",\\"desc\\":\\"%s\\",\\"ucsType\\":\\"%s\\",\\"sessionKey\\":\\"%s\\",\\"priority\\":%d,\\"ucsLevel\\":\\"%s\\",\\"quotaLimit\\":%d,\\"quotaType\\":\\"%s\\",\\"allowOverage\\":false,\\"baseUnit\\":null,\\"minBaseUnit\\":null,\\"appCond\\":{\\"application\\":\\"PCRF-Rules\\",\\"rules\\":[{\\"description\\":\\"\\",\\"conditionContainer\\":{\\"subContainers\\":[{\\"subContainers\\":[],\\"conditions\\":[{\\"criteria\\":{\\"name\\":\\"Load-Row-1Key\\",\\"sourceContext\\":\\"COMPLEX_MAP\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Key-Value\\",\\"value\\":{\\"type\\":\\"ATTRIBUTE\\",\\"value\\":\\"GX_MSG_SESSION.3GPP-SGSN-Address-String\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Map-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"BG_only\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Row-Label\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"sgsn_ip_list\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"ENUM\\",\\"value\\":\\"BooleanEnum.TRUE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]},{\\"criteria\\":{\\"name\\":\\"Load-Row-1Key\\",\\"sourceContext\\":\\"COMPLEX_MAP\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Key-Value\\",\\"value\\":{\\"type\\":\\"ATTRIBUTE\\",\\"value\\":\\"GX_MSG_SESSION.AN-GW-Address-String\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Map-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"BG_only\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Row-Label\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"sgsn_ip_list\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"ENUM\\",\\"value\\":\\"BooleanEnum.TRUE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]}],\\"operator\\":\\"OR\\"},{\\"subContainers\\":[],\\"conditions\\":[{\\"criteria\\":{\\"name\\":\\"Load-Row-1Key\\",\\"sourceContext\\":\\"COMPLEX_MAP\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Key-Value\\",\\"value\\":{\\"type\\":\\"ATTRIBUTE\\",\\"value\\":\\"GX_MSG_SESSION.3GPP-SGSN-Address-String\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Row-Label\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"EU_roaming_list\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Map-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"EURoaming\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"ENUM\\",\\"value\\":\\"BooleanEnum.TRUE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]},{\\"criteria\\":{\\"name\\":\\"Subscriber-Custom-Attribute\\",\\"sourceContext\\":\\"SPR_DEVICE\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Custom-Attribute-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"CDBaseFUPConsumed\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"FALSE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]}],\\"operator\\":\\"AND\\"},{\\"subContainers\\":[],\\"conditions\\":[{\\"criteria\\":{\\"name\\":\\"Load-Row-1Key\\",\\"sourceContext\\":\\"COMPLEX_MAP\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Key-Value\\",\\"value\\":{\\"type\\":\\"ATTRIBUTE\\",\\"value\\":\\"GX_MSG_SESSION.AN-GW-Address-String\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Row-Label\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"EU_roaming_list\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Map-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"EURoaming\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"ENUM\\",\\"value\\":\\"BooleanEnum.TRUE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]},{\\"criteria\\":{\\"name\\":\\"Subscriber-Custom-Attribute\\",\\"sourceContext\\":\\"SPR_DEVICE\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Custom-Attribute-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"CDBaseFUPConsumed\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"FALSE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]}],\\"operator\\":\\"AND\\"},{\\"subContainers\\":[],\\"conditions\\":[{\\"criteria\\":{\\"name\\":\\"Load-Row-1Key\\",\\"sourceContext\\":\\"COMPLEX_MAP\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Key-Value\\",\\"value\\":{\\"type\\":\\"ATTRIBUTE\\",\\"value\\":\\"GX_MSG_SESSION.3GPP-SGSN-Address-String\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Row-Label\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"EU_roaming_list\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Map-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"EURoaming\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"ENUM\\",\\"value\\":\\"BooleanEnum.TRUE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]},{\\"criteria\\":{\\"name\\":\\"Subscriber-Custom-Attribute\\",\\"sourceContext\\":\\"SPR_DEVICE\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Custom-Attribute-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"CDAllFupsConsumed\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"TRUE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]}],\\"operator\\":\\"AND\\"},{\\"subContainers\\":[],\\"conditions\\":[{\\"criteria\\":{\\"name\\":\\"Load-Row-1Key\\",\\"sourceContext\\":\\"COMPLEX_MAP\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Key-Value\\",\\"value\\":{\\"type\\":\\"ATTRIBUTE\\",\\"value\\":\\"GX_MSG_SESSION.AN-GW-Address-String\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Row-Label\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"EU_roaming_list\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Map-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"EURoaming\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"ENUM\\",\\"value\\":\\"BooleanEnum.TRUE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]},{\\"criteria\\":{\\"name\\":\\"Subscriber-Custom-Attribute\\",\\"sourceContext\\":\\"SPR_DEVICE\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Custom-Attribute-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"CDAllFupsConsumed\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"TRUE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]}],\\"operator\\":\\"AND\\"}],\\"conditions\\":[],\\"operator\\":\\"OR\\"},\\"actions\\":[{\\"attributeInfo\\":{\\"name\\":\\"Is-Service-Applicable\\",\\"resultContext\\":\\"POLICY\\"},\\"parameters\\":[],\\"resultContext\\":\\"POLICY\\",\\"name\\":\\"Is-Service-Applicable\\"}],\\"name\\":\\"applicabilityRule\\"}]},\\"doNotDisconnect\\":null,\\"quotaUnitType\\":{\\"unitTypeName\\":\\"%s\\",\\"kindOfUnit\\":\\"VOLUME\\",\\"shortName\\":\\"%s\\",\\"defaultUnit\\":false,\\"defaultSMUnit\\":false,\\"typeConverter\\":{\\"rightSideUnit\\":\\"Byte\\",\\"leftSideValue\\":1,\\"rightSideValue\\":1048576}},\\"thresholdProfileGroupIdList\\":[\\"test_1\\"],\\"clearPenalty\\":null,\\"resetUsage\\":null,\\"assign\\":null,\\"unAssign\\":null}"''' %(name,desc,ucsType,sessionKey,priority,ucsLevel,quotaLimit,quotaType,quotaUnitType,shortName)
                curl_command_1=str(curl_command_1)
                print('\n')
                print ("\033[94mUpdating UCS-{}:\033[00m".format(i))
                
                prlogonly("Running below command for UCS-{}:".format(i),logs)
                prlogonly(curl_command_1,logs)
                prlogonly('\n',logs)
                s,o=commands.getstatusoutput(curl_command_1)
                print(o)
                print("")
                prlogonly(o,logs)
                if "Success" not in o:
                        fail=fail+1
                        print("UCS-{} is FAILING".format(i))
                        prlogonly("UCS-{} is FAILING".format(i),logs)
                else: succ=succ+1
                #os.system('rm response.json')
        prlogonly("\033[91mSUCCESS: {}\033[00m".format(succ),logs)
        prlogonly("\033[91mFAIL: {}\033[00m".format(fail),logs)
        print("\033[91mSUCCESS: {}\033[00m".format(succ))
        print("\033[91mFAIL: {}\033[00m".format(fail))
                
    
    prlogonly('\n',logs)

    print("\033[92m----------PROCESS COMPLETED--------\033[00m".center(80))
    prlogonly("\033[92m----------PROCESS COMPLETED--------\033[00m",logs)
    logs.close()
    print("")
    print("=" * len)
    print("\033[93m 1. Type 1 to update with another UCS type\033[00m".ljust(len))
    print("\033[93m 2. Type 2 to go back to main menu\033[00m".ljust(len))
    print("\033[93m 0. Type 0 to close the app\033[00m".ljust(len))
    print("=" * len)
    print("")
    choice = input("YOUR SELECTION: >> ")
    if choice == 0:
        sys.exit()
    elif choice == 1:
        sub_menu1(sel=False)
        sys.exit()
    elif choice == 2:
        main_menu(sel=False)
        sys.exit()
    return choice

# define sub_menu2 function on the basis of below definitions
def sub_menu2(sel,choice):
    input_file=choice
    len=50

    os.system('cls' if os.name == 'nt' else 'clear')
    if sel:
        print("\033[91mInvalid selection.\033[00m")
    print("="*len)
    print("\033[95m Welcome to UCS modification\033[00m".center(len))
    print("="*len)
    print("")
    print("-" * len)
    print("\033[93m 1. Type 1 for Basic UCS updation\033[00m".ljust(len))
    print("-" * len)
    print("\033[93m 2. Type 2 for FUP UCS updation\033[00m".ljust(len))
    print("-" * len)
    print("\033[93m 3. Type 3 for ZES UCS updation\033[00m".ljust(len))
    print("-" * len)
    print("\033[93m 4. Type 4 for HYBRID UCS updation\033[00m".ljust(len))
    print("-" * len)
    print("\033[93m 9. Type 9 to return to Main Menu\033[00m".ljust(len))
    print("-" * len)
    print("\033[93m 0. Type 0 to close the app\033[00m".ljust(len))
    print("-" * len)
    print("")
    #prepare sub_menu2 choices
    choice = input("YOUR SELECTION: >> ")
    
    if choice == 0:
        sys.exit()
    elif choice == 9:
        main_menu(sel=False)
        sys.exit()
    elif choice not in [1,2,3,4,9]:
        choice = sub_menu1(sel=True)
    else:
        if choice == 1:
            Basic_UCS(sel=False,choice=input_file)
        elif choice == 2:
            FUP_UCS(sel=False,choice=input_file)
        elif choice == 3:
            ZES_UCS(sel=False,choice=input_file)
        elif choice == 4:
            HYBRID_UCS(sel=False,choice=input_file)
        else:
            choice = sub_menu1(sel=True)
    return choice

# define sub_menu1 function on the basis of below definitions
def sub_menu1(sel):
    os.system('cls' if os.name == 'nt' else 'clear')
    len=50
    if sel:
        print("\033[91m Invalid selection \033[00m")
    print("=" * len)
    print("\033[95m Welcome to UCS modification\033[00m".center(len))
    print("=" * len)
    print("")
    print("-" * len)
    print("\033[93m Please enter the input file name in csv format:\033[00m".ljust(len))
    print("-" * len)
    print("")
    #prepare sub_menu1 choices
    choice = input("YOUR SELECTION: >> ")
    
    
    if choice[-3:]!='csv':
        print ("\033[91mFile format is wrong!!!\033[00m")
        sys.exit()

    if not os.path.isfile(choice):     
        print ("\033[91minput_file file not found in current directory.\033[00m")
        sys.exit()
        
    sub_menu2(sel=False,choice=choice)     
    return choice


# define main_menu function for weather forecast app
def main_menu(sel):
    os.system('cls' if os.name == 'nt' else 'clear')
    len=50
    #base condition
    if sel:
        print("\033[91mInvalid selection.\033[00m")
    print("="*len)
    print("\033[95mWelcome to UCS modification\033[00m".center(len))
    print("="*len)
    print("")
    print("-" * len)
    print("\033[93m 1. Type 1 to start Bulk UCS updation\033[00m".ljust(len))
    print("\033[93m 0. Type 0 to close the app\033[00m".ljust(len))
    print("-" * len)

    print("")
    choice = input("YOUR SELECTION: >> ")
    
    #prepare main_menu choices
    if choice == 0:
        sys.exit()
    elif choice == 1:
        sub_menu1(sel=False)
    else:
        main_menu(sel=True)
    
    return choice

# define main function for weather forecast app
if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("\033[91mInvalid Usage\033[00m")
        print("\033[93mUsage        : ./{0} or python {0}".format(sys.argv[0]))
        print("")
        sys.exit(1)
    
    while True:
        main_menu(sel=False)
        input("Press Enter to continue...")
