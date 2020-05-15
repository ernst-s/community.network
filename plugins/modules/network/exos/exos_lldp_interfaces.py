#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################
"""
The module file for exos_lldp_interfaces
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = '''
---
module: exos_lldp_interfaces
short_description: Manage link layer discovery protocol (LLDP) attributes of interfaces on EXOS platforms.
description:
  - This module manages link layer discovery protocol (LLDP) attributes of interfaces on Extreme Networks EXOS platforms.
author: Jayalakshmi Viswanathan (@JayalakshmiV)
options:
  config:
    description: The list of link layer discovery protocol interface attribute configurations
    type: list
    elements: dict
    suboptions:
      name:
        description:
          - Name of the interface LLDP needs to be configured on.
        type: str
        required: True
      enabled:
        description:
          - This is a boolean value to control disabling of LLDP on the interface C(name)
        type: bool
  state:
    description:
      - The state the configuration should be left in.
    type: str
    choices:
      - merged
      - replaced
      - overridden
      - deleted
    default: merged
'''
EXAMPLES = """
# Using merged

# Before state:
# -------------
#
# path: /rest/restconf/data/openconfig-lldp:lldp/interfaces?depth=4
# method: GET
# data:
# {
#   "openconfig-lldp:interfaces": {
#     "interface": [
#       {
#         "config": {
#           "enabled": true,
#           "name": "1"
#         }
#       },
#       {
#         "config": {
#           "enabled": true,
#           "name": "2"
#         }
#       },
#       {
#         "config": {
#           "enabled": false,
#           "name": "3"
#         }
#       },
#       {
#         "config": {
#           "enabled": true,
#           "name": "4"
#         }
#       },
#       {
#         "config": {
#           "enabled": false,
#           "name": "5"
#         }
#       }
#     ]
#   }
# }

- name: Merge provided configuration with device configuration
  exos_lldp_interfaces:
    config:
      - name: '2'
        enabled: false
      - name: '5'
        enabled: true
    state: merged

# Module Execution Results:
# -------------------------
#
# "before":
#    - name: '1'
#      enabled: True
#    - name: '2'
#      enabled: True
#    - name: '3'
#      enabled: False
#    - name: '4'
#      enabled: True
#    - name: '5'
#      enabled: False
#
# "requests": [
#     {
#         "data": |
#         {
#           "openconfig-lldp:config": {
#             "enabled": false,
#             "name": "2"
#           }
#         }
#         "method": "PATCH",
#         "path": "/rest/restconf/data/openconfig-lldp:lldp/interfaces/interface=2/config"
#     },
#     {
#         "data": |
#         {
#           "openconfig-lldp:config": {
#             "enabled": true,
#             "name": "5"
#           }
#         }
#         "method": "PATCH",
#         "path": "/rest/restconf/data/openconfig-lldp:lldp/interfaces/interface=5/config"
#     }
# ]
#
# "after":
#    - name: '1'
#      enabled: True
#    - name: '2'
#      enabled: False
#    - name: '3'
#      enabled: False
#    - name: '4'
#      enabled: True
#    - name: '5'
#      enabled: True

# After state:
# -------------
#
# path: /rest/restconf/data/openconfig-lldp:lldp/interfaces?depth=4
# method: GET
# data:
# {
#   "openconfig-lldp:interfaces": {
#     "interface": [
#       {
#         "config": {
#           "enabled": true,
#           "name": "1"
#         }
#       },
#       {
#         "config": {
#           "enabled": false,
#           "name": "2"
#         }
#       },
#       {
#         "config": {
#           "enabled": false,
#           "name": "3"
#         }
#       },
#       {
#         "config": {
#           "enabled": true,
#           "name": "4"
#         }
#       },
#       {
#         "config": {
#           "enabled": true,
#           "name": "5"
#         }
#       }
#     ]
#   }
# }


# Using replaced

