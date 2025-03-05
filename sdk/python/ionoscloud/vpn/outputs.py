# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from .. import _utilities

__all__ = [
    'IpsecGatewayConnection',
    'IpsecGatewayMaintenanceWindow',
    'IpsecTunnelAuth',
    'IpsecTunnelEsp',
    'IpsecTunnelIke',
    'WireguardGatewayConnection',
    'WireguardGatewayMaintenanceWindow',
    'WireguardPeerEndpoint',
    'GetIpsecGatewayConnectionResult',
    'GetIpsecGatewayMaintenanceWindowResult',
    'GetIpsecTunnelAuthResult',
    'GetIpsecTunnelEspResult',
    'GetIpsecTunnelIkeResult',
    'GetWireguardGatewayConnectionResult',
    'GetWireguardGatewayMaintenanceWindowResult',
    'GetWireguardPeerEndpointResult',
]

@pulumi.output_type
class IpsecGatewayConnection(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "datacenterId":
            suggest = "datacenter_id"
        elif key == "ipv4Cidr":
            suggest = "ipv4_cidr"
        elif key == "lanId":
            suggest = "lan_id"
        elif key == "ipv6Cidr":
            suggest = "ipv6_cidr"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in IpsecGatewayConnection. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        IpsecGatewayConnection.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        IpsecGatewayConnection.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 datacenter_id: str,
                 ipv4_cidr: str,
                 lan_id: str,
                 ipv6_cidr: Optional[str] = None):
        """
        :param str datacenter_id: [string] The datacenter to connect your VPN Gateway to.
        :param str ipv4_cidr: [string] Describes the private ipv4 subnet in your LAN that should be accessible by the
               VPN Gateway. Note: this should be the subnet already assigned to the LAN
        :param str lan_id: [string] The numeric LAN ID to connect your VPN Gateway to.
        :param str ipv6_cidr: [string] Describes the ipv6 subnet in your LAN that should be accessible by the VPN
               Gateway. **Note**: this should be the subnet already assigned to the LAN
        """
        pulumi.set(__self__, "datacenter_id", datacenter_id)
        pulumi.set(__self__, "ipv4_cidr", ipv4_cidr)
        pulumi.set(__self__, "lan_id", lan_id)
        if ipv6_cidr is not None:
            pulumi.set(__self__, "ipv6_cidr", ipv6_cidr)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> str:
        """
        [string] The datacenter to connect your VPN Gateway to.
        """
        return pulumi.get(self, "datacenter_id")

    @property
    @pulumi.getter(name="ipv4Cidr")
    def ipv4_cidr(self) -> str:
        """
        [string] Describes the private ipv4 subnet in your LAN that should be accessible by the
        VPN Gateway. Note: this should be the subnet already assigned to the LAN
        """
        return pulumi.get(self, "ipv4_cidr")

    @property
    @pulumi.getter(name="lanId")
    def lan_id(self) -> str:
        """
        [string] The numeric LAN ID to connect your VPN Gateway to.
        """
        return pulumi.get(self, "lan_id")

    @property
    @pulumi.getter(name="ipv6Cidr")
    def ipv6_cidr(self) -> Optional[str]:
        """
        [string] Describes the ipv6 subnet in your LAN that should be accessible by the VPN
        Gateway. **Note**: this should be the subnet already assigned to the LAN
        """
        return pulumi.get(self, "ipv6_cidr")


@pulumi.output_type
class IpsecGatewayMaintenanceWindow(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "dayOfTheWeek":
            suggest = "day_of_the_week"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in IpsecGatewayMaintenanceWindow. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        IpsecGatewayMaintenanceWindow.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        IpsecGatewayMaintenanceWindow.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 day_of_the_week: str,
                 time: str):
        """
        :param str day_of_the_week: [string] The name of the week day.
        :param str time: [string] Start of the maintenance window in UTC time.
        """
        pulumi.set(__self__, "day_of_the_week", day_of_the_week)
        pulumi.set(__self__, "time", time)

    @property
    @pulumi.getter(name="dayOfTheWeek")
    def day_of_the_week(self) -> str:
        """
        [string] The name of the week day.
        """
        return pulumi.get(self, "day_of_the_week")

    @property
    @pulumi.getter
    def time(self) -> str:
        """
        [string] Start of the maintenance window in UTC time.
        """
        return pulumi.get(self, "time")


