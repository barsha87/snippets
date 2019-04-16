import json
import re
from pprint import pprint
from collections import OrderedDict

mapping = json.load(open('mapping.json'), object_pairs_hook=OrderedDict)
#get_regex = {'bandwidth': '(\\d+)','encaptype': '(\\S+)', 'intf': '(\\S+)', 'intfstate': '(\\S+)', 'lineprotostate': '(\\S+)','mtu': '(\\d+)'}
get_regex = {'access_list_name': '([\w\-]+)','address_family': '(ipv[4|6])', 'sequence_number': '(\d+)', 'action': '(\S+)', 'ace': '(.+)','matches': '(\d+)'}
#textfsm = "show_interfaces_brief"
textfsm = "show_access_lists"

show_interfaces_brief_textfsm = """
#**************************************************
# Copyright (c) 2017 Cisco Systems, Inc.
# All rights reserved.
#**************************************************
Value intf (\S+)
Value intfstate (\S+)
Value lineprotostate (\S+)
Value encaptype (\S+)
Value mtu (\d+)
Value bandwidth (\d+)

Start
  ^\s*${intf}\s+${intfstate}\s+${lineprotostate}\s+${encaptype}\s+${mtu}\s+${bandwidth} -> Record
"""

show_access_lists_testfsm = """
Value Filldown access_list_name ([\w\-]+)
Value Filldown address_family (ipv[4|6])
Value Required sequence_number (\d+)
Value action (\S+)
Value ace (.+)
Value matches (\d+)


Start
  ^${address_family}\saccess-list\s+${access_list_name}
  ^\s+${sequence_number}\s+${action}\s+${ace}\s+\(${matches} -> Record
  ^${address_family}\saccess-list\s+${access_list_name}
  ^\s+${sequence_number}\s+${action}\s+${ace} -> Record
"""

with open('interfaces.txt') as f:
    config_mapper = f.read()

###################################################


configs_list = eval(config_mapper)

def get_config_val (pattern_dict, cmd, config):
    #given cmd with marker and config str and pattern_dict
    #converts cmd with marker to regex and finds map_key
    #checks whether config matches cmd regex
    #if yes checks whether config mathes dict[cmd]
    #returns dict of config value
    #import pdb; pdb.set_trace()
    map_key = re.search('\{\{(\S+)\}\}', cmd).group(1)
    cmd_regex = re.sub('\{\{'+map_key+'\}\}', get_regex[map_key], cmd)
    ret_dict = {}
    match = re.search(cmd_regex, config) 
    if match:
        ret_dict[map_key]= match.group(1)
        if isinstance(pattern_dict[cmd],dict):
            for sub_cmd in pattern_dict[cmd]:
                sub_dict, sub_key = get_config_val(pattern_dict[cmd], sub_cmd, config)
                ret_dict.update(sub_dict)
    return ret_dict, map_key

ret_list = []
for config in configs_list:
    #import pdb; pdb.set_trace()
    for cmd in mapping[textfsm]:
        config_val_dict, mapkey = get_config_val(mapping[textfsm], cmd, config)
        ret_list.append(config_val_dict)

def merge_dicts(l1, key):
  merged = {}
  for item in l1:
    if item[key] in merged:
      merged[item[key]].update(item)
    else:
      merged[item[key]] = item
  return [val for (_, val) in merged.items()]
'''
for config in configs_list:
    for cmd in mapping[textfsm]:
        config_val_dict = get_config_val(mapping[textfsm], cmd, config)
        for already_prsnt_dict in ret_list:
            pprint(ret_list)
            print(config_val_dict)
            #import pdb;pdb.set_trace()
            if all(item in already_prsnt_dict.items() for item in config_val_dict.items()):
                already_prsnt_dict.update(config_val_dict)
            elif all(item in config_val_dict.items() for item in already_prsnt_dict.items()):
                already_prsnt_dict.update(config_val_dict)
        if config_val_dict not in ret_list:
            ret_list.append(config_val_dict)
'''
#pprint(mapping['show_interfaces_brief_default'])

#import pdb; pdb.set_trace()
'''
for cmd in mapping[textfsm]:
        map_key = re.search('\{\{(\S+)\}\}', cmd).group(1)
        map_str = re.sub('\{\{'+map_key+'\}\}', get_regex[map_key], cmd)
        matches = re.findall(map_str, config_mapper)
        matches = map(lambda x: x.split('\\n')[0], matches)
        matches = list(map(lambda x: {map_key:x}, set(matches)))
#pprint(matches)
'''
#matches = list(filter(None,ret_list))
matches = sorted(merge_dicts(filter(None, ret_list), mapkey), key=lambda k: k[mapkey])
#print('################before default#############')
#pprint(matches)
#import pdb; pdb.set_trace()
###################default value population########################

textfsm_default = mapping[textfsm+'_default']
pprint(textfsm_default)
for entry in matches:
    ########## unpack  dicts and make local vars ###########
    for value_keys in entry:
        locals()[value_keys] = entry[value_keys]
        
    ########## assign default value if value not already present to local var
    for value in textfsm_default:
        if value not in locals():
            locals()[value] = textfsm_default[value]
        if value in textfsm_default[value]:
            try:
                locals()[value]= eval(textfsm_default[value])
            except:
                locals()[value] = textfsm_default[value]
        
    ############# evaluate and assign default values #######################
    for value in textfsm_default:
        try:
            locals()[value] = eval(eval(value))
        except:
            pass
        entry[value] = eval(value)
        
    ############## del local values ##################
    for value in textfsm_default:
        del locals()[value]

#############just printing##############

for match in matches:
    print (match)
print(len(matches))

