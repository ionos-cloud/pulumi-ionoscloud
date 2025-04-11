// Copyright 2016-2024, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package ionoscloud

import (
	"path"

	// Allow embedding bridge-metadata.json in the provider.
	_ "embed"

	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge"
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge/info"
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge/tokens"
	shimv2 "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim/sdk-v2"

	// Replace this provider with the provider you are bridging.
	"github.com/ionos-cloud/terraform-provider-ionoscloud/v6/ionoscloud"

	"github.com/ionos-cloud/pulumi-ionoscloud/provider/pkg/version"
)

// all of the token components used below.
const (
	// This variable controls the default name of the package in the package
	// registries for nodejs and python:
	mainPkg = "ionoscloud"
	// modules:
	mainMod       = "index"       // the ionoscloud module
	computeModule = "compute"     // the compute module
	dbaasModule   = "dbaas"       // the dbaas module
	k8sModule     = "k8s"         // the k8s module
	certModule    = "cert"        // the certificate manager module
	dsaasModule   = "dsaas"       // the dataplatform module
	nfsModule     = "nfs"         // the nfs module
	vpnModule     = "vpn"         // the vpn module
	cdnModule     = "cdn"         // the cdn module
	dnsModule     = "dns"         // the dns module
	cregModule    = "creg"        // the container registry module
	kafkaModule   = "kafka"       // the kafka module
	apigModule    = "apigateway"  // the apigateway module
	autosclModule = "autoscaling" // the autoscaling module
	loggingModule = "logging"     // the logging module
	albModule     = "alb"         // the applicationloadblancer module
	nlbModule     = "nlb"         // the networkloadblancer module
	nsgModule     = "nsg"         // the network security group module
)

//go:embed cmd/pulumi-resource-ionoscloud/bridge-metadata.json
var metadata []byte

