import yaml

def read_from_file(filename="config.yml"):
    """
    Read Wispy configuration data from a file.
    """
    with open(filename) as f:
        config = yaml.load(f)
    return config

def save_to_file(config, filename="config.yml"):
    """
    Save Wispy configuration data to a file.
    """
    with open(filename, "w") as f:
        yaml.dump(config, f, default_flow_style=False, indent=4, default_style="")
