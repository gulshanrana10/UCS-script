'''
Author: Gulshan Rana
Email: gulshan.rana@nokia.com
Date: 22-02-2024
'''

import os
import commands

priority=5500
suffix=1
number_of_ucs=500
from datetime import datetime as dtm
file = open('create_ucs_{}.csv'.format(dtm.now().strftime("%Y%m%d_%H%M%S")), 'w') 

for i in range(number_of_ucs):
    name='''T-UCS_%d'''%(suffix)
    curl_command_1 = '''curl -k -X POST "https://labdatanpc01-oam.ncloud.vivacom.bg/services/ServiceManager/create/UsageControlService" -H "accept: application/json" -H "Authorization: Basic c21hZG1pbjpTcHMhc20w" -H "Content-Type: application/json" -d "{\\"name\\":\\"%s\\",\\"desc\\":\\"%sGB quota for home\\",\\"ucsType\\":\\"BASIC\\",\\"sessionKey\\":\\"1000\\",\\"priority\\":%d,\\"ucsLevel\\":\\"SESSION\\",\\"quotaLimit\\":%d,\\"quotaType\\":\\"TOTAL\\",\\"allowOverage\\":false,\\"shareSessionUsage\\":false,\\"baseUnit\\":1,\\"minBaseUnit\\":1,\\"appCond\\":{\\"application\\":\\"PCRF-Rules\\",\\"rules\\":[{\\"description\\":\\"\\",\\"conditionContainer\\":{\\"subContainers\\":[{\\"subContainers\\":[],\\"conditions\\":[{\\"criteria\\":{\\"name\\":\\"Load-Row-1Key\\",\\"sourceContext\\":\\"COMPLEX_MAP\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Key-Value\\",\\"value\\":{\\"type\\":\\"ATTRIBUTE\\",\\"value\\":\\"GX_MSG_SESSION.AN-GW-Address-String\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Map-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"BG_only\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Row-Label\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"sgsn_ip_list\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"ENUM\\",\\"value\\":\\"BooleanEnum.TRUE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]},{\\"criteria\\":{\\"name\\":\\"Load-Row-1Key\\",\\"sourceContext\\":\\"COMPLEX_MAP\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Key-Value\\",\\"value\\":{\\"type\\":\\"ATTRIBUTE\\",\\"value\\":\\"GX_MSG_SESSION.3GPP-SGSN-Address-String\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Map-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"BG_only\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Row-Label\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"sgsn_ip_list\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"ENUM\\",\\"value\\":\\"BooleanEnum.TRUE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]},{\\"criteria\\":{\\"name\\":\\"Load-Row-1Key\\",\\"sourceContext\\":\\"COMPLEX_MAP\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Key-Value\\",\\"value\\":{\\"type\\":\\"ATTRIBUTE\\",\\"value\\":\\"GX_MSG_SESSION.3GPP-SGSN-Address-String\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Row-Label\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"EU_roaming_list\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Map-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"EURoaming\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"ENUM\\",\\"value\\":\\"BooleanEnum.TRUE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]},{\\"criteria\\":{\\"name\\":\\"Load-Row-1Key\\",\\"sourceContext\\":\\"COMPLEX_MAP\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Key-Value\\",\\"value\\":{\\"type\\":\\"ATTRIBUTE\\",\\"value\\":\\"GX_MSG_SESSION.AN-GW-Address-String\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Row-Label\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"EU_roaming_list\\"},\\"valueArguments\\":[]},{\\"name\\":\\"Map-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"EURoaming\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"ENUM\\",\\"value\\":\\"BooleanEnum.TRUE\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]}],\\"operator\\":\\"OR\\"}],\\"conditions\\":[{\\"criteria\\":{\\"name\\":\\"Subscriber-Custom-Attribute\\",\\"sourceContext\\":\\"SPR_DEVICE\\"},\\"criteriaArguments\\":[{\\"name\\":\\"Custom-Attribute-Name\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"TariffType\\"},\\"valueArguments\\":[]}],\\"criteriaAdjustOperator\\":null,\\"criteriaAdjustValue\\":[],\\"operator\\":\\"EQUAL\\",\\"value\\":{\\"type\\":\\"STRING\\",\\"value\\":\\"ZES\\"},\\"valueArguments\\":[],\\"adjustOperator\\":null,\\"adjustValue\\":[]}],\\"operator\\":\\"AND\\"},\\"actions\\":[{\\"attributeInfo\\":{\\"name\\":\\"Is-Service-Applicable\\",\\"resultContext\\":\\"POLICY\\"},\\"parameters\\":[],\\"resultContext\\":\\"POLICY\\",\\"name\\":\\"Is-Service-Applicable\\"}],\\"name\\":\\"applicabilityRule\\"}]},\\"doNotDisconnect\\":null,\\"quotaUnitType\\":{\\"unitTypeName\\":\\"MByte\\",\\"kindOfUnit\\":\\"VOLUME\\",\\"shortName\\":\\"MB\\",\\"defaultUnit\\":false,\\"defaultSMUnit\\":false,\\"typeConverter\\":{\\"rightSideUnit\\":\\"Byte\\",\\"leftSideValue\\":1,\\"rightSideValue\\":1048576}},\\"thresholdProfileGroupIdList\\":[\\"test_1\\"],\\"clearPenalty\\":null,\\"resetUsage\\":null,\\"assign\\":null,\\"unAssign\\":null}"''' %(name,suffix,priority,suffix)
    
    suffix+=1
    priority+=1
    file.write(name)
    file.write('\n')    
    #print(curl_command_1)
    s,o=commands.getstatusoutput(curl_command_1)                
    print(o)

file.close()
