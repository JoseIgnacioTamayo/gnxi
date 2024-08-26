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

class openconfig_pcep(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-pcep - based on the path /openconfig-pcep. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This module defines configuration and operational state data
relating to Path Computation Element Protocol (PCEP) for communications
between a network element (router) acting as PCC and a PCE server,
according to RFC4655 definitions:

-PCC:  Path Computation Client; any client application requesting a
 path computation to be performed by a Path Computation Element.

-PCE:  Path Computation Element; an entity (component, application, or
 network node) that is capable of computing a network path or route
 based on a network graph and applying computational constraints.

Also according to RFC4655, a PCE can be either stateful or
stateless. In the former case, there is a strict synchronization
between the PCE and not only the network states (in term of
topology and resource information), but also the set of computed
paths and reserved resources in use in the network. Conversely,
stateless PCEs do not have to remember any computed path and each
set of request(s) is processed independently of each other. For
example, stateless PCEs may compute paths based on current TED
information, which could be out of sync with actual network state
given other recent PCE-computed paths changes.

On the other hand, RFC8051 defines for Stateful PCE two modes of
operation:

  -Passive Stateful PCE:  a PCE that uses LSP state information
   learned from PCCs to optimize path computations.  It does not
   actively update LSP state. A PCC maintains synchronization with
   the PCE.

  -Active Stateful PCE:  a PCE that may issue recommendations to
   the network. For example, an Active Stateful PCE may use the
   Delegation mechanism to update.

 LSP parameters in those PCCs that delegate control over their LSPs to
 the PCE.
  """
  _pyangbind_elements = {}

  

