import sys
import wispy
import wispy.config
import wispy.core

if __name__ == '__main__':
    config = wispy.config.read_from_file("config.yml")
    wispy.core.start(config)
