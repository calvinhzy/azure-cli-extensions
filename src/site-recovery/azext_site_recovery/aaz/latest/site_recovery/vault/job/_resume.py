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
    "site-recovery vault job resume",
)
class Resume(AAZCommand):
    """The operation to resume an Azure Site Recovery job.
    """

    _aaz_info = {
        "version": "2022-08-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.recoveryservices/vaults/{}/replicationjobs/{}/resume", "2022-08-01"],
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
        _args_schema.job_name = AAZStrArg(
            options=["--job-name"],
            help="Job identifier.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.vault_name = AAZStrArg(
            options=["--vault-name"],
            help="The name of the recovery services vault.",
            required=True,
            id_part="name",
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.comments = AAZStrArg(
            options=["--comments"],
            arg_group="Properties",
            help="Resume job comments.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.ReplicationJobsResume(ctx=self.ctx)()
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

    class ReplicationJobsResume(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationJobs/{jobName}/resume",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "jobName", self.ctx.args.job_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceName", self.ctx.args.vault_name,
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
            _builder.set_prop("properties", AAZObjectType)

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("comments", AAZStrType, ".comments")

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
            properties.activity_id = AAZStrType(
                serialized_name="activityId",
            )
            properties.allowed_actions = AAZListType(
                serialized_name="allowedActions",
            )
            properties.custom_details = AAZObjectType(
                serialized_name="customDetails",
            )
            properties.end_time = AAZStrType(
                serialized_name="endTime",
            )
            properties.errors = AAZListType()
            properties.friendly_name = AAZStrType(
                serialized_name="friendlyName",
            )
            properties.scenario_name = AAZStrType(
                serialized_name="scenarioName",
            )
            properties.start_time = AAZStrType(
                serialized_name="startTime",
            )
            properties.state = AAZStrType()
            properties.state_description = AAZStrType(
                serialized_name="stateDescription",
            )
            properties.target_instance_type = AAZStrType(
                serialized_name="targetInstanceType",
            )
            properties.target_object_id = AAZStrType(
                serialized_name="targetObjectId",
            )
            properties.target_object_name = AAZStrType(
                serialized_name="targetObjectName",
            )
            properties.tasks = AAZListType()

            allowed_actions = cls._schema_on_200.properties.allowed_actions
            allowed_actions.Element = AAZStrType()

            custom_details = cls._schema_on_200.properties.custom_details
            custom_details.affected_object_details = AAZDictType(
                serialized_name="affectedObjectDetails",
            )
            custom_details.instance_type = AAZStrType(
                serialized_name="instanceType",
                flags={"required": True},
            )

            affected_object_details = cls._schema_on_200.properties.custom_details.affected_object_details
            affected_object_details.Element = AAZStrType()

            disc_export_job_details = cls._schema_on_200.properties.custom_details.discriminate_by("instance_type", "ExportJobDetails")
            disc_export_job_details.blob_uri = AAZStrType(
                serialized_name="blobUri",
            )
            disc_export_job_details.sas_token = AAZStrType(
                serialized_name="sasToken",
            )

            disc_failover_job_details = cls._schema_on_200.properties.custom_details.discriminate_by("instance_type", "FailoverJobDetails")
            disc_failover_job_details.protected_item_details = AAZListType(
                serialized_name="protectedItemDetails",
            )

            protected_item_details = cls._schema_on_200.properties.custom_details.discriminate_by("instance_type", "FailoverJobDetails").protected_item_details
            protected_item_details.Element = AAZObjectType()
            _ResumeHelper._build_schema_failover_replication_protected_item_details_read(protected_item_details.Element)

            disc_switch_protection_job_details = cls._schema_on_200.properties.custom_details.discriminate_by("instance_type", "SwitchProtectionJobDetails")
            disc_switch_protection_job_details.new_replication_protected_item_id = AAZStrType(
                serialized_name="newReplicationProtectedItemId",
            )

            disc_test_failover_job_details = cls._schema_on_200.properties.custom_details.discriminate_by("instance_type", "TestFailoverJobDetails")
            disc_test_failover_job_details.comments = AAZStrType()
            disc_test_failover_job_details.network_friendly_name = AAZStrType(
                serialized_name="networkFriendlyName",
            )
            disc_test_failover_job_details.network_name = AAZStrType(
                serialized_name="networkName",
            )
            disc_test_failover_job_details.network_type = AAZStrType(
                serialized_name="networkType",
            )
            disc_test_failover_job_details.protected_item_details = AAZListType(
                serialized_name="protectedItemDetails",
            )
            disc_test_failover_job_details.test_failover_status = AAZStrType(
                serialized_name="testFailoverStatus",
            )

            protected_item_details = cls._schema_on_200.properties.custom_details.discriminate_by("instance_type", "TestFailoverJobDetails").protected_item_details
            protected_item_details.Element = AAZObjectType()
            _ResumeHelper._build_schema_failover_replication_protected_item_details_read(protected_item_details.Element)

            errors = cls._schema_on_200.properties.errors
            errors.Element = AAZObjectType()
            _ResumeHelper._build_schema_job_error_details_read(errors.Element)

            tasks = cls._schema_on_200.properties.tasks
            tasks.Element = AAZObjectType()
            _ResumeHelper._build_schema_asr_task_read(tasks.Element)

            return cls._schema_on_200


class _ResumeHelper:
    """Helper class for Resume"""

    _schema_asr_task_read = None

    @classmethod
    def _build_schema_asr_task_read(cls, _schema):
        if cls._schema_asr_task_read is not None:
            _schema.allowed_actions = cls._schema_asr_task_read.allowed_actions
            _schema.custom_details = cls._schema_asr_task_read.custom_details
            _schema.end_time = cls._schema_asr_task_read.end_time
            _schema.errors = cls._schema_asr_task_read.errors
            _schema.friendly_name = cls._schema_asr_task_read.friendly_name
            _schema.group_task_custom_details = cls._schema_asr_task_read.group_task_custom_details
            _schema.name = cls._schema_asr_task_read.name
            _schema.start_time = cls._schema_asr_task_read.start_time
            _schema.state = cls._schema_asr_task_read.state
            _schema.state_description = cls._schema_asr_task_read.state_description
            _schema.task_id = cls._schema_asr_task_read.task_id
            _schema.task_type = cls._schema_asr_task_read.task_type
            return

        cls._schema_asr_task_read = _schema_asr_task_read = AAZObjectType()

        asr_task_read = _schema_asr_task_read
        asr_task_read.allowed_actions = AAZListType(
            serialized_name="allowedActions",
        )
        asr_task_read.custom_details = AAZObjectType(
            serialized_name="customDetails",
        )
        asr_task_read.end_time = AAZStrType(
            serialized_name="endTime",
        )
        asr_task_read.errors = AAZListType()
        asr_task_read.friendly_name = AAZStrType(
            serialized_name="friendlyName",
        )
        asr_task_read.group_task_custom_details = AAZObjectType(
            serialized_name="groupTaskCustomDetails",
        )
        asr_task_read.name = AAZStrType()
        asr_task_read.start_time = AAZStrType(
            serialized_name="startTime",
        )
        asr_task_read.state = AAZStrType()
        asr_task_read.state_description = AAZStrType(
            serialized_name="stateDescription",
        )
        asr_task_read.task_id = AAZStrType(
            serialized_name="taskId",
        )
        asr_task_read.task_type = AAZStrType(
            serialized_name="taskType",
        )

        allowed_actions = _schema_asr_task_read.allowed_actions
        allowed_actions.Element = AAZStrType()

        custom_details = _schema_asr_task_read.custom_details
        custom_details.instance_type = AAZStrType(
            serialized_name="instanceType",
            flags={"required": True},
        )

        disc_automation_runbook_task_details = _schema_asr_task_read.custom_details.discriminate_by("instance_type", "AutomationRunbookTaskDetails")
        disc_automation_runbook_task_details.account_name = AAZStrType(
            serialized_name="accountName",
        )
        disc_automation_runbook_task_details.cloud_service_name = AAZStrType(
            serialized_name="cloudServiceName",
        )
        disc_automation_runbook_task_details.is_primary_side_script = AAZBoolType(
            serialized_name="isPrimarySideScript",
        )
        disc_automation_runbook_task_details.job_id = AAZStrType(
            serialized_name="jobId",
        )
        disc_automation_runbook_task_details.job_output = AAZStrType(
            serialized_name="jobOutput",
        )
        disc_automation_runbook_task_details.name = AAZStrType()
        disc_automation_runbook_task_details.runbook_id = AAZStrType(
            serialized_name="runbookId",
        )
        disc_automation_runbook_task_details.runbook_name = AAZStrType(
            serialized_name="runbookName",
        )
        disc_automation_runbook_task_details.subscription_id = AAZStrType(
            serialized_name="subscriptionId",
        )

        disc_consistency_check_task_details = _schema_asr_task_read.custom_details.discriminate_by("instance_type", "ConsistencyCheckTaskDetails")
        disc_consistency_check_task_details.vm_details = AAZListType(
            serialized_name="vmDetails",
        )

        vm_details = _schema_asr_task_read.custom_details.discriminate_by("instance_type", "ConsistencyCheckTaskDetails").vm_details
        vm_details.Element = AAZObjectType()

        _element = _schema_asr_task_read.custom_details.discriminate_by("instance_type", "ConsistencyCheckTaskDetails").vm_details.Element
        _element.cloud_name = AAZStrType(
            serialized_name="cloudName",
        )
        _element.details = AAZListType()
        _element.error_ids = AAZListType(
            serialized_name="errorIds",
        )
        _element.vm_name = AAZStrType(
            serialized_name="vmName",
        )

        details = _schema_asr_task_read.custom_details.discriminate_by("instance_type", "ConsistencyCheckTaskDetails").vm_details.Element.details
        details.Element = AAZStrType()

        error_ids = _schema_asr_task_read.custom_details.discriminate_by("instance_type", "ConsistencyCheckTaskDetails").vm_details.Element.error_ids
        error_ids.Element = AAZStrType()

        disc_fabric_replication_group_task_details = _schema_asr_task_read.custom_details.discriminate_by("instance_type", "FabricReplicationGroupTaskDetails")
        disc_fabric_replication_group_task_details.job_task = AAZObjectType(
            serialized_name="jobTask",
        )
        cls._build_schema_job_entity_read(disc_fabric_replication_group_task_details.job_task)
        disc_fabric_replication_group_task_details.skipped_reason = AAZStrType(
            serialized_name="skippedReason",
        )
        disc_fabric_replication_group_task_details.skipped_reason_string = AAZStrType(
            serialized_name="skippedReasonString",
        )

        disc_job_task_details = _schema_asr_task_read.custom_details.discriminate_by("instance_type", "JobTaskDetails")
        disc_job_task_details.job_task = AAZObjectType(
            serialized_name="jobTask",
        )
        cls._build_schema_job_entity_read(disc_job_task_details.job_task)

        disc_manual_action_task_details = _schema_asr_task_read.custom_details.discriminate_by("instance_type", "ManualActionTaskDetails")
        disc_manual_action_task_details.instructions = AAZStrType()
        disc_manual_action_task_details.name = AAZStrType()
        disc_manual_action_task_details.observation = AAZStrType()

        disc_script_action_task_details = _schema_asr_task_read.custom_details.discriminate_by("instance_type", "ScriptActionTaskDetails")
        disc_script_action_task_details.is_primary_side_script = AAZBoolType(
            serialized_name="isPrimarySideScript",
        )
        disc_script_action_task_details.name = AAZStrType()
        disc_script_action_task_details.output = AAZStrType()
        disc_script_action_task_details.path = AAZStrType()

        disc_virtual_machine_task_details = _schema_asr_task_read.custom_details.discriminate_by("instance_type", "VirtualMachineTaskDetails")
        disc_virtual_machine_task_details.job_task = AAZObjectType(
            serialized_name="jobTask",
        )
        cls._build_schema_job_entity_read(disc_virtual_machine_task_details.job_task)
        disc_virtual_machine_task_details.skipped_reason = AAZStrType(
            serialized_name="skippedReason",
        )
        disc_virtual_machine_task_details.skipped_reason_string = AAZStrType(
            serialized_name="skippedReasonString",
        )

        disc_vm_nic_updates_task_details = _schema_asr_task_read.custom_details.discriminate_by("instance_type", "VmNicUpdatesTaskDetails")
        disc_vm_nic_updates_task_details.name = AAZStrType()
        disc_vm_nic_updates_task_details.nic_id = AAZStrType(
            serialized_name="nicId",
        )
        disc_vm_nic_updates_task_details.vm_id = AAZStrType(
            serialized_name="vmId",
        )

        errors = _schema_asr_task_read.errors
        errors.Element = AAZObjectType()
        cls._build_schema_job_error_details_read(errors.Element)

        group_task_custom_details = _schema_asr_task_read.group_task_custom_details
        group_task_custom_details.child_tasks = AAZListType(
            serialized_name="childTasks",
        )
        group_task_custom_details.instance_type = AAZStrType(
            serialized_name="instanceType",
            flags={"required": True},
        )

        child_tasks = _schema_asr_task_read.group_task_custom_details.child_tasks
        child_tasks.Element = AAZObjectType()
        cls._build_schema_asr_task_read(child_tasks.Element)

        disc_inline_workflow_task_details = _schema_asr_task_read.group_task_custom_details.discriminate_by("instance_type", "InlineWorkflowTaskDetails")
        disc_inline_workflow_task_details.workflow_ids = AAZListType(
            serialized_name="workflowIds",
        )

        workflow_ids = _schema_asr_task_read.group_task_custom_details.discriminate_by("instance_type", "InlineWorkflowTaskDetails").workflow_ids
        workflow_ids.Element = AAZStrType()

        disc_recovery_plan_group_task_details = _schema_asr_task_read.group_task_custom_details.discriminate_by("instance_type", "RecoveryPlanGroupTaskDetails")
        disc_recovery_plan_group_task_details.group_id = AAZStrType(
            serialized_name="groupId",
        )
        disc_recovery_plan_group_task_details.name = AAZStrType()
        disc_recovery_plan_group_task_details.rp_group_type = AAZStrType(
            serialized_name="rpGroupType",
        )

        disc_recovery_plan_shutdown_group_task_details = _schema_asr_task_read.group_task_custom_details.discriminate_by("instance_type", "RecoveryPlanShutdownGroupTaskDetails")
        disc_recovery_plan_shutdown_group_task_details.group_id = AAZStrType(
            serialized_name="groupId",
        )
        disc_recovery_plan_shutdown_group_task_details.name = AAZStrType()
        disc_recovery_plan_shutdown_group_task_details.rp_group_type = AAZStrType(
            serialized_name="rpGroupType",
        )

        _schema.allowed_actions = cls._schema_asr_task_read.allowed_actions
        _schema.custom_details = cls._schema_asr_task_read.custom_details
        _schema.end_time = cls._schema_asr_task_read.end_time
        _schema.errors = cls._schema_asr_task_read.errors
        _schema.friendly_name = cls._schema_asr_task_read.friendly_name
        _schema.group_task_custom_details = cls._schema_asr_task_read.group_task_custom_details
        _schema.name = cls._schema_asr_task_read.name
        _schema.start_time = cls._schema_asr_task_read.start_time
        _schema.state = cls._schema_asr_task_read.state
        _schema.state_description = cls._schema_asr_task_read.state_description
        _schema.task_id = cls._schema_asr_task_read.task_id
        _schema.task_type = cls._schema_asr_task_read.task_type

    _schema_failover_replication_protected_item_details_read = None

    @classmethod
    def _build_schema_failover_replication_protected_item_details_read(cls, _schema):
        if cls._schema_failover_replication_protected_item_details_read is not None:
            _schema.friendly_name = cls._schema_failover_replication_protected_item_details_read.friendly_name
            _schema.name = cls._schema_failover_replication_protected_item_details_read.name
            _schema.network_connection_status = cls._schema_failover_replication_protected_item_details_read.network_connection_status
            _schema.network_friendly_name = cls._schema_failover_replication_protected_item_details_read.network_friendly_name
            _schema.recovery_point_id = cls._schema_failover_replication_protected_item_details_read.recovery_point_id
            _schema.recovery_point_time = cls._schema_failover_replication_protected_item_details_read.recovery_point_time
            _schema.subnet = cls._schema_failover_replication_protected_item_details_read.subnet
            _schema.test_vm_friendly_name = cls._schema_failover_replication_protected_item_details_read.test_vm_friendly_name
            _schema.test_vm_name = cls._schema_failover_replication_protected_item_details_read.test_vm_name
            return

        cls._schema_failover_replication_protected_item_details_read = _schema_failover_replication_protected_item_details_read = AAZObjectType()

        failover_replication_protected_item_details_read = _schema_failover_replication_protected_item_details_read
        failover_replication_protected_item_details_read.friendly_name = AAZStrType(
            serialized_name="friendlyName",
        )
        failover_replication_protected_item_details_read.name = AAZStrType()
        failover_replication_protected_item_details_read.network_connection_status = AAZStrType(
            serialized_name="networkConnectionStatus",
        )
        failover_replication_protected_item_details_read.network_friendly_name = AAZStrType(
            serialized_name="networkFriendlyName",
        )
        failover_replication_protected_item_details_read.recovery_point_id = AAZStrType(
            serialized_name="recoveryPointId",
        )
        failover_replication_protected_item_details_read.recovery_point_time = AAZStrType(
            serialized_name="recoveryPointTime",
        )
        failover_replication_protected_item_details_read.subnet = AAZStrType()
        failover_replication_protected_item_details_read.test_vm_friendly_name = AAZStrType(
            serialized_name="testVmFriendlyName",
        )
        failover_replication_protected_item_details_read.test_vm_name = AAZStrType(
            serialized_name="testVmName",
        )

        _schema.friendly_name = cls._schema_failover_replication_protected_item_details_read.friendly_name
        _schema.name = cls._schema_failover_replication_protected_item_details_read.name
        _schema.network_connection_status = cls._schema_failover_replication_protected_item_details_read.network_connection_status
        _schema.network_friendly_name = cls._schema_failover_replication_protected_item_details_read.network_friendly_name
        _schema.recovery_point_id = cls._schema_failover_replication_protected_item_details_read.recovery_point_id
        _schema.recovery_point_time = cls._schema_failover_replication_protected_item_details_read.recovery_point_time
        _schema.subnet = cls._schema_failover_replication_protected_item_details_read.subnet
        _schema.test_vm_friendly_name = cls._schema_failover_replication_protected_item_details_read.test_vm_friendly_name
        _schema.test_vm_name = cls._schema_failover_replication_protected_item_details_read.test_vm_name

    _schema_job_entity_read = None

    @classmethod
    def _build_schema_job_entity_read(cls, _schema):
        if cls._schema_job_entity_read is not None:
            _schema.job_friendly_name = cls._schema_job_entity_read.job_friendly_name
            _schema.job_id = cls._schema_job_entity_read.job_id
            _schema.job_scenario_name = cls._schema_job_entity_read.job_scenario_name
            _schema.target_instance_type = cls._schema_job_entity_read.target_instance_type
            _schema.target_object_id = cls._schema_job_entity_read.target_object_id
            _schema.target_object_name = cls._schema_job_entity_read.target_object_name
            return

        cls._schema_job_entity_read = _schema_job_entity_read = AAZObjectType()

        job_entity_read = _schema_job_entity_read
        job_entity_read.job_friendly_name = AAZStrType(
            serialized_name="jobFriendlyName",
        )
        job_entity_read.job_id = AAZStrType(
            serialized_name="jobId",
        )
        job_entity_read.job_scenario_name = AAZStrType(
            serialized_name="jobScenarioName",
        )
        job_entity_read.target_instance_type = AAZStrType(
            serialized_name="targetInstanceType",
        )
        job_entity_read.target_object_id = AAZStrType(
            serialized_name="targetObjectId",
        )
        job_entity_read.target_object_name = AAZStrType(
            serialized_name="targetObjectName",
        )

        _schema.job_friendly_name = cls._schema_job_entity_read.job_friendly_name
        _schema.job_id = cls._schema_job_entity_read.job_id
        _schema.job_scenario_name = cls._schema_job_entity_read.job_scenario_name
        _schema.target_instance_type = cls._schema_job_entity_read.target_instance_type
        _schema.target_object_id = cls._schema_job_entity_read.target_object_id
        _schema.target_object_name = cls._schema_job_entity_read.target_object_name

    _schema_job_error_details_read = None

    @classmethod
    def _build_schema_job_error_details_read(cls, _schema):
        if cls._schema_job_error_details_read is not None:
            _schema.creation_time = cls._schema_job_error_details_read.creation_time
            _schema.error_level = cls._schema_job_error_details_read.error_level
            _schema.provider_error_details = cls._schema_job_error_details_read.provider_error_details
            _schema.service_error_details = cls._schema_job_error_details_read.service_error_details
            _schema.task_id = cls._schema_job_error_details_read.task_id
            return

        cls._schema_job_error_details_read = _schema_job_error_details_read = AAZObjectType()

        job_error_details_read = _schema_job_error_details_read
        job_error_details_read.creation_time = AAZStrType(
            serialized_name="creationTime",
        )
        job_error_details_read.error_level = AAZStrType(
            serialized_name="errorLevel",
        )
        job_error_details_read.provider_error_details = AAZObjectType(
            serialized_name="providerErrorDetails",
        )
        job_error_details_read.service_error_details = AAZObjectType(
            serialized_name="serviceErrorDetails",
        )
        job_error_details_read.task_id = AAZStrType(
            serialized_name="taskId",
        )

        provider_error_details = _schema_job_error_details_read.provider_error_details
        provider_error_details.error_code = AAZIntType(
            serialized_name="errorCode",
        )
        provider_error_details.error_id = AAZStrType(
            serialized_name="errorId",
        )
        provider_error_details.error_message = AAZStrType(
            serialized_name="errorMessage",
        )
        provider_error_details.possible_causes = AAZStrType(
            serialized_name="possibleCauses",
        )
        provider_error_details.recommended_action = AAZStrType(
            serialized_name="recommendedAction",
        )

        service_error_details = _schema_job_error_details_read.service_error_details
        service_error_details.activity_id = AAZStrType(
            serialized_name="activityId",
        )
        service_error_details.code = AAZStrType()
        service_error_details.message = AAZStrType()
        service_error_details.possible_causes = AAZStrType(
            serialized_name="possibleCauses",
        )
        service_error_details.recommended_action = AAZStrType(
            serialized_name="recommendedAction",
        )

        _schema.creation_time = cls._schema_job_error_details_read.creation_time
        _schema.error_level = cls._schema_job_error_details_read.error_level
        _schema.provider_error_details = cls._schema_job_error_details_read.provider_error_details
        _schema.service_error_details = cls._schema_job_error_details_read.service_error_details
        _schema.task_id = cls._schema_job_error_details_read.task_id


__all__ = ["Resume"]