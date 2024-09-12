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

import builtins as __builtin__
long = int
class openconfig_mpls_igp(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-mpls-igp - based on the path /openconfig-mpls-igp. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration generic configuration parameters for IGP-congruent
LSPs
  """
  _pyangbind_elements = {}

  

class openconfig_mpls_ldp(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-mpls-ldp - based on the path /openconfig-mpls-ldp. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration of Label Distribution Protocol global and LSP-
specific parameters for IGP-congruent LSPs.

This model reuses data items defined in the IETF YANG model for
LDP described by draft-ietf-mpls-ldp-yang-04, YANG Data Model for
MPLS LDP, following an alternate structure.

Portions of this code were derived from draft-ietf-mpls-ldp-yang-04.
Please reproduce this note if possible.

IETF code is subject to the following copyright and license:
Copyright (c) IETF Trust and the persons identified as authors of
the code.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, is permitted pursuant to, and subject to the license
terms contained in, the Simplified BSD License set forth in
Section 4.c of the IETF Trust's Legal Provisions Relating
to IETF Documents (http://trustee.ietf.org/license-info).
  """
  _pyangbind_elements = {}

  

class openconfig_mpls_rsvp(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-mpls-rsvp - based on the path /openconfig-mpls-rsvp. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration for RSVP-TE signaling, including global protocol
parameters and LSP-specific configuration for constrained-path
LSPs
  """
  _pyangbind_elements = {}

  

class openconfig_mpls_sr(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-mpls-sr - based on the path /openconfig-mpls-sr. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration for MPLS with segment routing-based LSPs,
including global parameters, and LSP-specific configuration for
both constrained-path and IGP-congruent LSPs
  """
  _pyangbind_elements = {}

  

class openconfig_mpls_static(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-mpls-static - based on the path /openconfig-mpls-static. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Defines static LSP configuration
  """
  _pyangbind_elements = {}

  

class openconfig_mpls_te(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-mpls-te - based on the path /openconfig-mpls-te. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration related to constrained-path LSPs and traffic
engineering.  These definitions are not specific to a particular
signaling protocol or mechanism (see related submodules for
signaling protocol-specific configuration).
  """
  _pyangbind_elements = {}

  

class openconfig_mpls_types(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-mpls-types - based on the path /openconfig-mpls-types. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: General types for MPLS / TE data model
  """
  _pyangbind_elements = {}

  

class openconfig_mpls(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-mpls - based on the path /openconfig-mpls. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This module provides data definitions for configuration of
Multiprotocol Label Switching (MPLS) and associated protocols for
signaling and traffic engineering.

RFC 3031: Multiprotocol Label Switching Architecture

The MPLS / TE data model consists of several modules and
submodules as shown below.  The top-level MPLS module describes
the overall framework.  Three types of LSPs are supported:

i) traffic-engineered (or constrained-path)

ii) IGP-congruent (LSPs that follow the IGP path)

iii) static LSPs which are not signaled

The structure of each of these LSP configurations is defined in
corresponding submodules.  Companion modules define the relevant
configuration and operational data specific to key signaling
protocols used in operational practice.


                         +-------+
       +---------------->| MPLS  |<--------------+
       |                 +-------+               |
       |                     ^                   |
       |                     |                   |
  +----+-----+      +--------+-------+     +-----+-----+
  | TE LSPs  |      | IGP-based LSPs |     |static LSPs|
  |          |      |                |     |           |
  +----------+      +----------------+     +-----------+
      ^  ^                    ^  ^
      |  +----------------+   |  +--------+
      |                   |   |           |
      |   +------+      +-+---+-+      +--+--+
      +---+ RSVP |      |SEGMENT|      | LDP |
          +------+      |ROUTING|      +-----+
                        +-------+

  """
  _pyangbind_elements = {}

  

class openconfig_mpls_te(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-mpls-te - based on the path /openconfig-mpls-te. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration related to constrained-path LSPs and traffic
engineering.  These definitions are not specific to a particular
signaling protocol or mechanism (see related submodules for
signaling protocol-specific configuration).
  """
  _pyangbind_elements = {}

  

class openconfig_mpls_igp(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-mpls-igp - based on the path /openconfig-mpls-igp. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration generic configuration parameters for IGP-congruent
LSPs
  """
  _pyangbind_elements = {}

  

class openconfig_mpls_static(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-mpls-static - based on the path /openconfig-mpls-static. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Defines static LSP configuration
  """
  _pyangbind_elements = {}

  