@pulumi.output_type
class IpsecTunnelAuth(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "pskKey":
            suggest = "psk_key"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in IpsecTunnelAuth. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        IpsecTunnelAuth.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        IpsecTunnelAuth.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 method: Optional[str] = None,
                 psk_key: Optional[str] = None):
        """
        :param str method: [string] The authentication method to use for IPSec Authentication. Possible values: `PSK`.
               Default value: `PSK`.
        :param str psk_key: [string] The pre-shared key to use for IPSec Authentication. **Note**: Required if method is
               PSK.
        """
        if method is not None:
            pulumi.set(__self__, "method", method)
        if psk_key is not None:
            pulumi.set(__self__, "psk_key", psk_key)

    @property
    @pulumi.getter
    def method(self) -> Optional[str]:
        """
        [string] The authentication method to use for IPSec Authentication. Possible values: `PSK`.
        Default value: `PSK`.
        """
        return pulumi.get(self, "method")

    @property
    @pulumi.getter(name="pskKey")
    def psk_key(self) -> Optional[str]:
        """
        [string] The pre-shared key to use for IPSec Authentication. **Note**: Required if method is
        PSK.
        """
        return pulumi.get(self, "psk_key")


@pulumi.output_type
class IpsecTunnelEsp(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "diffieHellmanGroup":
            suggest = "diffie_hellman_group"
        elif key == "encryptionAlgorithm":
            suggest = "encryption_algorithm"
        elif key == "integrityAlgorithm":
            suggest = "integrity_algorithm"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in IpsecTunnelEsp. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        IpsecTunnelEsp.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        IpsecTunnelEsp.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 diffie_hellman_group: Optional[str] = None,
                 encryption_algorithm: Optional[str] = None,
                 integrity_algorithm: Optional[str] = None,
                 lifetime: Optional[int] = None):
        """
        :param str diffie_hellman_group: [string] The Diffie-Hellman Group to use for IPSec Encryption. Possible
               values: `15-MODP3072`, `16-MODP4096`, `19-ECP256`, `20-ECP384`, `21-ECP521`, `28-ECP256BP`, `29-ECP384BP`, `30-ECP512BP`.
               Default value: `16-MODP4096`.
        :param str encryption_algorithm: [string] The encryption algorithm to use for IPSec Encryption. Possible
               values: `AES128`, `AES256`, `AES128-CTR`, `AES256-CTR`, `AES128-GCM-16`, `AES256-GCM-16`, `AES128-GCM-12`, `AES256-GCM-12`, `AES128-CCM-12`,
               `AES256-CCM-12`. Default value: `AES256`.
        :param str integrity_algorithm: [string] The integrity algorithm to use for IPSec Encryption. Possible
               values: `SHA256`, `SHA384`, `SHA512`, `AES-XCBC`. Default value: `SHA256`.
        :param int lifetime: [string] The phase lifetime in seconds. Minimum value: `3600`. Maximum value: `86400`.
               Default value: `86400`.
        """
        if diffie_hellman_group is not None:
            pulumi.set(__self__, "diffie_hellman_group", diffie_hellman_group)
        if encryption_algorithm is not None:
            pulumi.set(__self__, "encryption_algorithm", encryption_algorithm)
        if integrity_algorithm is not None:
            pulumi.set(__self__, "integrity_algorithm", integrity_algorithm)
        if lifetime is not None:
            pulumi.set(__self__, "lifetime", lifetime)

    @property
    @pulumi.getter(name="diffieHellmanGroup")
    def diffie_hellman_group(self) -> Optional[str]:
        """
        [string] The Diffie-Hellman Group to use for IPSec Encryption. Possible
        values: `15-MODP3072`, `16-MODP4096`, `19-ECP256`, `20-ECP384`, `21-ECP521`, `28-ECP256BP`, `29-ECP384BP`, `30-ECP512BP`.
        Default value: `16-MODP4096`.
        """
        return pulumi.get(self, "diffie_hellman_group")

    @property
    @pulumi.getter(name="encryptionAlgorithm")
    def encryption_algorithm(self) -> Optional[str]:
        """
        [string] The encryption algorithm to use for IPSec Encryption. Possible
        values: `AES128`, `AES256`, `AES128-CTR`, `AES256-CTR`, `AES128-GCM-16`, `AES256-GCM-16`, `AES128-GCM-12`, `AES256-GCM-12`, `AES128-CCM-12`,
        `AES256-CCM-12`. Default value: `AES256`.
        """
        return pulumi.get(self, "encryption_algorithm")

    @property
    @pulumi.getter(name="integrityAlgorithm")
    def integrity_algorithm(self) -> Optional[str]:
        """
        [string] The integrity algorithm to use for IPSec Encryption. Possible
        values: `SHA256`, `SHA384`, `SHA512`, `AES-XCBC`. Default value: `SHA256`.
        """
        return pulumi.get(self, "integrity_algorithm")

    @property
    @pulumi.getter
    def lifetime(self) -> Optional[int]:
        """
        [string] The phase lifetime in seconds. Minimum value: `3600`. Maximum value: `86400`.
        Default value: `86400`.
        """
        return pulumi.get(self, "lifetime")


