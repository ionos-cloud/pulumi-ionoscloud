// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

// Export members:
export { ApigatewayArgs, ApigatewayState } from "./apigateway";
export type Apigateway = import("./apigateway").Apigateway;
export const Apigateway: typeof import("./apigateway").Apigateway = null as any;
utilities.lazyLoad(exports, ["Apigateway"], () => require("./apigateway"));

export { ApigatewayRouteArgs, ApigatewayRouteState } from "./apigatewayRoute";
export type ApigatewayRoute = import("./apigatewayRoute").ApigatewayRoute;
export const ApigatewayRoute: typeof import("./apigatewayRoute").ApigatewayRoute = null as any;
utilities.lazyLoad(exports, ["ApigatewayRoute"], () => require("./apigatewayRoute"));

export { AutoscalingGroupArgs, AutoscalingGroupState } from "./autoscalingGroup";
export type AutoscalingGroup = import("./autoscalingGroup").AutoscalingGroup;
export const AutoscalingGroup: typeof import("./autoscalingGroup").AutoscalingGroup = null as any;
utilities.lazyLoad(exports, ["AutoscalingGroup"], () => require("./autoscalingGroup"));

export { GetApigatewayArgs, GetApigatewayResult, GetApigatewayOutputArgs } from "./getApigateway";
export const getApigateway: typeof import("./getApigateway").getApigateway = null as any;
export const getApigatewayOutput: typeof import("./getApigateway").getApigatewayOutput = null as any;
utilities.lazyLoad(exports, ["getApigateway","getApigatewayOutput"], () => require("./getApigateway"));

export { GetApigatewayRouteArgs, GetApigatewayRouteResult, GetApigatewayRouteOutputArgs } from "./getApigatewayRoute";
export const getApigatewayRoute: typeof import("./getApigatewayRoute").getApigatewayRoute = null as any;
export const getApigatewayRouteOutput: typeof import("./getApigatewayRoute").getApigatewayRouteOutput = null as any;
utilities.lazyLoad(exports, ["getApigatewayRoute","getApigatewayRouteOutput"], () => require("./getApigatewayRoute"));

export { GetApplicationLoadbalancerArgs, GetApplicationLoadbalancerResult, GetApplicationLoadbalancerOutputArgs } from "./getApplicationLoadbalancer";
export const getApplicationLoadbalancer: typeof import("./getApplicationLoadbalancer").getApplicationLoadbalancer = null as any;
export const getApplicationLoadbalancerOutput: typeof import("./getApplicationLoadbalancer").getApplicationLoadbalancerOutput = null as any;
utilities.lazyLoad(exports, ["getApplicationLoadbalancer","getApplicationLoadbalancerOutput"], () => require("./getApplicationLoadbalancer"));

export { GetApplicationLoadbalancerForwardingruleArgs, GetApplicationLoadbalancerForwardingruleResult, GetApplicationLoadbalancerForwardingruleOutputArgs } from "./getApplicationLoadbalancerForwardingrule";
export const getApplicationLoadbalancerForwardingrule: typeof import("./getApplicationLoadbalancerForwardingrule").getApplicationLoadbalancerForwardingrule = null as any;
export const getApplicationLoadbalancerForwardingruleOutput: typeof import("./getApplicationLoadbalancerForwardingrule").getApplicationLoadbalancerForwardingruleOutput = null as any;
utilities.lazyLoad(exports, ["getApplicationLoadbalancerForwardingrule","getApplicationLoadbalancerForwardingruleOutput"], () => require("./getApplicationLoadbalancerForwardingrule"));

export { GetAutoCertificateArgs, GetAutoCertificateResult, GetAutoCertificateOutputArgs } from "./getAutoCertificate";
export const getAutoCertificate: typeof import("./getAutoCertificate").getAutoCertificate = null as any;
export const getAutoCertificateOutput: typeof import("./getAutoCertificate").getAutoCertificateOutput = null as any;
utilities.lazyLoad(exports, ["getAutoCertificate","getAutoCertificateOutput"], () => require("./getAutoCertificate"));

export { GetAutoCertificateProviderArgs, GetAutoCertificateProviderResult, GetAutoCertificateProviderOutputArgs } from "./getAutoCertificateProvider";
export const getAutoCertificateProvider: typeof import("./getAutoCertificateProvider").getAutoCertificateProvider = null as any;
export const getAutoCertificateProviderOutput: typeof import("./getAutoCertificateProvider").getAutoCertificateProviderOutput = null as any;
utilities.lazyLoad(exports, ["getAutoCertificateProvider","getAutoCertificateProviderOutput"], () => require("./getAutoCertificateProvider"));

export { GetAutoscalingGroupArgs, GetAutoscalingGroupResult, GetAutoscalingGroupOutputArgs } from "./getAutoscalingGroup";
export const getAutoscalingGroup: typeof import("./getAutoscalingGroup").getAutoscalingGroup = null as any;
export const getAutoscalingGroupOutput: typeof import("./getAutoscalingGroup").getAutoscalingGroupOutput = null as any;
utilities.lazyLoad(exports, ["getAutoscalingGroup","getAutoscalingGroupOutput"], () => require("./getAutoscalingGroup"));

