// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export { BackupUnitArgs, BackupUnitState } from "./backupUnit";
export type BackupUnit = import("./backupUnit").BackupUnit;
export const BackupUnit: typeof import("./backupUnit").BackupUnit = null as any;
utilities.lazyLoad(exports, ["BackupUnit"], () => require("./backupUnit"));

export { BalancerArgs, BalancerState } from "./balancer";
export type Balancer = import("./balancer").Balancer;
export const Balancer: typeof import("./balancer").Balancer = null as any;
utilities.lazyLoad(exports, ["Balancer"], () => require("./balancer"));

export { BootDeviceSelectionArgs, BootDeviceSelectionState } from "./bootDeviceSelection";
export type BootDeviceSelection = import("./bootDeviceSelection").BootDeviceSelection;
export const BootDeviceSelection: typeof import("./bootDeviceSelection").BootDeviceSelection = null as any;
utilities.lazyLoad(exports, ["BootDeviceSelection"], () => require("./bootDeviceSelection"));

export { CrossconnectArgs, CrossconnectState } from "./crossconnect";
export type Crossconnect = import("./crossconnect").Crossconnect;
export const Crossconnect: typeof import("./crossconnect").Crossconnect = null as any;
utilities.lazyLoad(exports, ["Crossconnect"], () => require("./crossconnect"));

export { CubeServerArgs, CubeServerState } from "./cubeServer";
export type CubeServer = import("./cubeServer").CubeServer;
export const CubeServer: typeof import("./cubeServer").CubeServer = null as any;
utilities.lazyLoad(exports, ["CubeServer"], () => require("./cubeServer"));

export { DatacenterArgs, DatacenterState } from "./datacenter";
export type Datacenter = import("./datacenter").Datacenter;
export const Datacenter: typeof import("./datacenter").Datacenter = null as any;
utilities.lazyLoad(exports, ["Datacenter"], () => require("./datacenter"));

export { FirewallArgs, FirewallState } from "./firewall";
export type Firewall = import("./firewall").Firewall;
export const Firewall: typeof import("./firewall").Firewall = null as any;
utilities.lazyLoad(exports, ["Firewall"], () => require("./firewall"));

export { GetBackupUnitArgs, GetBackupUnitResult, GetBackupUnitOutputArgs } from "./getBackupUnit";
export const getBackupUnit: typeof import("./getBackupUnit").getBackupUnit = null as any;
export const getBackupUnitOutput: typeof import("./getBackupUnit").getBackupUnitOutput = null as any;
utilities.lazyLoad(exports, ["getBackupUnit","getBackupUnitOutput"], () => require("./getBackupUnit"));

export { GetCrossconnectArgs, GetCrossconnectResult, GetCrossconnectOutputArgs } from "./getCrossconnect";
export const getCrossconnect: typeof import("./getCrossconnect").getCrossconnect = null as any;
export const getCrossconnectOutput: typeof import("./getCrossconnect").getCrossconnectOutput = null as any;
utilities.lazyLoad(exports, ["getCrossconnect","getCrossconnectOutput"], () => require("./getCrossconnect"));

export { GetCubeServerArgs, GetCubeServerResult, GetCubeServerOutputArgs } from "./getCubeServer";
export const getCubeServer: typeof import("./getCubeServer").getCubeServer = null as any;
export const getCubeServerOutput: typeof import("./getCubeServer").getCubeServerOutput = null as any;
utilities.lazyLoad(exports, ["getCubeServer","getCubeServerOutput"], () => require("./getCubeServer"));

export { GetDatacenterArgs, GetDatacenterResult, GetDatacenterOutputArgs } from "./getDatacenter";
export const getDatacenter: typeof import("./getDatacenter").getDatacenter = null as any;
export const getDatacenterOutput: typeof import("./getDatacenter").getDatacenterOutput = null as any;
utilities.lazyLoad(exports, ["getDatacenter","getDatacenterOutput"], () => require("./getDatacenter"));