# Before state:
# -------------
#
# path: /rest/restconf/data/openconfig-lldp:lldp/interfaces?depth=4
# method: GET
# data:
# {
#   "openconfig-lldp:interfaces": {
#     "interface": [
#       {
#         "config": {
#           "enabled": true,
#           "name": "1"
#         }
#       },
#       {
#         "config": {
#           "enabled": true,
#           "name": "2"
#         }
#       },
#       {
#         "config": {
#           "enabled": false,
#           "name": "3"
#         }
#       },
#       {
#         "config": {
#           "enabled": true,
#           "name": "4"
#         }
#       },
#       {
#         "config": {
#           "enabled": false,
#           "name": "5"
#         }
#       }
#     ]
#   }
# }

- name: Replaces device configuration of listed lldp_interfaces with provided configuration
  exos_lldp_interfaces:
    config:
      - name: '1'
        enabled: false
      - name: '3'
        enabled: true
    state: merged

# Module Execution Results:
# -------------------------
#
# "before":
#    - name: '1'
#      enabled: True
#    - name: '2'
#      enabled: True
#    - name: '3'
#      enabled: False
#    - name: '4'
#      enabled: True
#    - name: '5'
#      enabled: False
#
# "requests": [
#     {
#         "data": |
#         {
#           "openconfig-lldp:config": {
#             "enabled": false,
#             "name": "1"
#           }
#         }
#         "method": "PATCH",
#         "path": "/rest/restconf/data/openconfig-lldp:lldp/interfaces/interface=1/config"
#     },
#     {
#         "data": |
#         {
#           "openconfig-lldp:config": {
#             "enabled": true,
#             "name": "3"
#           }
#         }
#         "method": "PATCH",
#         "path": "/rest/restconf/data/openconfig-lldp:lldp/interfaces/interface=3/config"
#     }
# ]
#
# "after":
#    - name: '1'
#      enabled: False
#    - name: '2'
#      enabled: True
#    - name: '3'
#      enabled: True
#    - name: '4'
#      enabled: True
#    - name: '5'
#      enabled: False

# After state:
# -------------
#
# path: /rest/restconf/data/openconfig-lldp:lldp/interfaces?depth=4
# method: GET
# data:
# {
#   "openconfig-lldp:interfaces": {
#     "interface": [
#       {
#         "config": {
#           "enabled": false,
#           "name": "1"
#         }
#       },
#       {
#         "config": {
#           "enabled": true,
#           "name": "2"
#         }
#       },
#       {
#         "config": {
#           "enabled": true,
#           "name": "3"
#         }
#       },
#       {
#         "config": {
#           "enabled": true,
#           "name": "4"
#         }
#       },
#       {
#         "config": {
#           "enabled": false,
#           "name": "5"
#         }
#       }
#     ]
#   }
# }


# Using deleted

# Before state:
# -------------
#
# path: /rest/restconf/data/openconfig-lldp:lldp/interfaces?depth=4
# method: GET
# data:
# {
#   "openconfig-lldp:interfaces": {
#     "interface": [
#       {
#         "config": {
#           "enabled": false,
#           "name": "1"
#         },
#       },
#       {
#         "config": {
#           "enabled": false,
#           "name": "2"
#         },
#       },
#       {
#         "config": {
#           "enabled": false,
#           "name": "3"
#         },
#       }
#     ]
#   }
# }

- name: Delete lldp interface configuration (this will not delete other lldp configuration)
  exos_lldp_interfaces:
    config:
      - name: '1'
      - name: '3'
    state: deleted

# Module Execution Results:
# -------------------------
#
# "before":
#    - name: '1'
#      enabled: False
#    - name: '2'
#      enabled: False
#    - name: '3'
#      enabled: False
#
# "requests": [
#     {
#         "data": |
#         {
#           "openconfig-lldp:config": {
#             "enabled": true,
#             "name": "1"
#           }
#         }
#         "method": "PATCH",
#         "path": "/rest/restconf/data/openconfig-lldp:lldp/interfaces/interface=1/config"
#     },
#     {
#         "data": |
#         {
#           "openconfig-lldp:config": {
#             "enabled": true,
#             "name": "3"
#           }
#         }
#         "method": "PATCH",
#         "path": "/rest/restconf/data/openconfig-lldp:lldp/interfaces/interface=3/config"
#     }
# ]
#
# "after":
#    - name: '1'
#      enabled: True
#    - name: '2'
#      enabled: False
#    - name: '3'
#      enabled: True
#
#  After state:
# -------------
# path: /rest/restconf/data/openconfig-lldp:lldp/interfaces?depth=4
# method: GET
# data:
# {
#   "openconfig-lldp:interfaces": {
#     "interface": [
#       {
#         "config": {
#           "enabled": true,
#           "name": "1"
#         },
#       },
#       {
#         "config": {
#           "enabled": false,
#           "name": "2"
#         },
#       },
#       {
#         "config": {
#           "enabled": true,
#           "name": "3"
#         },
#       }
#     ]
#   }
# }