@pulumi.output_type
class IpsecTunnelIke(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "diffieHellmanGroup":
            suggest = "diffie_hellman_group"
        elif key == "encryptionAlgorithm":
            suggest = "encryption_algorithm"
        elif key == "integrityAlgorithm":
            suggest = "integrity_algorithm"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in IpsecTunnelIke. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        IpsecTunnelIke.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        IpsecTunnelIke.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 diffie_hellman_group: Optional[str] = None,
                 encryption_algorithm: Optional[str] = None,
                 integrity_algorithm: Optional[str] = None,
                 lifetime: Optional[int] = None):
        """
        :param str diffie_hellman_group: [string] The Diffie-Hellman Group to use for IPSec Encryption. Possible
               values: `15-MODP3072`, `16-MODP4096`, `19-ECP256`, `20-ECP384`, `21-ECP521`, `28-ECP256BP`, `29-ECP384BP`, `30-ECP512BP`.
               Default value: `16-MODP4096`.
        :param str encryption_algorithm: [string] The encryption algorithm to use for IPSec Encryption. Possible
               values: `AES128`, `AES256`, `AES128-CTR`, `AES256-CTR`, `AES128-GCM-16`, `AES256-GCM-16`, `AES128-GCM-12`, `AES256-GCM-12`, `AES128-CCM-12`,
               `AES256-CCM-12`. Default value: `AES256`.
        :param str integrity_algorithm: [string] The integrity algorithm to use for IPSec Encryption. Possible
               values: `SHA256`, `SHA384`, `SHA512`, `AES-XCBC`. Default value: `SHA256`.
        :param int lifetime: [string] The phase lifetime in seconds. Minimum value: `3600`. Maximum value: `86400`.
               Default value: `86400`.
        """
        if diffie_hellman_group is not None:
            pulumi.set(__self__, "diffie_hellman_group", diffie_hellman_group)
        if encryption_algorithm is not None:
            pulumi.set(__self__, "encryption_algorithm", encryption_algorithm)
        if integrity_algorithm is not None:
            pulumi.set(__self__, "integrity_algorithm", integrity_algorithm)
        if lifetime is not None:
            pulumi.set(__self__, "lifetime", lifetime)

    @property
    @pulumi.getter(name="diffieHellmanGroup")
    def diffie_hellman_group(self) -> Optional[str]:
        """
        [string] The Diffie-Hellman Group to use for IPSec Encryption. Possible
        values: `15-MODP3072`, `16-MODP4096`, `19-ECP256`, `20-ECP384`, `21-ECP521`, `28-ECP256BP`, `29-ECP384BP`, `30-ECP512BP`.
        Default value: `16-MODP4096`.
        """
        return pulumi.get(self, "diffie_hellman_group")

    @property
    @pulumi.getter(name="encryptionAlgorithm")
    def encryption_algorithm(self) -> Optional[str]:
        """
        [string] The encryption algorithm to use for IPSec Encryption. Possible
        values: `AES128`, `AES256`, `AES128-CTR`, `AES256-CTR`, `AES128-GCM-16`, `AES256-GCM-16`, `AES128-GCM-12`, `AES256-GCM-12`, `AES128-CCM-12`,
        `AES256-CCM-12`. Default value: `AES256`.
        """
        return pulumi.get(self, "encryption_algorithm")

    @property
    @pulumi.getter(name="integrityAlgorithm")
    def integrity_algorithm(self) -> Optional[str]:
        """
        [string] The integrity algorithm to use for IPSec Encryption. Possible
        values: `SHA256`, `SHA384`, `SHA512`, `AES-XCBC`. Default value: `SHA256`.
        """
        return pulumi.get(self, "integrity_algorithm")

    @property
    @pulumi.getter
    def lifetime(self) -> Optional[int]:
        """
        [string] The phase lifetime in seconds. Minimum value: `3600`. Maximum value: `86400`.
        Default value: `86400`.
        """
        return pulumi.get(self, "lifetime")


