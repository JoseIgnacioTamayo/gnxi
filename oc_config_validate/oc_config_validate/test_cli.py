"""Copyright 2023 Google LLC.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.

You may obtain a copy of the License at
            https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""
import argparse
import asyncio
import collections
import logging
import os
import sys
from typing import Any, Dict, List, Optional, Tuple

from oc_config_validate import context, schema, target
from oc_config_validate.gnmi import gnmi_pb2  # type: ignore

LOGGING_FORMAT = "%(levelname)s(%(filename)s:%(lineno)d):%(message)s"


def createArgsParser() -> argparse.ArgumentParser:
    """Create parser for arguments passed into the program from the CLI.

     Returns:
        argparse.ArgumentParser object.

     """
    parser = argparse.ArgumentParser(
        description="OpenConfig Configuration Validation utility.")
    parser.add_argument(
        "-tgt",
        "--target",
        type=str,
        help="The gNMI Target, as hostname:port.",
    )
    parser.add_argument(
        "-user",
        "--username",
        type=str,
        help="Username to use when establishing a gNMI Channel to the Target.",
    )
    parser.add_argument(
        "-pass",
        "--password",
        type=str,
        help="Password to use when establishing a gNMI Channel to the Target.",
    )
    parser.add_argument(
        "-x",
        "--xpath",
        type=str,
        action="store",
        help="gNMI Path to query.")
    parser.add_argument(
        "-V", "--verbose", help="Enable gRPC debugging and extra logging.",
        action="store_true")
    parser.add_argument(
        "--no_tls", help="gRPC insecure mode.", action="store_true")
    parser.add_argument(
        "-o",
        "--tls_host_override",
        type=str,
        action="store",
        help="Hostname to use during the TLS certificate check.",
    )
    parser.add_argument(
        "--target_cert_as_root_ca",
        action="store_true",
        help="Fetch the Target TLS cert and use it as client Root CA cert.",
    )
    parser.add_argument(
        "--stop_on_error",
        action="store_true",
        help="Stop the execution if a test fails.",
    )
    return parser


async def gNMIGet(test_target: target.TestTarget,
            xpath: str) -> Optional[gnmi_pb2.TypedValue]:
    logging.info("Get(%s)", xpath)
    try:
        resp = await test_target.gNMIGet(xpath)
    except target.RpcError as err:
        logging.error("<= gRCP Error: %s", err)
        return None
    try:
        resp_val = resp.notification[0].update[0].val
    except IndexError:
        logging.error("<= Bad response: %s", resp)
        return None
    logging.info("<= %s", resp_val)


async def gNMISubsOnce(test_target: target.TestTarget,
                       xpaths: List[str]) -> Optional[
        List[gnmi_pb2.Notification]]:
    logging.info("SubscribeOnce(%s)", xpaths)
    try:
        resp = await test_target.gNMISubsOnce(xpaths)
    except target.RpcError as err:
        logging.error("<= gRCP Error: %s", err)
        return None
    if not resp:
        logging.error("<= Empty response")
        return None
    logging.info("<= %s",
                 schema.notificationsJsonString(resp))


async def gNMISubsStreamSample(
        test_target: target.TestTarget,
        xpath: str,
        sample_interval: int,
        timeout: int) -> Optional[
            Dict[str, List[Tuple[int, Any]]]]:
    logging.info("SubscribeStream(%s)", xpath)
    try:
        resp = await test_target.gNMISubsStreamSample(
            xpath, sample_interval, timeout)
    except target.RpcError as err:
        logging.error("<= gRCP Error: %s", err)
        return None
    if not resp:
        logging.error("<= Empty response")
        return None

    logging.info("<= %s",
                 schema.notificationsJsonString(resp))

    stream_updates = collections.defaultdict(list)
    for n in resp:
        timestamp = n.timestamp
        for u in n.update:
            stream_updates[schema.pathToString(u.path)].append(
                (timestamp, schema.typedValueToPython(u.val)))
    return stream_updates


async def main():  # noqa
    argparser = createArgsParser()
    args = vars(argparser.parse_args())

    if args["verbose"]:
        # os.environ["GRPC_TRACE"] = "all"
        os.environ["GRPC_VERBOSITY"] = "DEBUG"
    logging.basicConfig(
        level=logging.DEBUG if args["verbose"] else logging.INFO,
        format=LOGGING_FORMAT)

    # Target definition
    ctx_tgt = context.Target()
    for arg in ["target", "username", "password", "tls_host_override",
                "target_cert_as_root_ca"]:
        if args[arg]:
            setattr(ctx_tgt, arg, args[arg])
    try:
        ctx_tgt.validate()
    except ValueError as error:
        sys.exit("Invalid Target: %s" % error)
    tgt = target.TestTarget(ctx_tgt)
    logging.info("Testing gNMI Target %s.", tgt)

    tgt.gNMIConnect()
    await gNMIGet(tgt, args["xpath"])
    await gNMISubsOnce(tgt, [args["xpath"]])
    await gNMISubsStreamSample(tgt, args["xpath"],
                               sample_interval=30*1000000000,
                               timeout=65)
    await tgt.gNMIClose()


if __name__ == "__main__":
    asyncio.run(main())
