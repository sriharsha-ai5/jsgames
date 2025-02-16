import yaml
import json

def compareMaps(map1,map2,itre,apen):
    def trunc(ob):
        st=str(ob)
        if len(st)>20:
            st=st[0:20]+'....'
        return st
    
    doubleApen= apen+apen
    for k in itre:
        if map1[k]==map2[k]:
            print("%skey values are equal %s" %(apen,k))
        else:
            print("%skey wrong %s:%s" %(apen,k,trunc(map1[k])))
            if isinstance(map1[k],dict):
                compareMaps(map1[k],map2[k],map1[k].keys(),doubleApen)
            elif isinstance(map1[k],list):
                compareMaps(map1[k],map2[k],range(len(map1[k])),doubleApen)


# reading file
f = open("kishore.yaml", "r")
kichu = f.read()
#print(kichu)

# parsing file in yaml
datas= list(yaml.load_all(kichu,Loader=yaml.SafeLoader))
#print(datas[0])
compareMaps(datas[0],datas[1],datas[0].keys(),' ')
#print(datas[2])
#configmap1=json.loads(datas[2]["zoraSecrets.json"])
#configmap2=json.loads(datas[3]["kotakSecrets.json"])
#compareMaps(configmap1,configmap2)




