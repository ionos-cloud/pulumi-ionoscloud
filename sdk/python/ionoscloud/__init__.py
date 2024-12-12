# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .apigateway import *
from .apigateway_route import *
from .application_loadbalancer import *
from .application_loadbalancer_forwardingrule import *
from .auto_certificate import *
from .auto_certificate_provider import *
from .autoscaling_group import *
from .certificate import *
from .cube_server import *
from .get_apigateway import *
from .get_apigateway_route import *
from .get_application_loadbalancer import *
from .get_application_loadbalancer_forwardingrule import *
from .get_auto_certificate import *
from .get_auto_certificate_provider import *
from .get_autoscaling_group import *
from .get_autoscaling_group_servers import *
from .get_backup_unit import *
from .get_cdn_distribution import *
from .get_certificate import *
from .get_container_registry import *
from .get_container_registry_locations import *
from .get_container_registry_token import *
from .get_cube_server import *
from .get_datacenter import *
from .get_dataplatform_cluster import *
from .get_dataplatform_node_pool import *
from .get_dataplatform_node_pools import *
from .get_dataplatform_versions import *
from .get_dns_record import *
from .get_dns_zone import *
from .get_firewall import *
from .get_group import *
from .get_image import *
from .get_inmemorydb_replicaset import *
from .get_inmemorydb_snapshot import *
from .get_ipblock import *
from .get_ipfailover import *
from .get_k8s_cluster import *
from .get_k8s_clusters import *
from .get_k8s_node_pool import *
from .get_k8s_node_pool_nodes import *
from .get_kafka_cluster import *
from .get_kafka_cluster_topic import *
from .get_lan import *
from .get_location import *
from .get_logging_pipeline import *
from .get_mariadb_backups import *
from .get_mariadb_cluster import *
from .get_mongo_cluster import *
from .get_mongo_template import *
from .get_mongo_user import *
from .get_natgateway import *
from .get_natgateway_rule import *
from .get_networkloadbalancer import *
from .get_networkloadbalancer_forwardingrule import *
from .get_nfs_cluster import *
from .get_nfs_share import *
from .get_nic import *
from .get_pg_backups import *
from .get_pg_cluster import *
from .get_pg_database import *
from .get_pg_databases import *
from .get_pg_user import *
from .get_pg_versions import *
from .get_private_crossconnect import *
from .get_resource import *
from .get_s3_key import *
from .get_server import *
from .get_servers import *
from .get_share import *
from .get_snapshot import *
from .get_target_group import *
from .get_template import *
from .get_user import *
from .get_vcpu_server import *
from .get_volume import *
from .get_vpn_ipsec_gateway import *
from .get_vpn_ipsec_tunnel import *
from .get_vpn_wireguard_gateway import *
from .get_vpn_wireguard_peer import *
from .ipfailover import *
from .kafka_cluster import *
from .kafka_cluster_topic import *
from .loadbalancer import *
from .logging_pipeline import *
from .natgateway import *
from .natgateway_rule import *
from .networkloadbalancer import *
from .networkloadbalancer_forwardingrule import *
from .private_crossconnect import *
from .provider import *
from .server_boot_device_selection import *
from .share import *
from .snapshot import *
from .target_group import *
from .vcpu_server import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import ionoscloud.cdn as __cdn
    cdn = __cdn
    import ionoscloud.compute as __compute
    compute = __compute
    import ionoscloud.config as __config
    config = __config
    import ionoscloud.creg as __creg
    creg = __creg
    import ionoscloud.dbaas as __dbaas
    dbaas = __dbaas
    import ionoscloud.dns as __dns
    dns = __dns
    import ionoscloud.dsaas as __dsaas
    dsaas = __dsaas
    import ionoscloud.k8s as __k8s
    k8s = __k8s
    import ionoscloud.nfs as __nfs
    nfs = __nfs
    import ionoscloud.vpn as __vpn
    vpn = __vpn
else:
    cdn = _utilities.lazy_import('ionoscloud.cdn')
    compute = _utilities.lazy_import('ionoscloud.compute')
    config = _utilities.lazy_import('ionoscloud.config')
    creg = _utilities.lazy_import('ionoscloud.creg')
    dbaas = _utilities.lazy_import('ionoscloud.dbaas')
    dns = _utilities.lazy_import('ionoscloud.dns')
    dsaas = _utilities.lazy_import('ionoscloud.dsaas')
    k8s = _utilities.lazy_import('ionoscloud.k8s')
    nfs = _utilities.lazy_import('ionoscloud.nfs')
    vpn = _utilities.lazy_import('ionoscloud.vpn')