@pulumi.output_type
class WireguardGatewayConnection(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "datacenterId":
            suggest = "datacenter_id"
        elif key == "lanId":
            suggest = "lan_id"
        elif key == "ipv4Cidr":
            suggest = "ipv4_cidr"
        elif key == "ipv6Cidr":
            suggest = "ipv6_cidr"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WireguardGatewayConnection. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WireguardGatewayConnection.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WireguardGatewayConnection.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 datacenter_id: str,
                 lan_id: str,
                 ipv4_cidr: Optional[str] = None,
                 ipv6_cidr: Optional[str] = None):
        """
        :param str datacenter_id: [String] The ID of the datacenter where the WireGuard Gateway is located.
        :param str lan_id: [String] The ID of the LAN where the WireGuard Gateway is connected.
        :param str ipv4_cidr: [String] The IPv4 CIDR for the WireGuard Gateway connection.
        :param str ipv6_cidr: [String] The IPv6 CIDR for the WireGuard Gateway connection.
        """
        pulumi.set(__self__, "datacenter_id", datacenter_id)
        pulumi.set(__self__, "lan_id", lan_id)
        if ipv4_cidr is not None:
            pulumi.set(__self__, "ipv4_cidr", ipv4_cidr)
        if ipv6_cidr is not None:
            pulumi.set(__self__, "ipv6_cidr", ipv6_cidr)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> str:
        """
        [String] The ID of the datacenter where the WireGuard Gateway is located.
        """
        return pulumi.get(self, "datacenter_id")

    @property
    @pulumi.getter(name="lanId")
    def lan_id(self) -> str:
        """
        [String] The ID of the LAN where the WireGuard Gateway is connected.
        """
        return pulumi.get(self, "lan_id")

    @property
    @pulumi.getter(name="ipv4Cidr")
    def ipv4_cidr(self) -> Optional[str]:
        """
        [String] The IPv4 CIDR for the WireGuard Gateway connection.
        """
        return pulumi.get(self, "ipv4_cidr")

    @property
    @pulumi.getter(name="ipv6Cidr")
    def ipv6_cidr(self) -> Optional[str]:
        """
        [String] The IPv6 CIDR for the WireGuard Gateway connection.
        """
        return pulumi.get(self, "ipv6_cidr")