export { GetAutoscalingGroupServersArgs, GetAutoscalingGroupServersResult, GetAutoscalingGroupServersOutputArgs } from "./getAutoscalingGroupServers";
export const getAutoscalingGroupServers: typeof import("./getAutoscalingGroupServers").getAutoscalingGroupServers = null as any;
export const getAutoscalingGroupServersOutput: typeof import("./getAutoscalingGroupServers").getAutoscalingGroupServersOutput = null as any;
utilities.lazyLoad(exports, ["getAutoscalingGroupServers","getAutoscalingGroupServersOutput"], () => require("./getAutoscalingGroupServers"));

export { GetBackupUnitArgs, GetBackupUnitResult, GetBackupUnitOutputArgs } from "./getBackupUnit";
export const getBackupUnit: typeof import("./getBackupUnit").getBackupUnit = null as any;
export const getBackupUnitOutput: typeof import("./getBackupUnit").getBackupUnitOutput = null as any;
utilities.lazyLoad(exports, ["getBackupUnit","getBackupUnitOutput"], () => require("./getBackupUnit"));

export { GetCdnDistributionArgs, GetCdnDistributionResult, GetCdnDistributionOutputArgs } from "./getCdnDistribution";
export const getCdnDistribution: typeof import("./getCdnDistribution").getCdnDistribution = null as any;
export const getCdnDistributionOutput: typeof import("./getCdnDistribution").getCdnDistributionOutput = null as any;
utilities.lazyLoad(exports, ["getCdnDistribution","getCdnDistributionOutput"], () => require("./getCdnDistribution"));

export { GetCertificateArgs, GetCertificateResult, GetCertificateOutputArgs } from "./getCertificate";
export const getCertificate: typeof import("./getCertificate").getCertificate = null as any;
export const getCertificateOutput: typeof import("./getCertificate").getCertificateOutput = null as any;
utilities.lazyLoad(exports, ["getCertificate","getCertificateOutput"], () => require("./getCertificate"));

export { GetContainerRegistryArgs, GetContainerRegistryResult, GetContainerRegistryOutputArgs } from "./getContainerRegistry";
export const getContainerRegistry: typeof import("./getContainerRegistry").getContainerRegistry = null as any;
export const getContainerRegistryOutput: typeof import("./getContainerRegistry").getContainerRegistryOutput = null as any;
utilities.lazyLoad(exports, ["getContainerRegistry","getContainerRegistryOutput"], () => require("./getContainerRegistry"));

export { GetContainerRegistryLocationsResult } from "./getContainerRegistryLocations";
export const getContainerRegistryLocations: typeof import("./getContainerRegistryLocations").getContainerRegistryLocations = null as any;
export const getContainerRegistryLocationsOutput: typeof import("./getContainerRegistryLocations").getContainerRegistryLocationsOutput = null as any;
utilities.lazyLoad(exports, ["getContainerRegistryLocations","getContainerRegistryLocationsOutput"], () => require("./getContainerRegistryLocations"));

export { GetContainerRegistryTokenArgs, GetContainerRegistryTokenResult, GetContainerRegistryTokenOutputArgs } from "./getContainerRegistryToken";
export const getContainerRegistryToken: typeof import("./getContainerRegistryToken").getContainerRegistryToken = null as any;
export const getContainerRegistryTokenOutput: typeof import("./getContainerRegistryToken").getContainerRegistryTokenOutput = null as any;
utilities.lazyLoad(exports, ["getContainerRegistryToken","getContainerRegistryTokenOutput"], () => require("./getContainerRegistryToken"));

export { GetCubeServerArgs, GetCubeServerResult, GetCubeServerOutputArgs } from "./getCubeServer";
export const getCubeServer: typeof import("./getCubeServer").getCubeServer = null as any;
export const getCubeServerOutput: typeof import("./getCubeServer").getCubeServerOutput = null as any;
utilities.lazyLoad(exports, ["getCubeServer","getCubeServerOutput"], () => require("./getCubeServer"));

export { GetDatacenterArgs, GetDatacenterResult, GetDatacenterOutputArgs } from "./getDatacenter";
export const getDatacenter: typeof import("./getDatacenter").getDatacenter = null as any;
export const getDatacenterOutput: typeof import("./getDatacenter").getDatacenterOutput = null as any;
utilities.lazyLoad(exports, ["getDatacenter","getDatacenterOutput"], () => require("./getDatacenter"));

export { GetDataplatformClusterArgs, GetDataplatformClusterResult, GetDataplatformClusterOutputArgs } from "./getDataplatformCluster";
export const getDataplatformCluster: typeof import("./getDataplatformCluster").getDataplatformCluster = null as any;
export const getDataplatformClusterOutput: typeof import("./getDataplatformCluster").getDataplatformClusterOutput = null as any;
utilities.lazyLoad(exports, ["getDataplatformCluster","getDataplatformClusterOutput"], () => require("./getDataplatformCluster"));

