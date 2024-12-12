// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export { BackupUnitArgs, BackupUnitState } from "./backupUnit";
export type BackupUnit = import("./backupUnit").BackupUnit;
export const BackupUnit: typeof import("./backupUnit").BackupUnit = null as any;
utilities.lazyLoad(exports, ["BackupUnit"], () => require("./backupUnit"));

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
pulumi.runtime.registerResourceModule("ionoscloud", "compute/crossconnect", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "compute/cubeServer", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "compute/datacenter", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "compute/firewall", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "compute/group", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "compute/iPBlock", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "compute/iPFailover", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "compute/lan", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "compute/nic", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "compute/s3Key", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "compute/server", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "compute/share", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "compute/snapshot", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "compute/user", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "compute/vCPUServer", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "compute/volume", _module)
