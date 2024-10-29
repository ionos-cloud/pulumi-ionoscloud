// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ionoscloud

import (
	"context"
	"reflect"

	"errors"
	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Manages a **Kafka Cluster** on IonosCloud.
//
// ## Example Usage
//
// This resource will create an operational Kafka Cluster. After this section completes, the provisioner can be called.
//
// <!--Start PulumiCodeChooser -->
// ```go
// package main
//
// import (
//
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud"
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/compute"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			// Basic example
//			exampleDatacenter, err := compute.NewDatacenter(ctx, "exampleDatacenter", &compute.DatacenterArgs{
//				Location: pulumi.String("de/fra"),
//			})
//			if err != nil {
//				return err
//			}
//			exampleLan, err := compute.NewLan(ctx, "exampleLan", &compute.LanArgs{
//				DatacenterId: exampleDatacenter.ID(),
//				Public:       pulumi.Bool(false),
//			})
//			if err != nil {
//				return err
//			}
//			_, err = ionoscloud.NewKafkaCluster(ctx, "exampleKafkaCluster", &ionoscloud.KafkaClusterArgs{
//				Location: pulumi.String("de/fra"),
//				Version:  pulumi.String("3.7.0"),
//				Size:     pulumi.String("S"),
//				Connections: &ionoscloud.KafkaClusterConnectionsArgs{
//					DatacenterId: exampleDatacenter.ID(),
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
//			return nil
//		})
//	}
//
// ```
// <!--End PulumiCodeChooser -->
//
// ## Import
//
// Kafka Cluster can be imported using the `location` and `kafka cluster id`:
//
// ```sh
// $ pulumi import ionoscloud:index/kafkaCluster:KafkaCluster mycluster {location}:{kafka cluster uuid}
// ```
type KafkaCluster struct {
	pulumi.CustomResourceState

	// [list] IP address and port of cluster brokers.
	BrokerAddresses pulumi.StringArrayOutput `pulumi:"brokerAddresses"`
	// Connection information of the Kafka Cluster. Minimum items: 1, maximum items: 1.
	Connections KafkaClusterConnectionsOutput `pulumi:"connections"`
	// [string] The location of the Kafka Cluster. Possible values: `de/fra`, `de/txl`
	Location pulumi.StringOutput `pulumi:"location"`
	// [string] Name of the Kafka Cluster.
	Name pulumi.StringOutput `pulumi:"name"`
	// [string] Size of the Kafka Cluster. Possible values: `XS`, `S`
	Size pulumi.StringOutput `pulumi:"size"`
	// [string] Version of the Kafka Cluster. Possible values: `3.7.0`
	Version pulumi.StringOutput `pulumi:"version"`
}

// NewKafkaCluster registers a new resource with the given unique name, arguments, and options.
func NewKafkaCluster(ctx *pulumi.Context,
	name string, args *KafkaClusterArgs, opts ...pulumi.ResourceOption) (*KafkaCluster, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Connections == nil {
		return nil, errors.New("invalid value for required argument 'Connections'")
	}
	if args.Location == nil {
		return nil, errors.New("invalid value for required argument 'Location'")
	}
	if args.Size == nil {
		return nil, errors.New("invalid value for required argument 'Size'")
	}
	if args.Version == nil {
		return nil, errors.New("invalid value for required argument 'Version'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource KafkaCluster
	err := ctx.RegisterResource("ionoscloud:index/kafkaCluster:KafkaCluster", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetKafkaCluster gets an existing KafkaCluster resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetKafkaCluster(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *KafkaClusterState, opts ...pulumi.ResourceOption) (*KafkaCluster, error) {
	var resource KafkaCluster
	err := ctx.ReadResource("ionoscloud:index/kafkaCluster:KafkaCluster", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering KafkaCluster resources.
type kafkaClusterState struct {
	// [list] IP address and port of cluster brokers.
	BrokerAddresses []string `pulumi:"brokerAddresses"`
	// Connection information of the Kafka Cluster. Minimum items: 1, maximum items: 1.
	Connections *KafkaClusterConnections `pulumi:"connections"`
	// [string] The location of the Kafka Cluster. Possible values: `de/fra`, `de/txl`
	Location *string `pulumi:"location"`
	// [string] Name of the Kafka Cluster.
	Name *string `pulumi:"name"`
	// [string] Size of the Kafka Cluster. Possible values: `XS`, `S`
	Size *string `pulumi:"size"`
	// [string] Version of the Kafka Cluster. Possible values: `3.7.0`
	Version *string `pulumi:"version"`
}

type KafkaClusterState struct {
	// [list] IP address and port of cluster brokers.
	BrokerAddresses pulumi.StringArrayInput
	// Connection information of the Kafka Cluster. Minimum items: 1, maximum items: 1.
	Connections KafkaClusterConnectionsPtrInput
	// [string] The location of the Kafka Cluster. Possible values: `de/fra`, `de/txl`
	Location pulumi.StringPtrInput
	// [string] Name of the Kafka Cluster.
	Name pulumi.StringPtrInput
	// [string] Size of the Kafka Cluster. Possible values: `XS`, `S`
	Size pulumi.StringPtrInput
	// [string] Version of the Kafka Cluster. Possible values: `3.7.0`
	Version pulumi.StringPtrInput
}

func (KafkaClusterState) ElementType() reflect.Type {
	return reflect.TypeOf((*kafkaClusterState)(nil)).Elem()
}

type kafkaClusterArgs struct {
	// Connection information of the Kafka Cluster. Minimum items: 1, maximum items: 1.
	Connections KafkaClusterConnections `pulumi:"connections"`
	// [string] The location of the Kafka Cluster. Possible values: `de/fra`, `de/txl`
	Location string `pulumi:"location"`
	// [string] Name of the Kafka Cluster.
	Name *string `pulumi:"name"`
	// [string] Size of the Kafka Cluster. Possible values: `XS`, `S`
	Size string `pulumi:"size"`
	// [string] Version of the Kafka Cluster. Possible values: `3.7.0`
	Version string `pulumi:"version"`
}

// The set of arguments for constructing a KafkaCluster resource.
type KafkaClusterArgs struct {
	// Connection information of the Kafka Cluster. Minimum items: 1, maximum items: 1.
	Connections KafkaClusterConnectionsInput
	// [string] The location of the Kafka Cluster. Possible values: `de/fra`, `de/txl`
	Location pulumi.StringInput
	// [string] Name of the Kafka Cluster.
	Name pulumi.StringPtrInput
	// [string] Size of the Kafka Cluster. Possible values: `XS`, `S`
	Size pulumi.StringInput
	// [string] Version of the Kafka Cluster. Possible values: `3.7.0`
	Version pulumi.StringInput
}

func (KafkaClusterArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*kafkaClusterArgs)(nil)).Elem()
}

type KafkaClusterInput interface {
	pulumi.Input

	ToKafkaClusterOutput() KafkaClusterOutput
	ToKafkaClusterOutputWithContext(ctx context.Context) KafkaClusterOutput
}

func (*KafkaCluster) ElementType() reflect.Type {
	return reflect.TypeOf((**KafkaCluster)(nil)).Elem()
}

func (i *KafkaCluster) ToKafkaClusterOutput() KafkaClusterOutput {
	return i.ToKafkaClusterOutputWithContext(context.Background())
}

func (i *KafkaCluster) ToKafkaClusterOutputWithContext(ctx context.Context) KafkaClusterOutput {
	return pulumi.ToOutputWithContext(ctx, i).(KafkaClusterOutput)
}

// KafkaClusterArrayInput is an input type that accepts KafkaClusterArray and KafkaClusterArrayOutput values.
// You can construct a concrete instance of `KafkaClusterArrayInput` via:
//
//	KafkaClusterArray{ KafkaClusterArgs{...} }
type KafkaClusterArrayInput interface {
	pulumi.Input

	ToKafkaClusterArrayOutput() KafkaClusterArrayOutput
	ToKafkaClusterArrayOutputWithContext(context.Context) KafkaClusterArrayOutput
}

type KafkaClusterArray []KafkaClusterInput

func (KafkaClusterArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*KafkaCluster)(nil)).Elem()
}

func (i KafkaClusterArray) ToKafkaClusterArrayOutput() KafkaClusterArrayOutput {
	return i.ToKafkaClusterArrayOutputWithContext(context.Background())
}

func (i KafkaClusterArray) ToKafkaClusterArrayOutputWithContext(ctx context.Context) KafkaClusterArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(KafkaClusterArrayOutput)
}

// KafkaClusterMapInput is an input type that accepts KafkaClusterMap and KafkaClusterMapOutput values.
// You can construct a concrete instance of `KafkaClusterMapInput` via:
//
//	KafkaClusterMap{ "key": KafkaClusterArgs{...} }
type KafkaClusterMapInput interface {
	pulumi.Input

	ToKafkaClusterMapOutput() KafkaClusterMapOutput
	ToKafkaClusterMapOutputWithContext(context.Context) KafkaClusterMapOutput
}

type KafkaClusterMap map[string]KafkaClusterInput

func (KafkaClusterMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*KafkaCluster)(nil)).Elem()
}

