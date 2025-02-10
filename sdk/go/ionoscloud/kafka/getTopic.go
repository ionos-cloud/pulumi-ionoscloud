// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package kafka

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The **Kafka topic data source** can be used to search for and return an existing Kafka Cluster Topic.
// You can provide a string for the name parameter which will be compared with provisioned Kafka Cluster Topics.
// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
// When this happens, please refine your search string so that it is specific enough to return only one result.
//
// ## Example Usage
//
// ### By ID
//
// ```go
// package main
//
// import (
//
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/kafka"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := kafka.LookupTopic(ctx, &kafka.LookupTopicArgs{
//				Id:        pulumi.StringRef("your_kafka_cluster_topic_id"),
//				ClusterId: "your_kafka_cluster_id",
//				Location:  "your_kafka_cluster_location",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
//
// ### By Name
//
// Needs to have the resource be previously created, or a dependsOn clause to ensure that the resource is created before
// this data source is called.
//
// ```go
// package main
//
// import (
//
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/kafka"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := kafka.LookupTopic(ctx, &kafka.LookupTopicArgs{
//				Name:      pulumi.StringRef("kafka-cluster-topic"),
//				ClusterId: "your_kafka_cluster_id",
//				Location:  "location_of_kafka_cluster",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func LookupTopic(ctx *pulumi.Context, args *LookupTopicArgs, opts ...pulumi.InvokeOption) (*LookupTopicResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupTopicResult
	err := ctx.Invoke("ionoscloud:kafka/getTopic:getTopic", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getTopic.
type LookupTopicArgs struct {
	// ID of the Kafka Cluster that the topic belongs to.
	ClusterId string `pulumi:"clusterId"`
	// ID of an existing Kafka Cluster Topic that you want to search for.
	Id *string `pulumi:"id"`
	// The location of the Kafka Cluster Topic. Must be the same as the location of the Kafka
	// Cluster. Possible values: `de/fra`, `de/txl`
	Location string `pulumi:"location"`
	// Name of an existing Kafka Cluster Topic that you want to search for.
	Name         *string `pulumi:"name"`
	PartialMatch *bool   `pulumi:"partialMatch"`
}

// A collection of values returned by getTopic.
type LookupTopicResult struct {
	// The id of the Kafka Cluster that the topic belongs to.
	ClusterId string `pulumi:"clusterId"`
	// UUID of the Kafka Cluster Topic.
	Id       string `pulumi:"id"`
	Location string `pulumi:"location"`
	// The name of the Kafka Cluster Topic.
	Name string `pulumi:"name"`
	// The number of partitions of the topic. Partitions allow for parallel processing of messages.
	NumberOfPartitions int   `pulumi:"numberOfPartitions"`
	PartialMatch       *bool `pulumi:"partialMatch"`
	// The number of replicas of the topic. The replication factor determines how many copies of the
	// topic are stored on different brokers.
	ReplicationFactor int `pulumi:"replicationFactor"`
	// This configuration controls the maximum time we will retain a log before we will discard old log
	// segments to free up space. This represents an SLA on how soon consumers must read their data. If set to -1, no time
	// limit is applied.
	RetentionTime int `pulumi:"retentionTime"`
	// This configuration controls the segment file size for the log. Retention and cleaning is always done a file at a time so a larger segment size means fewer files but less granular control over retention.
	SegmentBytes int `pulumi:"segmentBytes"`
}

func LookupTopicOutput(ctx *pulumi.Context, args LookupTopicOutputArgs, opts ...pulumi.InvokeOption) LookupTopicResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupTopicResultOutput, error) {
			args := v.(LookupTopicArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("ionoscloud:kafka/getTopic:getTopic", args, LookupTopicResultOutput{}, options).(LookupTopicResultOutput), nil
		}).(LookupTopicResultOutput)
}

// A collection of arguments for invoking getTopic.
type LookupTopicOutputArgs struct {
	// ID of the Kafka Cluster that the topic belongs to.
	ClusterId pulumi.StringInput `pulumi:"clusterId"`
	// ID of an existing Kafka Cluster Topic that you want to search for.
	Id pulumi.StringPtrInput `pulumi:"id"`
	// The location of the Kafka Cluster Topic. Must be the same as the location of the Kafka
	// Cluster. Possible values: `de/fra`, `de/txl`
	Location pulumi.StringInput `pulumi:"location"`
	// Name of an existing Kafka Cluster Topic that you want to search for.
	Name         pulumi.StringPtrInput `pulumi:"name"`
	PartialMatch pulumi.BoolPtrInput   `pulumi:"partialMatch"`
}

func (LookupTopicOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupTopicArgs)(nil)).Elem()
}

// A collection of values returned by getTopic.
type LookupTopicResultOutput struct{ *pulumi.OutputState }

func (LookupTopicResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupTopicResult)(nil)).Elem()
}

func (o LookupTopicResultOutput) ToLookupTopicResultOutput() LookupTopicResultOutput {
	return o
}

func (o LookupTopicResultOutput) ToLookupTopicResultOutputWithContext(ctx context.Context) LookupTopicResultOutput {
	return o
}

// The id of the Kafka Cluster that the topic belongs to.
func (o LookupTopicResultOutput) ClusterId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupTopicResult) string { return v.ClusterId }).(pulumi.StringOutput)
}

// UUID of the Kafka Cluster Topic.
func (o LookupTopicResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupTopicResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o LookupTopicResultOutput) Location() pulumi.StringOutput {
	return o.ApplyT(func(v LookupTopicResult) string { return v.Location }).(pulumi.StringOutput)
}

// The name of the Kafka Cluster Topic.
func (o LookupTopicResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupTopicResult) string { return v.Name }).(pulumi.StringOutput)
}

// The number of partitions of the topic. Partitions allow for parallel processing of messages.
func (o LookupTopicResultOutput) NumberOfPartitions() pulumi.IntOutput {
	return o.ApplyT(func(v LookupTopicResult) int { return v.NumberOfPartitions }).(pulumi.IntOutput)
}

func (o LookupTopicResultOutput) PartialMatch() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupTopicResult) *bool { return v.PartialMatch }).(pulumi.BoolPtrOutput)
}

// The number of replicas of the topic. The replication factor determines how many copies of the
// topic are stored on different brokers.
func (o LookupTopicResultOutput) ReplicationFactor() pulumi.IntOutput {
	return o.ApplyT(func(v LookupTopicResult) int { return v.ReplicationFactor }).(pulumi.IntOutput)
}

// This configuration controls the maximum time we will retain a log before we will discard old log
// segments to free up space. This represents an SLA on how soon consumers must read their data. If set to -1, no time
// limit is applied.
func (o LookupTopicResultOutput) RetentionTime() pulumi.IntOutput {
	return o.ApplyT(func(v LookupTopicResult) int { return v.RetentionTime }).(pulumi.IntOutput)
}

// This configuration controls the segment file size for the log. Retention and cleaning is always done a file at a time so a larger segment size means fewer files but less granular control over retention.
func (o LookupTopicResultOutput) SegmentBytes() pulumi.IntOutput {
	return o.ApplyT(func(v LookupTopicResult) int { return v.SegmentBytes }).(pulumi.IntOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupTopicResultOutput{})
}
