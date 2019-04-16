qos_data = {
    "policy_maps": {
        "policy": {
            "scale": 3,
            "direction": "ingress",
            "class1": {
                "scale" : "range(1,3)",
                "police": {
                    "rate": {
                        "value": 1,
                        "units": "mbps"
                    }
                },
                "set":{
                    "precedence" : 5
                }
            },
            "class2": {
                "priority" : 2
            }
        },
        "policy1": {
            "scale": 2,
            "class3": {
                "scale": "range(2,6,2)",
                "priority" : 1,
                "queue-limit": {
                    "value" : "50",
                    "units" : "mbytes"
                }
            }
        }
    }
}
policy_data = qos_data['policy_maps']
for policy in policy_data:
    scale = 1
    if 'scale' in policy_data[policy]:
        scale = policy_data[policy].pop('scale')
    for cmap in policy_data[policy]:
        rule = policy_data[policy][cmap]
        #import pdb; pdb.set_trace()
        for i in range(scale):
            if scale > 1 :
                pmap_name = policy + '_'  + str(i+1)
            else :
                pmap_name = policy
            class_scale = range(1)
            if 'scale' in rule:
                class_scale = eval(rule['scale'])
            for i in class_scale:
                if len(class_scale) > 1:
                    cmap_name = cmap + '_' + str(i)
                else :
                    cmap_name = cmap
                ############ policer config #############
                if 'police' in rule:
                    actions = rule['police']
                    for act in ['conform', 'exceed', 'violate']:
                        act_key = act +'_action'
                        set_key = act + '_set'
                        if act_key in actions:
                            if actions[act_key]== 'set':
                                actions[act_key] = {'set' : actions[set_key]}
                            if actions[act_key] in ['drop', 'transmit']:
                                actions[act_key] = {actions[act_key] : 'yes'}
                    print(pmap_name, cmap_name, 'police', actions)

                ############ shaper config ##############
                if 'shape' in rule:
                    actions = rule['shape']
                    if 'units' in actions['rate']:
                        actions['rate']['unit']= actions['rate'].pop('units')
                    print(pmap_name, cmap_name, 'shape', actions)

                ############ bandwidth config ##############
                if 'min_bandwidth' in rule:
                    actions = rule['min_bandwidth']
                    if 'units' in actions:
                        actions['unit']= actions.pop('units')
                    print(pmap_name, cmap_name, 'min_bandwidth', actions)

                ############ bandwidth remaining config ##############
                if 'bandwidth_remaining' in rule:
                    actions = rule['bandwidth_remaining']
                    if 'units' in actions:
                        actions['unit']= actions.pop('units')
                    print(pmap_name, cmap_name, 'bandwidth_rem',actions)

                ############ marking config ##############
                if 'set' in rule:
                    actions = rule['set']
                    print(pmap_name, cmap_name,'set', actions)

                ############ priority config ##############
                if 'priority' in rule:
                    value = rule['priority']
                    print(pmap_name, cmap_name,'priority',{'priority_level' : value})

                ############ queue-limit config ##############
                if 'queue-limit' in rule:
                    actions = rule['queue-limit']
                    if 'units' in actions:
                        actions['unit']= actions.pop('units')
                    print(pmap_name, cmap_name, 'queue-limit', actions)

                ############ random-detect config ##############
                if 'random-detect' in rule:
                    actions = rule['random-detect']
                    print(pmap_name, cmap_name, 'random-detect', actions)


'''
qos = {
"class_maps": {
    "class1": {
      "scale":50,
      "match_type": "any",
      "match": {
        "dscp": list(range(63)),
        "cos": [0,1,2,3,4,5,6,7],
        "vlan" : 1
      }
    },
    "class2": {
      "scale":3,
      "match_type": "all",
      "match": {
        "dscp": list(range(63)),
        "cos": [0,1,2,3,4,5,6,7]
        }
      }
    }
  }
class_data = qos['class_maps']
for cmap in class_data:
    cmap_data = class_data[cmap]
    ctr = {}
    if 'scale' in cmap_data:
        """do scale things"""
        scale = cmap_data['scale']
        match_data = cmap_data['match']
        match_type = cmap_data['match_type']
        for match_field in match_data:
            if isinstance(match_data[match_field],list):    
                ctr[match_field] = 0
        for i in range(scale):
            match_scale_data ={}
            cmap_name = cmap + '_'+ str(i+1)
            match_scale_data[cmap_name] = {}
            for match_field in match_data:
                if isinstance(match_data[match_field],list):
                    match_scale_data[cmap_name][match_field] =  match_data[match_field][ctr[match_field]]
                    ctr[match_field] +=1
                    if ctr[match_field] == len(match_data[match_field]):
                        ctr[match_field] = 0
                else:
                    match_scale_data[cmap_name][match_field] =  match_data[match_field]
            print (cmap_name,match_scale_data[cmap_name])     
        
    else:
        match_data = cmap_data['match']
        match_type = cmap_data['match_type']
        print(cmap, match_data)

'''
