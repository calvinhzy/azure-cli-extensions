# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from azure.cli.testsdk import (ScenarioTest, JMESPathCheck, ResourceGroupPreparer, StorageAccountPreparer,
                               api_version_constraint)
from azure.cli.testsdk.scenario_tests import AllowLargeResponse
from ..storage_test_util import StorageScenarioMixin
from knack.util import CLIError

class StorageAccountTests(StorageScenarioMixin, ScenarioTest):
    @AllowLargeResponse()
    @ResourceGroupPreparer()
    @StorageAccountPreparer()
    def test_create_account_sas(self, storage_account_info):
        from azure.cli.core.azclierror import RequiredArgumentMissingError
        with self.assertRaises(RequiredArgumentMissingError):
            self.cmd('storage account generate-sas --resource-types o --services b --expiry 2000-01-01 '
                     '--permissions r --account-name ""')

        invalid_connection_string = "DefaultEndpointsProtocol=https;EndpointSuffix=core.windows.net;"
        with self.assertRaises(RequiredArgumentMissingError):
            self.cmd('storage account generate-sas --resource-types o --services b --expiry 2000-01-01 '
                     '--permissions r --connection-string {}'.format(invalid_connection_string))

        sas = self.storage_cmd('storage account generate-sas --resource-types o --services b '
                               '--expiry 2046-12-31T08:23Z --permissions rwdxlacupfti --https-only ',
                               storage_account_info).output
        self.assertIn('sig=', sas, 'SAS token {} does not contain sig segment'.format(sas))
        self.assertIn('se=', sas, 'SAS token {} does not contain se segment'.format(sas))
        self.assertIn('sp=rwdxlacupfti', sas, 'SAS token {} does not contain sp segment'.format(sas))