export { GetDataplatformNodePoolArgs, GetDataplatformNodePoolResult, GetDataplatformNodePoolOutputArgs } from "./getDataplatformNodePool";
export const getDataplatformNodePool: typeof import("./getDataplatformNodePool").getDataplatformNodePool = null as any;
export const getDataplatformNodePoolOutput: typeof import("./getDataplatformNodePool").getDataplatformNodePoolOutput = null as any;
utilities.lazyLoad(exports, ["getDataplatformNodePool","getDataplatformNodePoolOutput"], () => require("./getDataplatformNodePool"));

export { GetDataplatformNodePoolsArgs, GetDataplatformNodePoolsResult, GetDataplatformNodePoolsOutputArgs } from "./getDataplatformNodePools";
export const getDataplatformNodePools: typeof import("./getDataplatformNodePools").getDataplatformNodePools = null as any;
export const getDataplatformNodePoolsOutput: typeof import("./getDataplatformNodePools").getDataplatformNodePoolsOutput = null as any;
utilities.lazyLoad(exports, ["getDataplatformNodePools","getDataplatformNodePoolsOutput"], () => require("./getDataplatformNodePools"));

export { GetDataplatformVersionsResult } from "./getDataplatformVersions";
export const getDataplatformVersions: typeof import("./getDataplatformVersions").getDataplatformVersions = null as any;
export const getDataplatformVersionsOutput: typeof import("./getDataplatformVersions").getDataplatformVersionsOutput = null as any;
utilities.lazyLoad(exports, ["getDataplatformVersions","getDataplatformVersionsOutput"], () => require("./getDataplatformVersions"));

export { GetDnsRecordArgs, GetDnsRecordResult, GetDnsRecordOutputArgs } from "./getDnsRecord";
export const getDnsRecord: typeof import("./getDnsRecord").getDnsRecord = null as any;
export const getDnsRecordOutput: typeof import("./getDnsRecord").getDnsRecordOutput = null as any;
utilities.lazyLoad(exports, ["getDnsRecord","getDnsRecordOutput"], () => require("./getDnsRecord"));

export { GetDnsZoneArgs, GetDnsZoneResult, GetDnsZoneOutputArgs } from "./getDnsZone";
export const getDnsZone: typeof import("./getDnsZone").getDnsZone = null as any;
export const getDnsZoneOutput: typeof import("./getDnsZone").getDnsZoneOutput = null as any;
utilities.lazyLoad(exports, ["getDnsZone","getDnsZoneOutput"], () => require("./getDnsZone"));

export { GetFirewallArgs, GetFirewallResult, GetFirewallOutputArgs } from "./getFirewall";
export const getFirewall: typeof import("./getFirewall").getFirewall = null as any;
export const getFirewallOutput: typeof import("./getFirewall").getFirewallOutput = null as any;
utilities.lazyLoad(exports, ["getFirewall","getFirewallOutput"], () => require("./getFirewall"));

export { GetGroupArgs, GetGroupResult, GetGroupOutputArgs } from "./getGroup";
export const getGroup: typeof import("./getGroup").getGroup = null as any;
export const getGroupOutput: typeof import("./getGroup").getGroupOutput = null as any;
utilities.lazyLoad(exports, ["getGroup","getGroupOutput"], () => require("./getGroup"));

export { GetImageArgs, GetImageResult, GetImageOutputArgs } from "./getImage";
export const getImage: typeof import("./getImage").getImage = null as any;
export const getImageOutput: typeof import("./getImage").getImageOutput = null as any;
utilities.lazyLoad(exports, ["getImage","getImageOutput"], () => require("./getImage"));

export { GetInmemorydbReplicasetArgs, GetInmemorydbReplicasetResult, GetInmemorydbReplicasetOutputArgs } from "./getInmemorydbReplicaset";
export const getInmemorydbReplicaset: typeof import("./getInmemorydbReplicaset").getInmemorydbReplicaset = null as any;
export const getInmemorydbReplicasetOutput: typeof import("./getInmemorydbReplicaset").getInmemorydbReplicasetOutput = null as any;
utilities.lazyLoad(exports, ["getInmemorydbReplicaset","getInmemorydbReplicasetOutput"], () => require("./getInmemorydbReplicaset"));

export { GetInmemorydbSnapshotArgs, GetInmemorydbSnapshotResult, GetInmemorydbSnapshotOutputArgs } from "./getInmemorydbSnapshot";
export const getInmemorydbSnapshot: typeof import("./getInmemorydbSnapshot").getInmemorydbSnapshot = null as any;
export const getInmemorydbSnapshotOutput: typeof import("./getInmemorydbSnapshot").getInmemorydbSnapshotOutput = null as any;
utilities.lazyLoad(exports, ["getInmemorydbSnapshot","getInmemorydbSnapshotOutput"], () => require("./getInmemorydbSnapshot"));

