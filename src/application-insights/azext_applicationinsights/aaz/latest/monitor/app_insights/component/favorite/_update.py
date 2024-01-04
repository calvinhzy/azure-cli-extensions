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
    "monitor app-insights component favorite update",
)
class Update(AAZCommand):
    """Update a new favorites to an Application Insights component.

    :example: Update favorite
        az monitor app-insights component favorite update -g rg -n favorite-name --resource-name component-name --config 'myconfig' --version ME --favorite-id favorite-name --favorite-type shared --tags [tag,test]
    """

    _aaz_info = {
        "version": "2015-05-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.insights/components/{}/favorites/{}", "2015-05-01"],
        ]
    }

    AZ_SUPPORT_GENERIC_UPDATE = True

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
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="The Id of a specific favorite defined in the Application Insights component",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.resource_name = AAZStrArg(
            options=["--resource-name"],
            help="The name of the Application Insights component resource.",
            required=True,
            id_part="name",
        )

        # define Arg Group "FavoriteProperties"

        _args_schema = cls._args_schema
        _args_schema.category = AAZStrArg(
            options=["--category"],
            arg_group="FavoriteProperties",
            help="Favorite category, as defined by the user at creation time.",
            nullable=True,
        )
        _args_schema.config = AAZStrArg(
            options=["--config"],
            arg_group="FavoriteProperties",
            help="Configuration of this particular favorite, which are driven by the Azure portal UX. Configuration data is a string containing valid JSON",
            nullable=True,
        )
        _args_schema.favorite_id = AAZStrArg(
            options=["--favorite-id"],
            arg_group="FavoriteProperties",
            help="Internally assigned unique id of the favorite definition.",
            nullable=True,
        )
        _args_schema.favorite_type = AAZStrArg(
            options=["--favorite-type"],
            arg_group="FavoriteProperties",
            help="Enum indicating if this favorite definition is owned by a specific user or is shared between all users with access to the Application Insights component.",
            nullable=True,
            enum={"shared": "shared", "user": "user"},
        )
        _args_schema.is_generated_from_template = AAZBoolArg(
            options=["--is-generated-from-template"],
            arg_group="FavoriteProperties",
            help="Flag denoting wether or not this favorite was generated from a template.",
            nullable=True,
        )
        _args_schema.source_type = AAZStrArg(
            options=["--source-type"],
            arg_group="FavoriteProperties",
            help="The source of the favorite definition.",
            nullable=True,
        )
        _args_schema.tags = AAZListArg(
            options=["--tags"],
            arg_group="FavoriteProperties",
            help="A list of 0 or more tags that are associated with this favorite definition",
            nullable=True,
        )
        _args_schema.version = AAZStrArg(
            options=["--version"],
            arg_group="FavoriteProperties",
            help="This instance's version of the data model. This can change as new features are added that can be marked favorite. Current examples include MetricsExplorer (ME) and Search.",
            nullable=True,
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg(
            nullable=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.FavoritesGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        self.FavoritesAdd(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class FavoritesGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/favorites/{favoriteName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "favoriteName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceName", self.ctx.args.resource_name,
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
                    "api-version", "2015-05-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

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
            _UpdateHelper._build_schema_application_insights_component_favorite_read(cls._schema_on_200)

            return cls._schema_on_200

    class FavoritesAdd(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/favorites/{favoriteName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "favoriteName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceName", self.ctx.args.resource_name,
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
                    "api-version", "2015-05-01",
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
                value=self.ctx.vars.instance,
            )

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
            _UpdateHelper._build_schema_application_insights_component_favorite_read(cls._schema_on_200)

            return cls._schema_on_200

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("Category", AAZStrType, ".category")
            _builder.set_prop("Config", AAZStrType, ".config")
            _builder.set_prop("FavoriteId", AAZStrType, ".favorite_id")
            _builder.set_prop("FavoriteType", AAZStrType, ".favorite_type")
            _builder.set_prop("IsGeneratedFromTemplate", AAZBoolType, ".is_generated_from_template")
            _builder.set_prop("Name", AAZStrType, ".name")
            _builder.set_prop("SourceType", AAZStrType, ".source_type")
            _builder.set_prop("Tags", AAZListType, ".tags")
            _builder.set_prop("Version", AAZStrType, ".version")

            tags = _builder.get(".Tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_application_insights_component_favorite_read = None

    @classmethod
    def _build_schema_application_insights_component_favorite_read(cls, _schema):
        if cls._schema_application_insights_component_favorite_read is not None:
            _schema.category = cls._schema_application_insights_component_favorite_read.category
            _schema.config = cls._schema_application_insights_component_favorite_read.config
            _schema.favorite_id = cls._schema_application_insights_component_favorite_read.favorite_id
            _schema.favorite_type = cls._schema_application_insights_component_favorite_read.favorite_type
            _schema.is_generated_from_template = cls._schema_application_insights_component_favorite_read.is_generated_from_template
            _schema.name = cls._schema_application_insights_component_favorite_read.name
            _schema.source_type = cls._schema_application_insights_component_favorite_read.source_type
            _schema.tags = cls._schema_application_insights_component_favorite_read.tags
            _schema.time_modified = cls._schema_application_insights_component_favorite_read.time_modified
            _schema.user_id = cls._schema_application_insights_component_favorite_read.user_id
            _schema.version = cls._schema_application_insights_component_favorite_read.version
            return

        cls._schema_application_insights_component_favorite_read = _schema_application_insights_component_favorite_read = AAZObjectType()

        application_insights_component_favorite_read = _schema_application_insights_component_favorite_read
        application_insights_component_favorite_read.category = AAZStrType(
            serialized_name="Category",
        )
        application_insights_component_favorite_read.config = AAZStrType(
            serialized_name="Config",
        )
        application_insights_component_favorite_read.favorite_id = AAZStrType(
            serialized_name="FavoriteId",
        )
        application_insights_component_favorite_read.favorite_type = AAZStrType(
            serialized_name="FavoriteType",
        )
        application_insights_component_favorite_read.is_generated_from_template = AAZBoolType(
            serialized_name="IsGeneratedFromTemplate",
        )
        application_insights_component_favorite_read.name = AAZStrType(
            serialized_name="Name",
        )
        application_insights_component_favorite_read.source_type = AAZStrType(
            serialized_name="SourceType",
        )
        application_insights_component_favorite_read.tags = AAZListType(
            serialized_name="Tags",
        )
        application_insights_component_favorite_read.time_modified = AAZStrType(
            serialized_name="TimeModified",
            flags={"read_only": True},
        )
        application_insights_component_favorite_read.user_id = AAZStrType(
            serialized_name="UserId",
            flags={"read_only": True},
        )
        application_insights_component_favorite_read.version = AAZStrType(
            serialized_name="Version",
        )

        tags = _schema_application_insights_component_favorite_read.tags
        tags.Element = AAZStrType()

        _schema.category = cls._schema_application_insights_component_favorite_read.category
        _schema.config = cls._schema_application_insights_component_favorite_read.config
        _schema.favorite_id = cls._schema_application_insights_component_favorite_read.favorite_id
        _schema.favorite_type = cls._schema_application_insights_component_favorite_read.favorite_type
        _schema.is_generated_from_template = cls._schema_application_insights_component_favorite_read.is_generated_from_template
        _schema.name = cls._schema_application_insights_component_favorite_read.name
        _schema.source_type = cls._schema_application_insights_component_favorite_read.source_type
        _schema.tags = cls._schema_application_insights_component_favorite_read.tags
        _schema.time_modified = cls._schema_application_insights_component_favorite_read.time_modified
        _schema.user_id = cls._schema_application_insights_component_favorite_read.user_id
        _schema.version = cls._schema_application_insights_component_favorite_read.version


__all__ = ["Update"]