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
        '''do scale things'''
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