export { GetFirewallArgs, GetFirewallResult, GetFirewallOutputArgs } from "./getFirewall";
export const getFirewall: typeof import("./getFirewall").getFirewall = null as any;
export const getFirewallOutput: typeof import("./getFirewall").getFirewallOutput = null as any;
utilities.lazyLoad(exports, ["getFirewall","getFirewallOutput"], () => require("./getFirewall"));

export { GetGroupArgs, GetGroupResult, GetGroupOutputArgs } from "./getGroup";
export const getGroup: typeof import("./getGroup").getGroup = null as any;
export const getGroupOutput: typeof import("./getGroup").getGroupOutput = null as any;
utilities.lazyLoad(exports, ["getGroup","getGroupOutput"], () => require("./getGroup"));

export { GetIPBlockArgs, GetIPBlockResult, GetIPBlockOutputArgs } from "./getIPBlock";
export const getIPBlock: typeof import("./getIPBlock").getIPBlock = null as any;
export const getIPBlockOutput: typeof import("./getIPBlock").getIPBlockOutput = null as any;
utilities.lazyLoad(exports, ["getIPBlock","getIPBlockOutput"], () => require("./getIPBlock"));

export { GetIPFailoverArgs, GetIPFailoverResult, GetIPFailoverOutputArgs } from "./getIPFailover";
export const getIPFailover: typeof import("./getIPFailover").getIPFailover = null as any;
export const getIPFailoverOutput: typeof import("./getIPFailover").getIPFailoverOutput = null as any;
utilities.lazyLoad(exports, ["getIPFailover","getIPFailoverOutput"], () => require("./getIPFailover"));

export { GetImageArgs, GetImageResult, GetImageOutputArgs } from "./getImage";
export const getImage: typeof import("./getImage").getImage = null as any;
export const getImageOutput: typeof import("./getImage").getImageOutput = null as any;
utilities.lazyLoad(exports, ["getImage","getImageOutput"], () => require("./getImage"));

export { GetLanArgs, GetLanResult, GetLanOutputArgs } from "./getLan";
export const getLan: typeof import("./getLan").getLan = null as any;
export const getLanOutput: typeof import("./getLan").getLanOutput = null as any;
utilities.lazyLoad(exports, ["getLan","getLanOutput"], () => require("./getLan"));

export { GetLocationArgs, GetLocationResult, GetLocationOutputArgs } from "./getLocation";
export const getLocation: typeof import("./getLocation").getLocation = null as any;
export const getLocationOutput: typeof import("./getLocation").getLocationOutput = null as any;
utilities.lazyLoad(exports, ["getLocation","getLocationOutput"], () => require("./getLocation"));

export { GetNatGatewayArgs, GetNatGatewayResult, GetNatGatewayOutputArgs } from "./getNatGateway";
export const getNatGateway: typeof import("./getNatGateway").getNatGateway = null as any;
export const getNatGatewayOutput: typeof import("./getNatGateway").getNatGatewayOutput = null as any;
utilities.lazyLoad(exports, ["getNatGateway","getNatGatewayOutput"], () => require("./getNatGateway"));

export { GetNatGatewayRuleArgs, GetNatGatewayRuleResult, GetNatGatewayRuleOutputArgs } from "./getNatGatewayRule";
export const getNatGatewayRule: typeof import("./getNatGatewayRule").getNatGatewayRule = null as any;
export const getNatGatewayRuleOutput: typeof import("./getNatGatewayRule").getNatGatewayRuleOutput = null as any;
utilities.lazyLoad(exports, ["getNatGatewayRule","getNatGatewayRuleOutput"], () => require("./getNatGatewayRule"));

export { GetNicArgs, GetNicResult, GetNicOutputArgs } from "./getNic";
export const getNic: typeof import("./getNic").getNic = null as any;
export const getNicOutput: typeof import("./getNic").getNicOutput = null as any;
utilities.lazyLoad(exports, ["getNic","getNicOutput"], () => require("./getNic"));

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

