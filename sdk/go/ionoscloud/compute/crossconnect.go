// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Manages a **Cross Connect** on IonosCloud.
// Cross Connect allows you to connect virtual data centers (VDC) with each other using a private LAN.
// The VDCs to be connected need to belong to the same IONOS Cloud contract and location.
// You can only use private LANs for a Cross Connect connection. A LAN can only be a part of one Cross Connect.
//
// The IP addresses of the NICs used for the Cross Connect connection may not be used in more than one NIC and they need to belong to the same IP range.
//
// ## Example Usage
//
// To connect two datacenters we need 2 lans defined, one in each datacenter. After, we reference the cross-connect through which we want the connection to be established.
//
// <!--Start PulumiCodeChooser -->
// ```go
// package main
//
// import (
//
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/compute"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			crossConnectTestResource, err := compute.NewCrossconnect(ctx, "crossConnectTestResource", &compute.CrossconnectArgs{
//				Description: pulumi.String("CrossConnectTestResource"),
//			})
//			if err != nil {
//				return err
//			}
//			dc1, err := compute.NewDatacenter(ctx, "dc1", &compute.DatacenterArgs{
//				Location: pulumi.String("de/txl"),
//			})
//			if err != nil {
//				return err
//			}
//			dc2, err := compute.NewDatacenter(ctx, "dc2", &compute.DatacenterArgs{
//				Location: pulumi.String("de/txl"),
//			})
//			if err != nil {
//				return err
//			}
//			_, err = compute.NewLan(ctx, "dc1lan", &compute.LanArgs{
//				DatacenterId: dc1.ID(),
//				Public:       pulumi.Bool(false),
//				Pcc:          crossConnectTestResource.ID(),
//			})
//			if err != nil {
//				return err
//			}
//			_, err = compute.NewLan(ctx, "dc2lan", &compute.LanArgs{
//				DatacenterId: dc2.ID(),
//				Public:       pulumi.Bool(false),
//				Pcc:          crossConnectTestResource.ID(),
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
// A Cross Connect resource can be imported using its `resource id`, e.g.
//
// ```sh
// $ pulumi import ionoscloud:compute/crossconnect:Crossconnect demo {ionoscloud_private_crossconnect_uuid}
// ```
//
// This can be helpful when you want to import cross-connects which you have already created manually or using other means, outside of terraform.
type Crossconnect struct {
	pulumi.CustomResourceState

	// A list containing all the connectable datacenters
	ConnectableDatacenters CrossconnectConnectableDatacenterArrayOutput `pulumi:"connectableDatacenters"`
	// [string] A short description for the cross-connection.
	// - `connectable datacenters` - (Computed) A list containing all the connectable datacenters
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The name of the connectable datacenter
	Name pulumi.StringOutput `pulumi:"name"`
	// Lists LAN's joined to this cross connect
	Peers CrossconnectPeerArrayOutput `pulumi:"peers"`
}

