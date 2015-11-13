import ConfigParser

cfg = ConfigParser.ConfigParser()
cfg.read('files/three.conf')

if not cfg.has_section('EXAMPLE'):
    cfg.add_section('EXAMPLE')

cfg.set('EXAMPLE', 'name', 'myname')

f = open('files/three.conf', 'w')
cfg.write(f)
f.close()