export { GetVCPUServerArgs, GetVCPUServerResult, GetVCPUServerOutputArgs } from "./getVCPUServer";
export const getVCPUServer: typeof import("./getVCPUServer").getVCPUServer = null as any;
export const getVCPUServerOutput: typeof import("./getVCPUServer").getVCPUServerOutput = null as any;
utilities.lazyLoad(exports, ["getVCPUServer","getVCPUServerOutput"], () => require("./getVCPUServer"));

export { GetVolumeArgs, GetVolumeResult, GetVolumeOutputArgs } from "./getVolume";
export const getVolume: typeof import("./getVolume").getVolume = null as any;
export const getVolumeOutput: typeof import("./getVolume").getVolumeOutput = null as any;
utilities.lazyLoad(exports, ["getVolume","getVolumeOutput"], () => require("./getVolume"));

export { GroupArgs, GroupState } from "./group";
export type Group = import("./group").Group;
export const Group: typeof import("./group").Group = null as any;
utilities.lazyLoad(exports, ["Group"], () => require("./group"));

export { IPBlockArgs, IPBlockState } from "./ipblock";
export type IPBlock = import("./ipblock").IPBlock;
export const IPBlock: typeof import("./ipblock").IPBlock = null as any;
utilities.lazyLoad(exports, ["IPBlock"], () => require("./ipblock"));

export { IPFailoverArgs, IPFailoverState } from "./ipfailover";
export type IPFailover = import("./ipfailover").IPFailover;
export const IPFailover: typeof import("./ipfailover").IPFailover = null as any;
utilities.lazyLoad(exports, ["IPFailover"], () => require("./ipfailover"));

export { LanArgs, LanState } from "./lan";
export type Lan = import("./lan").Lan;
export const Lan: typeof import("./lan").Lan = null as any;
utilities.lazyLoad(exports, ["Lan"], () => require("./lan"));

export { NatGatewayArgs, NatGatewayState } from "./natGateway";
export type NatGateway = import("./natGateway").NatGateway;
export const NatGateway: typeof import("./natGateway").NatGateway = null as any;
utilities.lazyLoad(exports, ["NatGateway"], () => require("./natGateway"));

export { NatGatewayRuleArgs, NatGatewayRuleState } from "./natGatewayRule";
export type NatGatewayRule = import("./natGatewayRule").NatGatewayRule;
export const NatGatewayRule: typeof import("./natGatewayRule").NatGatewayRule = null as any;
utilities.lazyLoad(exports, ["NatGatewayRule"], () => require("./natGatewayRule"));

export { NicArgs, NicState } from "./nic";
export type Nic = import("./nic").Nic;
export const Nic: typeof import("./nic").Nic = null as any;
utilities.lazyLoad(exports, ["Nic"], () => require("./nic"));

export { S3KeyArgs, S3KeyState } from "./s3key";
export type S3Key = import("./s3key").S3Key;
export const S3Key: typeof import("./s3key").S3Key = null as any;
utilities.lazyLoad(exports, ["S3Key"], () => require("./s3key"));

export { ServerArgs, ServerState } from "./server";
export type Server = import("./server").Server;
export const Server: typeof import("./server").Server = null as any;
utilities.lazyLoad(exports, ["Server"], () => require("./server"));

export { ShareArgs, ShareState } from "./share";
export type Share = import("./share").Share;
export const Share: typeof import("./share").Share = null as any;
utilities.lazyLoad(exports, ["Share"], () => require("./share"));

export { SnapshotArgs, SnapshotState } from "./snapshot";
export type Snapshot = import("./snapshot").Snapshot;
export const Snapshot: typeof import("./snapshot").Snapshot = null as any;
utilities.lazyLoad(exports, ["Snapshot"], () => require("./snapshot"));

export { TargetGroupArgs, TargetGroupState } from "./targetGroup";
export type TargetGroup = import("./targetGroup").TargetGroup;
export const TargetGroup: typeof import("./targetGroup").TargetGroup = null as any;
utilities.lazyLoad(exports, ["TargetGroup"], () => require("./targetGroup"));