// Provider returns additional overlaid schema and metadata associated with the provider.
func Provider() tfbridge.ProviderInfo {
	// Create a Pulumi provider mapping
	prov := tfbridge.ProviderInfo{
		// Instantiate the Terraform provider
		//
		// The [pulumi-terraform-bridge](https://github.com/pulumi/pulumi-terraform-bridge) supports 3
		// types of Terraform providers:
		//
		// 1. Providers written with the terraform-plugin-sdk/v1:
		//
		//    If the provider you are bridging is written with the terraform-plugin-sdk/v1, then you
		//    will need to adapt the boilerplate:
		//
		//    - Change the import "shimv2" to "shimv1" and change the associated import to
		//      "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim/sdk-v1".
		//
		//    You can then proceed as normal.
		//
		// 2. Providers written with terraform-plugin-sdk/v2:
		//
		//    This boilerplate is already geared towards providers written with the
		//    terraform-plugin-sdk/v2, since it is the most common provider framework used. No
		//    adaptions are needed.
		//
		// 3. Providers written with terraform-plugin-framework:
		//
		//    If the provider you are bridging is written with the terraform-plugin-framework, then
		//    you will need to adapt the boilerplate:
		//
		//    - Remove the `shimv2` import and add:
		//
		//      	pfbridge "github.com/pulumi/pulumi-terraform-bridge/pf/tfbridge"
		//
		//    - Replace `shimv2.NewProvider` with `pfbridge.ShimProvider`.
		//
		//    - In provider/cmd/pulumi-tfgen-ionoscloud/main.go, replace the
		//      "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfgen" import with
		//      "github.com/pulumi/pulumi-terraform-bridge/pf/tfgen". Remove the `version.Version`
		//      argument to `tfgen.Main`.
		//
		//    - In provider/cmd/pulumi-resource-ionoscloud/main.go, replace the
		//      "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge" import with
		//      "github.com/pulumi/pulumi-terraform-bridge/pf/tfbridge". Replace the arguments to the
		//      `tfbridge.Main` so it looks like this:
		//
		//      	tfbridge.Main(context.Background(), "ionoscloud", ionoscloud.Provider(),
		//			tfbridge.ProviderMetadata{PulumiSchema: pulumiSchema})
		//
		//   Detailed instructions can be found at
		//   https://github.com/pulumi/pulumi-terraform-bridge/blob/master/pf/README.md#how-to-upgrade-a-bridged-provider-to-plugin-framework.
		//   After that, you can proceed as normal.
		//
		// This is where you give the bridge a handle to the upstream terraform provider. SDKv2
		// convention is to have a function at "github.com/iwahbe/terraform-provider-ionoscloud/provider".New
		// which takes a version and produces a factory function. The provider you are bridging may
		// not do that. You will need to find the function (generally called in upstream's main.go)
		// that produces a:
		//
		// - *"github.com/hashicorp/terraform-plugin-sdk/v2/helper/schema".Provider (for SDKv2)
		// - *"github.com/hashicorp/terraform-plugin-sdk/v1/helper/schema".Provider (for SDKv1)
		// - "github.com/hashicorp/terraform-plugin-framework/provider".Provider (for plugin-framework)
		//
		//nolint:lll
		P: shimv2.NewProvider(ionoscloud.Provider()),

		Name:    "ionoscloud",
		Version: version.Version,
		// DisplayName is a way to be able to change the casing of the provider name when being
		// displayed on the Pulumi registry
		DisplayName: "IonosCloud",
		// Change this to your personal name (or a company name) that you would like to be shown in
		// the Pulumi Registry if this package is published there.
		Publisher: "ionos-cloud",
		// LogoURL is optional but useful to help identify your package in the Pulumi Registry
		// if this package is published there.
		//
		// You may host a logo on a domain you control or add an PNG logo (100x100) for your package
		// in your repository and use the raw content URL for that file as your logo URL.
		LogoURL: "",
		// PluginDownloadURL is an optional URL used to download the Provider
		// for use in Pulumi programs
		// e.g. https://github.com/org/pulumi-provider-name/releases/download/v${VERSION}/
		//PluginDownloadURL: "github://api.github.com/ionos-cloud",
		Description: "A Pulumi package for creating and managing ionoscloud cloud resources.",
		// category/cloud tag helps with categorizing the package in the Pulumi Registry.
		// For all available categories, see `Keywords` in
		// https://www.pulumi.com/docs/guides/pulumi-packages/schema/#package.
		Keywords:                []string{"ionos-cloud", "ionoscloud", "category/cloud"},
		License:                 "Apache-2.0",
		Homepage:                "https://www.pulumi.com",
		Repository:              "https://github.com/ionos-cloud/pulumi-ionoscloud",
		UpstreamRepoPath:        "./upstream",
		TFProviderModuleVersion: "v6",
		SkipValidateProviderConfigForPluginFramework: true,
		// The GitHub Org for the provider - defaults to `terraform-providers`. Note that this should
		// match the TF provider module's require directive, not any replace directives.
		GitHubOrg:    "ionos-cloud",
		MetadataInfo: tfbridge.NewProviderMetadata(metadata),
		Config:       map[string]*tfbridge.SchemaInfo{
			// Add any required configuration here, or remove the example below if
			// no additional points are required.
			// "region": {
			// 	Type: tfbridge.MakeType("region", "Region"),
			// 	Default: &tfbridge.DefaultInfo{
			// 		EnvVars: []string{"AWS_REGION", "AWS_DEFAULT_REGION"},
			// 	},
			// },
		},
		JavaScript: &tfbridge.JavaScriptInfo{
			PackageName:          "@ionos-cloud/sdk-pulumi",
			RespectSchemaVersion: true,
			// List any npm dependencies and their versions
			Dependencies: map[string]string{
				"@pulumi/pulumi": "^3.0.0",
			},
			DevDependencies: map[string]string{
				"@types/node": "^10.0.0", // so we can access strongly typed node definitions.
				"@types/mime": "^2.0.0",
			},
		},
		Python: (func() *tfbridge.PythonInfo {
			i := &tfbridge.PythonInfo{
				RespectSchemaVersion: true,
				PackageName:          "pulumi_" + mainPkg,
				Requires: map[string]string{
					"pulumi": ">=3.0.0,<4.0.0",
				},
			}
			i.PyProject.Enabled = true
			i.InputTypes = tfbridge.PythonInputTypeClassesAndDicts
			return i
		})(),
		Golang: &tfbridge.GolangInfo{
			ImportBasePath: path.Join(
				"github.com/ionos-cloud/pulumi-ionoscloud/sdk/",
				tfbridge.GetModuleMajorVersion(version.Version),
				"go",
				mainPkg,
			),
			GenerateResourceContainerTypes: true,
			RespectSchemaVersion:           true,
		},
		CSharp: &tfbridge.CSharpInfo{
			RootNamespace:        "Ionoscloud.Pulumi",
			RespectSchemaVersion: true,
			PackageReferences: map[string]string{
				"Pulumi": "3.*",
			},
		},
		Java: &tfbridge.JavaInfo{
			BasePackage: "com.ionoscloud.pulumi",
		},
		DataSources: map[string]*info.DataSource{
			"ionoscloud_kafka_cluster": {
				Tok:  tfbridge.MakeDataSource(mainPkg, kafkaModule, "getCluster"),
				Docs: &tfbridge.DocInfo{Source: "kafka_cluster.md"},
			},
			"ionoscloud_kafka_cluster_topic": {
				Tok:  tfbridge.MakeDataSource(mainPkg, kafkaModule, "getTopic"),
				Docs: &tfbridge.DocInfo{Source: "kafka_topic.md"},
			},
			"ionoscloud_apigateway": {
				Tok: tfbridge.MakeDataSource(mainPkg, apigModule, "getApigateway"),
			},
			"ionoscloud_apigateway_route": {
				Tok: tfbridge.MakeDataSource(mainPkg, apigModule, "getRoute"),
			},
			"ionoscloud_autoscaling_group": {
				Tok: tfbridge.MakeDataSource(mainPkg, autosclModule, "getGroup"),
			},
			"ionoscloud_autoscaling_group_servers": {
				Tok: tfbridge.MakeDataSource(mainPkg, autosclModule, "getServers"),
			},
			"ionoscloud_datacenter": {
				Tok: tfbridge.MakeDataSource(mainPkg, computeModule, "getDatacenter"),
			},
			"ionoscloud_server": {
				Tok: tfbridge.MakeDataSource(mainPkg, computeModule, "getServer"),
			},
			"ionoscloud_servers": {
				Tok: tfbridge.MakeDataSource(mainPkg, computeModule, "getServers"),
			},
			"ionoscloud_vcpu_server": {
				Tok: tfbridge.MakeDataSource(mainPkg, computeModule, "getVCPUServer"),
			},
			"ionoscloud_cube_server": {
				Tok: tfbridge.MakeDataSource(mainPkg, computeModule, "getCubeServer"),
			},
			"ionoscloud_lan": {
				Tok: tfbridge.MakeDataSource(mainPkg, computeModule, "getLan"),
			},
			"ionoscloud_nic": {
				Tok: tfbridge.MakeDataSource(mainPkg, computeModule, "getNic"),
			},
			"ionoscloud_volume": {
				Tok: tfbridge.MakeDataSource(mainPkg, computeModule, "getVolume"),
			},
			"ionoscloud_firewall": {
				Tok: tfbridge.MakeDataSource(mainPkg, computeModule, "getFirewall"),
			},
			"ionoscloud_group": {
				Tok: tfbridge.MakeDataSource(mainPkg, computeModule, "getGroup"),
			},
			"ionoscloud_user": {
				Tok: tfbridge.MakeDataSource(mainPkg, computeModule, "getUser"),
			},
			"ionoscloud_ipblock": {
				Tok: tfbridge.MakeDataSource(mainPkg, computeModule, "getIPBlock"),
			},
			"ionoscloud_share": {
				Tok: tfbridge.MakeDataSource(mainPkg, computeModule, "getShare"),
			},
			"ionoscloud_ipfailover": {
				Tok: tfbridge.MakeDataSource(mainPkg, computeModule, "getIPFailover"),
			},
			"ionoscloud_private_crossconnect": {
				Tok: tfbridge.MakeDataSource(mainPkg, computeModule, "getCrossconnect"),
			},
			"ionoscloud_s3_key": {
				Tok: tfbridge.MakeDataSource(mainPkg, computeModule, "getS3Key"),
			},
			"ionoscloud_backup_unit": {
				Tok: tfbridge.MakeDataSource(mainPkg, computeModule, "getBackupUnit"),
			},
			"ionoscloud_snapshot": {
				Tok: tfbridge.MakeDataSource(mainPkg, computeModule, "getSnapshot"),
			},
			"ionoscloud_natgateway": {
				Tok: tfbridge.MakeDataSource(mainPkg, computeModule, "getNatGateway"),
			},
			"ionoscloud_natgateway_rule": {
				Tok: tfbridge.MakeDataSource(mainPkg, computeModule, "getNatGatewayRule"),
			},
			"ionoscloud_image": {
				Tok: tfbridge.MakeDataSource(mainPkg, computeModule, "getImage"),
			},
			"ionoscloud_location": {
				Tok: tfbridge.MakeDataSource(mainPkg, computeModule, "getLocation"),
			},
			"ionoscloud_template": {
				Tok: tfbridge.MakeDataSource(mainPkg, computeModule, "getTemplate"),
			},
			"ionoscloud_target_group": {
				Tok: tfbridge.MakeDataSource(mainPkg, computeModule, "getTargetGroup"),
			},
			"ionoscloud_resource": {
				Tok: tfbridge.MakeDataSource(mainPkg, computeModule, "getResource"),
			},
			"ionoscloud_pg_cluster": {
				Tok:  tfbridge.MakeDataSource(mainPkg, dbaasModule, "getPSQLCluster"),
				Docs: &tfbridge.DocInfo{Source: "dbaas_pgsql_cluster.md"},
			},
			"ionoscloud_pg_user": {
				Tok:  tfbridge.MakeDataSource(mainPkg, dbaasModule, "getPSQLUser"),
				Docs: &tfbridge.DocInfo{Source: "dbaas_pgsql_user.md"},
			},
			"ionoscloud_pg_database": {
				Tok:  tfbridge.MakeDataSource(mainPkg, dbaasModule, "getPSQLDatabase"),
				Docs: &tfbridge.DocInfo{Source: "dbaas_pgsql_database.md"},
			},
			"ionoscloud_pg_databases": {
				Tok:  tfbridge.MakeDataSource(mainPkg, dbaasModule, "getPSQLDatabases"),
				Docs: &tfbridge.DocInfo{Source: "dbaas_pgsql_databases.md"},
			},
			"ionoscloud_pg_backups": {
				Tok:  tfbridge.MakeDataSource(mainPkg, dbaasModule, "getPSQLBackups"),
				Docs: &tfbridge.DocInfo{Source: "dbaas_pgsql_backups.md"},
			},
			"ionoscloud_pg_versions": {
				Tok:  tfbridge.MakeDataSource(mainPkg, dbaasModule, "getPSQLVersions"),
				Docs: &tfbridge.DocInfo{Source: "dbaas_pgsql_versions.md"},
			},
			"ionoscloud_mongo_cluster": {
				Tok:  tfbridge.MakeDataSource(mainPkg, dbaasModule, "getMongoCluster"),
				Docs: &tfbridge.DocInfo{Source: "dbaas_mongo_cluster.md"},
			},
			"ionoscloud_mongo_user": {
				Tok:  tfbridge.MakeDataSource(mainPkg, dbaasModule, "getMongoUser"),
				Docs: &tfbridge.DocInfo{Source: "dbaas_mongo_user.md"},
			},
			"ionoscloud_mongo_template": {
				Tok:  tfbridge.MakeDataSource(mainPkg, dbaasModule, "getMongoTemplate"),
				Docs: &tfbridge.DocInfo{Source: "dbaas_mongo_template.md"},
			},
			"ionoscloud_mariadb_cluster": {
				Tok:  tfbridge.MakeDataSource(mainPkg, dbaasModule, "getMariaDBCluster"),
				Docs: &tfbridge.DocInfo{Source: "dbaas_mariadb_cluster.md"},
			},
			"ionoscloud_mariadb_backups": {
				Tok:  tfbridge.MakeDataSource(mainPkg, dbaasModule, "getMariaDBBackups"),
				Docs: &tfbridge.DocInfo{Source: "dbaas_mariadb_backups.md"},
			},
			"ionoscloud_inmemorydb_replicaset": {
				Tok:  tfbridge.MakeDataSource(mainPkg, dbaasModule, "getInMemoryDBReplicaSet"),
				Docs: &tfbridge.DocInfo{Source: "dbaas_inmemorydb_replica_set.md"},
			},
			"ionoscloud_inmemorydb_snapshot": {
				Tok:  tfbridge.MakeDataSource(mainPkg, dbaasModule, "getInmemorydbSnapshot"),
				Docs: &tfbridge.DocInfo{Source: "dbaas_inmemorydb_snapshot.md"},
			},
			"ionoscloud_k8s_cluster": {
				Tok: tfbridge.MakeDataSource(mainPkg, k8sModule, "getCluster"),
			},
			"ionoscloud_k8s_clusters": {
				Tok:  tfbridge.MakeDataSource(mainPkg, k8sModule, "getClusters"),
				Docs: &tfbridge.DocInfo{Source: "k8s_clusters.md"},
			},
			"ionoscloud_k8s_node_pool": {
				Tok: tfbridge.MakeDataSource(mainPkg, k8sModule, "getNodePool"),
			},
			"ionoscloud_k8s_node_pool_nodes": {
				Tok:  tfbridge.MakeDataSource(mainPkg, k8sModule, "getNodePoolNodes"),
				Docs: &tfbridge.DocInfo{Source: "k8s_nodepool_nodes.md"},
			},
			"ionoscloud_auto_certificate": {
				Tok:  tfbridge.MakeDataSource(mainPkg, certModule, "getAutoCertificate"),
				Docs: &tfbridge.DocInfo{Source: "certificate_manager_auto_certificate.md"},
			},
			"ionoscloud_auto_certificate_provider": {
				Tok:  tfbridge.MakeDataSource(mainPkg, certModule, "getAutoCertificateProvider"),
				Docs: &tfbridge.DocInfo{Source: "certificate_manager_provider.md"},
			},
			"ionoscloud_certificate": {
				Tok:  tfbridge.MakeDataSource(mainPkg, certModule, "getCertificate"),
				Docs: &tfbridge.DocInfo{Source: "certificate_manager_certificate.md"},
			},
			"ionoscloud_dataplatform_cluster": {
				Tok: tfbridge.MakeDataSource(mainPkg, dsaasModule, "getCluster"),
			},
			"ionoscloud_dataplatform_node_pool": {
				Tok: tfbridge.MakeDataSource(mainPkg, dsaasModule, "getNodePool"),
			},
			"ionoscloud_dataplatform_node_pools": {
				Tok: tfbridge.MakeDataSource(mainPkg, dsaasModule, "getNodePools"),
			},
			"ionoscloud_dataplatform_versions": {
				Tok: tfbridge.MakeDataSource(mainPkg, dsaasModule, "getVersions"),
			},
			"ionoscloud_nfs_cluster": {
				Tok: tfbridge.MakeDataSource(mainPkg, nfsModule, "getCluster"),
			},
			"ionoscloud_nfs_share": {
				Tok: tfbridge.MakeDataSource(mainPkg, nfsModule, "getShare"),
			},
			"ionoscloud_vpn_ipsec_gateway": {
				Tok: tfbridge.MakeDataSource(mainPkg, vpnModule, "getIpsecGateway"),
			},
			"ionoscloud_vpn_ipsec_tunnel": {
				Tok: tfbridge.MakeDataSource(mainPkg, vpnModule, "getIpsecTunnel"),
			},
			"ionoscloud_vpn_wireguard_gateway": {
				Tok: tfbridge.MakeDataSource(mainPkg, vpnModule, "getWireguardGateway"),
			},
			"ionoscloud_vpn_wireguard_peer": {
				Tok: tfbridge.MakeDataSource(mainPkg, vpnModule, "getWireguardPeer"),
			},
			"ionoscloud_cdn_distribution": {
				Tok: tfbridge.MakeDataSource(mainPkg, cdnModule, "getDistribution"),
			},
			"ionoscloud_dns_zone": {
				Tok: tfbridge.MakeDataSource(mainPkg, dnsModule, "getZone"),
			},
			"ionoscloud_dns_record": {
				Tok: tfbridge.MakeDataSource(mainPkg, dnsModule, "getRecord"),
			},
			"ionoscloud_container_registry": {
				Tok: tfbridge.MakeDataSource(mainPkg, cregModule, "getRegistry"),
			},
			"ionoscloud_container_registry_token": {
				Tok: tfbridge.MakeDataSource(mainPkg, cregModule, "getRegistryToken"),
			},
			"ionoscloud_container_registry_locations": {
				Tok: tfbridge.MakeDataSource(mainPkg, cregModule, "getRegistryLocations"),
			},
			"ionoscloud_logging_pipeline": {
				Tok: tfbridge.MakeDataSource(mainPkg, loggingModule, "getPipeline"),
			},
			"ionoscloud_application_loadbalancer": {
				Tok: tfbridge.MakeDataSource(mainPkg, albModule, "getBalancer"),
			},
			"ionoscloud_application_loadbalancer_forwardingrule": {
				Tok: tfbridge.MakeDataSource(mainPkg, albModule, "getForwardingRule"),
			},
			"ionoscloud_networkloadbalancer": {
				Tok: tfbridge.MakeDataSource(mainPkg, nlbModule, "getBalancer"),
			},
			"ionoscloud_networkloadbalancer_forwardingrule": {
				Tok: tfbridge.MakeDataSource(mainPkg, nlbModule, "getForwardingRule"),
			},
			"ionoscloud_nsg": {
				Tok: tfbridge.MakeDataSource(mainPkg, nsgModule, "getNsg"),
			},
		},
		Resources: map[string]*tfbridge.ResourceInfo{
			"ionoscloud_datacenter": {
				Tok: tfbridge.MakeResource(mainPkg, computeModule, "Datacenter"),
			},
			"ionoscloud_server": {
				Tok: tfbridge.MakeResource(mainPkg, computeModule, "Server"),
			},
			"ionoscloud_vcpu_server": {
				Tok: tfbridge.MakeResource(mainPkg, computeModule, "VCPUServer"),
			},
			"ionoscloud_cube_server": {
				Tok: tfbridge.MakeResource(mainPkg, computeModule, "CubeServer"),
			},
			"ionoscloud_lan": {
				Tok: tfbridge.MakeResource(mainPkg, computeModule, "Lan"),
			},
			"ionoscloud_nic": {
				Tok: tfbridge.MakeResource(mainPkg, computeModule, "Nic"),
			},
			"ionoscloud_volume": {
				Tok: tfbridge.MakeResource(mainPkg, computeModule, "Volume"),
			},
			"ionoscloud_firewall": {
				Tok: tfbridge.MakeResource(mainPkg, computeModule, "Firewall"),
			},
			"ionoscloud_group": {
				Tok: tfbridge.MakeResource(mainPkg, computeModule, "Group"),
			},
			"ionoscloud_user": {
				Tok: tfbridge.MakeResource(mainPkg, computeModule, "User"),
			},
			"ionoscloud_ipblock": {
				Tok: tfbridge.MakeResource(mainPkg, computeModule, "IPBlock"),
			},
			"ionoscloud_share": {
				Tok: tfbridge.MakeResource(mainPkg, computeModule, "Share"),
			},
			"ionoscloud_ipfailover": {
				Tok: tfbridge.MakeResource(mainPkg, computeModule, "IPFailover"),
			},
			"ionoscloud_private_crossconnect": {
				Tok: tfbridge.MakeResource(mainPkg, computeModule, "Crossconnect"),
			},
			"ionoscloud_s3_key": {
				Tok: tfbridge.MakeResource(mainPkg, computeModule, "S3Key"),
			},
			"ionoscloud_backup_unit": {
				Tok: tfbridge.MakeResource(mainPkg, computeModule, "BackupUnit"),
			},
			"ionoscloud_snapshot": {
				Tok: tfbridge.MakeResource(mainPkg, computeModule, "Snapshot"),
			},
			"ionoscloud_server_boot_device_selection": {
				Tok: tfbridge.MakeResource(mainPkg, computeModule, "BootDeviceSelection"),
			},
			"ionoscloud_natgateway": {
				Tok: tfbridge.MakeResource(mainPkg, computeModule, "NatGateway"),
			},
			"ionoscloud_natgateway_rule": {
				Tok: tfbridge.MakeResource(mainPkg, computeModule, "NatGatewayRule"),
			},
			"ionoscloud_loadbalancer": {
				Tok: tfbridge.MakeResource(mainPkg, computeModule, "Balancer"),
			},
			"ionoscloud_target_group": {
				Tok: tfbridge.MakeResource(mainPkg, computeModule, "TargetGroup"),
			},
			"ionoscloud_pg_cluster": {
				Tok:  tfbridge.MakeResource(mainPkg, dbaasModule, "PSQLCluster"),
				Docs: &tfbridge.DocInfo{Source: "dbaas_pgsql_cluster.md"},
			},
			"ionoscloud_pg_user": {
				Tok:  tfbridge.MakeResource(mainPkg, dbaasModule, "PSQLUser"),
				Docs: &tfbridge.DocInfo{Source: "dbaas_pgsql_user.md"},
			},
			"ionoscloud_pg_database": {
				Tok:  tfbridge.MakeResource(mainPkg, dbaasModule, "PSQLDatabase"),
				Docs: &tfbridge.DocInfo{Source: "dbaas_pgsql_database.md"},
			},
			"ionoscloud_mongo_cluster": {
				Tok:  tfbridge.MakeResource(mainPkg, dbaasModule, "MongoCluster"),
				Docs: &tfbridge.DocInfo{Source: "dbaas_mongo_cluster.md"},
			},
			"ionoscloud_mongo_user": {
				Tok:  tfbridge.MakeResource(mainPkg, dbaasModule, "MongoUser"),
				Docs: &tfbridge.DocInfo{Source: "dbaas_mongo_user.md"},
			},
			"ionoscloud_mariadb_cluster": {
				Tok:  tfbridge.MakeResource(mainPkg, dbaasModule, "MariaDBCluster"),
				Docs: &tfbridge.DocInfo{Source: "dbaas_mariadb_cluster.md"},
			},
			"ionoscloud_inmemorydb_replicaset": {
				Tok:  tfbridge.MakeResource(mainPkg, dbaasModule, "InMemoryDBReplicaSet"),
				Docs: &tfbridge.DocInfo{Source: "dbaas_inmemorydb_replica_set.md"},
			},
			"ionoscloud_k8s_cluster": {
				Tok: tfbridge.MakeResource(mainPkg, k8sModule, "Cluster"),
			},
			"ionoscloud_k8s_node_pool": {
				Tok: tfbridge.MakeResource(mainPkg, k8sModule, "NodePool"),
			},
			"ionoscloud_auto_certificate": {
				Tok:  tfbridge.MakeResource(mainPkg, certModule, "AutoCertificate"),
				Docs: &tfbridge.DocInfo{Source: "certificate_manager_auto_certificate.md"},
			},
			"ionoscloud_auto_certificate_provider": {
				Tok:  tfbridge.MakeResource(mainPkg, certModule, "AutoCertificateProvider"),
				Docs: &tfbridge.DocInfo{Source: "certificate_manager_provider.md"},
			},
			"ionoscloud_certificate": {
				Tok:        tfbridge.MakeResource(mainPkg, certModule, "Certificate"),
				Docs:       &tfbridge.DocInfo{Source: "certificate_manager_certificate.md"},
				CSharpName: "IonosCertificate",
			},
			"ionoscloud_dataplatform_cluster": {
				Tok: tfbridge.MakeResource(mainPkg, dsaasModule, "Cluster"),
			},
			"ionoscloud_dataplatform_node_pool": {
				Tok: tfbridge.MakeResource(mainPkg, dsaasModule, "NodePool"),
			},
			"ionoscloud_nfs_cluster": {
				Tok: tfbridge.MakeResource(mainPkg, nfsModule, "Cluster"),
			},
			"ionoscloud_nfs_share": {
				Tok: tfbridge.MakeResource(mainPkg, nfsModule, "Share"),
			},
			"ionoscloud_vpn_ipsec_gateway": {
				Tok: tfbridge.MakeResource(mainPkg, vpnModule, "IpsecGateway"),
			},
			"ionoscloud_vpn_ipsec_tunnel": {
				Tok: tfbridge.MakeResource(mainPkg, vpnModule, "IpsecTunnel"),
			},
			"ionoscloud_vpn_wireguard_gateway": {
				Tok: tfbridge.MakeResource(mainPkg, vpnModule, "WireguardGateway"),
			},
			"ionoscloud_vpn_wireguard_peer": {
				Tok: tfbridge.MakeResource(mainPkg, vpnModule, "WireguardPeer"),
			},
			"ionoscloud_cdn_distribution": {
				Tok: tfbridge.MakeResource(mainPkg, cdnModule, "Distribution"),
			},
			"ionoscloud_dns_zone": {
				Tok: tfbridge.MakeResource(mainPkg, dnsModule, "Zone"),
			},
			"ionoscloud_dns_record": {
				Tok: tfbridge.MakeResource(mainPkg, dnsModule, "Record"),
			},
			"ionoscloud_container_registry": {
				Tok: tfbridge.MakeResource(mainPkg, cregModule, "Registry"),
			},
			"ionoscloud_container_registry_token": {
				Tok: tfbridge.MakeResource(mainPkg, cregModule, "RegistryToken"),
			},
			"ionoscloud_kafka_cluster": {
				Tok:  tfbridge.MakeResource(mainPkg, kafkaModule, "Cluster"),
				Docs: &tfbridge.DocInfo{Source: "kafka_cluster.md"},
			},
			"ionoscloud_kafka_cluster_topic": {
				Tok:  tfbridge.MakeResource(mainPkg, kafkaModule, "Topic"),
				Docs: &tfbridge.DocInfo{Source: "kafka_topic.md"},
			},
			"ionoscloud_apigateway": {
				Tok: tfbridge.MakeResource(mainPkg, apigModule, "Apigateway"),
			},
			"ionoscloud_apigateway_route": {
				Tok: tfbridge.MakeResource(mainPkg, apigModule, "Route"),
			},
			"ionoscloud_autoscaling_group": {
				Tok: tfbridge.MakeResource(mainPkg, autosclModule, "Group"),
			},
			"ionoscloud_logging_pipeline": {
				Tok: tfbridge.MakeResource(mainPkg, loggingModule, "Pipeline"),
			},
			"ionoscloud_application_loadbalancer": {
				Tok: tfbridge.MakeResource(mainPkg, albModule, "Balancer"),
			},
			"ionoscloud_application_loadbalancer_forwardingrule": {
				Tok: tfbridge.MakeResource(mainPkg, albModule, "ForwardingRule"),
			},
			"ionoscloud_networkloadbalancer": {
				Tok: tfbridge.MakeResource(mainPkg, nlbModule, "Balancer"),
			},
			"ionoscloud_networkloadbalancer_forwardingrule": {
				Tok: tfbridge.MakeResource(mainPkg, nlbModule, "ForwardingRule"),
			},
			"ionoscloud_nsg": {
				Tok: tfbridge.MakeResource(mainPkg, nsgModule, "Nsg"),
			},
			"ionoscloud_nsg_firewallrule": {
				Tok: tfbridge.MakeResource(mainPkg, nsgModule, "Firewall"),
			},
			"ionoscloud_datacenter_nsg_selection": {
				Tok: tfbridge.MakeResource(mainPkg, nsgModule, "DatacenterNsgSelection"),
			},
		},
	}

	// MustComputeTokens maps all resources and datasources from the upstream provider into Pulumi.
	//
	// tokens.SingleModule puts every upstream item into your provider's main module.
	//
	// You shouldn't need to override anything, but if you do, use the [tfbridge.ProviderInfo.Resources]
	// and [tfbridge.ProviderInfo.DataSources].
	prov.MustComputeTokens(tokens.SingleModule("ionoscloud_", mainMod,
		tokens.MakeStandard(mainPkg)))

	prov.MustApplyAutoAliases()
	prov.SetAutonaming(255, "-")

	return prov
}