export { GetIpblockArgs, GetIpblockResult, GetIpblockOutputArgs } from "./getIpblock";
export const getIpblock: typeof import("./getIpblock").getIpblock = null as any;
export const getIpblockOutput: typeof import("./getIpblock").getIpblockOutput = null as any;
utilities.lazyLoad(exports, ["getIpblock","getIpblockOutput"], () => require("./getIpblock"));

export { GetIpfailoverArgs, GetIpfailoverResult, GetIpfailoverOutputArgs } from "./getIpfailover";
export const getIpfailover: typeof import("./getIpfailover").getIpfailover = null as any;
export const getIpfailoverOutput: typeof import("./getIpfailover").getIpfailoverOutput = null as any;
utilities.lazyLoad(exports, ["getIpfailover","getIpfailoverOutput"], () => require("./getIpfailover"));

export { GetK8sClusterArgs, GetK8sClusterResult, GetK8sClusterOutputArgs } from "./getK8sCluster";
export const getK8sCluster: typeof import("./getK8sCluster").getK8sCluster = null as any;
export const getK8sClusterOutput: typeof import("./getK8sCluster").getK8sClusterOutput = null as any;
utilities.lazyLoad(exports, ["getK8sCluster","getK8sClusterOutput"], () => require("./getK8sCluster"));

export { GetK8sClustersArgs, GetK8sClustersResult, GetK8sClustersOutputArgs } from "./getK8sClusters";
export const getK8sClusters: typeof import("./getK8sClusters").getK8sClusters = null as any;
export const getK8sClustersOutput: typeof import("./getK8sClusters").getK8sClustersOutput = null as any;
utilities.lazyLoad(exports, ["getK8sClusters","getK8sClustersOutput"], () => require("./getK8sClusters"));

export { GetK8sNodePoolArgs, GetK8sNodePoolResult, GetK8sNodePoolOutputArgs } from "./getK8sNodePool";
export const getK8sNodePool: typeof import("./getK8sNodePool").getK8sNodePool = null as any;
export const getK8sNodePoolOutput: typeof import("./getK8sNodePool").getK8sNodePoolOutput = null as any;
utilities.lazyLoad(exports, ["getK8sNodePool","getK8sNodePoolOutput"], () => require("./getK8sNodePool"));

export { GetK8sNodePoolNodesArgs, GetK8sNodePoolNodesResult, GetK8sNodePoolNodesOutputArgs } from "./getK8sNodePoolNodes";
export const getK8sNodePoolNodes: typeof import("./getK8sNodePoolNodes").getK8sNodePoolNodes = null as any;
export const getK8sNodePoolNodesOutput: typeof import("./getK8sNodePoolNodes").getK8sNodePoolNodesOutput = null as any;
utilities.lazyLoad(exports, ["getK8sNodePoolNodes","getK8sNodePoolNodesOutput"], () => require("./getK8sNodePoolNodes"));

export { GetKafkaClusterArgs, GetKafkaClusterResult, GetKafkaClusterOutputArgs } from "./getKafkaCluster";
export const getKafkaCluster: typeof import("./getKafkaCluster").getKafkaCluster = null as any;
export const getKafkaClusterOutput: typeof import("./getKafkaCluster").getKafkaClusterOutput = null as any;
utilities.lazyLoad(exports, ["getKafkaCluster","getKafkaClusterOutput"], () => require("./getKafkaCluster"));

export { GetKafkaClusterTopicArgs, GetKafkaClusterTopicResult, GetKafkaClusterTopicOutputArgs } from "./getKafkaClusterTopic";
export const getKafkaClusterTopic: typeof import("./getKafkaClusterTopic").getKafkaClusterTopic = null as any;
export const getKafkaClusterTopicOutput: typeof import("./getKafkaClusterTopic").getKafkaClusterTopicOutput = null as any;
utilities.lazyLoad(exports, ["getKafkaClusterTopic","getKafkaClusterTopicOutput"], () => require("./getKafkaClusterTopic"));

export { GetLanArgs, GetLanResult, GetLanOutputArgs } from "./getLan";
export const getLan: typeof import("./getLan").getLan = null as any;
export const getLanOutput: typeof import("./getLan").getLanOutput = null as any;
utilities.lazyLoad(exports, ["getLan","getLanOutput"], () => require("./getLan"));

export { GetLocationArgs, GetLocationResult, GetLocationOutputArgs } from "./getLocation";
export const getLocation: typeof import("./getLocation").getLocation = null as any;
export const getLocationOutput: typeof import("./getLocation").getLocationOutput = null as any;
utilities.lazyLoad(exports, ["getLocation","getLocationOutput"], () => require("./getLocation"));

export { GetLoggingPipelineArgs, GetLoggingPipelineResult, GetLoggingPipelineOutputArgs } from "./getLoggingPipeline";
export const getLoggingPipeline: typeof import("./getLoggingPipeline").getLoggingPipeline = null as any;
export const getLoggingPipelineOutput: typeof import("./getLoggingPipeline").getLoggingPipelineOutput = null as any;
utilities.lazyLoad(exports, ["getLoggingPipeline","getLoggingPipelineOutput"], () => require("./getLoggingPipeline"));

