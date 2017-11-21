from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('config.ini')

print parser.get('moist','time')