// NewCrossconnect registers a new resource with the given unique name, arguments, and options.
func NewCrossconnect(ctx *pulumi.Context,
	name string, args *CrossconnectArgs, opts ...pulumi.ResourceOption) (*Crossconnect, error) {
	if args == nil {
		args = &CrossconnectArgs{}
	}

	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Crossconnect
	err := ctx.RegisterResource("ionoscloud:compute/crossconnect:Crossconnect", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCrossconnect gets an existing Crossconnect resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCrossconnect(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CrossconnectState, opts ...pulumi.ResourceOption) (*Crossconnect, error) {
	var resource Crossconnect
	err := ctx.ReadResource("ionoscloud:compute/crossconnect:Crossconnect", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Crossconnect resources.
type crossconnectState struct {
	// A list containing all the connectable datacenters
	ConnectableDatacenters []CrossconnectConnectableDatacenter `pulumi:"connectableDatacenters"`
	// [string] A short description for the cross-connection.
	// - `connectable datacenters` - (Computed) A list containing all the connectable datacenters
	Description *string `pulumi:"description"`
	// The name of the connectable datacenter
	Name *string `pulumi:"name"`
	// Lists LAN's joined to this cross connect
	Peers []CrossconnectPeer `pulumi:"peers"`
}

type CrossconnectState struct {
	// A list containing all the connectable datacenters
	ConnectableDatacenters CrossconnectConnectableDatacenterArrayInput
	// [string] A short description for the cross-connection.
	// - `connectable datacenters` - (Computed) A list containing all the connectable datacenters
	Description pulumi.StringPtrInput
	// The name of the connectable datacenter
	Name pulumi.StringPtrInput
	// Lists LAN's joined to this cross connect
	Peers CrossconnectPeerArrayInput
}

func (CrossconnectState) ElementType() reflect.Type {
	return reflect.TypeOf((*crossconnectState)(nil)).Elem()
}

type crossconnectArgs struct {
	// A list containing all the connectable datacenters
	ConnectableDatacenters []CrossconnectConnectableDatacenter `pulumi:"connectableDatacenters"`
	// [string] A short description for the cross-connection.
	// - `connectable datacenters` - (Computed) A list containing all the connectable datacenters
	Description *string `pulumi:"description"`
	// The name of the connectable datacenter
	Name *string `pulumi:"name"`
	// Lists LAN's joined to this cross connect
	Peers []CrossconnectPeer `pulumi:"peers"`
}

// The set of arguments for constructing a Crossconnect resource.
type CrossconnectArgs struct {
	// A list containing all the connectable datacenters
	ConnectableDatacenters CrossconnectConnectableDatacenterArrayInput
	// [string] A short description for the cross-connection.
	// - `connectable datacenters` - (Computed) A list containing all the connectable datacenters
	Description pulumi.StringPtrInput
	// The name of the connectable datacenter
	Name pulumi.StringPtrInput
	// Lists LAN's joined to this cross connect
	Peers CrossconnectPeerArrayInput
}

func (CrossconnectArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*crossconnectArgs)(nil)).Elem()
}

type CrossconnectInput interface {
	pulumi.Input

	ToCrossconnectOutput() CrossconnectOutput
	ToCrossconnectOutputWithContext(ctx context.Context) CrossconnectOutput
}

func (*Crossconnect) ElementType() reflect.Type {
	return reflect.TypeOf((**Crossconnect)(nil)).Elem()
}

func (i *Crossconnect) ToCrossconnectOutput() CrossconnectOutput {
	return i.ToCrossconnectOutputWithContext(context.Background())
}

func (i *Crossconnect) ToCrossconnectOutputWithContext(ctx context.Context) CrossconnectOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CrossconnectOutput)
}

// CrossconnectArrayInput is an input type that accepts CrossconnectArray and CrossconnectArrayOutput values.
// You can construct a concrete instance of `CrossconnectArrayInput` via:
//
//	CrossconnectArray{ CrossconnectArgs{...} }
type CrossconnectArrayInput interface {
	pulumi.Input

	ToCrossconnectArrayOutput() CrossconnectArrayOutput
	ToCrossconnectArrayOutputWithContext(context.Context) CrossconnectArrayOutput
}

type CrossconnectArray []CrossconnectInput

func (CrossconnectArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Crossconnect)(nil)).Elem()
}

func (i CrossconnectArray) ToCrossconnectArrayOutput() CrossconnectArrayOutput {
	return i.ToCrossconnectArrayOutputWithContext(context.Background())
}

func (i CrossconnectArray) ToCrossconnectArrayOutputWithContext(ctx context.Context) CrossconnectArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CrossconnectArrayOutput)
}

