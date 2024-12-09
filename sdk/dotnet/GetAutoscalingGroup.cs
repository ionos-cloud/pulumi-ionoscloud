// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud
{
    public static class GetAutoscalingGroup
    {
        /// <summary>
        /// The autoscaling group data source can be used to search for and return an existing Autoscaling Group. You can provide a string for the name or id parameters which will be compared with provisioned Autoscaling Groups. If a single match is found, it will be returned.
        /// 
        /// ## Example Usage
        /// 
        /// ### By Name
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var autoscalingGroup = Ionoscloud.GetAutoscalingGroup.Invoke(new()
        ///     {
        ///         Name = "test_ds",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Task<GetAutoscalingGroupResult> InvokeAsync(GetAutoscalingGroupArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetAutoscalingGroupResult>("ionoscloud:index/getAutoscalingGroup:getAutoscalingGroup", args ?? new GetAutoscalingGroupArgs(), options.WithDefaults());

        /// <summary>
        /// The autoscaling group data source can be used to search for and return an existing Autoscaling Group. You can provide a string for the name or id parameters which will be compared with provisioned Autoscaling Groups. If a single match is found, it will be returned.
        /// 
        /// ## Example Usage
        /// 
        /// ### By Name
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Ionoscloud = Pulumi.Ionoscloud;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var autoscalingGroup = Ionoscloud.GetAutoscalingGroup.Invoke(new()
        ///     {
        ///         Name = "test_ds",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetAutoscalingGroupResult> Invoke(GetAutoscalingGroupInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetAutoscalingGroupResult>("ionoscloud:index/getAutoscalingGroup:getAutoscalingGroup", args ?? new GetAutoscalingGroupInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetAutoscalingGroupArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Id of an existing Autoscaling Group that you want to search for.
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        /// <summary>
        /// Name of an existing Autoscaling Group that you want to search for.
        /// 
        /// Either `name` or `id` must be provided. If none or both are provided, the datasource will return an error.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        public GetAutoscalingGroupArgs()
        {
        }
        public static new GetAutoscalingGroupArgs Empty => new GetAutoscalingGroupArgs();
    }

    public sealed class GetAutoscalingGroupInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Id of an existing Autoscaling Group that you want to search for.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// Name of an existing Autoscaling Group that you want to search for.
        /// 
        /// Either `name` or `id` must be provided. If none or both are provided, the datasource will return an error.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public GetAutoscalingGroupInvokeArgs()
        {
        }
        public static new GetAutoscalingGroupInvokeArgs Empty => new GetAutoscalingGroupInvokeArgs();
    }


    [OutputType]
    public sealed class GetAutoscalingGroupResult
    {
        public readonly string DatacenterId;
        /// <summary>
        /// Unique identifier for the resource
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// Location of the datacenter. This location is the same as the one from the selected template.
        /// </summary>
        public readonly string Location;
        /// <summary>
        /// Maximum replica count value for `targetReplicaCount`. Will be enforced for both automatic and manual changes.
        /// </summary>
        public readonly int MaxReplicaCount;
        /// <summary>
        /// Minimum replica count value for `targetReplicaCount`. Will be enforced for both automatic and manual changes.
        /// </summary>
        public readonly int MinReplicaCount;
        /// <summary>
        /// The name of the Autoscaling Group.
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// Specifies the behavior of this Autoscaling Group. A policy consists of Triggers and Actions, whereby an Action is some kind of automated behavior, and a Trigger is defined by the circumstances under which the Action is triggered. Currently, two separate Actions, namely Scaling In and Out are supported, triggered through Thresholds defined on a given Metric.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetAutoscalingGroupPolicyResult> Policies;
        public readonly ImmutableArray<Outputs.GetAutoscalingGroupReplicaConfigurationResult> ReplicaConfigurations;
        public readonly int TargetReplicaCount;

        [OutputConstructor]
        private GetAutoscalingGroupResult(
            string datacenterId,

            string? id,

            string location,

            int maxReplicaCount,

            int minReplicaCount,

            string? name,

            ImmutableArray<Outputs.GetAutoscalingGroupPolicyResult> policies,

            ImmutableArray<Outputs.GetAutoscalingGroupReplicaConfigurationResult> replicaConfigurations,

            int targetReplicaCount)
        {
            DatacenterId = datacenterId;
            Id = id;
            Location = location;
            MaxReplicaCount = maxReplicaCount;
            MinReplicaCount = minReplicaCount;
            Name = name;
            Policies = policies;
            ReplicaConfigurations = replicaConfigurations;
            TargetReplicaCount = targetReplicaCount;
        }
    }
}
