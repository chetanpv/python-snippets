from oslo.config import cfg

OPT_ONE_GROUP = cfg.OptGroup(name='DATA',
                         title='My data')

ONE_OPTS = [
    cfg.StrOpt('uri',
               default='http://my-uri:8909'),
            ]

OPT_TWO_GROUP = cfg.OptGroup(name='SIMPLE',
                         title='My Simple data')

TWO_OPTS = [
    cfg.StrOpt('myid',
               default=5)]

CONF = cfg.CONF
CONF.register_group(OPT_ONE_GROUP)
CONF.register_group(OPT_TWO_GROUP)
CONF.register_opts(ONE_OPTS, OPT_ONE_GROUP)
CONF.register_opts(TWO_OPTS, OPT_TWO_GROUP)
CONF(default_config_files=['files/one.conf','files/two.conf'])


if __name__ == "__main__":
    print(CONF.DATA.uri)
    print(CONF.SIMPLE.myid)

