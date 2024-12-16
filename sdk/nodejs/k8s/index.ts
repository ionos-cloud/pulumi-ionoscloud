// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export { ClusterArgs, ClusterState } from "./cluster";
export type Cluster = import("./cluster").Cluster;
export const Cluster: typeof import("./cluster").Cluster = null as any;
utilities.lazyLoad(exports, ["Cluster"], () => require("./cluster"));

export { GetClusterArgs, GetClusterResult, GetClusterOutputArgs } from "./getCluster";
export const getCluster: typeof import("./getCluster").getCluster = null as any;
export const getClusterOutput: typeof import("./getCluster").getClusterOutput = null as any;
utilities.lazyLoad(exports, ["getCluster","getClusterOutput"], () => require("./getCluster"));

export { GetNodePoolArgs, GetNodePoolResult, GetNodePoolOutputArgs } from "./getNodePool";
export const getNodePool: typeof import("./getNodePool").getNodePool = null as any;
export const getNodePoolOutput: typeof import("./getNodePool").getNodePoolOutput = null as any;
utilities.lazyLoad(exports, ["getNodePool","getNodePoolOutput"], () => require("./getNodePool"));

export { NodePoolArgs, NodePoolState } from "./nodePool";
export type NodePool = import("./nodePool").NodePool;
export const NodePool: typeof import("./nodePool").NodePool = null as any;
utilities.lazyLoad(exports, ["NodePool"], () => require("./nodePool"));


const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "ionoscloud:k8s/cluster:Cluster":
                return new Cluster(name, <any>undefined, { urn })
            case "ionoscloud:k8s/nodePool:NodePool":
                return new NodePool(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("ionoscloud", "k8s/cluster", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "k8s/nodePool", _module)