// CrossconnectMapInput is an input type that accepts CrossconnectMap and CrossconnectMapOutput values.
// You can construct a concrete instance of `CrossconnectMapInput` via:
//
//	CrossconnectMap{ "key": CrossconnectArgs{...} }
type CrossconnectMapInput interface {
	pulumi.Input

	ToCrossconnectMapOutput() CrossconnectMapOutput
	ToCrossconnectMapOutputWithContext(context.Context) CrossconnectMapOutput
}

type CrossconnectMap map[string]CrossconnectInput

func (CrossconnectMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Crossconnect)(nil)).Elem()
}

func (i CrossconnectMap) ToCrossconnectMapOutput() CrossconnectMapOutput {
	return i.ToCrossconnectMapOutputWithContext(context.Background())
}

func (i CrossconnectMap) ToCrossconnectMapOutputWithContext(ctx context.Context) CrossconnectMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CrossconnectMapOutput)
}

type CrossconnectOutput struct{ *pulumi.OutputState }

func (CrossconnectOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Crossconnect)(nil)).Elem()
}

func (o CrossconnectOutput) ToCrossconnectOutput() CrossconnectOutput {
	return o
}

func (o CrossconnectOutput) ToCrossconnectOutputWithContext(ctx context.Context) CrossconnectOutput {
	return o
}

// A list containing all the connectable datacenters
func (o CrossconnectOutput) ConnectableDatacenters() CrossconnectConnectableDatacenterArrayOutput {
	return o.ApplyT(func(v *Crossconnect) CrossconnectConnectableDatacenterArrayOutput { return v.ConnectableDatacenters }).(CrossconnectConnectableDatacenterArrayOutput)
}

// [string] A short description for the cross-connection.
// - `connectable datacenters` - (Computed) A list containing all the connectable datacenters
func (o CrossconnectOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Crossconnect) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// The name of the connectable datacenter
func (o CrossconnectOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Crossconnect) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// Lists LAN's joined to this cross connect
func (o CrossconnectOutput) Peers() CrossconnectPeerArrayOutput {
	return o.ApplyT(func(v *Crossconnect) CrossconnectPeerArrayOutput { return v.Peers }).(CrossconnectPeerArrayOutput)
}

type CrossconnectArrayOutput struct{ *pulumi.OutputState }

func (CrossconnectArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Crossconnect)(nil)).Elem()
}

func (o CrossconnectArrayOutput) ToCrossconnectArrayOutput() CrossconnectArrayOutput {
	return o
}

func (o CrossconnectArrayOutput) ToCrossconnectArrayOutputWithContext(ctx context.Context) CrossconnectArrayOutput {
	return o
}

func (o CrossconnectArrayOutput) Index(i pulumi.IntInput) CrossconnectOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Crossconnect {
		return vs[0].([]*Crossconnect)[vs[1].(int)]
	}).(CrossconnectOutput)
}

type CrossconnectMapOutput struct{ *pulumi.OutputState }

func (CrossconnectMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Crossconnect)(nil)).Elem()
}

func (o CrossconnectMapOutput) ToCrossconnectMapOutput() CrossconnectMapOutput {
	return o
}

func (o CrossconnectMapOutput) ToCrossconnectMapOutputWithContext(ctx context.Context) CrossconnectMapOutput {
	return o
}

func (o CrossconnectMapOutput) MapIndex(k pulumi.StringInput) CrossconnectOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Crossconnect {
		return vs[0].(map[string]*Crossconnect)[vs[1].(string)]
	}).(CrossconnectOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*CrossconnectInput)(nil)).Elem(), &Crossconnect{})
	pulumi.RegisterInputType(reflect.TypeOf((*CrossconnectArrayInput)(nil)).Elem(), CrossconnectArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*CrossconnectMapInput)(nil)).Elem(), CrossconnectMap{})
	pulumi.RegisterOutputType(CrossconnectOutput{})
	pulumi.RegisterOutputType(CrossconnectArrayOutput{})
	pulumi.RegisterOutputType(CrossconnectMapOutput{})
}
