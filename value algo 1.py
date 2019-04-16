dummy_template_dict = {}
dummy_template_dict['show_policy_map_interface.textfsm']='''
#**************************************************
# Copyright (c) 2017 Cisco Systems, Inc.
# All rights reserved.
#**************************************************
Value Filldown intf_class (\S+)
Value Filldown statistics (\S+)
Value Required statistics_key (([A-Za-z\(\)\-\/]+) | (([A-Za-z\(\)\-\/]+)\s+([A-Za-z\(\)\-\/]+))|(([A-Za-z\(\)\-\/]+)\s+([A-Za-z\(\)\-\/]+)\s+([A-Za-z\(\)\-\/]+))) 
Value packets (\d+)
Value bytes (\d+)
Value rate (\d+)

Start
  ^(\s+)?Class\s+${intf_class}
  ^\s+${statistics}\s+statistics -> Record
  ^\s+${statistics_key}\s+:\s+${packets}/${bytes}\s+${rate} -> Record 
  ^\s+${statistics_key}(\s+)?:\s+${packets}/${bytes} -> Record
'''
dummy_template_dict['show_interfaces_brief.textfsm']='''
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
'''
#all config_cmds from script
config_cmds= [
'class-map prec_class1\n match precedence 1 \n end-class-map',
'policy-map prec_dscp_policy \n class prec_class1 \n police rate 100 kbps burst 1000 bytes',
'interface tenGigE 0/0/0/2/5 \n service-policy input prec_dscp_policy',
'interface tenGigE 0/0/0/2/5',
'username aaa password pass'
]

show_cmds = ['show policy-map interface tenGigE 0/0/0/2/5', 'show interfaces']

templates_db = ['show_policy_map_interface.textfsm', 'show_interfaces_brief.textfsm', 'show_policy_map_interface_bundle_input_member.textfsm']

keywords = ['policy-map', 'interface', 'class-map',
            'match-any', 'match', 'precedence', 'end-class-map',
            'class', 'service-policy', 'username', 'password', 'interfaces']
all_configs= {}
#optional keywords: values or keys
########################################################

import re
'''
def get_all_matches (show_cmds, config_cmds):
    # show_cmds : list of all show commands from db
    # config_cmds : list of all config commands from db
    # returns matches based on priority
    
    for cmd in show_cmds:
        template = get_template(cmd)
        if template is not None:
            #do things
'''
'''
def get_all_matches (show_cmd):
    # show_cmd : show command from script
    # returns list of config_cmd matches in order of priority
    # config_cmds list from script???
    #todo: get list of all config_cmds from db
    match_list = []
    show_keys, show_key_val = get_keywords(show_cmd)
    #print(show_keys, show_key_val)
    for keyword in show_keys:
        for conf_cmd in all_configs:
            #import pdb; pdb.set_trace()
            conf_keys= all_configs[conf_cmd][0]
            if keyword in conf_keys:
                #index of keyword
                #print(conf_keys.index(keyword))
                #todo: make score a dict , func of cmd; decrement score
                score = show_keys.index(keyword) + conf_keys.index(keyword)
                match_list.append((conf_cmd, score))
                #insert at index
                #score based on index
    #print(match_list)
    match_list.sort(key= lambda x: x[1])
    return match_list
'''
def get_all_matches (show_cmd):
    # show_cmd : show command from script
    # returns list of config_cmd matches in order of priority
    # config_cmds list from script???
    #todo: get list of all config_cmds from db
    match_dict = {}
    show_keys, show_key_val = get_keywords(show_cmd)
    #print(show_keys, show_key_val)
    for keyword in show_keys:
        for conf_cmd in all_configs:
            #import pdb; pdb.set_trace()
            conf_keys= all_configs[conf_cmd][0]
            if keyword in conf_keys:
                score = 100 - show_keys.index(keyword) + conf_keys.index(keyword)
                if conf_cmd in match_dict:
                    match_dict[conf_cmd] += score
                else:
                    match_dict[conf_cmd] = score
    #print(match_list)
    match_list = sorted(match_dict, key=match_dict.get, reverse= True)
    return match_list

def generate_config_keywords(config_cmds):
    for cmd in config_cmds:
        conf_keys, conf_key_val = get_keywords(cmd)
        #print(conf_keys, conf_key_val)
        all_configs[cmd] = (conf_keys, conf_key_val)
        #to do : store in db
    
def get_keywords(cmd):
    # cmd : config or show cmd
    # returns list of keywords in cmd( in order)
    # dict of keyword value pairs

    #todo : how can we know if its a keyword ?? cmd file??
    #todo: handle when keywords are values; optional keywords
    keys = []
    key_val = {}
    cmd = cmd.split(' ')
    for i,word in enumerate(cmd):
        if word in keywords:
            keys.append(word),
            key_val[word] = None
            for next_word in cmd[i+1:]:
                if next_word in keywords:
                    break
                else:
                    if key_val[word] is None:
                        key_val[word] = ''
                    key_val[word] = (key_val[word]+' '+ next_word).strip()
    return keys, key_val

#patterns.py
def get_template (show_cmd):
    # returns template from db based on longest string match else None
    #todo: admin mode
    # how to handle non-standard template names
    file_name = re.split(' |-', show_cmd)
    while file_name:
        #todo: check in db for filename
        if '_'.join(file_name)+'.textfsm' in templates_db:
            file_name= '_'.join(file_name)+'.textfsm'
            # todo: get template contents from db
            return dummy_template_dict[file_name]
        else:
            file_name = file_name[:-1]

def populate_template(filename, key_val_dict, ):
    #returns the parsed value of the textfsm template
    #temp return: just the populated template string
    #filename: template filename
    #key_val_dict: key_val from get_keywords()
    #todo: multiple dicts or concated dicts shd be passed
    #example outputs in db for learning with example configs????
    pass
    
#################################################################
            
#get_all_matches(show_cmds, config_cmds)
'''
print('############ get keywords output ###############')
a,sample= get_keywords('show policy-map interface tenGigE 0/0/0/2/5')
for key in a:
    print("key:%s, val:%s" %(key, sample[key]))
#################################
 
generate_config_keywords(config_cmds)
#################################
print('\n########## get all matches output #########')
#print(get_all_matches('show policy-map interface tenGigE 0/0/0/2/5'))
matches = get_all_matches('show policy-map interface tenGigE 0/0/0/2/5')
for i in matches:
    print(i)
    print()#################################################################
'''            
#get_all_matches(show_cmds, config_cmds)
print('############ get keywords output ###############')
a,sample= get_keywords('show ipv4 interface brief')
for key in a:
    print("key:%s, val:%s" %(key, sample[key]))
#################################
 
generate_config_keywords(config_cmds)
#################################
print('\n########## get all matches output #########')
#print(get_all_matches('show ipv4 interface brief'))
matches = get_all_matches('show ipv4 interface brief')
for i in matches:
    print(i)
    print()


