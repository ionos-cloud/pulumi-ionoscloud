// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package kafka

import (
	"context"
	"reflect"

	"errors"
	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Manages a **Kafka Cluster Topic** on IonosCloud.
//
// ## Example Usage
//
// This resource will create an operational Kafka Cluster Topic. After this section completes, the provisioner can be
// called.
//
// ```go
// package main
//
// import (
//
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/compute"
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/kafka"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			// Basic example
//			example, err := compute.NewDatacenter(ctx, "example", &compute.DatacenterArgs{
//				Name:     pulumi.String("example-kafka-datacenter"),
//				Location: pulumi.String("de/fra"),
//			})
//			if err != nil {
//				return err
//			}
//			exampleLan, err := compute.NewLan(ctx, "example", &compute.LanArgs{
//				DatacenterId: example.ID(),
//				Public:       pulumi.Bool(false),
//				Name:         pulumi.String("example-kafka-lan"),
//			})
//			if err != nil {
//				return err
//			}
//			exampleCluster, err := kafka.NewCluster(ctx, "example", &kafka.ClusterArgs{
//				Name:     pulumi.String("example-kafka-cluster"),
//				Location: example.Location,
//				Version:  pulumi.String("3.7.0"),
//				Size:     pulumi.String("S"),
//				Connections: &kafka.ClusterConnectionsArgs{
//					DatacenterId: example.ID(),
//					LanId:        exampleLan.ID(),
//					BrokerAddresses: pulumi.StringArray{
//						pulumi.String("192.168.1.101/24"),
//						pulumi.String("192.168.1.102/24"),
//						pulumi.String("192.168.1.103/24"),
//					},
//				},
//			})
//			if err != nil {
//				return err
//			}
//			_, err = kafka.NewTopic(ctx, "example", &kafka.TopicArgs{
//				ClusterId:          exampleCluster.ID(),
//				Name:               pulumi.String("kafka-cluster-topic"),
//				Location:           exampleCluster.Location,
//				ReplicationFactor:  pulumi.Int(1),
//				NumberOfPartitions: pulumi.Int(1),
//				RetentionTime:      pulumi.Int(86400000),
//				SegmentBytes:       pulumi.Int(1073741824),
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
//
// ```go
// package main
//
// import (
//
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/compute"
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/kafka"
//	"github.com/pulumi/pulumi-random/sdk/go/random"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			// Complete example
//			example, err := compute.NewDatacenter(ctx, "example", &compute.DatacenterArgs{
//				Name:     pulumi.String("example-kafka-datacenter"),
//				Location: pulumi.String("de/fra"),
//			})
//			if err != nil {
//				return err
//			}
//			exampleLan, err := compute.NewLan(ctx, "example", &compute.LanArgs{
//				DatacenterId: example.ID(),
//				Public:       pulumi.Bool(false),
//				Name:         pulumi.String("example-kafka-lan"),
//			})
//			if err != nil {
//				return err
//			}
//			password, err := random.NewPassword(ctx, "password", &random.PasswordArgs{
//				Length:  16,
//				Special: false,
//			})
//			if err != nil {
//				return err
//			}
//			_, err = compute.NewServer(ctx, "example", &compute.ServerArgs{
//				Name:             pulumi.String("example-kafka-server"),
//				DatacenterId:     example.ID(),
//				Cores:            pulumi.Int(1),
//				Ram:              int(2 * 1024),
//				AvailabilityZone: pulumi.String("AUTO"),
//				CpuFamily:        pulumi.String("INTEL_SKYLAKE"),
//				ImageName:        pulumi.String("ubuntu:latest"),
//				ImagePassword:    password.Result,
//				Volume: &compute.ServerVolumeArgs{
//					Name:     pulumi.String("example-kafka-volume"),
//					Size:     pulumi.Int(6),
//					DiskType: pulumi.String("SSD Standard"),
//				},
//				Nic: &compute.ServerNicArgs{
//					Lan:  exampleLan.ID(),
//					Name: pulumi.String("example-kafka-nic"),
//					Dhcp: pulumi.Bool(true),
//				},
//			})
//			if err != nil {
//				return err
//			}
//			exampleCluster, err := kafka.NewCluster(ctx, "example", &kafka.ClusterArgs{
//				Name:     pulumi.String("example-kafka-cluster"),
//				Location: example.Location,
//				Version:  pulumi.String("3.7.0"),
//				Size:     pulumi.String("S"),
//				Connections: &kafka.ClusterConnectionsArgs{
//					DatacenterId:    example.ID(),
//					LanId:           exampleLan.ID(),
//					BrokerAddresses: pulumi.StringArray("kafka_cluster_broker_ips_cidr_list"),
//				},
//			})
//			if err != nil {
//				return err
//			}
//			_, err = kafka.NewTopic(ctx, "example", &kafka.TopicArgs{
//				ClusterId:          exampleCluster.ID(),
//				Name:               pulumi.String("kafka-cluster-topic"),
//				Location:           exampleCluster.Location,
//				ReplicationFactor:  pulumi.Int(1),
//				NumberOfPartitions: pulumi.Int(1),
//				RetentionTime:      pulumi.Int(86400000),
//				SegmentBytes:       pulumi.Int(1073741824),
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
//
// ## Import
//
// Kafka Cluster Topic can be imported using the `location`, `kafka cluster id` and the `kafka cluster topic id`:
//
// ```sh
// $ pulumi import ionoscloud:kafka/topic:Topic my_topic location:kafka cluster uuid:kafka cluster topic uuid
// ```
type Topic struct {
	pulumi.CustomResourceState

	// [string] ID of the Kafka Cluster that the topic belongs to.
	ClusterId pulumi.StringOutput `pulumi:"clusterId"`
	// [string] The location of the Kafka Cluster Topic. Possible values: `de/fra`, `de/txl`. If this is not set and if no value is provided for the `IONOS_API_URL` env var, the default `location` will be: `de/fra`.
	Location pulumi.StringPtrOutput `pulumi:"location"`
	// [string] Name of the Kafka Cluster.
	Name pulumi.StringOutput `pulumi:"name"`
	// [int] The number of partitions of the topic. Partitions allow for parallel
	// processing of messages. The partition count must be greater than or equal to the replication factor. Minimum value: 1.
	// Default value: 3.
	NumberOfPartitions pulumi.IntPtrOutput `pulumi:"numberOfPartitions"`
	// [int] The number of replicas of the topic. The replication factor determines how many
	// copies of the topic are stored on different brokers. The replication factor must be less than or equal to the number
	// of brokers in the Kafka Cluster. Minimum value: 1. Default value: 3.
	ReplicationFactor pulumi.IntPtrOutput `pulumi:"replicationFactor"`
	// [int] This configuration controls the maximum time we will retain a log before we will
	// discard old log segments to free up space. This represents an SLA on how soon consumers must read their data. If set
	// to -1, no time limit is applied. Default value: 604800000.
	RetentionTime pulumi.IntPtrOutput `pulumi:"retentionTime"`
	// [int] This configuration controls the segment file size for the log. Retention and
	// cleaning is always done a file at a time so a larger segment size means fewer files but less granular control over
	// retention. Default value: 1073741824.
	SegmentBytes pulumi.IntPtrOutput `pulumi:"segmentBytes"`
}

// NewTopic registers a new resource with the given unique name, arguments, and options.
func NewTopic(ctx *pulumi.Context,
	name string, args *TopicArgs, opts ...pulumi.ResourceOption) (*Topic, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ClusterId == nil {
		return nil, errors.New("invalid value for required argument 'ClusterId'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Topic
	err := ctx.RegisterResource("ionoscloud:kafka/topic:Topic", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetTopic gets an existing Topic resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTopic(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TopicState, opts ...pulumi.ResourceOption) (*Topic, error) {
	var resource Topic
	err := ctx.ReadResource("ionoscloud:kafka/topic:Topic", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Topic resources.
type topicState struct {
	// [string] ID of the Kafka Cluster that the topic belongs to.
	ClusterId *string `pulumi:"clusterId"`
	// [string] The location of the Kafka Cluster Topic. Possible values: `de/fra`, `de/txl`. If this is not set and if no value is provided for the `IONOS_API_URL` env var, the default `location` will be: `de/fra`.
	Location *string `pulumi:"location"`
	// [string] Name of the Kafka Cluster.
	Name *string `pulumi:"name"`
	// [int] The number of partitions of the topic. Partitions allow for parallel
	// processing of messages. The partition count must be greater than or equal to the replication factor. Minimum value: 1.
	// Default value: 3.
	NumberOfPartitions *int `pulumi:"numberOfPartitions"`
	// [int] The number of replicas of the topic. The replication factor determines how many
	// copies of the topic are stored on different brokers. The replication factor must be less than or equal to the number
	// of brokers in the Kafka Cluster. Minimum value: 1. Default value: 3.
	ReplicationFactor *int `pulumi:"replicationFactor"`
	// [int] This configuration controls the maximum time we will retain a log before we will
	// discard old log segments to free up space. This represents an SLA on how soon consumers must read their data. If set
	// to -1, no time limit is applied. Default value: 604800000.
	RetentionTime *int `pulumi:"retentionTime"`
	// [int] This configuration controls the segment file size for the log. Retention and
	// cleaning is always done a file at a time so a larger segment size means fewer files but less granular control over
	// retention. Default value: 1073741824.
	SegmentBytes *int `pulumi:"segmentBytes"`
}

type TopicState struct {
	// [string] ID of the Kafka Cluster that the topic belongs to.
	ClusterId pulumi.StringPtrInput
	// [string] The location of the Kafka Cluster Topic. Possible values: `de/fra`, `de/txl`. If this is not set and if no value is provided for the `IONOS_API_URL` env var, the default `location` will be: `de/fra`.
	Location pulumi.StringPtrInput
	// [string] Name of the Kafka Cluster.
	Name pulumi.StringPtrInput
	// [int] The number of partitions of the topic. Partitions allow for parallel
	// processing of messages. The partition count must be greater than or equal to the replication factor. Minimum value: 1.
	// Default value: 3.
	NumberOfPartitions pulumi.IntPtrInput
	// [int] The number of replicas of the topic. The replication factor determines how many
	// copies of the topic are stored on different brokers. The replication factor must be less than or equal to the number
	// of brokers in the Kafka Cluster. Minimum value: 1. Default value: 3.
	ReplicationFactor pulumi.IntPtrInput
	// [int] This configuration controls the maximum time we will retain a log before we will
	// discard old log segments to free up space. This represents an SLA on how soon consumers must read their data. If set
	// to -1, no time limit is applied. Default value: 604800000.
	RetentionTime pulumi.IntPtrInput
	// [int] This configuration controls the segment file size for the log. Retention and
	// cleaning is always done a file at a time so a larger segment size means fewer files but less granular control over
	// retention. Default value: 1073741824.
	SegmentBytes pulumi.IntPtrInput
}

func (TopicState) ElementType() reflect.Type {
	return reflect.TypeOf((*topicState)(nil)).Elem()
}

type topicArgs struct {
	// [string] ID of the Kafka Cluster that the topic belongs to.
	ClusterId string `pulumi:"clusterId"`
	// [string] The location of the Kafka Cluster Topic. Possible values: `de/fra`, `de/txl`. If this is not set and if no value is provided for the `IONOS_API_URL` env var, the default `location` will be: `de/fra`.
	Location *string `pulumi:"location"`
	// [string] Name of the Kafka Cluster.
	Name *string `pulumi:"name"`
	// [int] The number of partitions of the topic. Partitions allow for parallel
	// processing of messages. The partition count must be greater than or equal to the replication factor. Minimum value: 1.
	// Default value: 3.
	NumberOfPartitions *int `pulumi:"numberOfPartitions"`
	// [int] The number of replicas of the topic. The replication factor determines how many
	// copies of the topic are stored on different brokers. The replication factor must be less than or equal to the number
	// of brokers in the Kafka Cluster. Minimum value: 1. Default value: 3.
	ReplicationFactor *int `pulumi:"replicationFactor"`
	// [int] This configuration controls the maximum time we will retain a log before we will
	// discard old log segments to free up space. This represents an SLA on how soon consumers must read their data. If set
	// to -1, no time limit is applied. Default value: 604800000.
	RetentionTime *int `pulumi:"retentionTime"`
	// [int] This configuration controls the segment file size for the log. Retention and
	// cleaning is always done a file at a time so a larger segment size means fewer files but less granular control over
	// retention. Default value: 1073741824.
	SegmentBytes *int `pulumi:"segmentBytes"`
}

// The set of arguments for constructing a Topic resource.
type TopicArgs struct {
	// [string] ID of the Kafka Cluster that the topic belongs to.
	ClusterId pulumi.StringInput
	// [string] The location of the Kafka Cluster Topic. Possible values: `de/fra`, `de/txl`. If this is not set and if no value is provided for the `IONOS_API_URL` env var, the default `location` will be: `de/fra`.
	Location pulumi.StringPtrInput
	// [string] Name of the Kafka Cluster.
	Name pulumi.StringPtrInput
	// [int] The number of partitions of the topic. Partitions allow for parallel
	// processing of messages. The partition count must be greater than or equal to the replication factor. Minimum value: 1.
	// Default value: 3.
	NumberOfPartitions pulumi.IntPtrInput
	// [int] The number of replicas of the topic. The replication factor determines how many
	// copies of the topic are stored on different brokers. The replication factor must be less than or equal to the number
	// of brokers in the Kafka Cluster. Minimum value: 1. Default value: 3.
	ReplicationFactor pulumi.IntPtrInput
	// [int] This configuration controls the maximum time we will retain a log before we will
	// discard old log segments to free up space. This represents an SLA on how soon consumers must read their data. If set
	// to -1, no time limit is applied. Default value: 604800000.
	RetentionTime pulumi.IntPtrInput
	// [int] This configuration controls the segment file size for the log. Retention and
	// cleaning is always done a file at a time so a larger segment size means fewer files but less granular control over
	// retention. Default value: 1073741824.
	SegmentBytes pulumi.IntPtrInput
}

func (TopicArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*topicArgs)(nil)).Elem()
}

type TopicInput interface {
	pulumi.Input

	ToTopicOutput() TopicOutput
	ToTopicOutputWithContext(ctx context.Context) TopicOutput
}

func (*Topic) ElementType() reflect.Type {
	return reflect.TypeOf((**Topic)(nil)).Elem()
}

func (i *Topic) ToTopicOutput() TopicOutput {
	return i.ToTopicOutputWithContext(context.Background())
}

func (i *Topic) ToTopicOutputWithContext(ctx context.Context) TopicOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TopicOutput)
}

// TopicArrayInput is an input type that accepts TopicArray and TopicArrayOutput values.
// You can construct a concrete instance of `TopicArrayInput` via:
//
//	TopicArray{ TopicArgs{...} }
type TopicArrayInput interface {
	pulumi.Input

	ToTopicArrayOutput() TopicArrayOutput
	ToTopicArrayOutputWithContext(context.Context) TopicArrayOutput
}

type TopicArray []TopicInput

func (TopicArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Topic)(nil)).Elem()
}

func (i TopicArray) ToTopicArrayOutput() TopicArrayOutput {
	return i.ToTopicArrayOutputWithContext(context.Background())
}

func (i TopicArray) ToTopicArrayOutputWithContext(ctx context.Context) TopicArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TopicArrayOutput)
}

