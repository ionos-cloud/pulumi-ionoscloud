// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package dsaas

import (
	"context"
	"reflect"

	"errors"
	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Manages a **Dataplatform Cluster**.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/compute"
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/dsaas"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			example, err := compute.NewDatacenter(ctx, "example", &compute.DatacenterArgs{
//				Name:        pulumi.String("Datacenter_Example"),
//				Location:    pulumi.String("de/txl"),
//				Description: pulumi.String("Datacenter for testing Dataplatform Cluster"),
//			})
//			if err != nil {
//				return err
//			}
//			exampleLan, err := compute.NewLan(ctx, "example", &compute.LanArgs{
//				DatacenterId: example.ID(),
//				Public:       pulumi.Bool(false),
//				Name:         pulumi.String("LAN_Example"),
//			})
//			if err != nil {
//				return err
//			}
//			_, err = dsaas.NewCluster(ctx, "example", &dsaas.ClusterArgs{
//				DatacenterId: example.ID(),
//				Name:         pulumi.String("Dataplatform_Cluster_Example"),
//				MaintenanceWindows: dsaas.ClusterMaintenanceWindowArray{
//					&dsaas.ClusterMaintenanceWindowArgs{
//						DayOfTheWeek: pulumi.String("Sunday"),
//						Time:         pulumi.String("09:00:00"),
//					},
//				},
//				Version: pulumi.String("23.11"),
//				Lans: dsaas.ClusterLanArray{
//					&dsaas.ClusterLanArgs{
//						LanId: exampleLan.ID(),
//						Dhcp:  pulumi.Bool(false),
//						Routes: dsaas.ClusterLanRouteArray{
//							&dsaas.ClusterLanRouteArgs{
//								Network: pulumi.String("182.168.42.1/24"),
//								Gateway: pulumi.String("192.168.42.1"),
//							},
//						},
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
//
// ## Import
//
// Resource Dataplatform Cluster can be imported using the `cluster_id`, e.g.
//
// ```sh
// $ pulumi import ionoscloud:dsaas/cluster:Cluster mycluser cluster uuid
// ```
type Cluster struct {
	pulumi.CustomResourceState

	// [string] The UUID of the virtual data center (VDC) the cluster is provisioned.
	DatacenterId pulumi.StringOutput `pulumi:"datacenterId"`
	// [list] A list of LANs you want this node pool to be part of.
	Lans ClusterLanArrayOutput `pulumi:"lans"`
	// Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
	MaintenanceWindows ClusterMaintenanceWindowArrayOutput `pulumi:"maintenanceWindows"`
	// [string] The name of your cluster. Must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]). It can contain dashes (-), underscores (_), dots (.), and alphanumerics in-between.
	Name pulumi.StringOutput `pulumi:"name"`
	// [int] The version of the Data Platform.
	Version pulumi.StringOutput `pulumi:"version"`
}

// NewCluster registers a new resource with the given unique name, arguments, and options.
func NewCluster(ctx *pulumi.Context,
	name string, args *ClusterArgs, opts ...pulumi.ResourceOption) (*Cluster, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DatacenterId == nil {
		return nil, errors.New("invalid value for required argument 'DatacenterId'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Cluster
	err := ctx.RegisterResource("ionoscloud:dsaas/cluster:Cluster", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCluster gets an existing Cluster resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCluster(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ClusterState, opts ...pulumi.ResourceOption) (*Cluster, error) {
	var resource Cluster
	err := ctx.ReadResource("ionoscloud:dsaas/cluster:Cluster", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Cluster resources.
type clusterState struct {
	// [string] The UUID of the virtual data center (VDC) the cluster is provisioned.
	DatacenterId *string `pulumi:"datacenterId"`
	// [list] A list of LANs you want this node pool to be part of.
	Lans []ClusterLan `pulumi:"lans"`
	// Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
	MaintenanceWindows []ClusterMaintenanceWindow `pulumi:"maintenanceWindows"`
	// [string] The name of your cluster. Must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]). It can contain dashes (-), underscores (_), dots (.), and alphanumerics in-between.
	Name *string `pulumi:"name"`
	// [int] The version of the Data Platform.
	Version *string `pulumi:"version"`
}

type ClusterState struct {
	// [string] The UUID of the virtual data center (VDC) the cluster is provisioned.
	DatacenterId pulumi.StringPtrInput
	// [list] A list of LANs you want this node pool to be part of.
	Lans ClusterLanArrayInput
	// Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
	MaintenanceWindows ClusterMaintenanceWindowArrayInput
	// [string] The name of your cluster. Must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]). It can contain dashes (-), underscores (_), dots (.), and alphanumerics in-between.
	Name pulumi.StringPtrInput
	// [int] The version of the Data Platform.
	Version pulumi.StringPtrInput
}

func (ClusterState) ElementType() reflect.Type {
	return reflect.TypeOf((*clusterState)(nil)).Elem()
}

type clusterArgs struct {
	// [string] The UUID of the virtual data center (VDC) the cluster is provisioned.
	DatacenterId string `pulumi:"datacenterId"`
	// [list] A list of LANs you want this node pool to be part of.
	Lans []ClusterLan `pulumi:"lans"`
	// Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
	MaintenanceWindows []ClusterMaintenanceWindow `pulumi:"maintenanceWindows"`
	// [string] The name of your cluster. Must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]). It can contain dashes (-), underscores (_), dots (.), and alphanumerics in-between.
	Name *string `pulumi:"name"`
	// [int] The version of the Data Platform.
	Version *string `pulumi:"version"`
}

// The set of arguments for constructing a Cluster resource.
type ClusterArgs struct {
	// [string] The UUID of the virtual data center (VDC) the cluster is provisioned.
	DatacenterId pulumi.StringInput
	// [list] A list of LANs you want this node pool to be part of.
	Lans ClusterLanArrayInput
	// Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
	MaintenanceWindows ClusterMaintenanceWindowArrayInput
	// [string] The name of your cluster. Must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]). It can contain dashes (-), underscores (_), dots (.), and alphanumerics in-between.
	Name pulumi.StringPtrInput
	// [int] The version of the Data Platform.
	Version pulumi.StringPtrInput
}

func (ClusterArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*clusterArgs)(nil)).Elem()
}

type ClusterInput interface {
	pulumi.Input

	ToClusterOutput() ClusterOutput
	ToClusterOutputWithContext(ctx context.Context) ClusterOutput
}

func (*Cluster) ElementType() reflect.Type {
	return reflect.TypeOf((**Cluster)(nil)).Elem()
}

func (i *Cluster) ToClusterOutput() ClusterOutput {
	return i.ToClusterOutputWithContext(context.Background())
}

func (i *Cluster) ToClusterOutputWithContext(ctx context.Context) ClusterOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ClusterOutput)
}

// ClusterArrayInput is an input type that accepts ClusterArray and ClusterArrayOutput values.
// You can construct a concrete instance of `ClusterArrayInput` via:
//
//	ClusterArray{ ClusterArgs{...} }
type ClusterArrayInput interface {
	pulumi.Input

	ToClusterArrayOutput() ClusterArrayOutput
	ToClusterArrayOutputWithContext(context.Context) ClusterArrayOutput
}

type ClusterArray []ClusterInput

func (ClusterArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Cluster)(nil)).Elem()
}

func (i ClusterArray) ToClusterArrayOutput() ClusterArrayOutput {
	return i.ToClusterArrayOutputWithContext(context.Background())
}

func (i ClusterArray) ToClusterArrayOutputWithContext(ctx context.Context) ClusterArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ClusterArrayOutput)
}

