template_qos = '''
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

template_ospf = '''
#**************************************************
# Copyright (c) 2017 Cisco Systems, Inc.
# All rights reserved.
#**************************************************
Value Filldown process_id (\S+)
Value Required nbr (\S+)                
Value intf (\S+)
Value intf_addr (\S+)
Value priority (\d+)
Value state (\w+)
Value role (\s*[-\w]+)
Value dead_time (\S+)
Value Fillup total_neighbor (\d+)

Start
  ^Neighbors for O(\S+) ${process_id}
  ^${nbr}\s+${priority}\s+${state}/${role}\s+${dead_time}\s+${intf_addr}\s+${intf} -> Record
  ^Total neighbor count: ${total_neighbor} -> Record

'''

template_bfd = '''
#**************************************************
# Copyright (c) 2017 Cisco Systems, Inc.
# All rights reserved.
#**************************************************
Value ipv4_session_up (\d+)
Value ipv4_session_down (\d+)
Value ipv4_unknown (\d+)
Value ipv4_total (\d+)
Value ipv6_session_up (\d+)
Value ipv6_session_down (\d+)
Value ipv6_unknown (\d+)
Value ipv6_total (\d+)
Value label_session_up (\d+)
Value label_session_down (\d+)
Value label_unknown (\d+)
Value label_total (\d+)

Start
  ^\s*IPV4 Sessions Up:\s+${ipv4_session_up},\s+Down:\s+${ipv4_session_down},\s+Unknown\/Retry:\s+${ipv4_unknown},\s+Total:\s+${ipv4_total}
  ^\s*IPV6 Sessions Up:\s+${ipv6_session_up},\s+Down:\s+${ipv6_session_down},\s+Unknown\/Retry:\s+${ipv6_unknown},\s+Total:\s+${ipv6_total}
  ^\s*Label Sessions Up:\s+${label_session_up},\s+Down:\s+${label_session_down},\s+Unknown\/Retry:\s+${label_unknown},\s+Total:\s+${label_total}

'''
testcase_qos= '''
HundredGigE0/0/0/21 output: p1

Class c1
  Classification statistics          (packets/bytes)     (rate - kbps)
    Matched             :                   0/0                    0
    Transmitted         : N/A 
    Total Dropped       :                   0/0                    0
  Policing statistics                (packets/bytes)     (rate - kbps) 
    Policed(conform)    :                   0/0                    0
    Policed(exceed)     :                   0/0                    0
    Policed(violate)    :                   0/0                    0
    Policed and dropped :                   0/0                  

Class c2
  Classification statistics          (packets/bytes)     (rate - kbps)
    Matched             :                   0/0                    0
    Transmitted         :                   0/0                    0
    Total Dropped       :                   0/0                    0
  Queueing statistics
    Queue ID                             : 122898 
    High watermark                       : N/A 
    Inst-queue-len  (packets)            : 0
    Avg-queue-len                        : N/A 
    Taildropped(packets/bytes)           : 0/0
    Queue(conform)      :                   0/0                    0
    Queue(exceed)       :                   0/0                    0
    RED random drops(packets/bytes)      : 0/0

Class c3
  Classification statistics          (packets/bytes)     (rate - kbps)
    Matched             :                   0/0                    0
    Transmitted         : N/A 
    Total Dropped       : N/A 

Class c4
  Classification statistics          (packets/bytes)     (rate - kbps)
    Matched             :                   0/0                    0
    Transmitted         :                   0/0                    0
    Total Dropped       :                   0/0                    0
  Queueing statistics
    Queue ID                             : 122897 
    High watermark                       : N/A 
    Inst-queue-len  (packets)            : 0
    Avg-queue-len                        : N/A 
    Taildropped(packets/bytes)           : 0/0
    Queue(conform)      :                   0/0                    0
    Queue(exceed)       :                   0/0                    0
    RED random drops(packets/bytes)      : 0/0

