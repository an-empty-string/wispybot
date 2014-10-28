import sys
import wispy
import wispy.config
import wispy.core

if __name__ == '__main__':
    config = wispy.config.read_from_file(sys.argv[1])
    wispy.core.start(config)