// ClusterMapInput is an input type that accepts ClusterMap and ClusterMapOutput values.
// You can construct a concrete instance of `ClusterMapInput` via:
//
//	ClusterMap{ "key": ClusterArgs{...} }
type ClusterMapInput interface {
	pulumi.Input

	ToClusterMapOutput() ClusterMapOutput
	ToClusterMapOutputWithContext(context.Context) ClusterMapOutput
}

type ClusterMap map[string]ClusterInput

func (ClusterMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Cluster)(nil)).Elem()
}

func (i ClusterMap) ToClusterMapOutput() ClusterMapOutput {
	return i.ToClusterMapOutputWithContext(context.Background())
}

func (i ClusterMap) ToClusterMapOutputWithContext(ctx context.Context) ClusterMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ClusterMapOutput)
}

type ClusterOutput struct{ *pulumi.OutputState }

func (ClusterOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Cluster)(nil)).Elem()
}

func (o ClusterOutput) ToClusterOutput() ClusterOutput {
	return o
}

func (o ClusterOutput) ToClusterOutputWithContext(ctx context.Context) ClusterOutput {
	return o
}

// [string] The UUID of the virtual data center (VDC) the cluster is provisioned.
func (o ClusterOutput) DatacenterId() pulumi.StringOutput {
	return o.ApplyT(func(v *Cluster) pulumi.StringOutput { return v.DatacenterId }).(pulumi.StringOutput)
}