// TopicMapInput is an input type that accepts TopicMap and TopicMapOutput values.
// You can construct a concrete instance of `TopicMapInput` via:
//
//	TopicMap{ "key": TopicArgs{...} }
type TopicMapInput interface {
	pulumi.Input

	ToTopicMapOutput() TopicMapOutput
	ToTopicMapOutputWithContext(context.Context) TopicMapOutput
}

type TopicMap map[string]TopicInput

func (TopicMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Topic)(nil)).Elem()
}

func (i TopicMap) ToTopicMapOutput() TopicMapOutput {
	return i.ToTopicMapOutputWithContext(context.Background())
}

func (i TopicMap) ToTopicMapOutputWithContext(ctx context.Context) TopicMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TopicMapOutput)
}

type TopicOutput struct{ *pulumi.OutputState }

func (TopicOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Topic)(nil)).Elem()
}

func (o TopicOutput) ToTopicOutput() TopicOutput {
	return o
}

func (o TopicOutput) ToTopicOutputWithContext(ctx context.Context) TopicOutput {
	return o
}

// [string] ID of the Kafka Cluster that the topic belongs to.
func (o TopicOutput) ClusterId() pulumi.StringOutput {
	return o.ApplyT(func(v *Topic) pulumi.StringOutput { return v.ClusterId }).(pulumi.StringOutput)
}