@pulumi.output_type
class WireguardGatewayMaintenanceWindow(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "dayOfTheWeek":
            suggest = "day_of_the_week"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WireguardGatewayMaintenanceWindow. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WireguardGatewayMaintenanceWindow.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WireguardGatewayMaintenanceWindow.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 day_of_the_week: str,
                 time: str):
        """
        :param str day_of_the_week: [string] The name of the week day.
        :param str time: [string] Start of the maintenance window in UTC time.
        """
        pulumi.set(__self__, "day_of_the_week", day_of_the_week)
        pulumi.set(__self__, "time", time)

    @property
    @pulumi.getter(name="dayOfTheWeek")
    def day_of_the_week(self) -> str:
        """
        [string] The name of the week day.
        """
        return pulumi.get(self, "day_of_the_week")

    @property
    @pulumi.getter
    def time(self) -> str:
        """
        [string] Start of the maintenance window in UTC time.
        """
        return pulumi.get(self, "time")


@pulumi.output_type
class WireguardPeerEndpoint(dict):
    def __init__(__self__, *,
                 host: str,
                 port: Optional[int] = None):
        """
        :param str host: [string] The hostname or IPV4 address that the WireGuard Server will connect to.
        :param int port: [int] The port that the WireGuard Server will connect to. Defaults to `51820`.
        """
        pulumi.set(__self__, "host", host)
        if port is not None:
            pulumi.set(__self__, "port", port)

    @property
    @pulumi.getter
    def host(self) -> str:
        """
        [string] The hostname or IPV4 address that the WireGuard Server will connect to.
        """
        return pulumi.get(self, "host")

    @property
    @pulumi.getter
    def port(self) -> Optional[int]:
        """
        [int] The port that the WireGuard Server will connect to. Defaults to `51820`.
        """
        return pulumi.get(self, "port")


@pulumi.output_type
class GetIpsecGatewayConnectionResult(dict):
    def __init__(__self__, *,
                 datacenter_id: str,
                 ipv4_cidr: str,
                 ipv6_cidr: str,
                 lan_id: str):
        """
        :param str datacenter_id: The datacenter to connect your VPN Gateway to.
        :param str ipv4_cidr: Describes the private ipv4 subnet in your LAN that should be accessible by the
               VPN Gateway.
        :param str ipv6_cidr: Describes the ipv6 subnet in your LAN that should be accessible by the VPN Gateway.
        :param str lan_id: The numeric LAN ID to connect your VPN Gateway to.
        """
        pulumi.set(__self__, "datacenter_id", datacenter_id)
        pulumi.set(__self__, "ipv4_cidr", ipv4_cidr)
        pulumi.set(__self__, "ipv6_cidr", ipv6_cidr)
        pulumi.set(__self__, "lan_id", lan_id)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> str:
        """
        The datacenter to connect your VPN Gateway to.
        """
        return pulumi.get(self, "datacenter_id")

    @property
    @pulumi.getter(name="ipv4Cidr")
    def ipv4_cidr(self) -> str:
        """
        Describes the private ipv4 subnet in your LAN that should be accessible by the
        VPN Gateway.
        """
        return pulumi.get(self, "ipv4_cidr")

    @property
    @pulumi.getter(name="ipv6Cidr")
    def ipv6_cidr(self) -> str:
        """
        Describes the ipv6 subnet in your LAN that should be accessible by the VPN Gateway.
        """
        return pulumi.get(self, "ipv6_cidr")

    @property
    @pulumi.getter(name="lanId")
    def lan_id(self) -> str:
        """
        The numeric LAN ID to connect your VPN Gateway to.
        """
        return pulumi.get(self, "lan_id")


