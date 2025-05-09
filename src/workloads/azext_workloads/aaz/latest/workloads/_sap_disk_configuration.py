# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "workloads sap-disk-configuration",
)
class SapDiskConfiguration(AAZCommand):
    """Show the SAP Disk Configuration Layout prod/non-prod SAP System.

    :example: Get the SAP Disk Configuration Layout for prod/non-prod SAP System
        az workloads sap-disk-configuration --app-location eastus --database-type HANA --db-vm-sku Standard_M32ts --deployment-type SingleServer --environment NonProd --sap-product S4HANA --location eastus
    """

    _aaz_info = {
        "version": "2024-09-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/providers/microsoft.workloads/locations/{}/sapvirtualinstancemetadata/default/getdiskconfigurations", "2024-09-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.location = AAZResourceLocationArg(
            required=True,
            id_part="name",
        )

        # define Arg Group "SAPDiskConfigurations"

        _args_schema = cls._args_schema
        _args_schema.app_location = AAZStrArg(
            options=["--app-location"],
            arg_group="SAPDiskConfigurations",
            help="The geo-location where the SAP resources will be created.",
            required=True,
        )
        _args_schema.database_type = AAZStrArg(
            options=["--database-type"],
            arg_group="SAPDiskConfigurations",
            help="The database type. Eg: HANA, DB2, etc",
            required=True,
            enum={"DB2": "DB2", "HANA": "HANA"},
        )
        _args_schema.db_vm_sku = AAZStrArg(
            options=["--db-vm-sku"],
            arg_group="SAPDiskConfigurations",
            help="The VM SKU for database instance.",
            required=True,
        )
        _args_schema.deployment_type = AAZStrArg(
            options=["--deployment-type"],
            arg_group="SAPDiskConfigurations",
            help="The deployment type. Eg: SingleServer/ThreeTier",
            required=True,
            enum={"SingleServer": "SingleServer", "ThreeTier": "ThreeTier"},
        )
        _args_schema.environment = AAZStrArg(
            options=["--environment"],
            arg_group="SAPDiskConfigurations",
            help="Defines the environment type - Production/Non Production.",
            required=True,
            enum={"NonProd": "NonProd", "Prod": "Prod"},
        )
        _args_schema.sap_product = AAZStrArg(
            options=["--sap-product"],
            arg_group="SAPDiskConfigurations",
            help="Defines the SAP Product type.",
            required=True,
            enum={"ECC": "ECC", "Other": "Other", "S4HANA": "S4HANA"},
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.SapVirtualInstancesInvokeDiskConfigurations(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class SapVirtualInstancesInvokeDiskConfigurations(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/providers/Microsoft.Workloads/locations/{location}/sapVirtualInstanceMetadata/default/getDiskConfigurations",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "location", self.ctx.args.location,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-09-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("appLocation", AAZStrType, ".app_location", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("databaseType", AAZStrType, ".database_type", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("dbVmSku", AAZStrType, ".db_vm_sku", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("deploymentType", AAZStrType, ".deployment_type", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("environment", AAZStrType, ".environment", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("sapProduct", AAZStrType, ".sap_product", typ_kwargs={"flags": {"required": True}})

            return self.serialize_content(_content_value)

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.volume_configurations = AAZDictType(
                serialized_name="volumeConfigurations",
            )

            volume_configurations = cls._schema_on_200.volume_configurations
            volume_configurations.Element = AAZObjectType()

            _element = cls._schema_on_200.volume_configurations.Element
            _element.recommended_configuration = AAZObjectType(
                serialized_name="recommendedConfiguration",
            )
            _element.supported_configurations = AAZListType(
                serialized_name="supportedConfigurations",
            )

            recommended_configuration = cls._schema_on_200.volume_configurations.Element.recommended_configuration
            recommended_configuration.count = AAZIntType()
            recommended_configuration.size_gb = AAZIntType(
                serialized_name="sizeGB",
            )
            recommended_configuration.sku = AAZObjectType()
            _SapDiskConfigurationHelper._build_schema_disk_sku_read(recommended_configuration.sku)

            supported_configurations = cls._schema_on_200.volume_configurations.Element.supported_configurations
            supported_configurations.Element = AAZObjectType()

            _element = cls._schema_on_200.volume_configurations.Element.supported_configurations.Element
            _element.disk_tier = AAZStrType(
                serialized_name="diskTier",
            )
            _element.iops_read_write = AAZIntType(
                serialized_name="iopsReadWrite",
            )
            _element.maximum_supported_disk_count = AAZIntType(
                serialized_name="maximumSupportedDiskCount",
            )
            _element.mbps_read_write = AAZIntType(
                serialized_name="mbpsReadWrite",
            )
            _element.minimum_supported_disk_count = AAZIntType(
                serialized_name="minimumSupportedDiskCount",
            )
            _element.size_gb = AAZIntType(
                serialized_name="sizeGB",
            )
            _element.sku = AAZObjectType()
            _SapDiskConfigurationHelper._build_schema_disk_sku_read(_element.sku)

            return cls._schema_on_200


class _SapDiskConfigurationHelper:
    """Helper class for SapDiskConfiguration"""

    _schema_disk_sku_read = None

    @classmethod
    def _build_schema_disk_sku_read(cls, _schema):
        if cls._schema_disk_sku_read is not None:
            _schema.name = cls._schema_disk_sku_read.name
            return

        cls._schema_disk_sku_read = _schema_disk_sku_read = AAZObjectType()

        disk_sku_read = _schema_disk_sku_read
        disk_sku_read.name = AAZStrType()

        _schema.name = cls._schema_disk_sku_read.name


__all__ = ["SapDiskConfiguration"]
