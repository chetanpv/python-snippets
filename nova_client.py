from novaclient import client as novaclient


def get_nova_creds():
    d  = {}
    d['username'] = "nova"
    d['api_key'] = "e0f759ec587ab18fa8c1d1216f3f3772afc73702"
    d['auth_url'] = "http://192.168.0.1:35357/v2.0"
    d['project_id'] = "service"
    d['cacert'] = "/etc/ssl/certs/ca-certificates.crt"
    return d

creds = get_nova_creds()
nova = novaclient.Client("1.1", **creds)

print dir(nova)
