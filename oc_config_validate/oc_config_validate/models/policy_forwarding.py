# -*- coding: utf-8 -*-
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.yangtypes import YANGBinary
from pyangbind.lib.yangtypes import YANGBitsType
from pyangbind.lib.base import PybindBase
from collections import OrderedDict
from decimal import Decimal
import six

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
  import builtins as __builtin__
  long = int
elif six.PY2:
  import __builtin__

class openconfig_pf_forwarding_policies(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-pf-forwarding-policies - based on the path /openconfig-pf-forwarding-policies. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This submodule contains configuration and operational state
relating to the definition of policy-forwarding policies.
  """
  _pyangbind_elements = {}

  

class openconfig_pf_path_groups(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-pf-path-groups - based on the path /openconfig-pf-path-groups. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This submodule contains configuration and operational state
relating to path-selection-groups which are used to group
forwarding entities together to be used as policy forwarding
targets.
  """
  _pyangbind_elements = {}

  

class openconfig_pf_interfaces(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-pf-interfaces - based on the path /openconfig-pf-interfaces. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This submodule contains groupings related to the association
between interfaces and policy forwarding rules.
  """
  _pyangbind_elements = {}

  

class openconfig_pf_forwarding_policies(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-pf-forwarding-policies - based on the path /openconfig-pf-forwarding-policies. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This submodule contains configuration and operational state
relating to the definition of policy-forwarding policies.
  """
  _pyangbind_elements = {}

  

class openconfig_pf_path_groups(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-pf-path-groups - based on the path /openconfig-pf-path-groups. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This submodule contains configuration and operational state
relating to path-selection-groups which are used to group
forwarding entities together to be used as policy forwarding
targets.
  """
  _pyangbind_elements = {}

  

class openconfig_pf_srte(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-pf-srte - based on the path /openconfig-pf-srte. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This module defines extensions to the OpenConfig policy forwarding
module to support static segment routing traffic engineering policy
definitions. Extensions are provided to match:

 - Ingress binding SIDs, such that traffic can be mapped based on
   an ingress label.
 - A colour community and endpoint combination, such that the
   routes can be resolved according to the policy forwarding
   entries that are to be installed.

In addition, policy forwarding actions associated with next-hops are
added to the model. The next-hop set to be forwarded to is augmented
to cover a set of lists of segments. The most common application of
such segment lists is to express stacks of MPLS labels which are used
as SR segments. In addition, they may be used to expressed segments
in the form of IPv6 addresses.
  """
  _pyangbind_elements = {}

  

class openconfig_policy_forwarding(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-policy-forwarding - based on the path /openconfig-policy-forwarding. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This module defines configuration and operational state data
relating to policy-based forwarding. Policy-based forwarding is
utilised when a system chooses how to forward packets (including
applying data-plane operations such as encapsulation or
decapsulation) based on policies other than destination L2 or L3
header. Typically, systems may implement:

- IP policy-based routing, where routing may be done based on the
  source plus destination of an IP packet; information within the
  L4 header; or some combination of both.
- Encapsulation or decapsulation based on certain policy
  information - for example, matching particular IP destinations
  and decapsulating GRE headers.
- Class-based selection of egress routes - such as class-based
  selection of an egress MPLS path.

The policies that are defined in this model are applied to a
particular ingress context of a network element (e.g., interface)
and are defined to apply following other interface policy such as
QoS classification and access control lists.

This module defines:

- policy-forwarding
|
|--- policies
|    |-- policy
|        |-- [match criteria]    How packets are defined to
|        |                       match policy.
|        |-- [forwarding-action] How packets matching should
|                                 be forwarded.
|--- interfaces
|    |-- interfaces
|        | -- apply-forwarding-policy  Forwarding policy to
|                                      used on the interface.
|--- path-selection-groups
    |-- path-selection-group     A group of forwarding resources
                                 that are grouped for purposes
                                 of next-hop selection.

A forwarding-policy specifies the match criteria that it intends
to use to determine the packets that it reroutes - this may
consist of a number of criteria, such as DSCP. The action of the
policy results in a forwarding action being applied to matching
packets. For example, decapsulating the packet from a GRE header.
In order to enact the policy based on particular interfaces - the
forwarding-policy is applied to an interface via referencing it
within an 'apply-forwarding-policy' statement associated with an
interface.

In some cases (e.g., Class-Based Tunnel Selection) the forwarding
action does not resolve to a single egress action, and rather
normal forwarding rules are to be applied but considering a subset
of forwarding resources. In these cases, a path-selection-group
can be created, referencing the subset of forwarding paths that
should be used for the egress selection. In the case that a subset
of MPLS LSPs are eligible for, say, DSCP 46 marked packets, a
path-selection-group is created, referencing the subset of LSPs.
The forwarding action of the corresponding policy is set to
PATH_GROUP and references the configured group of LSPs.
  """
  _pyangbind_elements = {}

  

class openconfig_pf_forwarding_policies(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-pf-forwarding-policies - based on the path /openconfig-pf-forwarding-policies. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This submodule contains configuration and operational state
relating to the definition of policy-forwarding policies.
  """
  _pyangbind_elements = {}

  

class openconfig_pf_path_groups(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-pf-path-groups - based on the path /openconfig-pf-path-groups. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This submodule contains configuration and operational state
relating to path-selection-groups which are used to group
forwarding entities together to be used as policy forwarding
targets.
  """
  _pyangbind_elements = {}

  

class openconfig_pf_interfaces(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-pf-interfaces - based on the path /openconfig-pf-interfaces. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This submodule contains groupings related to the association
between interfaces and policy forwarding rules.
  """
  _pyangbind_elements = {}

  