Class class-default
  Classification statistics          (packets/bytes)     (rate - kbps)
    Matched             :                   0/0                    0
    Transmitted         : N/A 
    Total Dropped       : N/A 
  Queueing statistics
    Queue ID                             : 122899 
    High watermark                       : N/A 
    Inst-queue-len  (packets)            : 0
    Avg-queue-len                        : N/A 
    Taildropped(packets/bytes)           : 0/0
    Queue(conform)      :                   0/0                    0
    Queue(exceed)       :                   0/0                    0
    RED random drops(packets/bytes)      : 0/0
'''

testcase_ospf= '''
Neighbors for OSPF core1

Neighbor ID Pri State Dead Time Address Interface
21.1.1.2 1 FULL/DR 00:00:32 21.1.1.2 GigabitEthernet0/0/0/8.11 Neighbor is up for 00:23:27

21.1.1.2 1 FULL/DR 00:00:39 21.1.2.2 GigabitEthernet0/0/0/8.12 Neighbor is up for 00:23:27

21.1.1.2 1 FULL/DR 00:00:32 21.1.3.2 GigabitEthernet0/0/0/8.13 Neighbor is up for 00:23:19

21.1.1.2 1 FULL/DR 00:00:39 21.1.4.2 GigabitEthernet0/0/0/8.14 Neighbor is up for 00:23:19

21.1.1.2 1 FULL/DR 00:00:33 21.1.5.2 GigabitEthernet0/0/0/8.15 Neighbor is up for 00:23:18

21.1.1.2 1 FULL/DR 00:00:34 21.1.6.2 GigabitEthernet0/0/0/8.16 Neighbor is up for 00:23:26

21.1.1.2 1 FULL/DR 00:00:31 21.1.7.2 GigabitEthernet0/0/0/8.17 Neighbor is up for 00:23:25

21.1.1.2 1 FULL/DR 00:00:39 21.1.8.2 GigabitEthernet0/0/0/8.18 Neighbor is up for 00:23:26

21.1.1.2 1 FULL/DR 00:00:35 21.1.9.2 GigabitEthernet0/0/0/8.19 Neighbor is up for 00:23:25

21.1.1.2 1 FULL/DR 00:00:33 21.1.10.2 GigabitEthernet0/0/0/8.20 Neighbor is up for 00:23:26

Total neighbor count: 10
'''


parsed_dict_meta_ospf = '''
===Parsed Headers====================================================================

process_id      nbr      intf      intf_addr      priority      state      role      dead_time      total_neighbor      

===Parsed data=======================================================================

['core1',
 '21.1.1.2',
 'GigabitEthernet0/0/0/8.12',
 '21.1.2.2',
 '1',
 'FULL',
 'DR',
 '00:00:39',
 '10']
['core1',
 '21.1.1.2',
 'GigabitEthernet0/0/0/8.13',
 '21.1.3.2',
 '1',
 'FULL',
 'DR',
 '00:00:32',
 '10']
['core1',
 '21.1.1.2',
 'GigabitEthernet0/0/0/8.14',
 '21.1.4.2',
 '1',
 'FULL',
 'DR',
 '00:00:39',
 '10']
['core1',
 '21.1.1.2',
 'GigabitEthernet0/0/0/8.15',
 '21.1.5.2',
 '1',
 'FULL',
 'DR',
 '00:00:33',
 '10']
['core1',
 '21.1.1.2',
 'GigabitEthernet0/0/0/8.16',
 '21.1.6.2',
 '1',
 'FULL',
 'DR',
 '00:00:34',
 '10']
['core1',
 '21.1.1.2',
 'GigabitEthernet0/0/0/8.17',
 '21.1.7.2',
 '1',
 'FULL',
 'DR',
 '00:00:31',
 '10']
['core1',
 '21.1.1.2',
 'GigabitEthernet0/0/0/8.18',
 '21.1.8.2',
 '1',
 'FULL',
 'DR',
 '00:00:39',
 '10']