export { GetMariadbBackupsArgs, GetMariadbBackupsResult, GetMariadbBackupsOutputArgs } from "./getMariadbBackups";
export const getMariadbBackups: typeof import("./getMariadbBackups").getMariadbBackups = null as any;
export const getMariadbBackupsOutput: typeof import("./getMariadbBackups").getMariadbBackupsOutput = null as any;
utilities.lazyLoad(exports, ["getMariadbBackups","getMariadbBackupsOutput"], () => require("./getMariadbBackups"));

export { GetMariadbClusterArgs, GetMariadbClusterResult, GetMariadbClusterOutputArgs } from "./getMariadbCluster";
export const getMariadbCluster: typeof import("./getMariadbCluster").getMariadbCluster = null as any;
export const getMariadbClusterOutput: typeof import("./getMariadbCluster").getMariadbClusterOutput = null as any;
utilities.lazyLoad(exports, ["getMariadbCluster","getMariadbClusterOutput"], () => require("./getMariadbCluster"));

export { GetMongoClusterArgs, GetMongoClusterResult, GetMongoClusterOutputArgs } from "./getMongoCluster";
export const getMongoCluster: typeof import("./getMongoCluster").getMongoCluster = null as any;
export const getMongoClusterOutput: typeof import("./getMongoCluster").getMongoClusterOutput = null as any;
utilities.lazyLoad(exports, ["getMongoCluster","getMongoClusterOutput"], () => require("./getMongoCluster"));

export { GetMongoTemplateArgs, GetMongoTemplateResult, GetMongoTemplateOutputArgs } from "./getMongoTemplate";
export const getMongoTemplate: typeof import("./getMongoTemplate").getMongoTemplate = null as any;
export const getMongoTemplateOutput: typeof import("./getMongoTemplate").getMongoTemplateOutput = null as any;
utilities.lazyLoad(exports, ["getMongoTemplate","getMongoTemplateOutput"], () => require("./getMongoTemplate"));

export { GetMongoUserArgs, GetMongoUserResult, GetMongoUserOutputArgs } from "./getMongoUser";
export const getMongoUser: typeof import("./getMongoUser").getMongoUser = null as any;
export const getMongoUserOutput: typeof import("./getMongoUser").getMongoUserOutput = null as any;
utilities.lazyLoad(exports, ["getMongoUser","getMongoUserOutput"], () => require("./getMongoUser"));

export { GetNatgatewayArgs, GetNatgatewayResult, GetNatgatewayOutputArgs } from "./getNatgateway";
export const getNatgateway: typeof import("./getNatgateway").getNatgateway = null as any;
export const getNatgatewayOutput: typeof import("./getNatgateway").getNatgatewayOutput = null as any;
utilities.lazyLoad(exports, ["getNatgateway","getNatgatewayOutput"], () => require("./getNatgateway"));

export { GetNatgatewayRuleArgs, GetNatgatewayRuleResult, GetNatgatewayRuleOutputArgs } from "./getNatgatewayRule";
export const getNatgatewayRule: typeof import("./getNatgatewayRule").getNatgatewayRule = null as any;
export const getNatgatewayRuleOutput: typeof import("./getNatgatewayRule").getNatgatewayRuleOutput = null as any;
utilities.lazyLoad(exports, ["getNatgatewayRule","getNatgatewayRuleOutput"], () => require("./getNatgatewayRule"));

export { GetNetworkloadbalancerArgs, GetNetworkloadbalancerResult, GetNetworkloadbalancerOutputArgs } from "./getNetworkloadbalancer";
export const getNetworkloadbalancer: typeof import("./getNetworkloadbalancer").getNetworkloadbalancer = null as any;
export const getNetworkloadbalancerOutput: typeof import("./getNetworkloadbalancer").getNetworkloadbalancerOutput = null as any;
utilities.lazyLoad(exports, ["getNetworkloadbalancer","getNetworkloadbalancerOutput"], () => require("./getNetworkloadbalancer"));

export { GetNetworkloadbalancerForwardingruleArgs, GetNetworkloadbalancerForwardingruleResult, GetNetworkloadbalancerForwardingruleOutputArgs } from "./getNetworkloadbalancerForwardingrule";
export const getNetworkloadbalancerForwardingrule: typeof import("./getNetworkloadbalancerForwardingrule").getNetworkloadbalancerForwardingrule = null as any;
export const getNetworkloadbalancerForwardingruleOutput: typeof import("./getNetworkloadbalancerForwardingrule").getNetworkloadbalancerForwardingruleOutput = null as any;
utilities.lazyLoad(exports, ["getNetworkloadbalancerForwardingrule","getNetworkloadbalancerForwardingruleOutput"], () => require("./getNetworkloadbalancerForwardingrule"));