@pulumi.output_type
class GetIpsecGatewayMaintenanceWindowResult(dict):
    def __init__(__self__, *,
                 day_of_the_week: str,
                 time: str):
        """
        :param str day_of_the_week: The name of the week day.
        :param str time: Start of the maintenance window in UTC time.
        """
        pulumi.set(__self__, "day_of_the_week", day_of_the_week)
        pulumi.set(__self__, "time", time)

    @property
    @pulumi.getter(name="dayOfTheWeek")
    def day_of_the_week(self) -> str:
        """
        The name of the week day.
        """
        return pulumi.get(self, "day_of_the_week")

    @property
    @pulumi.getter
    def time(self) -> str:
        """
        Start of the maintenance window in UTC time.
        """
        return pulumi.get(self, "time")


@pulumi.output_type
class GetIpsecTunnelAuthResult(dict):
    def __init__(__self__, *,
                 method: str):
        """
        :param str method: The Authentication Method to use for IPSec Authentication.
        """
        pulumi.set(__self__, "method", method)

    @property
    @pulumi.getter
    def method(self) -> str:
        """
        The Authentication Method to use for IPSec Authentication.
        """
        return pulumi.get(self, "method")


@pulumi.output_type
class GetIpsecTunnelEspResult(dict):
    def __init__(__self__, *,
                 diffie_hellman_group: str,
                 encryption_algorithm: str,
                 integrity_algorithm: str,
                 lifetime: int):
        """
        :param str diffie_hellman_group: The Diffie-Hellman Group to use for IPSec Encryption.
        :param str encryption_algorithm: The encryption algorithm to use for IPSec Encryption.
        :param str integrity_algorithm: The integrity algorithm to use for IPSec Encryption.
        :param int lifetime: The phase lifetime in seconds.
        """
        pulumi.set(__self__, "diffie_hellman_group", diffie_hellman_group)
        pulumi.set(__self__, "encryption_algorithm", encryption_algorithm)
        pulumi.set(__self__, "integrity_algorithm", integrity_algorithm)
        pulumi.set(__self__, "lifetime", lifetime)

    @property
    @pulumi.getter(name="diffieHellmanGroup")
    def diffie_hellman_group(self) -> str:
        """
        The Diffie-Hellman Group to use for IPSec Encryption.
        """
        return pulumi.get(self, "diffie_hellman_group")

    @property
    @pulumi.getter(name="encryptionAlgorithm")
    def encryption_algorithm(self) -> str:
        """
        The encryption algorithm to use for IPSec Encryption.
        """
        return pulumi.get(self, "encryption_algorithm")

    @property
    @pulumi.getter(name="integrityAlgorithm")
    def integrity_algorithm(self) -> str:
        """
        The integrity algorithm to use for IPSec Encryption.
        """
        return pulumi.get(self, "integrity_algorithm")

    @property
    @pulumi.getter
    def lifetime(self) -> int:
        """
        The phase lifetime in seconds.
        """
        return pulumi.get(self, "lifetime")


@pulumi.output_type
class GetIpsecTunnelIkeResult(dict):
    def __init__(__self__, *,
                 diffie_hellman_group: str,
                 encryption_algorithm: str,
                 integrity_algorithm: str,
                 lifetime: int):
        """
        :param str diffie_hellman_group: The Diffie-Hellman Group to use for IPSec Encryption.
        :param str encryption_algorithm: The encryption algorithm to use for IPSec Encryption.
        :param str integrity_algorithm: The integrity algorithm to use for IPSec Encryption.
        :param int lifetime: The phase lifetime in seconds.
        """
        pulumi.set(__self__, "diffie_hellman_group", diffie_hellman_group)
        pulumi.set(__self__, "encryption_algorithm", encryption_algorithm)
        pulumi.set(__self__, "integrity_algorithm", integrity_algorithm)
        pulumi.set(__self__, "lifetime", lifetime)

    @property
    @pulumi.getter(name="diffieHellmanGroup")
    def diffie_hellman_group(self) -> str:
        """
        The Diffie-Hellman Group to use for IPSec Encryption.
        """
        return pulumi.get(self, "diffie_hellman_group")

    @property
    @pulumi.getter(name="encryptionAlgorithm")
    def encryption_algorithm(self) -> str:
        """
        The encryption algorithm to use for IPSec Encryption.
        """
        return pulumi.get(self, "encryption_algorithm")

    @property
    @pulumi.getter(name="integrityAlgorithm")
    def integrity_algorithm(self) -> str:
        """
        The integrity algorithm to use for IPSec Encryption.
        """
        return pulumi.get(self, "integrity_algorithm")

    @property
    @pulumi.getter
    def lifetime(self) -> int:
        """
        The phase lifetime in seconds.
        """
        return pulumi.get(self, "lifetime")