func (i KafkaClusterMap) ToKafkaClusterMapOutput() KafkaClusterMapOutput {
	return i.ToKafkaClusterMapOutputWithContext(context.Background())
}

func (i KafkaClusterMap) ToKafkaClusterMapOutputWithContext(ctx context.Context) KafkaClusterMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(KafkaClusterMapOutput)
}

type KafkaClusterOutput struct{ *pulumi.OutputState }

func (KafkaClusterOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**KafkaCluster)(nil)).Elem()
}

func (o KafkaClusterOutput) ToKafkaClusterOutput() KafkaClusterOutput {
	return o
}

func (o KafkaClusterOutput) ToKafkaClusterOutputWithContext(ctx context.Context) KafkaClusterOutput {
	return o
}

// [list] IP address and port of cluster brokers.
func (o KafkaClusterOutput) BrokerAddresses() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *KafkaCluster) pulumi.StringArrayOutput { return v.BrokerAddresses }).(pulumi.StringArrayOutput)
}

// Connection information of the Kafka Cluster. Minimum items: 1, maximum items: 1.
func (o KafkaClusterOutput) Connections() KafkaClusterConnectionsOutput {
	return o.ApplyT(func(v *KafkaCluster) KafkaClusterConnectionsOutput { return v.Connections }).(KafkaClusterConnectionsOutput)
}

