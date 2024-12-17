// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Manages an Autoscaling Group on IonosCloud.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 * import * as random from "@pulumi/random";
 *
 * const datacenterExample = new ionoscloud.compute.Datacenter("datacenterExample", {location: "de/fra"});
 * const lanExample1 = new ionoscloud.compute.Lan("lanExample1", {
 *     datacenterId: datacenterExample.id,
 *     "public": false,
 * });
 * const lanExample2 = new ionoscloud.compute.Lan("lanExample2", {
 *     datacenterId: datacenterExample.id,
 *     "public": false,
 * });
 * const autoscalingTargetGroup = new ionoscloud.compute.TargetGroup("autoscalingTargetGroup", {
 *     algorithm: "ROUND_ROBIN",
 *     protocol: "HTTP",
 * });
 * const serverImagePassword = new random.RandomPassword("serverImagePassword", {
 *     length: 16,
 *     special: false,
 * });
 * const autoscalingGroupExample = new ionoscloud.autoscaling.Group("autoscalingGroupExample", {
 *     datacenterId: datacenterExample.id,
 *     maxReplicaCount: 2,
 *     minReplicaCount: 1,
 *     policy: {
 *         metric: "INSTANCE_CPU_UTILIZATION_AVERAGE",
 *         range: "PT24H",
 *         scaleInAction: {
 *             amount: 1,
 *             amountType: "ABSOLUTE",
 *             terminationPolicyType: "OLDEST_SERVER_FIRST",
 *             cooldownPeriod: "PT5M",
 *             deleteVolumes: true,
 *         },
 *         scaleInThreshold: 33,
 *         scaleOutAction: {
 *             amount: 1,
 *             amountType: "ABSOLUTE",
 *             cooldownPeriod: "PT5M",
 *         },
 *         scaleOutThreshold: 77,
 *         unit: "PER_HOUR",
 *     },
 *     replicaConfiguration: {
 *         availabilityZone: "AUTO",
 *         cores: 2,
 *         cpuFamily: "INTEL_SKYLAKE",
 *         ram: 2048,
 *         nics: [
 *             {
 *                 lan: lanExample1.id,
 *                 name: "nic_example_1",
 *                 dhcp: true,
 *             },
 *             {
 *                 lan: lanExample2.id,
 *                 name: "nic_example_2",
 *                 dhcp: true,
 *                 firewallActive: true,
 *                 firewallType: "INGRESS",
 *                 firewallRules: [{
 *                     name: "rule_1",
 *                     protocol: "TCP",
 *                     portRangeStart: 1,
 *                     portRangeEnd: 1000,
 *                     type: "INGRESS",
 *                 }],
 *                 flowLogs: [{
 *                     name: "flow_log_1",
 *                     bucket: "test-de-bucket",
 *                     action: "ALL",
 *                     direction: "BIDIRECTIONAL",
 *                 }],
 *                 targetGroup: {
 *                     targetGroupId: autoscalingTargetGroup.id,
 *                     port: 80,
 *                     weight: 50,
 *                 },
 *             },
 *         ],
 *         volumes: [{
 *             imageAlias: "ubuntu:latest",
 *             name: "volume_example",
 *             size: 10,
 *             type: "HDD",
 *             userData: "ZWNobyAiSGVsbG8sIFdvcmxkIgo=",
 *             imagePassword: serverImagePassword.result,
 *             bootOrder: "AUTO",
 *         }],
 *     },
 * });
 * ```
 */
export class Group extends pulumi.CustomResource {
    /**
     * Get an existing Group resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GroupState, opts?: pulumi.CustomResourceOptions): Group {
        return new Group(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ionoscloud:autoscaling/group:Group';

    /**
     * Returns true if the given object is an instance of Group.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Group {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Group.__pulumiType;
    }

    /**
     * [string] Unique identifier for the resource
     */
    public readonly datacenterId!: pulumi.Output<string>;
    /**
     * Location of the data center.
     */
    public /*out*/ readonly location!: pulumi.Output<string>;
    /**
     * [int] The maximum value for the number of replicas on a VM Auto Scaling Group. Must be >= 0 and <= 200. Will be enforced for both automatic and manual changes.
     */
    public readonly maxReplicaCount!: pulumi.Output<number>;
    /**
     * [int] The minimum value for the number of replicas on a VM Auto Scaling Group. Must be >= 0 and <= 200. Will be enforced for both automatic and manual changes.
     */
    public readonly minReplicaCount!: pulumi.Output<number>;
    /**
     * [string] User-defined name for the Autoscaling Group.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * [List] Specifies the behavior of this Autoscaling Group. A policy consists of Triggers and Actions, whereby an Action is some kind of automated behavior, and a Trigger is defined by the circumstances under which the Action is triggered. Currently, two separate Actions, namely Scaling In and Out are supported, triggered through Thresholds defined on a given Metric.
     */
    public readonly policy!: pulumi.Output<outputs.autoscaling.GroupPolicy>;
    /**
     * [List]
     */
    public readonly replicaConfiguration!: pulumi.Output<outputs.autoscaling.GroupReplicaConfiguration>;

    /**
     * Create a Group resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: GroupArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: GroupArgs | GroupState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as GroupState | undefined;
            resourceInputs["datacenterId"] = state ? state.datacenterId : undefined;
            resourceInputs["location"] = state ? state.location : undefined;
            resourceInputs["maxReplicaCount"] = state ? state.maxReplicaCount : undefined;
            resourceInputs["minReplicaCount"] = state ? state.minReplicaCount : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["policy"] = state ? state.policy : undefined;
            resourceInputs["replicaConfiguration"] = state ? state.replicaConfiguration : undefined;
        } else {
            const args = argsOrState as GroupArgs | undefined;
            if ((!args || args.datacenterId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'datacenterId'");
            }
            if ((!args || args.maxReplicaCount === undefined) && !opts.urn) {
                throw new Error("Missing required property 'maxReplicaCount'");
            }
            if ((!args || args.minReplicaCount === undefined) && !opts.urn) {
                throw new Error("Missing required property 'minReplicaCount'");
            }
            if ((!args || args.policy === undefined) && !opts.urn) {
                throw new Error("Missing required property 'policy'");
            }
            if ((!args || args.replicaConfiguration === undefined) && !opts.urn) {
                throw new Error("Missing required property 'replicaConfiguration'");
            }
            resourceInputs["datacenterId"] = args ? args.datacenterId : undefined;
            resourceInputs["maxReplicaCount"] = args ? args.maxReplicaCount : undefined;
            resourceInputs["minReplicaCount"] = args ? args.minReplicaCount : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["policy"] = args ? args.policy : undefined;
            resourceInputs["replicaConfiguration"] = args ? args.replicaConfiguration : undefined;
            resourceInputs["location"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Group.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Group resources.
 */
export interface GroupState {
    /**
     * [string] Unique identifier for the resource
     */
    datacenterId?: pulumi.Input<string>;
    /**
     * Location of the data center.
     */
    location?: pulumi.Input<string>;
    /**
     * [int] The maximum value for the number of replicas on a VM Auto Scaling Group. Must be >= 0 and <= 200. Will be enforced for both automatic and manual changes.
     */
    maxReplicaCount?: pulumi.Input<number>;
    /**
     * [int] The minimum value for the number of replicas on a VM Auto Scaling Group. Must be >= 0 and <= 200. Will be enforced for both automatic and manual changes.
     */
    minReplicaCount?: pulumi.Input<number>;
    /**
     * [string] User-defined name for the Autoscaling Group.
     */
    name?: pulumi.Input<string>;
    /**
     * [List] Specifies the behavior of this Autoscaling Group. A policy consists of Triggers and Actions, whereby an Action is some kind of automated behavior, and a Trigger is defined by the circumstances under which the Action is triggered. Currently, two separate Actions, namely Scaling In and Out are supported, triggered through Thresholds defined on a given Metric.
     */
    policy?: pulumi.Input<inputs.autoscaling.GroupPolicy>;
    /**
     * [List]
     */
    replicaConfiguration?: pulumi.Input<inputs.autoscaling.GroupReplicaConfiguration>;
}

/**
 * The set of arguments for constructing a Group resource.
 */
export interface GroupArgs {
    /**
     * [string] Unique identifier for the resource
     */
    datacenterId: pulumi.Input<string>;
    /**
     * [int] The maximum value for the number of replicas on a VM Auto Scaling Group. Must be >= 0 and <= 200. Will be enforced for both automatic and manual changes.
     */
    maxReplicaCount: pulumi.Input<number>;
    /**
     * [int] The minimum value for the number of replicas on a VM Auto Scaling Group. Must be >= 0 and <= 200. Will be enforced for both automatic and manual changes.
     */
    minReplicaCount: pulumi.Input<number>;
    /**
     * [string] User-defined name for the Autoscaling Group.
     */
    name?: pulumi.Input<string>;
    /**
     * [List] Specifies the behavior of this Autoscaling Group. A policy consists of Triggers and Actions, whereby an Action is some kind of automated behavior, and a Trigger is defined by the circumstances under which the Action is triggered. Currently, two separate Actions, namely Scaling In and Out are supported, triggered through Thresholds defined on a given Metric.
     */
    policy: pulumi.Input<inputs.autoscaling.GroupPolicy>;
    /**
     * [List]
     */
    replicaConfiguration: pulumi.Input<inputs.autoscaling.GroupReplicaConfiguration>;
}
