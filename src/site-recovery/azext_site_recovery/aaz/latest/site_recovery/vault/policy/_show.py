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
    "site-recovery vault policy show",
)
class Show(AAZCommand):
    """Get the details of a replication policy.
    """

    _aaz_info = {
        "version": "2022-08-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.recoveryservices/vaults/{}/replicationpolicies/{}", "2022-08-01"],
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
        _args_schema.policy_name = AAZStrArg(
            options=["-n", "--name", "--policy-name"],
            help="Replication policy name.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.resource_name = AAZStrArg(
            options=["--resource-name"],
            help="The name of the recovery services vault.",
            required=True,
            id_part="name",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.ReplicationPoliciesGet(ctx=self.ctx)()

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ReplicationPoliciesGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationPolicies/{policyName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "policyName", self.ctx.args.policy_name,
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
                    "api-version", "2022-08-01",
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

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.location = AAZStrType()
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.friendly_name = AAZStrType(
                serialized_name="friendlyName",
            )
            properties.provider_specific_details = AAZObjectType(
                serialized_name="providerSpecificDetails",
            )

            provider_specific_details = cls._schema_on_200.properties.provider_specific_details
            provider_specific_details.instance_type = AAZStrType(
                serialized_name="instanceType",
                flags={"required": True},
            )

            disc_a2_a = cls._schema_on_200.properties.provider_specific_details.discriminate_by("instance_type", "A2A")
            disc_a2_a.app_consistent_frequency_in_minutes = AAZIntType(
                serialized_name="appConsistentFrequencyInMinutes",
            )
            disc_a2_a.crash_consistent_frequency_in_minutes = AAZIntType(
                serialized_name="crashConsistentFrequencyInMinutes",
            )
            disc_a2_a.multi_vm_sync_status = AAZStrType(
                serialized_name="multiVmSyncStatus",
            )
            disc_a2_a.recovery_point_history = AAZIntType(
                serialized_name="recoveryPointHistory",
            )
            disc_a2_a.recovery_point_threshold_in_minutes = AAZIntType(
                serialized_name="recoveryPointThresholdInMinutes",
            )

            disc_hyper_v_replica2012 = cls._schema_on_200.properties.provider_specific_details.discriminate_by("instance_type", "HyperVReplica2012")
            disc_hyper_v_replica2012.allowed_authentication_type = AAZIntType(
                serialized_name="allowedAuthenticationType",
            )
            disc_hyper_v_replica2012.application_consistent_snapshot_frequency_in_hours = AAZIntType(
                serialized_name="applicationConsistentSnapshotFrequencyInHours",
            )
            disc_hyper_v_replica2012.compression = AAZStrType()
            disc_hyper_v_replica2012.initial_replication_method = AAZStrType(
                serialized_name="initialReplicationMethod",
            )
            disc_hyper_v_replica2012.offline_replication_export_path = AAZStrType(
                serialized_name="offlineReplicationExportPath",
            )
            disc_hyper_v_replica2012.offline_replication_import_path = AAZStrType(
                serialized_name="offlineReplicationImportPath",
            )
            disc_hyper_v_replica2012.online_replication_start_time = AAZStrType(
                serialized_name="onlineReplicationStartTime",
            )
            disc_hyper_v_replica2012.recovery_points = AAZIntType(
                serialized_name="recoveryPoints",
            )
            disc_hyper_v_replica2012.replica_deletion_option = AAZStrType(
                serialized_name="replicaDeletionOption",
            )
            disc_hyper_v_replica2012.replication_port = AAZIntType(
                serialized_name="replicationPort",
            )

            disc_hyper_v_replica2012_r2 = cls._schema_on_200.properties.provider_specific_details.discriminate_by("instance_type", "HyperVReplica2012R2")
            disc_hyper_v_replica2012_r2.allowed_authentication_type = AAZIntType(
                serialized_name="allowedAuthenticationType",
            )
            disc_hyper_v_replica2012_r2.application_consistent_snapshot_frequency_in_hours = AAZIntType(
                serialized_name="applicationConsistentSnapshotFrequencyInHours",
            )
            disc_hyper_v_replica2012_r2.compression = AAZStrType()
            disc_hyper_v_replica2012_r2.initial_replication_method = AAZStrType(
                serialized_name="initialReplicationMethod",
            )
            disc_hyper_v_replica2012_r2.offline_replication_export_path = AAZStrType(
                serialized_name="offlineReplicationExportPath",
            )
            disc_hyper_v_replica2012_r2.offline_replication_import_path = AAZStrType(
                serialized_name="offlineReplicationImportPath",
            )
            disc_hyper_v_replica2012_r2.online_replication_start_time = AAZStrType(
                serialized_name="onlineReplicationStartTime",
            )
            disc_hyper_v_replica2012_r2.recovery_points = AAZIntType(
                serialized_name="recoveryPoints",
            )
            disc_hyper_v_replica2012_r2.replica_deletion_option = AAZStrType(
                serialized_name="replicaDeletionOption",
            )
            disc_hyper_v_replica2012_r2.replication_frequency_in_seconds = AAZIntType(
                serialized_name="replicationFrequencyInSeconds",
            )
            disc_hyper_v_replica2012_r2.replication_port = AAZIntType(
                serialized_name="replicationPort",
            )

            disc_hyper_v_replica_azure = cls._schema_on_200.properties.provider_specific_details.discriminate_by("instance_type", "HyperVReplicaAzure")
            disc_hyper_v_replica_azure.active_storage_account_id = AAZStrType(
                serialized_name="activeStorageAccountId",
            )
            disc_hyper_v_replica_azure.application_consistent_snapshot_frequency_in_hours = AAZIntType(
                serialized_name="applicationConsistentSnapshotFrequencyInHours",
            )
            disc_hyper_v_replica_azure.encryption = AAZStrType()
            disc_hyper_v_replica_azure.online_replication_start_time = AAZStrType(
                serialized_name="onlineReplicationStartTime",
            )
            disc_hyper_v_replica_azure.recovery_point_history_duration_in_hours = AAZIntType(
                serialized_name="recoveryPointHistoryDurationInHours",
            )
            disc_hyper_v_replica_azure.replication_interval = AAZIntType(
                serialized_name="replicationInterval",
            )

            disc_hyper_v_replica_base_policy_details = cls._schema_on_200.properties.provider_specific_details.discriminate_by("instance_type", "HyperVReplicaBasePolicyDetails")
            disc_hyper_v_replica_base_policy_details.allowed_authentication_type = AAZIntType(
                serialized_name="allowedAuthenticationType",
            )
            disc_hyper_v_replica_base_policy_details.application_consistent_snapshot_frequency_in_hours = AAZIntType(
                serialized_name="applicationConsistentSnapshotFrequencyInHours",
            )
            disc_hyper_v_replica_base_policy_details.compression = AAZStrType()
            disc_hyper_v_replica_base_policy_details.initial_replication_method = AAZStrType(
                serialized_name="initialReplicationMethod",
            )
            disc_hyper_v_replica_base_policy_details.offline_replication_export_path = AAZStrType(
                serialized_name="offlineReplicationExportPath",
            )
            disc_hyper_v_replica_base_policy_details.offline_replication_import_path = AAZStrType(
                serialized_name="offlineReplicationImportPath",
            )
            disc_hyper_v_replica_base_policy_details.online_replication_start_time = AAZStrType(
                serialized_name="onlineReplicationStartTime",
            )
            disc_hyper_v_replica_base_policy_details.recovery_points = AAZIntType(
                serialized_name="recoveryPoints",
            )
            disc_hyper_v_replica_base_policy_details.replica_deletion_option = AAZStrType(
                serialized_name="replicaDeletionOption",
            )
            disc_hyper_v_replica_base_policy_details.replication_port = AAZIntType(
                serialized_name="replicationPort",
            )

            disc_in_mage = cls._schema_on_200.properties.provider_specific_details.discriminate_by("instance_type", "InMage")
            disc_in_mage.app_consistent_frequency_in_minutes = AAZIntType(
                serialized_name="appConsistentFrequencyInMinutes",
            )
            disc_in_mage.multi_vm_sync_status = AAZStrType(
                serialized_name="multiVmSyncStatus",
            )
            disc_in_mage.recovery_point_history = AAZIntType(
                serialized_name="recoveryPointHistory",
            )
            disc_in_mage.recovery_point_threshold_in_minutes = AAZIntType(
                serialized_name="recoveryPointThresholdInMinutes",
            )

            disc_in_mage_azure_v2 = cls._schema_on_200.properties.provider_specific_details.discriminate_by("instance_type", "InMageAzureV2")
            disc_in_mage_azure_v2.app_consistent_frequency_in_minutes = AAZIntType(
                serialized_name="appConsistentFrequencyInMinutes",
            )
            disc_in_mage_azure_v2.crash_consistent_frequency_in_minutes = AAZIntType(
                serialized_name="crashConsistentFrequencyInMinutes",
            )
            disc_in_mage_azure_v2.multi_vm_sync_status = AAZStrType(
                serialized_name="multiVmSyncStatus",
            )
            disc_in_mage_azure_v2.recovery_point_history = AAZIntType(
                serialized_name="recoveryPointHistory",
            )
            disc_in_mage_azure_v2.recovery_point_threshold_in_minutes = AAZIntType(
                serialized_name="recoveryPointThresholdInMinutes",
            )

            disc_in_mage_base_policy_details = cls._schema_on_200.properties.provider_specific_details.discriminate_by("instance_type", "InMageBasePolicyDetails")
            disc_in_mage_base_policy_details.app_consistent_frequency_in_minutes = AAZIntType(
                serialized_name="appConsistentFrequencyInMinutes",
            )
            disc_in_mage_base_policy_details.multi_vm_sync_status = AAZStrType(
                serialized_name="multiVmSyncStatus",
            )
            disc_in_mage_base_policy_details.recovery_point_history = AAZIntType(
                serialized_name="recoveryPointHistory",
            )
            disc_in_mage_base_policy_details.recovery_point_threshold_in_minutes = AAZIntType(
                serialized_name="recoveryPointThresholdInMinutes",
            )

            disc_in_mage_rcm = cls._schema_on_200.properties.provider_specific_details.discriminate_by("instance_type", "InMageRcm")
            disc_in_mage_rcm.app_consistent_frequency_in_minutes = AAZIntType(
                serialized_name="appConsistentFrequencyInMinutes",
            )
            disc_in_mage_rcm.crash_consistent_frequency_in_minutes = AAZIntType(
                serialized_name="crashConsistentFrequencyInMinutes",
            )
            disc_in_mage_rcm.enable_multi_vm_sync = AAZStrType(
                serialized_name="enableMultiVmSync",
            )
            disc_in_mage_rcm.recovery_point_history_in_minutes = AAZIntType(
                serialized_name="recoveryPointHistoryInMinutes",
            )

            disc_in_mage_rcm_failback = cls._schema_on_200.properties.provider_specific_details.discriminate_by("instance_type", "InMageRcmFailback")
            disc_in_mage_rcm_failback.app_consistent_frequency_in_minutes = AAZIntType(
                serialized_name="appConsistentFrequencyInMinutes",
            )
            disc_in_mage_rcm_failback.crash_consistent_frequency_in_minutes = AAZIntType(
                serialized_name="crashConsistentFrequencyInMinutes",
            )

            disc_v_mware_cbt = cls._schema_on_200.properties.provider_specific_details.discriminate_by("instance_type", "VMwareCbt")
            disc_v_mware_cbt.app_consistent_frequency_in_minutes = AAZIntType(
                serialized_name="appConsistentFrequencyInMinutes",
            )
            disc_v_mware_cbt.crash_consistent_frequency_in_minutes = AAZIntType(
                serialized_name="crashConsistentFrequencyInMinutes",
            )
            disc_v_mware_cbt.recovery_point_history_in_minutes = AAZIntType(
                serialized_name="recoveryPointHistoryInMinutes",
            )

            return cls._schema_on_200


__all__ = ["Show"]