export { UserArgs, UserState } from "./user";
export type User = import("./user").User;
export const User: typeof import("./user").User = null as any;
utilities.lazyLoad(exports, ["User"], () => require("./user"));

export { VCPUServerArgs, VCPUServerState } from "./vcpuserver";
export type VCPUServer = import("./vcpuserver").VCPUServer;
export const VCPUServer: typeof import("./vcpuserver").VCPUServer = null as any;
utilities.lazyLoad(exports, ["VCPUServer"], () => require("./vcpuserver"));

export { VolumeArgs, VolumeState } from "./volume";
export type Volume = import("./volume").Volume;
export const Volume: typeof import("./volume").Volume = null as any;
utilities.lazyLoad(exports, ["Volume"], () => require("./volume"));


const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "ionoscloud:compute/backupUnit:BackupUnit":
                return new BackupUnit(name, <any>undefined, { urn })
            case "ionoscloud:compute/balancer:Balancer":
                return new Balancer(name, <any>undefined, { urn })
            case "ionoscloud:compute/bootDeviceSelection:BootDeviceSelection":
                return new BootDeviceSelection(name, <any>undefined, { urn })
            case "ionoscloud:compute/crossconnect:Crossconnect":
                return new Crossconnect(name, <any>undefined, { urn })
            case "ionoscloud:compute/cubeServer:CubeServer":
                return new CubeServer(name, <any>undefined, { urn })
            case "ionoscloud:compute/datacenter:Datacenter":
                return new Datacenter(name, <any>undefined, { urn })
            case "ionoscloud:compute/firewall:Firewall":
                return new Firewall(name, <any>undefined, { urn })
            case "ionoscloud:compute/group:Group":
                return new Group(name, <any>undefined, { urn })
            case "ionoscloud:compute/iPBlock:IPBlock":
                return new IPBlock(name, <any>undefined, { urn })
            case "ionoscloud:compute/iPFailover:IPFailover":
                return new IPFailover(name, <any>undefined, { urn })
            case "ionoscloud:compute/lan:Lan":
                return new Lan(name, <any>undefined, { urn })
            case "ionoscloud:compute/natGateway:NatGateway":
                return new NatGateway(name, <any>undefined, { urn })
            case "ionoscloud:compute/natGatewayRule:NatGatewayRule":
                return new NatGatewayRule(name, <any>undefined, { urn })
            case "ionoscloud:compute/nic:Nic":
                return new Nic(name, <any>undefined, { urn })
            case "ionoscloud:compute/s3Key:S3Key":
                return new S3Key(name, <any>undefined, { urn })
            case "ionoscloud:compute/server:Server":
                return new Server(name, <any>undefined, { urn })
            case "ionoscloud:compute/share:Share":
                return new Share(name, <any>undefined, { urn })
            case "ionoscloud:compute/snapshot:Snapshot":
                return new Snapshot(name, <any>undefined, { urn })
            case "ionoscloud:compute/targetGroup:TargetGroup":
                return new TargetGroup(name, <any>undefined, { urn })
            case "ionoscloud:compute/user:User":
                return new User(name, <any>undefined, { urn })
            case "ionoscloud:compute/vCPUServer:VCPUServer":
                return new VCPUServer(name, <any>undefined, { urn })
            case "ionoscloud:compute/volume:Volume":
                return new Volume(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("ionoscloud", "compute/backupUnit", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "compute/balancer", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "compute/bootDeviceSelection", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "compute/crossconnect", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "compute/cubeServer", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "compute/datacenter", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "compute/firewall", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "compute/group", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "compute/iPBlock", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "compute/iPFailover", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "compute/lan", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "compute/natGateway", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "compute/natGatewayRule", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "compute/nic", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "compute/s3Key", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "compute/server", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "compute/share", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "compute/snapshot", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "compute/targetGroup", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "compute/user", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "compute/vCPUServer", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "compute/volume", _module)