['core1',
 '21.1.1.2',
 'GigabitEthernet0/0/0/8.19',
 '21.1.9.2',
 '1',
 'FULL',
 'DR',
 '00:00:35',
 '10']
['core1',
 '21.1.1.2',
 'GigabitEthernet0/0/0/8.20',
 '21.1.10.2',
 '1',
 'FULL',
 'DR',
 '00:00:33',
 '10']
'''

parsed_dict_ospf = {'process_id': {'core1': {'nbr': {'21.1.1.2': {'intf': {'gigabitethernet0/0/0/8.12': {'dead_time': '00:00:39',
                                                                                      'intf_addr': '21.1.2.2',
                                                                                      'priority': '1',
                                                                                      'role': 'dr',
                                                                                      'state': 'full',
                                                                                      'total_neighbor': '10'},
                                                        'gigabitethernet0/0/0/8.13': {'dead_time': '00:00:32',
                                                                                      'intf_addr': '21.1.3.2',
                                                                                      'priority': '1',
                                                                                      'role': 'dr',
                                                                                      'state': 'full',
                                                                                      'total_neighbor': '10'},
                                                        'gigabitethernet0/0/0/8.14': {'dead_time': '00:00:39',
                                                                                      'intf_addr': '21.1.4.2',
                                                                                      'priority': '1',
                                                                                      'role': 'dr',
                                                                                      'state': 'full',
                                                                                      'total_neighbor': '10'},
                                                        'gigabitethernet0/0/0/8.15': {'dead_time': '00:00:33',
                                                                                      'intf_addr': '21.1.5.2',
                                                                                      'priority': '1',
                                                                                      'role': 'dr',
                                                                                      'state': 'full',
                                                                                      'total_neighbor': '10'},
                                                        'gigabitethernet0/0/0/8.16': {'dead_time': '00:00:34',
                                                                                      'intf_addr': '21.1.6.2',
                                                                                      'priority': '1',
                                                                                      'role': 'dr',
                                                                                      'state': 'full',
                                                                                      'total_neighbor': '10'},
                                                        'gigabitethernet0/0/0/8.17': {'dead_time': '00:00:31',
                                                                                      'intf_addr': '21.1.7.2',
                                                                                      'priority': '1',
                                                                                      'role': 'dr',
                                                                                      'state': 'full',
                                                                                      'total_neighbor': '10'},
                                                        'gigabitethernet0/0/0/8.18': {'dead_time': '00:00:39',
                                                                                      'intf_addr': '21.1.8.2',
                                                                                      'priority': '1',
                                                                                      'role': 'dr',
                                                                                      'state': 'full',
                                                                                      'total_neighbor': '10'},
                                                        'gigabitethernet0/0/0/8.19': {'dead_time': '00:00:35',
                                                                                      'intf_addr': '21.1.9.2',
                                                                                      'priority': '1',
                                                                                      'role': 'dr',
                                                                                      'state': 'full',
                                                                                      'total_neighbor': '10'},
                                                        'gigabitethernet0/0/0/8.20': {'dead_time': '00:00:33',
                                                                                      'intf_addr': '21.1.10.2',
                                                                                      'priority': '1',
                                                                                      'role': 'dr',
                                                                                      'state': 'full',
                                                                                      'total_neighbor': '10'}}}}}}}

parsed_dict_meta_qos ='''

===Parsed Headers====================================================================

intf_class      statistics      statistics_key      packets      bytes      rate      

===Parsed data=======================================================================