export { GetNfsClusterArgs, GetNfsClusterResult, GetNfsClusterOutputArgs } from "./getNfsCluster";
export const getNfsCluster: typeof import("./getNfsCluster").getNfsCluster = null as any;
export const getNfsClusterOutput: typeof import("./getNfsCluster").getNfsClusterOutput = null as any;
utilities.lazyLoad(exports, ["getNfsCluster","getNfsClusterOutput"], () => require("./getNfsCluster"));

export { GetNfsShareArgs, GetNfsShareResult, GetNfsShareOutputArgs } from "./getNfsShare";
export const getNfsShare: typeof import("./getNfsShare").getNfsShare = null as any;
export const getNfsShareOutput: typeof import("./getNfsShare").getNfsShareOutput = null as any;
utilities.lazyLoad(exports, ["getNfsShare","getNfsShareOutput"], () => require("./getNfsShare"));

export { GetNicArgs, GetNicResult, GetNicOutputArgs } from "./getNic";
export const getNic: typeof import("./getNic").getNic = null as any;
export const getNicOutput: typeof import("./getNic").getNicOutput = null as any;
utilities.lazyLoad(exports, ["getNic","getNicOutput"], () => require("./getNic"));

export { GetPgBackupsArgs, GetPgBackupsResult, GetPgBackupsOutputArgs } from "./getPgBackups";
export const getPgBackups: typeof import("./getPgBackups").getPgBackups = null as any;
export const getPgBackupsOutput: typeof import("./getPgBackups").getPgBackupsOutput = null as any;
utilities.lazyLoad(exports, ["getPgBackups","getPgBackupsOutput"], () => require("./getPgBackups"));

export { GetPgClusterArgs, GetPgClusterResult, GetPgClusterOutputArgs } from "./getPgCluster";
export const getPgCluster: typeof import("./getPgCluster").getPgCluster = null as any;
export const getPgClusterOutput: typeof import("./getPgCluster").getPgClusterOutput = null as any;
utilities.lazyLoad(exports, ["getPgCluster","getPgClusterOutput"], () => require("./getPgCluster"));

export { GetPgDatabaseArgs, GetPgDatabaseResult, GetPgDatabaseOutputArgs } from "./getPgDatabase";
export const getPgDatabase: typeof import("./getPgDatabase").getPgDatabase = null as any;
export const getPgDatabaseOutput: typeof import("./getPgDatabase").getPgDatabaseOutput = null as any;
utilities.lazyLoad(exports, ["getPgDatabase","getPgDatabaseOutput"], () => require("./getPgDatabase"));

export { GetPgDatabasesArgs, GetPgDatabasesResult, GetPgDatabasesOutputArgs } from "./getPgDatabases";
export const getPgDatabases: typeof import("./getPgDatabases").getPgDatabases = null as any;
export const getPgDatabasesOutput: typeof import("./getPgDatabases").getPgDatabasesOutput = null as any;
utilities.lazyLoad(exports, ["getPgDatabases","getPgDatabasesOutput"], () => require("./getPgDatabases"));

export { GetPgUserArgs, GetPgUserResult, GetPgUserOutputArgs } from "./getPgUser";
export const getPgUser: typeof import("./getPgUser").getPgUser = null as any;
export const getPgUserOutput: typeof import("./getPgUser").getPgUserOutput = null as any;
utilities.lazyLoad(exports, ["getPgUser","getPgUserOutput"], () => require("./getPgUser"));

export { GetPgVersionsArgs, GetPgVersionsResult, GetPgVersionsOutputArgs } from "./getPgVersions";
export const getPgVersions: typeof import("./getPgVersions").getPgVersions = null as any;
export const getPgVersionsOutput: typeof import("./getPgVersions").getPgVersionsOutput = null as any;
utilities.lazyLoad(exports, ["getPgVersions","getPgVersionsOutput"], () => require("./getPgVersions"));

export { GetPrivateCrossconnectArgs, GetPrivateCrossconnectResult, GetPrivateCrossconnectOutputArgs } from "./getPrivateCrossconnect";
export const getPrivateCrossconnect: typeof import("./getPrivateCrossconnect").getPrivateCrossconnect = null as any;
export const getPrivateCrossconnectOutput: typeof import("./getPrivateCrossconnect").getPrivateCrossconnectOutput = null as any;
utilities.lazyLoad(exports, ["getPrivateCrossconnect","getPrivateCrossconnectOutput"], () => require("./getPrivateCrossconnect"));

export { GetResourceArgs, GetResourceResult, GetResourceOutputArgs } from "./getResource";
export const getResource: typeof import("./getResource").getResource = null as any;
export const getResourceOutput: typeof import("./getResource").getResourceOutput = null as any;
utilities.lazyLoad(exports, ["getResource","getResourceOutput"], () => require("./getResource"));

export { GetS3KeyArgs, GetS3KeyResult, GetS3KeyOutputArgs } from "./getS3Key";
export const getS3Key: typeof import("./getS3Key").getS3Key = null as any;
export const getS3KeyOutput: typeof import("./getS3Key").getS3KeyOutput = null as any;
utilities.lazyLoad(exports, ["getS3Key","getS3KeyOutput"], () => require("./getS3Key"));