# Using overridden

# Before state:
# -------------
#
# path: /rest/restconf/data/openconfig-lldp:lldp/interfaces?depth=4
# method: GET
# data:
# {
#   "openconfig-lldp:interfaces": {
#     "interface": [
#       {
#         "config": {
#           "enabled": true,
#           "name": "1"
#         }
#       },
#       {
#         "config": {
#           "enabled": true,
#           "name": "2"
#         }
#       },
#       {
#         "config": {
#           "enabled": false,
#           "name": "3"
#         }
#       },
#       {
#         "config": {
#           "enabled": true,
#           "name": "4"
#         }
#       },
#       {
#         "config": {
#           "enabled": false,
#           "name": "5"
#         }
#       }
#     ]
#   }
# }

- name: Override device configuration of all lldp_interfaces with provided configuration
  exos_lldp_interfaces:
    config:
      - name: '3'
        enabled: true
    state: overridden

# Module Execution Results:
# -------------------------
#
# "before":
#    - name: '1'
#      enabled: True
#    - name: '2'
#      enabled: True
#    - name: '3'
#      enabled: False
#    - name: '4'
#      enabled: True
#    - name: '5'
#      enabled: False
#
# "requests": [
#     {
#         "data": |
#         {
#           "openconfig-lldp:config": {
#             "enabled": true,
#             "name": "5"
#           }
#         }
#         "method": "PATCH",
#         "path": "/rest/restconf/data/openconfig-lldp:lldp/interfaces/interface=5/config"
#     },
#     {
#         "data": |
#         {
#           "openconfig-lldp:config": {
#             "enabled": true,
#             "name": "3"
#           }
#         }
#         "method": "PATCH",
#         "path": "/rest/restconf/data/openconfig-lldp:lldp/interfaces/interface=3/config"
#     }
# ]
#
# "after":
#    - name: '1'
#      enabled: True
#    - name: '2'
#      enabled: True
#    - name: '3'
#      enabled: True
#    - name: '4'
#      enabled: True
#    - name: '5'
#      enabled: True

# After state:
# -------------
#
# path: /rest/restconf/data/openconfig-lldp:lldp/interfaces?depth=4
# method: GET
# data:
# {
#   "openconfig-lldp:interfaces": {
#     "interface": [
#       {
#         "config": {
#           "enabled": true,
#           "name": "1"
#         }
#       },
#       {
#         "config": {
#           "enabled": true,
#           "name": "2"
#         }
#       },
#       {
#         "config": {
#           "enabled": true,
#           "name": "3"
#         }
#       },
#       {
#         "config": {
#           "enabled": true,
#           "name": "4"
#         }
#       },
#       {
#         "config": {
#           "enabled": true,
#           "name": "5"
#         }
#       }
#     ]
#   }
# }


"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
  type: list
after:
  description: The resulting configuration model invocation.
  returned: when changed
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
  type: list
requests:
  description: The set of requests pushed to the remote device.
  returned: always
  type: list
  sample: [{"data": "...", "method": "...", "path": "..."}, {"data": "...", "method": "...", "path": "..."}, {"data": "...", "method": "...", "path": "..."}]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.network.plugins.module_utils.network.exos.argspec.lldp_interfaces.lldp_interfaces import Lldp_interfacesArgs
from ansible_collections.community.network.plugins.module_utils.network.exos.config.lldp_interfaces.lldp_interfaces import Lldp_interfaces


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    required_if = [('state', 'merged', ('config', )),
                   ('state', 'replaced', ('config', ))]
    module = AnsibleModule(argument_spec=Lldp_interfacesArgs.argument_spec,
                           required_if=required_if,
                           supports_check_mode=True)

    result = Lldp_interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