['c1', 'Classification', 'Matched ', '0', '0', '0']
['c1', 'Classification', ' Total Dropped', '0', '0', '0']
['c1', 'Policing', 'Policed(conform) ', '0', '0', '0']
['c1', 'Policing', 'Policed(exceed) ', '0', '0', '0']
['c1', 'Policing', 'Policed(violate) ', '0', '0', '0']
['c1', 'Policing', 'Policed and dropped', '0', '0', '']
['c2', 'Classification', 'Matched ', '0', '0', '0']
['c2', 'Classification', 'Transmitted ', '0', '0', '0']
['c2', 'Classification', ' Total Dropped', '0', '0', '0']
['c2', 'Queueing', 'Taildropped(packets/bytes) ', '0', '0', '']
['c2', 'Queueing', 'Queue(conform) ', '0', '0', '0']
['c2', 'Queueing', 'Queue(exceed) ', '0', '0', '0']
['c2', 'Queueing', 'RED random drops(packets/bytes)', '0', '0', '']
['c3', 'Classification', 'Matched ', '0', '0', '0']
['c4', 'Classification', 'Matched ', '0', '0', '0']
['c4', 'Classification', 'Transmitted ', '0', '0', '0']
['c4', 'Classification', ' Total Dropped', '0', '0', '0']
['c4', 'Queueing', 'Taildropped(packets/bytes) ', '0', '0', '']
['c4', 'Queueing', 'Queue(conform) ', '0', '0', '0']
['c4', 'Queueing', 'Queue(exceed) ', '0', '0', '0']
['c4', 'Queueing', 'RED random drops(packets/bytes)', '0', '0', '']
['class-default', 'Classification', 'Matched ', '0', '0', '0']
['class-default', 'Queueing', 'Taildropped(packets/bytes) ', '0', '0', '']
['class-default', 'Queueing', 'Queue(conform) ', '0', '0', '0']
['class-default', 'Queueing', 'Queue(exceed) ', '0', '0', '0']
['class-default', 'Queueing', 'RED random drops(packets/bytes)', '0', '0', '']
'''

parsed_dict_qos = {'intf_class': {'c1': {'statistics': {'classification': {'statistics_key': {' total dropped': {'bytes': '0',
                                                                                               'packets': '0',
                                                                                               'rate': '0'},
                                                                            'matched ': {'bytes': '0',
                                                                                         'packets': '0',
                                                                                         'rate': '0'}}},
                                      'policing': {'statistics_key': {'policed and dropped': {'bytes': '0',
                                                                                              'packets': '0',
                                                                                              'rate': ''},
                                                                      'policed(conform) ': {'bytes': '0',
                                                                                            'packets': '0',
                                                                                            'rate': '0'},
                                                                      'policed(exceed) ': {'bytes': '0',
                                                                                           'packets': '0',
                                                                                           'rate': '0'},
                                                                      'policed(violate) ': {'bytes': '0',
                                                                                            'packets': '0',
                                                                                            'rate': '0'}}}}},
                'c2': {'statistics': {'classification': {'statistics_key': {' total dropped': {'bytes': '0',
                                                                                               'packets': '0',
                                                                                               'rate': '0'},
                                                                            'matched ': {'bytes': '0',
                                                                                         'packets': '0',
                                                                                         'rate': '0'},
                                                                            'transmitted ': {'bytes': '0',
                                                                                             'packets': '0',
                                                                                             'rate': '0'}}},
                                      'queueing': {'statistics_key': {'queue(conform) ': {'bytes': '0',
                                                                                          'packets': '0',
                                                                                          'rate': '0'},
                                                                      'queue(exceed) ': {'bytes': '0',
                                                                                         'packets': '0',
                                                                                         'rate': '0'},
                                                                      'red random drops(packets/bytes)': {'bytes': '0',
                                                                                                          'packets': '0',
                                                                                                          'rate': ''},
                                                                      'taildropped(packets/bytes) ': {'bytes': '0',
                                                                                                      'packets': '0',
                                                                                                      'rate': ''}}}}},
                'c3': {'bytes': '0',
                       'packets': '0',
                       'rate': '0',
                       'statistics': 'classification',
                       'statistics_key': 'matched '},
                'c4': {'statistics': {'classification': {'statistics_key': {' total dropped': {'bytes': '0',
                                                                                               'packets': '0',
                                                                                               'rate': '0'},
                                                                            'matched ': {'bytes': '0',
                                                                                         'packets': '0',
                                                                                         'rate': '0'},
                                                                            'transmitted ': {'bytes': '0',
                                                                                             'packets': '0',
                                                                                             'rate': '0'}}},
                                      'queueing': {'statistics_key': {'queue(conform) ': {'bytes': '0',
                                                                                          'packets': '0',
                                                                                          'rate': '0'},
                                                                      'queue(exceed) ': {'bytes': '0',
                                                                                         'packets': '0',
                                                                                         'rate': '0'},
                                                                      'red random drops(packets/bytes)': {'bytes': '0',
                                                                                                          'packets': '0',
                                                                                                          'rate': ''},
                                                                      'taildropped(packets/bytes) ': {'bytes': '0',
                                                                                                      'packets': '0',
                                                                                                      'rate': ''}}}}},
                'class-default': {'statistics': {'classification': {'bytes': '0',
                                                                    'packets': '0',
                                                                    'rate': '0',
                                                                    'statistics_key': 'matched '},
                                                 'queueing': {'statistics_key': {'queue(conform) ': {'bytes': '0',
                                                                                                     'packets': '0',
                                                                                                     'rate': '0'},
                                                                                 'queue(exceed) ': {'bytes': '0',
                                                                                                    'packets': '0',
                                                                                                    'rate': '0'},
                                                                                 'red random drops(packets/bytes)': {'bytes': '0',
                                                                                                                     'packets': '0',
                                                                                                                     'rate': ''},
                                                                                 'taildropped(packets/bytes) ': {'bytes': '0',
                                                                                                                 'packets': '0',
                                                                                                                 'rate': ''}}}}}}}

#########################################################################################
    
def find_template_values(template):

        """
            Find the Value part from the Template
            :param template : Template to parse
        """

        try:

            return [findval for findval in template if str(findval).lower().startswith("value")]

        except Exception as error:

            raise error
        
def find_template_dynamic_keys(template , dtype = None):

        """
            Find the dynamic value part from the Template
            :param template : Template to parse
            :param dtype : Check the datatype
        """

        try:

            for findval in template:

                try:
                
                    yield str(findval.strip().split(" ")[-2].strip())            

                except Exception as error :

                    continue

        except Exception as error:

            raise error

############################################################################################
import rstr
import re
import random

def find_template_dynamic_values(template):
    """
    Returns dict of textfsm_keys and regex
    """
    textfsm_Values = {}
    try:
        template= template.split('Start')[0]
        matches= re.findall('Value\s+(\w+\s+)*(\w+)\s+\((.*)\)', template)
        for match in matches:
            textfsm_Values[match[1]]= match[2]
        return textfsm_Values
    except Exception as error:
        raise error

def simplify_regex(regex):
    ""
    #regex = '\s*[-\w]+'
    # simplify * : replaces x*, \x*, ()* with nothing
    regex = re.sub(r'(\(.*?\))\*', '', regex)
    regex = re.sub(r'(\[.*?\])\*', '', regex)
    regex = re.sub(r'\\?.\*', '', regex)
    
    #simplify space : replaces \s+ with single /s
    regex = re.sub(r'(\\s\+)', ' ', regex)
    
    #simplify + : replaces x+, \x+, ()+ with 5 occurences
    regex = re.sub(r'(\(.*?\))\+', '\g<1>\g<1>\g<1>\g<1>\g<1>', regex)
    regex = re.sub(r'(\[.*?\])\+', '\g<1>\g<1>\g<1>\g<1>\g<1>', regex)
    regex = re.sub(r'(\\?.)\+', '(\g<1>\g<1>\g<1>\g<1>\g<1>)', regex)

    return regex

def get_regex_to_text(regex):
    try:
        #print(regex)
        text= rstr.xeger(simplify_regex(regex))
        #print(text)
        return text
    except Exception as error:
        raise error
def generate_unique_values(template, count=1):
    """
    """
    proxy_data = []
    for i in range(count):
            proxy_data.append({})
            try:
                textfsm_Values = find_template_dynamic_values(template)
                for key,val in textfsm_Values.items():
                    #import pdb; pdb.set_trace()
                    #print(key.upper())
                    value = get_regex_to_text(val)
                    while value in proxy_data[i].values():
                        value = get_regex_to_text(val)
                    proxy_data[i][key] = value
            except Exception as error:
                raise error
    return proxy_data

def filter_textfsm_for_output(template):
    filtered_tmp = template.split('Start')[-1].strip()
    filtered_tmp = re.sub(r'\(*\s*\^\)*', '\n', filtered_tmp)
    filtered_tmp = re.sub(r'\(*\\s(\*|\+)\)*', '    ', filtered_tmp)
    filtered_tmp = re.sub(r'\(*\\(S|w)(\*|\+)\)*', 'S', filtered_tmp)
    filtered_tmp = re.sub(r'\(*\\d(\*|\+)\)*', '0', filtered_tmp)
    filtered_tmp = re.sub(r'\?', '', filtered_tmp)
    filtered_tmp = re.sub(r'\s*->\s*Record\h*', '', filtered_tmp)
    return filtered_tmp

def populate_textfsm(template, values):
        """
        values = list of dicts
        """
        template = filter_textfsm_for_output(template)
        output = ''
        for value in values:
            tmp = template
            for key in value:
                pattern = '\$\{\s*'+key+'\s*\}'
                tmp = re.sub(pattern,value[key], tmp)
            output += tmp
        return output

def preprocess_expected_obj_dict(expected):
        '''
        expected : expected obj dict
        '''
        return_dict = expected.copy()
        remove_keys = ['_args', 'log', '_vkeys']
        for key in remove_keys:
                if key in expected:
                        del return_dict[key]
        if '_kwargs' in expected:
                for key in expected['_kwargs']:
                        return_dict[key] = expected['_kwargs'][key]
                del return_dict['_kwargs']
        for key in list(expected.keys()):
                if expected[key] is None:
                        del return_dict[key]
        return return_dict
'''
def map_proxy_to_expected(proxy,expected):
        # in progress; handle data types
        keys_to_be_mapped = []
        expected_keys = list(set(expected) - set(proxy))
        proxy_keys = list(set(proxy)- set(expected))
        """
        for key in expected_keys:
                if expected[key] is not None:
                        keys_to_be_mapped.append(key)
        """
        for key in expected:
                if expected[key] is None:
                        expected[key] = 'NULL '
        #mapped = get_random_mapping(keys_to_be_mapped, proxy_keys, expected, proxy)
        mapped = get_random_mapping(expected_keys, proxy_keys, expected, proxy)
        print(mapped)
        import pdb; pdb.set_trace()
        for key,val in mapped.items():
                expected[val]= expected[key]
        return(expected)