_utilities.register(
    resource_modules="""
[
 {
  "pkg": "ionoscloud",
  "mod": "cdn/distribution",
  "fqn": "ionoscloud.cdn",
  "classes": {
   "ionoscloud:cdn/distribution:Distribution": "Distribution"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "compute/backupUnit",
  "fqn": "ionoscloud.compute",
  "classes": {
   "ionoscloud:compute/backupUnit:BackupUnit": "BackupUnit"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "compute/datacenter",
  "fqn": "ionoscloud.compute",
  "classes": {
   "ionoscloud:compute/datacenter:Datacenter": "Datacenter"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "compute/firewall",
  "fqn": "ionoscloud.compute",
  "classes": {
   "ionoscloud:compute/firewall:Firewall": "Firewall"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "compute/group",
  "fqn": "ionoscloud.compute",
  "classes": {
   "ionoscloud:compute/group:Group": "Group"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "compute/iPBlock",
  "fqn": "ionoscloud.compute",
  "classes": {
   "ionoscloud:compute/iPBlock:IPBlock": "IPBlock"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "compute/lan",
  "fqn": "ionoscloud.compute",
  "classes": {
   "ionoscloud:compute/lan:Lan": "Lan"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "compute/nic",
  "fqn": "ionoscloud.compute",
  "classes": {
   "ionoscloud:compute/nic:Nic": "Nic"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "compute/s3Key",
  "fqn": "ionoscloud.compute",
  "classes": {
   "ionoscloud:compute/s3Key:S3Key": "S3Key"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "compute/server",
  "fqn": "ionoscloud.compute",
  "classes": {
   "ionoscloud:compute/server:Server": "Server"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "compute/user",
  "fqn": "ionoscloud.compute",
  "classes": {
   "ionoscloud:compute/user:User": "User"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "compute/volume",
  "fqn": "ionoscloud.compute",
  "classes": {
   "ionoscloud:compute/volume:Volume": "Volume"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "creg/registry",
  "fqn": "ionoscloud.creg",
  "classes": {
   "ionoscloud:creg/registry:Registry": "Registry"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "creg/registryToken",
  "fqn": "ionoscloud.creg",
  "classes": {
   "ionoscloud:creg/registryToken:RegistryToken": "RegistryToken"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "dbaas/inMemoryDBReplicaSet",
  "fqn": "ionoscloud.dbaas",
  "classes": {
   "ionoscloud:dbaas/inMemoryDBReplicaSet:InMemoryDBReplicaSet": "InMemoryDBReplicaSet"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "dbaas/mariaDBCluster",
  "fqn": "ionoscloud.dbaas",
  "classes": {
   "ionoscloud:dbaas/mariaDBCluster:MariaDBCluster": "MariaDBCluster"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "dbaas/mongoCluster",
  "fqn": "ionoscloud.dbaas",
  "classes": {
   "ionoscloud:dbaas/mongoCluster:MongoCluster": "MongoCluster"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "dbaas/mongoUser",
  "fqn": "ionoscloud.dbaas",
  "classes": {
   "ionoscloud:dbaas/mongoUser:MongoUser": "MongoUser"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "dbaas/pSQLCluster",
  "fqn": "ionoscloud.dbaas",
  "classes": {
   "ionoscloud:dbaas/pSQLCluster:PSQLCluster": "PSQLCluster"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "dbaas/pSQLDatabase",
  "fqn": "ionoscloud.dbaas",
  "classes": {
   "ionoscloud:dbaas/pSQLDatabase:PSQLDatabase": "PSQLDatabase"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "dbaas/pSQLUser",
  "fqn": "ionoscloud.dbaas",
  "classes": {
   "ionoscloud:dbaas/pSQLUser:PSQLUser": "PSQLUser"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "dns/record",
  "fqn": "ionoscloud.dns",
  "classes": {
   "ionoscloud:dns/record:Record": "Record"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "dns/zone",
  "fqn": "ionoscloud.dns",
  "classes": {
   "ionoscloud:dns/zone:Zone": "Zone"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "dsaas/cluster",
  "fqn": "ionoscloud.dsaas",
  "classes": {
   "ionoscloud:dsaas/cluster:Cluster": "Cluster"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "dsaas/nodePool",
  "fqn": "ionoscloud.dsaas",
  "classes": {
   "ionoscloud:dsaas/nodePool:NodePool": "NodePool"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "index/apigateway",
  "fqn": "ionoscloud",
  "classes": {
   "ionoscloud:index/apigateway:Apigateway": "Apigateway"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "index/apigatewayRoute",
  "fqn": "ionoscloud",
  "classes": {
   "ionoscloud:index/apigatewayRoute:ApigatewayRoute": "ApigatewayRoute"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "index/applicationLoadbalancer",
  "fqn": "ionoscloud",
  "classes": {
   "ionoscloud:index/applicationLoadbalancer:ApplicationLoadbalancer": "ApplicationLoadbalancer"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "index/applicationLoadbalancerForwardingrule",
  "fqn": "ionoscloud",
  "classes": {
   "ionoscloud:index/applicationLoadbalancerForwardingrule:ApplicationLoadbalancerForwardingrule": "ApplicationLoadbalancerForwardingrule"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "index/autoCertificate",
  "fqn": "ionoscloud",
  "classes": {
   "ionoscloud:index/autoCertificate:AutoCertificate": "AutoCertificate"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "index/autoCertificateProvider",
  "fqn": "ionoscloud",
  "classes": {
   "ionoscloud:index/autoCertificateProvider:AutoCertificateProvider": "AutoCertificateProvider"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "index/autoscalingGroup",
  "fqn": "ionoscloud",
  "classes": {
   "ionoscloud:index/autoscalingGroup:AutoscalingGroup": "AutoscalingGroup"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "index/certificate",
  "fqn": "ionoscloud",
  "classes": {
   "ionoscloud:index/certificate:Certificate": "Certificate"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "index/cubeServer",
  "fqn": "ionoscloud",
  "classes": {
   "ionoscloud:index/cubeServer:CubeServer": "CubeServer"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "index/ipfailover",
  "fqn": "ionoscloud",
  "classes": {
   "ionoscloud:index/ipfailover:Ipfailover": "Ipfailover"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "index/kafkaCluster",
  "fqn": "ionoscloud",
  "classes": {
   "ionoscloud:index/kafkaCluster:KafkaCluster": "KafkaCluster"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "index/kafkaClusterTopic",
  "fqn": "ionoscloud",
  "classes": {
   "ionoscloud:index/kafkaClusterTopic:KafkaClusterTopic": "KafkaClusterTopic"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "index/loadbalancer",
  "fqn": "ionoscloud",
  "classes": {
   "ionoscloud:index/loadbalancer:Loadbalancer": "Loadbalancer"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "index/loggingPipeline",
  "fqn": "ionoscloud",
  "classes": {
   "ionoscloud:index/loggingPipeline:LoggingPipeline": "LoggingPipeline"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "index/natgateway",
  "fqn": "ionoscloud",
  "classes": {
   "ionoscloud:index/natgateway:Natgateway": "Natgateway"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "index/natgatewayRule",
  "fqn": "ionoscloud",
  "classes": {
   "ionoscloud:index/natgatewayRule:NatgatewayRule": "NatgatewayRule"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "index/networkloadbalancer",
  "fqn": "ionoscloud",
  "classes": {
   "ionoscloud:index/networkloadbalancer:Networkloadbalancer": "Networkloadbalancer"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "index/networkloadbalancerForwardingrule",
  "fqn": "ionoscloud",
  "classes": {
   "ionoscloud:index/networkloadbalancerForwardingrule:NetworkloadbalancerForwardingrule": "NetworkloadbalancerForwardingrule"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "index/privateCrossconnect",
  "fqn": "ionoscloud",
  "classes": {
   "ionoscloud:index/privateCrossconnect:PrivateCrossconnect": "PrivateCrossconnect"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "index/serverBootDeviceSelection",
  "fqn": "ionoscloud",
  "classes": {
   "ionoscloud:index/serverBootDeviceSelection:ServerBootDeviceSelection": "ServerBootDeviceSelection"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "index/share",
  "fqn": "ionoscloud",
  "classes": {
   "ionoscloud:index/share:Share": "Share"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "index/snapshot",
  "fqn": "ionoscloud",
  "classes": {
   "ionoscloud:index/snapshot:Snapshot": "Snapshot"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "index/targetGroup",
  "fqn": "ionoscloud",
  "classes": {
   "ionoscloud:index/targetGroup:TargetGroup": "TargetGroup"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "index/vcpuServer",
  "fqn": "ionoscloud",
  "classes": {
   "ionoscloud:index/vcpuServer:VcpuServer": "VcpuServer"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "k8s/cluster",
  "fqn": "ionoscloud.k8s",
  "classes": {
   "ionoscloud:k8s/cluster:Cluster": "Cluster"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "k8s/nodePool",
  "fqn": "ionoscloud.k8s",
  "classes": {
   "ionoscloud:k8s/nodePool:NodePool": "NodePool"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "nfs/cluster",
  "fqn": "ionoscloud.nfs",
  "classes": {
   "ionoscloud:nfs/cluster:Cluster": "Cluster"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "nfs/share",
  "fqn": "ionoscloud.nfs",
  "classes": {
   "ionoscloud:nfs/share:Share": "Share"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "vpn/ipsecGateway",
  "fqn": "ionoscloud.vpn",
  "classes": {
   "ionoscloud:vpn/ipsecGateway:IpsecGateway": "IpsecGateway"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "vpn/ipsecTunnel",
  "fqn": "ionoscloud.vpn",
  "classes": {
   "ionoscloud:vpn/ipsecTunnel:IpsecTunnel": "IpsecTunnel"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "vpn/wireguardGateway",
  "fqn": "ionoscloud.vpn",
  "classes": {
   "ionoscloud:vpn/wireguardGateway:WireguardGateway": "WireguardGateway"
  }
 },
 {
  "pkg": "ionoscloud",
  "mod": "vpn/wireguardPeer",
  "fqn": "ionoscloud.vpn",
  "classes": {
   "ionoscloud:vpn/wireguardPeer:WireguardPeer": "WireguardPeer"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "ionoscloud",
  "token": "pulumi:providers:ionoscloud",
  "fqn": "ionoscloud",
  "class": "Provider"
 }
]
"""
)