export { GetServerArgs, GetServerResult, GetServerOutputArgs } from "./getServer";
export const getServer: typeof import("./getServer").getServer = null as any;
export const getServerOutput: typeof import("./getServer").getServerOutput = null as any;
utilities.lazyLoad(exports, ["getServer","getServerOutput"], () => require("./getServer"));

export { GetServersArgs, GetServersResult, GetServersOutputArgs } from "./getServers";
export const getServers: typeof import("./getServers").getServers = null as any;
export const getServersOutput: typeof import("./getServers").getServersOutput = null as any;
utilities.lazyLoad(exports, ["getServers","getServersOutput"], () => require("./getServers"));

export { GetShareArgs, GetShareResult, GetShareOutputArgs } from "./getShare";
export const getShare: typeof import("./getShare").getShare = null as any;
export const getShareOutput: typeof import("./getShare").getShareOutput = null as any;
utilities.lazyLoad(exports, ["getShare","getShareOutput"], () => require("./getShare"));

export { GetSnapshotArgs, GetSnapshotResult, GetSnapshotOutputArgs } from "./getSnapshot";
export const getSnapshot: typeof import("./getSnapshot").getSnapshot = null as any;
export const getSnapshotOutput: typeof import("./getSnapshot").getSnapshotOutput = null as any;
utilities.lazyLoad(exports, ["getSnapshot","getSnapshotOutput"], () => require("./getSnapshot"));

export { GetTargetGroupArgs, GetTargetGroupResult, GetTargetGroupOutputArgs } from "./getTargetGroup";
export const getTargetGroup: typeof import("./getTargetGroup").getTargetGroup = null as any;
export const getTargetGroupOutput: typeof import("./getTargetGroup").getTargetGroupOutput = null as any;
utilities.lazyLoad(exports, ["getTargetGroup","getTargetGroupOutput"], () => require("./getTargetGroup"));

export { GetTemplateArgs, GetTemplateResult, GetTemplateOutputArgs } from "./getTemplate";
export const getTemplate: typeof import("./getTemplate").getTemplate = null as any;
export const getTemplateOutput: typeof import("./getTemplate").getTemplateOutput = null as any;
utilities.lazyLoad(exports, ["getTemplate","getTemplateOutput"], () => require("./getTemplate"));

export { GetUserArgs, GetUserResult, GetUserOutputArgs } from "./getUser";
export const getUser: typeof import("./getUser").getUser = null as any;
export const getUserOutput: typeof import("./getUser").getUserOutput = null as any;
utilities.lazyLoad(exports, ["getUser","getUserOutput"], () => require("./getUser"));

export { GetVcpuServerArgs, GetVcpuServerResult, GetVcpuServerOutputArgs } from "./getVcpuServer";
export const getVcpuServer: typeof import("./getVcpuServer").getVcpuServer = null as any;
export const getVcpuServerOutput: typeof import("./getVcpuServer").getVcpuServerOutput = null as any;
utilities.lazyLoad(exports, ["getVcpuServer","getVcpuServerOutput"], () => require("./getVcpuServer"));

export { GetVolumeArgs, GetVolumeResult, GetVolumeOutputArgs } from "./getVolume";
export const getVolume: typeof import("./getVolume").getVolume = null as any;
export const getVolumeOutput: typeof import("./getVolume").getVolumeOutput = null as any;
utilities.lazyLoad(exports, ["getVolume","getVolumeOutput"], () => require("./getVolume"));

export { GetVpnIpsecGatewayArgs, GetVpnIpsecGatewayResult, GetVpnIpsecGatewayOutputArgs } from "./getVpnIpsecGateway";
export const getVpnIpsecGateway: typeof import("./getVpnIpsecGateway").getVpnIpsecGateway = null as any;
export const getVpnIpsecGatewayOutput: typeof import("./getVpnIpsecGateway").getVpnIpsecGatewayOutput = null as any;
utilities.lazyLoad(exports, ["getVpnIpsecGateway","getVpnIpsecGatewayOutput"], () => require("./getVpnIpsecGateway"));

export { GetVpnIpsecTunnelArgs, GetVpnIpsecTunnelResult, GetVpnIpsecTunnelOutputArgs } from "./getVpnIpsecTunnel";
export const getVpnIpsecTunnel: typeof import("./getVpnIpsecTunnel").getVpnIpsecTunnel = null as any;
export const getVpnIpsecTunnelOutput: typeof import("./getVpnIpsecTunnel").getVpnIpsecTunnelOutput = null as any;
utilities.lazyLoad(exports, ["getVpnIpsecTunnel","getVpnIpsecTunnelOutput"], () => require("./getVpnIpsecTunnel"));