'''

def map_proxy_to_actual(proxy,actual):
        # in progress; handle data types
        mapped = {}
        proxy = preprocess_expected_obj(proxy)
        actual = preprocess_expected_obj(actual)
        #expected_keys = list(set(expected) - set(proxy))
        proxy_keys_to_be_mapped = list(set(proxy)- set(actual))
        
        for key in proxy:
                if key in actual:
                   mapped[key] = key
                else:
                   val = proxy[key]
                   for act_key in actual:
                           if actual[act_key]== val:
                                   mapped[key] = act_key
                           
        
        return(mapped)

def get_random_mapping(expected_keys, proxy_keys, expected, proxy):
        #in progress
        #if len(expected) == len(proxy)
        exp_int_fields = list(filter(lambda x: expected[x].isdigit(), expected_keys))
        proxy_int_fields = list(filter(lambda x: proxy[x].isdigit(), proxy_keys))
        exp_str_fields= list(set(expected_keys) - set(exp_int_fields))
        proxy_str_fields = list(set(proxy_keys) - set(proxy_int_fields))
        mapped_keys = {}
        #import pdb; pdb.set_trace()
        try:
                for key in expected_keys:
                    if key in exp_int_fields:
                        mapped_keys[key] = random.choice(proxy_int_fields)
                        proxy_int_fields.remove(mapped_keys[key])
                    else :
                        mapped_keys[key] = random.choice(proxy_str_fields)
                        proxy_str_fields.remove(mapped_keys[key])
                return mapped_keys
        except Exception as error:
                raise error                
        #to do: if length of proxy is lesser
        
# call expected object at random.. many times to populate data as many as possible
#################################################################    
#print(find_template_values(template_qos.split('\n')))
#print(find_template_dynamic_values(template_ospf))
#for key, val in generate_unique_values(template_ospf).items():
#        print(key, val)
def populate_with_proxy(template):
        res = 0
        while res == 0 :
                try:
                        values = generate_unique_values(template)
                        d1 = values[0]
                        #print(d1)
                        populate_textfsm(template, values)
                        res = 1
                except:
                        continue



d_ospf = {'interface_name': 'TenGigE0/0/0/10.17',
      'log': 'log_obj',
      'interface_addr': None,
      'priority': None,
      '_kwargs': {'state': 'FULL', 'interface_name': 'TenGigE0/0/0/10.17'},
      '_vkeys': {},
      'nbr': None,
      'total_neighbor': None,
      'role': None,
      '_args': (),
      'process_id': None,
      'dead_time': None,
      'state': 'FULL'}

d_bfd = {'_args': (), 
        'log': 'log_obj', 
        '_vkeys': {}, 
        'session_down': None, 
        'ipv4_session_up': '10', 
        'session_up': None, 'ipv6_session_up': '0', 
        '_kwargs': {'ipv6_session_up': '0', 'ipv4_session_total': '10', 'ipv4_session_up': '10', 'ipv6_session_total': '0'}, 
        'session_unknown': None, 
        'session_total': None, 
        'ipv4_session_total': '10', 
        'ipv6_session_total': '0'
        }

d_bfd_compare = {'ipv6_unknown': '28284',
                 'ipv6_total': '81338',
                 'ipv4_unknown': '51081',
                 'ipv4_session_up': '27833',
                 'ipv6_session_up': '80136',
                 'ipv4_total': '34067',
                 'label_session_up': '92923',
                 'ipv4_session_down': '64143',
                 'label_unknown': '71582',
                 'ipv6_session_down': '55772',
                 'label_total': '46105',
                 'label_session_down': '72261'}

intf_proxy = {'_kwargs': {},
             'ipv6_address': None,
             'bfd_detection_multiplier': None,
             'max_bandwidth': None,
             'ipv4_address': None,
             'ipv4_mask': None,
             'line_state': None,
             'interface_type': None,
             'log': 'some_log',
             'ipv4_prefix_length': None,
             'input_pkts': None,
             'interface_name': None,
             'description': None,
             'encapsulation': None,
             '_args': (),
             'ipv6_mask': None,
             'bandwidth': '53434',
             'bfd_dest': None,
             'bundle_id': None,
             'bfd_afi': None,
             'mtu': '41744',
             'intf': 'JYUZQ',
             'port_activity': None,
             'unshut_state': None,
             'encaptype': 'x)9:z',
             'parent_interface': None,
             'mac_address': None,
             'bfd': None,
             'output_pkts': None,
             'bfd_interval': None,
             'vlan_id': None,
             'port_priority': None,
             '_vkeys': {},
             'lineprotostate': 'U{@Pm',
             'state': None,
             'intfstate': "c~z?'"}


#d2 = preprocess_expected_obj_dict(d_ospf)
#print(d2)

populate_with_proxy(template_ospf)
#d1 is proxy dict: all values reqd, d2 is acrtual dict

#values=[map_proxy_to_expected(d1,d2)]
#populate_textfsm(template_ospf,values)
#import pdb; pdb.set_trace()
print (preprocess_expected_obj_dict(intf_proxy))
print(intf_proxy)
