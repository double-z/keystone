# vim: tabstop=4 shiftwidth=4 softtabstop=4
import nose.exc

from keystone import config
from keystone import test
from keystone.common import utils

import default_fixtures
import test_keystoneclient

CONF = config.CONF
KEYSTONECLIENT_REPO = 'git://github.com/openstack/python-keystoneclient.git'


class CliMasterTestCase(test_keystoneclient.KcMasterTestCase):
    def setUp(self):
        super(CliMasterTestCase, self).setUp()
        from keystone import cli
        self.cli = cli

    def get_client(self, user_ref=None, tenant_ref=None):
        if user_ref is None:
            user_ref = self.user_foo
        if tenant_ref is None:
            for user in default_fixtures.USERS:
                if user['id'] == user_ref['id']:
                    tenant_id = user['tenants'][0]
        else:
            tenant_id = tenant_ref['id']

        cl = self._client(username=user_ref['name'],
                          password=user_ref['password'],
                          tenant_id=tenant_id)
        gen = self.cli.CommandLineGenerator(
                cmd=test.rootdir('bin', 'keystone-manage'),
                execute=True,
                auth_token=cl.auth_token,
                endpoint=cl.management_url)
        gen.auth_token = cl.auth_token
        gen.management_url = cl.management_url
        return gen

    def test_authenticate_tenant_id_and_tenants(self):
        raise nose.exc.SkipTest('N/A')

    def test_authenticate_token_no_tenant(self):
        raise nose.exc.SkipTest('N/A')

    def test_authenticate_token_tenant_id(self):
        raise nose.exc.SkipTest('N/A')

    def test_authenticate_token_tenant_name(self):
        raise nose.exc.SkipTest('N/A')

    def test_tenant_create_update_and_delete(self):
        raise nose.exc.SkipTest('cli does not support booleans yet')
    def test_invalid_password(self):
        raise nose.exc.SkipTest('N/A')

    def test_user_create_update_delete(self):
        raise nose.exc.SkipTest('cli does not support booleans yet')