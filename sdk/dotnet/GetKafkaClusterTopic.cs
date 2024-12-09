// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud
{
    public static class GetKafkaClusterTopic
    {
        public static Task<GetKafkaClusterTopicResult> InvokeAsync(GetKafkaClusterTopicArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetKafkaClusterTopicResult>("ionoscloud:index/getKafkaClusterTopic:getKafkaClusterTopic", args ?? new GetKafkaClusterTopicArgs(), options.WithDefaults());

        public static Output<GetKafkaClusterTopicResult> Invoke(GetKafkaClusterTopicInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetKafkaClusterTopicResult>("ionoscloud:index/getKafkaClusterTopic:getKafkaClusterTopic", args ?? new GetKafkaClusterTopicInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetKafkaClusterTopicArgs : global::Pulumi.InvokeArgs
    {
        [Input("clusterId", required: true)]
        public string ClusterId { get; set; } = null!;

        [Input("id")]
        public string? Id { get; set; }

        [Input("location", required: true)]
        public string Location { get; set; } = null!;

        [Input("name")]
        public string? Name { get; set; }

        [Input("partialMatch")]
        public bool? PartialMatch { get; set; }

        public GetKafkaClusterTopicArgs()
        {
        }
        public static new GetKafkaClusterTopicArgs Empty => new GetKafkaClusterTopicArgs();
    }

    public sealed class GetKafkaClusterTopicInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("clusterId", required: true)]
        public Input<string> ClusterId { get; set; } = null!;

        [Input("id")]
        public Input<string>? Id { get; set; }

        [Input("location", required: true)]
        public Input<string> Location { get; set; } = null!;

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("partialMatch")]
        public Input<bool>? PartialMatch { get; set; }

        public GetKafkaClusterTopicInvokeArgs()
        {
        }
        public static new GetKafkaClusterTopicInvokeArgs Empty => new GetKafkaClusterTopicInvokeArgs();
    }


    [OutputType]
    public sealed class GetKafkaClusterTopicResult
    {
        public readonly string ClusterId;
        public readonly string Id;
        public readonly string Location;
        public readonly string Name;
        public readonly int NumberOfPartitions;
        public readonly bool? PartialMatch;
        public readonly int ReplicationFactor;
        public readonly int RetentionTime;
        public readonly int SegmentBytes;

        [OutputConstructor]
        private GetKafkaClusterTopicResult(
            string clusterId,

            string id,

            string location,

            string name,

            int numberOfPartitions,

            bool? partialMatch,

            int replicationFactor,

            int retentionTime,

            int segmentBytes)
        {
            ClusterId = clusterId;
            Id = id;
            Location = location;
            Name = name;
            NumberOfPartitions = numberOfPartitions;
            PartialMatch = partialMatch;
            ReplicationFactor = replicationFactor;
            RetentionTime = retentionTime;
            SegmentBytes = segmentBytes;
        }
    }
}
