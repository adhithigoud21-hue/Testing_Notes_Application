import yaml
#This helps to read the data from config.yaml file
def load_config():
    with open("config/config.yaml", "r") as file:
        return yaml.safe_load(file)
    