@pulumi.output_type
class GetWireguardGatewayConnectionResult(dict):
    def __init__(__self__, *,
                 datacenter_id: str,
                 ipv4_cidr: str,
                 ipv6_cidr: str,
                 lan_id: str):
        """
        :param str datacenter_id: The ID of the datacenter where the WireGuard Gateway is located.
        :param str ipv4_cidr: The IPv4 CIDR for the WireGuard Gateway connection.
        :param str ipv6_cidr: The IPv6 CIDR for the WireGuard Gateway connection.
        :param str lan_id: The ID of the LAN where the WireGuard Gateway is connected.
        """
        pulumi.set(__self__, "datacenter_id", datacenter_id)
        pulumi.set(__self__, "ipv4_cidr", ipv4_cidr)
        pulumi.set(__self__, "ipv6_cidr", ipv6_cidr)
        pulumi.set(__self__, "lan_id", lan_id)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> str:
        """
        The ID of the datacenter where the WireGuard Gateway is located.
        """
        return pulumi.get(self, "datacenter_id")

    @property
    @pulumi.getter(name="ipv4Cidr")
    def ipv4_cidr(self) -> str:
        """
        The IPv4 CIDR for the WireGuard Gateway connection.
        """
        return pulumi.get(self, "ipv4_cidr")

    @property
    @pulumi.getter(name="ipv6Cidr")
    def ipv6_cidr(self) -> str:
        """
        The IPv6 CIDR for the WireGuard Gateway connection.
        """
        return pulumi.get(self, "ipv6_cidr")

    @property
    @pulumi.getter(name="lanId")
    def lan_id(self) -> str:
        """
        The ID of the LAN where the WireGuard Gateway is connected.
        """
        return pulumi.get(self, "lan_id")


@pulumi.output_type
class GetWireguardGatewayMaintenanceWindowResult(dict):
    def __init__(__self__, *,
                 day_of_the_week: str,
                 time: str):
        """
        :param str day_of_the_week: The name of the week day.
        :param str time: Start of the maintenance window in UTC time.
        """
        pulumi.set(__self__, "day_of_the_week", day_of_the_week)
        pulumi.set(__self__, "time", time)

    @property
    @pulumi.getter(name="dayOfTheWeek")
    def day_of_the_week(self) -> str:
        """
        The name of the week day.
        """
        return pulumi.get(self, "day_of_the_week")

    @property
    @pulumi.getter
    def time(self) -> str:
        """
        Start of the maintenance window in UTC time.
        """
        return pulumi.get(self, "time")


@pulumi.output_type
class GetWireguardPeerEndpointResult(dict):
    def __init__(__self__, *,
                 host: str,
                 port: int):
        """
        :param str host: Hostname or IPV4 address that the WireGuard Server will connect to.
        :param int port: Port that the WireGuard Server will connect to. Default: 51820
        """
        pulumi.set(__self__, "host", host)
        pulumi.set(__self__, "port", port)

    @property
    @pulumi.getter
    def host(self) -> str:
        """
        Hostname or IPV4 address that the WireGuard Server will connect to.
        """
        return pulumi.get(self, "host")

    @property
    @pulumi.getter
    def port(self) -> int:
        """
        Port that the WireGuard Server will connect to. Default: 51820
        """
        return pulumi.get(self, "port")


