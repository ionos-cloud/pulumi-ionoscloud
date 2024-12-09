// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud
{
    /// <summary>
    /// Manages an Autoscaling Group on IonosCloud.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Ionoscloud = Pulumi.Ionoscloud;
    /// using Random = Pulumi.Random;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var datacenterExample = new Ionoscloud.Compute.Datacenter("datacenterExample", new()
    ///     {
    ///         Location = "de/fra",
    ///     });
    /// 
    ///     var lanExample1 = new Ionoscloud.Compute.Lan("lanExample1", new()
    ///     {
    ///         DatacenterId = datacenterExample.Id,
    ///         Public = false,
    ///     });
    /// 
    ///     var lanExample2 = new Ionoscloud.Compute.Lan("lanExample2", new()
    ///     {
    ///         DatacenterId = datacenterExample.Id,
    ///         Public = false,
    ///     });
    /// 
    ///     var autoscalingTargetGroup = new Ionoscloud.TargetGroup("autoscalingTargetGroup", new()
    ///     {
    ///         Algorithm = "ROUND_ROBIN",
    ///         Protocol = "HTTP",
    ///     });
    /// 
    ///     var serverImagePassword = new Random.RandomPassword("serverImagePassword", new()
    ///     {
    ///         Length = 16,
    ///         Special = false,
    ///     });
    /// 
    ///     var autoscalingGroupExample = new Ionoscloud.AutoscalingGroup("autoscalingGroupExample", new()
    ///     {
    ///         DatacenterId = datacenterExample.Id,
    ///         MaxReplicaCount = 2,
    ///         MinReplicaCount = 1,
    ///         Policy = new Ionoscloud.Inputs.AutoscalingGroupPolicyArgs
    ///         {
    ///             Metric = "INSTANCE_CPU_UTILIZATION_AVERAGE",
    ///             Range = "PT24H",
    ///             ScaleInAction = new Ionoscloud.Inputs.AutoscalingGroupPolicyScaleInActionArgs
    ///             {
    ///                 Amount = 1,
    ///                 AmountType = "ABSOLUTE",
    ///                 TerminationPolicyType = "OLDEST_SERVER_FIRST",
    ///                 CooldownPeriod = "PT5M",
    ///                 DeleteVolumes = true,
    ///             },
    ///             ScaleInThreshold = 33,
    ///             ScaleOutAction = new Ionoscloud.Inputs.AutoscalingGroupPolicyScaleOutActionArgs
    ///             {
    ///                 Amount = 1,
    ///                 AmountType = "ABSOLUTE",
    ///                 CooldownPeriod = "PT5M",
    ///             },
    ///             ScaleOutThreshold = 77,
    ///             Unit = "PER_HOUR",
    ///         },
    ///         ReplicaConfiguration = new Ionoscloud.Inputs.AutoscalingGroupReplicaConfigurationArgs
    ///         {
    ///             AvailabilityZone = "AUTO",
    ///             Cores = 2,
    ///             CpuFamily = "INTEL_SKYLAKE",
    ///             Ram = 2048,
    ///             Nics = new[]
    ///             {
    ///                 new Ionoscloud.Inputs.AutoscalingGroupReplicaConfigurationNicArgs
    ///                 {
    ///                     Lan = lanExample1.Id,
    ///                     Name = "nic_example_1",
    ///                     Dhcp = true,
    ///                 },
    ///                 new Ionoscloud.Inputs.AutoscalingGroupReplicaConfigurationNicArgs
    ///                 {
    ///                     Lan = lanExample2.Id,
    ///                     Name = "nic_example_2",
    ///                     Dhcp = true,
    ///                     FirewallActive = true,
    ///                     FirewallType = "INGRESS",
    ///                     FirewallRules = new[]
    ///                     {
    ///                         new Ionoscloud.Inputs.AutoscalingGroupReplicaConfigurationNicFirewallRuleArgs
    ///                         {
    ///                             Name = "rule_1",
    ///                             Protocol = "TCP",
    ///                             PortRangeStart = 1,
    ///                             PortRangeEnd = 1000,
    ///                             Type = "INGRESS",
    ///                         },
    ///                     },
    ///                     FlowLogs = new[]
    ///                     {
    ///                         new Ionoscloud.Inputs.AutoscalingGroupReplicaConfigurationNicFlowLogArgs
    ///                         {
    ///                             Name = "flow_log_1",
    ///                             Bucket = "test-de-bucket",
    ///                             Action = "ALL",
    ///                             Direction = "BIDIRECTIONAL",
    ///                         },
    ///                     },
    ///                     TargetGroup = new Ionoscloud.Inputs.AutoscalingGroupReplicaConfigurationNicTargetGroupArgs
    ///                     {
    ///                         TargetGroupId = autoscalingTargetGroup.Id,
    ///                         Port = 80,
    ///                         Weight = 50,
    ///                     },
    ///                 },
    ///             },
    ///             Volumes = new[]
    ///             {
    ///                 new Ionoscloud.Inputs.AutoscalingGroupReplicaConfigurationVolumeArgs
    ///                 {
    ///                     ImageAlias = "ubuntu:latest",
    ///                     Name = "volume_example",
    ///                     Size = 10,
    ///                     Type = "HDD",
    ///                     UserData = "ZWNobyAiSGVsbG8sIFdvcmxkIgo=",
    ///                     ImagePassword = serverImagePassword.Result,
    ///                     BootOrder = "AUTO",
    ///                 },
    ///             },
    ///         },
    ///     });
    /// 
    /// });
    /// ```
    /// </summary>
    [IonoscloudResourceType("ionoscloud:index/autoscalingGroup:AutoscalingGroup")]
    public partial class AutoscalingGroup : global::Pulumi.CustomResource
    {
        /// <summary>
        /// [string] Unique identifier for the resource
        /// </summary>
        [Output("datacenterId")]
        public Output<string> DatacenterId { get; private set; } = null!;

        /// <summary>
        /// Location of the data center.
        /// </summary>
        [Output("location")]
        public Output<string> Location { get; private set; } = null!;

        /// <summary>
        /// [int] The maximum value for the number of replicas on a VM Auto Scaling Group. Must be &gt;= 0 and &lt;= 200. Will be enforced for both automatic and manual changes.
        /// </summary>
        [Output("maxReplicaCount")]
        public Output<int> MaxReplicaCount { get; private set; } = null!;

        /// <summary>
        /// [int] The minimum value for the number of replicas on a VM Auto Scaling Group. Must be &gt;= 0 and &lt;= 200. Will be enforced for both automatic and manual changes.
        /// </summary>
        [Output("minReplicaCount")]
        public Output<int> MinReplicaCount { get; private set; } = null!;

        /// <summary>
        /// [string] User-defined name for the Autoscaling Group.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// [List] Specifies the behavior of this Autoscaling Group. A policy consists of Triggers and Actions, whereby an Action is some kind of automated behavior, and a Trigger is defined by the circumstances under which the Action is triggered. Currently, two separate Actions, namely Scaling In and Out are supported, triggered through Thresholds defined on a given Metric.
        /// </summary>
        [Output("policy")]
        public Output<Outputs.AutoscalingGroupPolicy> Policy { get; private set; } = null!;

        /// <summary>
        /// [List]
        /// </summary>
        [Output("replicaConfiguration")]
        public Output<Outputs.AutoscalingGroupReplicaConfiguration> ReplicaConfiguration { get; private set; } = null!;


        /// <summary>
        /// Create a AutoscalingGroup resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public AutoscalingGroup(string name, AutoscalingGroupArgs args, CustomResourceOptions? options = null)
            : base("ionoscloud:index/autoscalingGroup:AutoscalingGroup", name, args ?? new AutoscalingGroupArgs(), MakeResourceOptions(options, ""))
        {
        }

        private AutoscalingGroup(string name, Input<string> id, AutoscalingGroupState? state = null, CustomResourceOptions? options = null)
            : base("ionoscloud:index/autoscalingGroup:AutoscalingGroup", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing AutoscalingGroup resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static AutoscalingGroup Get(string name, Input<string> id, AutoscalingGroupState? state = null, CustomResourceOptions? options = null)
        {
            return new AutoscalingGroup(name, id, state, options);
        }
    }

    public sealed class AutoscalingGroupArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [string] Unique identifier for the resource
        /// </summary>
        [Input("datacenterId", required: true)]
        public Input<string> DatacenterId { get; set; } = null!;

        /// <summary>
        /// [int] The maximum value for the number of replicas on a VM Auto Scaling Group. Must be &gt;= 0 and &lt;= 200. Will be enforced for both automatic and manual changes.
        /// </summary>
        [Input("maxReplicaCount", required: true)]
        public Input<int> MaxReplicaCount { get; set; } = null!;

        /// <summary>
        /// [int] The minimum value for the number of replicas on a VM Auto Scaling Group. Must be &gt;= 0 and &lt;= 200. Will be enforced for both automatic and manual changes.
        /// </summary>
        [Input("minReplicaCount", required: true)]
        public Input<int> MinReplicaCount { get; set; } = null!;

        /// <summary>
        /// [string] User-defined name for the Autoscaling Group.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// [List] Specifies the behavior of this Autoscaling Group. A policy consists of Triggers and Actions, whereby an Action is some kind of automated behavior, and a Trigger is defined by the circumstances under which the Action is triggered. Currently, two separate Actions, namely Scaling In and Out are supported, triggered through Thresholds defined on a given Metric.
        /// </summary>
        [Input("policy", required: true)]
        public Input<Inputs.AutoscalingGroupPolicyArgs> Policy { get; set; } = null!;

        /// <summary>
        /// [List]
        /// </summary>
        [Input("replicaConfiguration", required: true)]
        public Input<Inputs.AutoscalingGroupReplicaConfigurationArgs> ReplicaConfiguration { get; set; } = null!;

        public AutoscalingGroupArgs()
        {
        }
        public static new AutoscalingGroupArgs Empty => new AutoscalingGroupArgs();
    }

    public sealed class AutoscalingGroupState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [string] Unique identifier for the resource
        /// </summary>
        [Input("datacenterId")]
        public Input<string>? DatacenterId { get; set; }

        /// <summary>
        /// Location of the data center.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// [int] The maximum value for the number of replicas on a VM Auto Scaling Group. Must be &gt;= 0 and &lt;= 200. Will be enforced for both automatic and manual changes.
        /// </summary>
        [Input("maxReplicaCount")]
        public Input<int>? MaxReplicaCount { get; set; }

        /// <summary>
        /// [int] The minimum value for the number of replicas on a VM Auto Scaling Group. Must be &gt;= 0 and &lt;= 200. Will be enforced for both automatic and manual changes.
        /// </summary>
        [Input("minReplicaCount")]
        public Input<int>? MinReplicaCount { get; set; }

        /// <summary>
        /// [string] User-defined name for the Autoscaling Group.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// [List] Specifies the behavior of this Autoscaling Group. A policy consists of Triggers and Actions, whereby an Action is some kind of automated behavior, and a Trigger is defined by the circumstances under which the Action is triggered. Currently, two separate Actions, namely Scaling In and Out are supported, triggered through Thresholds defined on a given Metric.
        /// </summary>
        [Input("policy")]
        public Input<Inputs.AutoscalingGroupPolicyGetArgs>? Policy { get; set; }

        /// <summary>
        /// [List]
        /// </summary>
        [Input("replicaConfiguration")]
        public Input<Inputs.AutoscalingGroupReplicaConfigurationGetArgs>? ReplicaConfiguration { get; set; }

        public AutoscalingGroupState()
        {
        }
        public static new AutoscalingGroupState Empty => new AutoscalingGroupState();
    }
}