// [list] A list of LANs you want this node pool to be part of.
func (o ClusterOutput) Lans() ClusterLanArrayOutput {
	return o.ApplyT(func(v *Cluster) ClusterLanArrayOutput { return v.Lans }).(ClusterLanArrayOutput)
}

// Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
func (o ClusterOutput) MaintenanceWindows() ClusterMaintenanceWindowArrayOutput {
	return o.ApplyT(func(v *Cluster) ClusterMaintenanceWindowArrayOutput { return v.MaintenanceWindows }).(ClusterMaintenanceWindowArrayOutput)
}

// [string] The name of your cluster. Must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]). It can contain dashes (-), underscores (_), dots (.), and alphanumerics in-between.
func (o ClusterOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Cluster) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// [int] The version of the Data Platform.
func (o ClusterOutput) Version() pulumi.StringOutput {
	return o.ApplyT(func(v *Cluster) pulumi.StringOutput { return v.Version }).(pulumi.StringOutput)
}

type ClusterArrayOutput struct{ *pulumi.OutputState }

func (ClusterArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Cluster)(nil)).Elem()
}

func (o ClusterArrayOutput) ToClusterArrayOutput() ClusterArrayOutput {
	return o
}

func (o ClusterArrayOutput) ToClusterArrayOutputWithContext(ctx context.Context) ClusterArrayOutput {
	return o
}

func (o ClusterArrayOutput) Index(i pulumi.IntInput) ClusterOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Cluster {
		return vs[0].([]*Cluster)[vs[1].(int)]
	}).(ClusterOutput)
}

type ClusterMapOutput struct{ *pulumi.OutputState }

func (ClusterMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Cluster)(nil)).Elem()
}

func (o ClusterMapOutput) ToClusterMapOutput() ClusterMapOutput {
	return o
}

func (o ClusterMapOutput) ToClusterMapOutputWithContext(ctx context.Context) ClusterMapOutput {
	return o
}

func (o ClusterMapOutput) MapIndex(k pulumi.StringInput) ClusterOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Cluster {
		return vs[0].(map[string]*Cluster)[vs[1].(string)]
	}).(ClusterOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ClusterInput)(nil)).Elem(), &Cluster{})
	pulumi.RegisterInputType(reflect.TypeOf((*ClusterArrayInput)(nil)).Elem(), ClusterArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ClusterMapInput)(nil)).Elem(), ClusterMap{})
	pulumi.RegisterOutputType(ClusterOutput{})
	pulumi.RegisterOutputType(ClusterArrayOutput{})
	pulumi.RegisterOutputType(ClusterMapOutput{})
}
