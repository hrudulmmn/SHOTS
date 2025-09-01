import yaml 

def load_memory():
    try:
        with open("memory.yaml","r") as l:
            load = yaml.safe_load(l)
            if load is None:
                load = {"conversations": []}
            return load
    except FileNotFoundError:
        return {"conversations": []}
                
            
        
def save_memory(user):
    with open("memory.yaml","w") as l:
        yaml.safe_dump(user,l,default_flow_style=False)
        
def add_convo(speaker,convo):
    mem = load_memory()
    mem["conversations"].append({"chat": convo , "speaker": speaker})
    save_memory(mem)