// [string] The location of the Kafka Cluster. Possible values: `de/fra`, `de/txl`
func (o KafkaClusterOutput) Location() pulumi.StringOutput {
	return o.ApplyT(func(v *KafkaCluster) pulumi.StringOutput { return v.Location }).(pulumi.StringOutput)
}

// [string] Name of the Kafka Cluster.
func (o KafkaClusterOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *KafkaCluster) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// [string] Size of the Kafka Cluster. Possible values: `XS`, `S`
func (o KafkaClusterOutput) Size() pulumi.StringOutput {
	return o.ApplyT(func(v *KafkaCluster) pulumi.StringOutput { return v.Size }).(pulumi.StringOutput)
}

// [string] Version of the Kafka Cluster. Possible values: `3.7.0`
func (o KafkaClusterOutput) Version() pulumi.StringOutput {
	return o.ApplyT(func(v *KafkaCluster) pulumi.StringOutput { return v.Version }).(pulumi.StringOutput)
}

type KafkaClusterArrayOutput struct{ *pulumi.OutputState }

func (KafkaClusterArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*KafkaCluster)(nil)).Elem()
}

func (o KafkaClusterArrayOutput) ToKafkaClusterArrayOutput() KafkaClusterArrayOutput {
	return o
}

func (o KafkaClusterArrayOutput) ToKafkaClusterArrayOutputWithContext(ctx context.Context) KafkaClusterArrayOutput {
	return o
}

func (o KafkaClusterArrayOutput) Index(i pulumi.IntInput) KafkaClusterOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *KafkaCluster {
		return vs[0].([]*KafkaCluster)[vs[1].(int)]
	}).(KafkaClusterOutput)
}

type KafkaClusterMapOutput struct{ *pulumi.OutputState }

func (KafkaClusterMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*KafkaCluster)(nil)).Elem()
}

func (o KafkaClusterMapOutput) ToKafkaClusterMapOutput() KafkaClusterMapOutput {
	return o
}

func (o KafkaClusterMapOutput) ToKafkaClusterMapOutputWithContext(ctx context.Context) KafkaClusterMapOutput {
	return o
}

func (o KafkaClusterMapOutput) MapIndex(k pulumi.StringInput) KafkaClusterOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *KafkaCluster {
		return vs[0].(map[string]*KafkaCluster)[vs[1].(string)]
	}).(KafkaClusterOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*KafkaClusterInput)(nil)).Elem(), &KafkaCluster{})
	pulumi.RegisterInputType(reflect.TypeOf((*KafkaClusterArrayInput)(nil)).Elem(), KafkaClusterArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*KafkaClusterMapInput)(nil)).Elem(), KafkaClusterMap{})
	pulumi.RegisterOutputType(KafkaClusterOutput{})
	pulumi.RegisterOutputType(KafkaClusterArrayOutput{})
	pulumi.RegisterOutputType(KafkaClusterMapOutput{})
}