// [string] The location of the Kafka Cluster Topic. Possible values: `de/fra`, `de/txl`. If this is not set and if no value is provided for the `IONOS_API_URL` env var, the default `location` will be: `de/fra`.
func (o TopicOutput) Location() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Topic) pulumi.StringPtrOutput { return v.Location }).(pulumi.StringPtrOutput)
}

// [string] Name of the Kafka Cluster.
func (o TopicOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Topic) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// [int] The number of partitions of the topic. Partitions allow for parallel
// processing of messages. The partition count must be greater than or equal to the replication factor. Minimum value: 1.
// Default value: 3.
func (o TopicOutput) NumberOfPartitions() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *Topic) pulumi.IntPtrOutput { return v.NumberOfPartitions }).(pulumi.IntPtrOutput)
}

// [int] The number of replicas of the topic. The replication factor determines how many
// copies of the topic are stored on different brokers. The replication factor must be less than or equal to the number
// of brokers in the Kafka Cluster. Minimum value: 1. Default value: 3.
func (o TopicOutput) ReplicationFactor() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *Topic) pulumi.IntPtrOutput { return v.ReplicationFactor }).(pulumi.IntPtrOutput)
}

// [int] This configuration controls the maximum time we will retain a log before we will
// discard old log segments to free up space. This represents an SLA on how soon consumers must read their data. If set
// to -1, no time limit is applied. Default value: 604800000.
func (o TopicOutput) RetentionTime() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *Topic) pulumi.IntPtrOutput { return v.RetentionTime }).(pulumi.IntPtrOutput)
}