export { GetVpnWireguardGatewayArgs, GetVpnWireguardGatewayResult, GetVpnWireguardGatewayOutputArgs } from "./getVpnWireguardGateway";
export const getVpnWireguardGateway: typeof import("./getVpnWireguardGateway").getVpnWireguardGateway = null as any;
export const getVpnWireguardGatewayOutput: typeof import("./getVpnWireguardGateway").getVpnWireguardGatewayOutput = null as any;
utilities.lazyLoad(exports, ["getVpnWireguardGateway","getVpnWireguardGatewayOutput"], () => require("./getVpnWireguardGateway"));

export { GetVpnWireguardPeerArgs, GetVpnWireguardPeerResult, GetVpnWireguardPeerOutputArgs } from "./getVpnWireguardPeer";
export const getVpnWireguardPeer: typeof import("./getVpnWireguardPeer").getVpnWireguardPeer = null as any;
export const getVpnWireguardPeerOutput: typeof import("./getVpnWireguardPeer").getVpnWireguardPeerOutput = null as any;
utilities.lazyLoad(exports, ["getVpnWireguardPeer","getVpnWireguardPeerOutput"], () => require("./getVpnWireguardPeer"));

export { KafkaClusterArgs, KafkaClusterState } from "./kafkaCluster";
export type KafkaCluster = import("./kafkaCluster").KafkaCluster;
export const KafkaCluster: typeof import("./kafkaCluster").KafkaCluster = null as any;
utilities.lazyLoad(exports, ["KafkaCluster"], () => require("./kafkaCluster"));

export { KafkaClusterTopicArgs, KafkaClusterTopicState } from "./kafkaClusterTopic";
export type KafkaClusterTopic = import("./kafkaClusterTopic").KafkaClusterTopic;
export const KafkaClusterTopic: typeof import("./kafkaClusterTopic").KafkaClusterTopic = null as any;
utilities.lazyLoad(exports, ["KafkaClusterTopic"], () => require("./kafkaClusterTopic"));

export { LoadbalancerArgs, LoadbalancerState } from "./loadbalancer";
export type Loadbalancer = import("./loadbalancer").Loadbalancer;
export const Loadbalancer: typeof import("./loadbalancer").Loadbalancer = null as any;
utilities.lazyLoad(exports, ["Loadbalancer"], () => require("./loadbalancer"));

export { ProviderArgs } from "./provider";
export type Provider = import("./provider").Provider;
export const Provider: typeof import("./provider").Provider = null as any;
utilities.lazyLoad(exports, ["Provider"], () => require("./provider"));

export { TargetGroupArgs, TargetGroupState } from "./targetGroup";
export type TargetGroup = import("./targetGroup").TargetGroup;
export const TargetGroup: typeof import("./targetGroup").TargetGroup = null as any;
utilities.lazyLoad(exports, ["TargetGroup"], () => require("./targetGroup"));


// Export sub-modules:
import * as alb from "./alb";
import * as cdn from "./cdn";
import * as cert from "./cert";
import * as compute from "./compute";
import * as config from "./config";
import * as creg from "./creg";
import * as dbaas from "./dbaas";
import * as dns from "./dns";
import * as dsaas from "./dsaas";
import * as k8s from "./k8s";
import * as logging from "./logging";
import * as nfs from "./nfs";
import * as nlb from "./nlb";
import * as types from "./types";
import * as vpn from "./vpn";

export {
    alb,
    cdn,
    cert,
    compute,
    config,
    creg,
    dbaas,
    dns,
    dsaas,
    k8s,
    logging,
    nfs,
    nlb,
    types,
    vpn,
};

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "ionoscloud:index/apigateway:Apigateway":
                return new Apigateway(name, <any>undefined, { urn })
            case "ionoscloud:index/apigatewayRoute:ApigatewayRoute":
                return new ApigatewayRoute(name, <any>undefined, { urn })
            case "ionoscloud:index/autoscalingGroup:AutoscalingGroup":
                return new AutoscalingGroup(name, <any>undefined, { urn })
            case "ionoscloud:index/kafkaCluster:KafkaCluster":
                return new KafkaCluster(name, <any>undefined, { urn })
            case "ionoscloud:index/kafkaClusterTopic:KafkaClusterTopic":
                return new KafkaClusterTopic(name, <any>undefined, { urn })
            case "ionoscloud:index/loadbalancer:Loadbalancer":
                return new Loadbalancer(name, <any>undefined, { urn })
            case "ionoscloud:index/targetGroup:TargetGroup":
                return new TargetGroup(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("ionoscloud", "index/apigateway", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "index/apigatewayRoute", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "index/autoscalingGroup", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "index/kafkaCluster", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "index/kafkaClusterTopic", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "index/loadbalancer", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "index/targetGroup", _module)
pulumi.runtime.registerResourcePackage("ionoscloud", {
    version: utilities.getVersion(),
    constructProvider: (name: string, type: string, urn: string): pulumi.ProviderResource => {
        if (type !== "pulumi:providers:ionoscloud") {
            throw new Error(`unknown provider type ${type}`);
        }
        return new Provider(name, <any>undefined, { urn });
    },
});
