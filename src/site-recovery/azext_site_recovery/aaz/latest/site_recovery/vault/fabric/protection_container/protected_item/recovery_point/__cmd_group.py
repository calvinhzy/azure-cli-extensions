# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command_group(
    "site-recovery vault fabric protection-container protected-item recovery-point",
)
class __CMDGroup(AAZCommandGroup):
    """Manage the recovery points for a replication protected item.
    """
    pass


__all__ = ["__CMDGroup"]