// [int] This configuration controls the segment file size for the log. Retention and
// cleaning is always done a file at a time so a larger segment size means fewer files but less granular control over
// retention. Default value: 1073741824.
func (o TopicOutput) SegmentBytes() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *Topic) pulumi.IntPtrOutput { return v.SegmentBytes }).(pulumi.IntPtrOutput)
}

type TopicArrayOutput struct{ *pulumi.OutputState }

func (TopicArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Topic)(nil)).Elem()
}

func (o TopicArrayOutput) ToTopicArrayOutput() TopicArrayOutput {
	return o
}

func (o TopicArrayOutput) ToTopicArrayOutputWithContext(ctx context.Context) TopicArrayOutput {
	return o
}

func (o TopicArrayOutput) Index(i pulumi.IntInput) TopicOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Topic {
		return vs[0].([]*Topic)[vs[1].(int)]
	}).(TopicOutput)
}

type TopicMapOutput struct{ *pulumi.OutputState }

func (TopicMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Topic)(nil)).Elem()
}

func (o TopicMapOutput) ToTopicMapOutput() TopicMapOutput {
	return o
}

func (o TopicMapOutput) ToTopicMapOutputWithContext(ctx context.Context) TopicMapOutput {
	return o
}

func (o TopicMapOutput) MapIndex(k pulumi.StringInput) TopicOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Topic {
		return vs[0].(map[string]*Topic)[vs[1].(string)]
	}).(TopicOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*TopicInput)(nil)).Elem(), &Topic{})
	pulumi.RegisterInputType(reflect.TypeOf((*TopicArrayInput)(nil)).Elem(), TopicArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*TopicMapInput)(nil)).Elem(), TopicMap{})
	pulumi.RegisterOutputType(TopicOutput{})
	pulumi.RegisterOutputType(TopicArrayOutput{})
	pulumi.RegisterOutputType(TopicMapOutput{})
}
