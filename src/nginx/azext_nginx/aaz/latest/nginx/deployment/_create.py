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
    "nginx deployment create",
)
class Create(AAZCommand):
    """Create an NGINX for Azure resource

    :example: Deployment Create with PublicIP
        az nginx deployment create --name myDeployment --resource-group myResourceGroup --location eastus2 --sku name="standard_Monthly" --network-profile front-end-ip-configuration="{public-ip-addresses:[{id:/subscriptions/mySubscription/resourceGroups/myResourceGroup/providers/Microsoft.Network/publicIPAddresses/myPublicIP}]}" network-interface-configuration="{subnet-id:/subscriptions/mySubscription/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualNetworks/myVNet/subnets/mySubnet}"

    :example: Deployment Create with PrivateIP
        az nginx deployment create --name myDeployment --resource-group myResourceGroup --location eastus2 --sku name="standard_Monthly" --network-profile front-end-ip-configuration="{private-ip-addresses:[{private-ip-allocation-method:Static,subnet-id:/subscriptions/mySubscription/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualNetworks/myVNet/subnets/mySubnet,private-ip-address:10.0.0.2}]}" network-interface-configuration="{subnet-id:/subscriptions/mySubscription/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualNetworks/myVNet/subnets/mySubnet}"
        az nginx deployment create --name myDeployment --resource-group myResourceGroup --location eastus2 --sku name="standard_Monthly" --network-profile front-end-ip-configuration="{private-ip-addresses:[{private-ip-allocation-method:Dynamic,subnet-id:/subscriptions/mySubscription/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualNetworks/myVNet/subnets/mySubnet,private-ip-address:10.0.0.2}]}" network-interface-configuration="{subnet-id:/subscriptions/mySubscription/resourceGroups/myResourceGroup/providers/Microsoft.Network/virtualNetworks/myVNet/subnets/mySubnet}"
    """

    _aaz_info = {
        "version": "2022-08-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/nginx.nginxplus/nginxdeployments/{}", "2022-08-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.deployment_name = AAZStrArg(
            options=["-n", "--name", "--deployment-name"],
            help="The name of targeted Nginx deployment",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Body"

        _args_schema = cls._args_schema
        _args_schema.identity = AAZObjectArg(
            options=["--identity"],
            arg_group="Body",
        )
        _args_schema.location = AAZResourceLocationArg(
            arg_group="Body",
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.sku = AAZObjectArg(
            options=["--sku"],
            arg_group="Body",
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Body",
        )

        identity = cls._args_schema.identity
        identity.type = AAZStrArg(
            options=["type"],
            enum={"None": "None", "SystemAssigned": "SystemAssigned", "SystemAssigned, UserAssigned": "SystemAssigned, UserAssigned", "UserAssigned": "UserAssigned"},
        )
        identity.user_assigned_identities = AAZDictArg(
            options=["user-assigned-identities"],
        )

        user_assigned_identities = cls._args_schema.identity.user_assigned_identities
        user_assigned_identities.Element = AAZObjectArg(
            blank={},
        )

        sku = cls._args_schema.sku
        sku.name = AAZStrArg(
            options=["name"],
            help="Name of the SKU.",
            required=True,
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.enable_diagnostics = AAZBoolArg(
            options=["--enable-diagnostics"],
            help="Boolean to enable or disable diagnostics on your deployment",
            arg_group="Properties",
        )
        _args_schema.logging = AAZObjectArg(
            options=["--logging"],
            arg_group="Properties",
        )
        _args_schema.managed_resource_group = AAZStrArg(
            options=["--managed-resource-group"],
            arg_group="Properties",
            help="The managed resource group to deploy VNet injection related network resources.",
        )
        _args_schema.network_profile = AAZObjectArg(
            options=["--network-profile"],
            arg_group="Properties",
        )
        _args_schema.provisioning_state = AAZStrArg(
            options=["--provisioning-state"],
            help="State of the deployment",
            arg_group="Properties",
            enum={"Accepted": "Accepted", "Canceled": "Canceled", "Creating": "Creating", "Deleted": "Deleted", "Deleting": "Deleting", "Failed": "Failed", "NotSpecified": "NotSpecified", "Succeeded": "Succeeded", "Updating": "Updating"},
        )

        logging = cls._args_schema.logging
        logging.storage_account = AAZObjectArg(
            options=["storage-account"],
        )

        storage_account = cls._args_schema.logging.storage_account
        storage_account.account_name = AAZStrArg(
            options=["account-name"],
        )
        storage_account.container_name = AAZStrArg(
            options=["container-name"],
        )

        network_profile = cls._args_schema.network_profile
        network_profile.front_end_ip_configuration = AAZObjectArg(
            options=["front-end-ip-configuration"],
        )
        network_profile.network_interface_configuration = AAZObjectArg(
            options=["network-interface-configuration"],
        )

        front_end_ip_configuration = cls._args_schema.network_profile.front_end_ip_configuration
        front_end_ip_configuration.private_ip_addresses = AAZListArg(
            options=["private-ip-addresses"],
        )
        front_end_ip_configuration.public_ip_addresses = AAZListArg(
            options=["public-ip-addresses"],
        )

        private_ip_addresses = cls._args_schema.network_profile.front_end_ip_configuration.private_ip_addresses
        private_ip_addresses.Element = AAZObjectArg()

        _element = cls._args_schema.network_profile.front_end_ip_configuration.private_ip_addresses.Element
        _element.private_ip_address = AAZStrArg(
            options=["private-ip-address"],
        )
        _element.private_ip_allocation_method = AAZStrArg(
            options=["private-ip-allocation-method"],
            enum={"Dynamic": "Dynamic", "Static": "Static"},
        )
        _element.subnet_id = AAZStrArg(
            options=["subnet-id"],
        )

        public_ip_addresses = cls._args_schema.network_profile.front_end_ip_configuration.public_ip_addresses
        public_ip_addresses.Element = AAZObjectArg()

        _element = cls._args_schema.network_profile.front_end_ip_configuration.public_ip_addresses.Element
        _element.id = AAZStrArg(
            options=["id"],
        )

        network_interface_configuration = cls._args_schema.network_profile.network_interface_configuration
        network_interface_configuration.subnet_id = AAZStrArg(
            options=["subnet-id"],
        )
        return cls._args_schema

    def _execute_operations(self):
        yield self.DeploymentsCreate(ctx=self.ctx)()

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class DeploymentsCreate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Nginx.NginxPlus/nginxDeployments/{deploymentName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"
        
        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-08-01",
                    required=True,
                ),
            }
            return parameters
            
        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "deploymentName", self.ctx.args.deployment_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
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
                typ_kwargs={"flags": {"client_flatten": True}}
            )
            _builder.set_prop("identity", AAZObjectType, ".identity")
            _builder.set_prop("location", AAZStrType, ".location")
            _builder.set_prop("properties", AAZObjectType)
            _builder.set_prop("sku", AAZObjectType, ".sku")
            _builder.set_prop("tags", AAZDictType, ".tags")

            identity = _builder.get(".identity")
            if identity is not None:
                identity.set_prop("type", AAZStrType, ".type")
                identity.set_prop("userAssignedIdentities", AAZDictType, ".user_assigned_identities")

            user_assigned_identities = _builder.get(".identity.userAssignedIdentities")
            if user_assigned_identities is not None:
                user_assigned_identities.set_elements(AAZObjectType, ".")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("enableDiagnosticsSupport", AAZBoolType, ".enable_diagnostics")
                properties.set_prop("logging", AAZObjectType, ".logging")
                properties.set_prop("managedResourceGroup", AAZStrType, ".managed_resource_group")
                properties.set_prop("networkProfile", AAZObjectType, ".network_profile")
                properties.set_prop("provisioningState", AAZStrType, ".provisioning_state")

            logging = _builder.get(".properties.logging")
            if logging is not None:
                logging.set_prop("storageAccount", AAZObjectType, ".storage_account")

            storage_account = _builder.get(".properties.logging.storageAccount")
            if storage_account is not None:
                storage_account.set_prop("accountName", AAZStrType, ".account_name")
                storage_account.set_prop("containerName", AAZStrType, ".container_name")

            network_profile = _builder.get(".properties.networkProfile")
            if network_profile is not None:
                network_profile.set_prop("frontEndIPConfiguration", AAZObjectType, ".front_end_ip_configuration")
                network_profile.set_prop("networkInterfaceConfiguration", AAZObjectType, ".network_interface_configuration")

            front_end_ip_configuration = _builder.get(".properties.networkProfile.frontEndIPConfiguration")
            if front_end_ip_configuration is not None:
                front_end_ip_configuration.set_prop("privateIPAddresses", AAZListType, ".private_ip_addresses")
                front_end_ip_configuration.set_prop("publicIPAddresses", AAZListType, ".public_ip_addresses")

            private_ip_addresses = _builder.get(".properties.networkProfile.frontEndIPConfiguration.privateIPAddresses")
            if private_ip_addresses is not None:
                private_ip_addresses.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.networkProfile.frontEndIPConfiguration.privateIPAddresses[]")
            if _elements is not None:
                _elements.set_prop("privateIPAddress", AAZStrType, ".private_ip_address")
                _elements.set_prop("privateIPAllocationMethod", AAZStrType, ".private_ip_allocation_method")
                _elements.set_prop("subnetId", AAZStrType, ".subnet_id")

            public_ip_addresses = _builder.get(".properties.networkProfile.frontEndIPConfiguration.publicIPAddresses")
            if public_ip_addresses is not None:
                public_ip_addresses.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.networkProfile.frontEndIPConfiguration.publicIPAddresses[]")
            if _elements is not None:
                _elements.set_prop("id", AAZStrType, ".id")

            network_interface_configuration = _builder.get(".properties.networkProfile.networkInterfaceConfiguration")
            if network_interface_configuration is not None:
                network_interface_configuration.set_prop("subnetId", AAZStrType, ".subnet_id")

            sku = _builder.get(".sku")
            if sku is not None:
                sku.set_prop("name", AAZStrType, ".name", typ_kwargs={"flags": {"required": True}})

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.identity = AAZObjectType()
            _schema_on_200_201.location = AAZStrType()
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType()
            _schema_on_200_201.sku = AAZObjectType()
            _schema_on_200_201.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200_201.tags = AAZDictType()
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200_201.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            identity.type = AAZStrType()
            identity.user_assigned_identities = AAZDictType(
                serialized_name="userAssignedIdentities",
            )

            user_assigned_identities = cls._schema_on_200_201.identity.user_assigned_identities
            user_assigned_identities.Element = AAZObjectType()

            _element = cls._schema_on_200_201.identity.user_assigned_identities.Element
            _element.client_id = AAZStrType(
                serialized_name="clientId",
                flags={"read_only": True},
            )
            _element.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.enable_diagnostics_support = AAZBoolType(
                serialized_name="enableDiagnosticsSupport",
            )
            properties.ip_address = AAZStrType(
                serialized_name="ipAddress",
                flags={"read_only": True},
            )
            properties.logging = AAZObjectType()
            properties.managed_resource_group = AAZStrType(
                serialized_name="managedResourceGroup",
            )
            properties.network_profile = AAZObjectType(
                serialized_name="networkProfile",
            )
            properties.nginx_version = AAZStrType(
                serialized_name="nginxVersion",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
            )

            logging = cls._schema_on_200_201.properties.logging
            logging.storage_account = AAZObjectType(
                serialized_name="storageAccount",
            )

            storage_account = cls._schema_on_200_201.properties.logging.storage_account
            storage_account.account_name = AAZStrType(
                serialized_name="accountName",
            )
            storage_account.container_name = AAZStrType(
                serialized_name="containerName",
            )

            network_profile = cls._schema_on_200_201.properties.network_profile
            network_profile.front_end_ip_configuration = AAZObjectType(
                serialized_name="frontEndIPConfiguration",
            )
            network_profile.network_interface_configuration = AAZObjectType(
                serialized_name="networkInterfaceConfiguration",
            )

            front_end_ip_configuration = cls._schema_on_200_201.properties.network_profile.front_end_ip_configuration
            front_end_ip_configuration.private_ip_addresses = AAZListType(
                serialized_name="privateIPAddresses",
            )
            front_end_ip_configuration.public_ip_addresses = AAZListType(
                serialized_name="publicIPAddresses",
            )

            private_ip_addresses = cls._schema_on_200_201.properties.network_profile.front_end_ip_configuration.private_ip_addresses
            private_ip_addresses.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.network_profile.front_end_ip_configuration.private_ip_addresses.Element
            _element.private_ip_address = AAZStrType(
                serialized_name="privateIPAddress",
            )
            _element.private_ip_allocation_method = AAZStrType(
                serialized_name="privateIPAllocationMethod",
            )
            _element.subnet_id = AAZStrType(
                serialized_name="subnetId",
            )

            public_ip_addresses = cls._schema_on_200_201.properties.network_profile.front_end_ip_configuration.public_ip_addresses
            public_ip_addresses.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.network_profile.front_end_ip_configuration.public_ip_addresses.Element
            _element.id = AAZStrType()

            network_interface_configuration = cls._schema_on_200_201.properties.network_profile.network_interface_configuration
            network_interface_configuration.subnet_id = AAZStrType(
                serialized_name="subnetId",
            )

            sku = cls._schema_on_200_201.sku
            sku.name = AAZStrType(
                flags={"required": True},
            )

            system_data = cls._schema_on_200_201.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
                flags={"read_only": True},
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
                flags={"read_only": True},
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
                flags={"read_only": True},
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
                flags={"read_only": True},
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
                flags={"read_only": True},
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
                flags={"read_only": True},
            )

            tags = cls._schema_on_200_201.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200_201


__all__ = ["Create"]