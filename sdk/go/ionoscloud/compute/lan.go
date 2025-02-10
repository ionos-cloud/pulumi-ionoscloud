// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"context"
	"reflect"

	"errors"
	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Manages a **LAN** on IonosCloud.
//
// ## Example Usage
//
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
//			example, err := compute.NewDatacenter(ctx, "example", &compute.DatacenterArgs{
//				Name:              pulumi.String("Datacenter Example"),
//				Location:          pulumi.String("us/las"),
//				Description:       pulumi.String("Datacenter Description"),
//				SecAuthProtection: pulumi.Bool(false),
//			})
//			if err != nil {
//				return err
//			}
//			exampleCrossconnect, err := compute.NewCrossconnect(ctx, "example", &compute.CrossconnectArgs{
//				Name:        pulumi.String("Cross Connect Example"),
//				Description: pulumi.String("Cross Connect Description"),
//			})
//			if err != nil {
//				return err
//			}
//			_, err = compute.NewLan(ctx, "example", &compute.LanArgs{
//				DatacenterId: example.ID(),
//				Public:       pulumi.Bool(false),
//				Name:         pulumi.String("Lan Example"),
//				Pcc:          exampleCrossconnect.ID(),
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
// ### With IPv6 Enabled
//
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
//			example, err := compute.NewDatacenter(ctx, "example", &compute.DatacenterArgs{
//				Name:              pulumi.String("Datacenter Example"),
//				Location:          pulumi.String("de/txl"),
//				Description:       pulumi.String("Datacenter Description"),
//				SecAuthProtection: pulumi.Bool(false),
//			})
//			if err != nil {
//				return err
//			}
//			_, err = compute.NewLan(ctx, "example", &compute.LanArgs{
//				DatacenterId:  example.ID(),
//				Public:        pulumi.Bool(true),
//				Name:          pulumi.String("Lan IPv6 Example"),
//				Ipv6CidrBlock: pulumi.String("AUTO"),
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
// ## Important Notes
//
// - Please note that only LANs datacenters found in the same physical location can be connected through a Cross-connect
// - A LAN cannot be a part of two Cross-connects
//
// ## Import
//
// Resource Lan can be imported using the `resource id`, e.g.
//
// ```sh
// $ pulumi import ionoscloud:compute/lan:Lan mylandatacenter uuid/lan id
// ```
type Lan struct {
	pulumi.CustomResourceState

	// [string] The ID of a Virtual Data Center.
	DatacenterId pulumi.StringOutput `pulumi:"datacenterId"`
	// IP failover configurations for lan
	IpFailovers LanIpFailoverArrayOutput `pulumi:"ipFailovers"`
	// [String] For public LANs this property is null, for private LANs it contains the private IPv4 CIDR range. This property is a read only property.
	Ipv4CidrBlock pulumi.StringOutput `pulumi:"ipv4CidrBlock"`
	// Contains the LAN's /64 IPv6 CIDR block if this LAN is IPv6 enabled. 'AUTO' will result in enabling this LAN for IPv6 and automatically assign a /64 IPv6 CIDR block to this LAN. If you specify your own IPv6 CIDR block then you must provide a unique /64 block, which is inside the IPv6 CIDR block of the virtual datacenter and unique inside all LANs from this virtual datacenter.
	Ipv6CidrBlock pulumi.StringOutput `pulumi:"ipv6CidrBlock"`
	// [string] The name of the LAN.
	Name pulumi.StringOutput `pulumi:"name"`
	// [String] The unique id of a `compute.Crossconnect` resource, in order. It needs to be ensured that IP addresses of the NICs of all LANs connected to a given Cross Connect is not duplicated and belongs to the same subnet range
	Pcc pulumi.StringPtrOutput `pulumi:"pcc"`
	// [Boolean] Indicates if the LAN faces the public Internet (true) or not (false).
	Public pulumi.BoolPtrOutput `pulumi:"public"`
}

// NewLan registers a new resource with the given unique name, arguments, and options.
func NewLan(ctx *pulumi.Context,
	name string, args *LanArgs, opts ...pulumi.ResourceOption) (*Lan, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DatacenterId == nil {
		return nil, errors.New("invalid value for required argument 'DatacenterId'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Lan
	err := ctx.RegisterResource("ionoscloud:compute/lan:Lan", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetLan gets an existing Lan resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetLan(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *LanState, opts ...pulumi.ResourceOption) (*Lan, error) {
	var resource Lan
	err := ctx.ReadResource("ionoscloud:compute/lan:Lan", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Lan resources.
type lanState struct {
	// [string] The ID of a Virtual Data Center.
	DatacenterId *string `pulumi:"datacenterId"`
	// IP failover configurations for lan
	IpFailovers []LanIpFailover `pulumi:"ipFailovers"`
	// [String] For public LANs this property is null, for private LANs it contains the private IPv4 CIDR range. This property is a read only property.
	Ipv4CidrBlock *string `pulumi:"ipv4CidrBlock"`
	// Contains the LAN's /64 IPv6 CIDR block if this LAN is IPv6 enabled. 'AUTO' will result in enabling this LAN for IPv6 and automatically assign a /64 IPv6 CIDR block to this LAN. If you specify your own IPv6 CIDR block then you must provide a unique /64 block, which is inside the IPv6 CIDR block of the virtual datacenter and unique inside all LANs from this virtual datacenter.
	Ipv6CidrBlock *string `pulumi:"ipv6CidrBlock"`
	// [string] The name of the LAN.
	Name *string `pulumi:"name"`
	// [String] The unique id of a `compute.Crossconnect` resource, in order. It needs to be ensured that IP addresses of the NICs of all LANs connected to a given Cross Connect is not duplicated and belongs to the same subnet range
	Pcc *string `pulumi:"pcc"`
	// [Boolean] Indicates if the LAN faces the public Internet (true) or not (false).
	Public *bool `pulumi:"public"`
}

type LanState struct {
	// [string] The ID of a Virtual Data Center.
	DatacenterId pulumi.StringPtrInput
	// IP failover configurations for lan
	IpFailovers LanIpFailoverArrayInput
	// [String] For public LANs this property is null, for private LANs it contains the private IPv4 CIDR range. This property is a read only property.
	Ipv4CidrBlock pulumi.StringPtrInput
	// Contains the LAN's /64 IPv6 CIDR block if this LAN is IPv6 enabled. 'AUTO' will result in enabling this LAN for IPv6 and automatically assign a /64 IPv6 CIDR block to this LAN. If you specify your own IPv6 CIDR block then you must provide a unique /64 block, which is inside the IPv6 CIDR block of the virtual datacenter and unique inside all LANs from this virtual datacenter.
	Ipv6CidrBlock pulumi.StringPtrInput
	// [string] The name of the LAN.
	Name pulumi.StringPtrInput
	// [String] The unique id of a `compute.Crossconnect` resource, in order. It needs to be ensured that IP addresses of the NICs of all LANs connected to a given Cross Connect is not duplicated and belongs to the same subnet range
	Pcc pulumi.StringPtrInput
	// [Boolean] Indicates if the LAN faces the public Internet (true) or not (false).
	Public pulumi.BoolPtrInput
}

func (LanState) ElementType() reflect.Type {
	return reflect.TypeOf((*lanState)(nil)).Elem()
}

type lanArgs struct {
	// [string] The ID of a Virtual Data Center.
	DatacenterId string `pulumi:"datacenterId"`
	// IP failover configurations for lan
	IpFailovers []LanIpFailover `pulumi:"ipFailovers"`
	// Contains the LAN's /64 IPv6 CIDR block if this LAN is IPv6 enabled. 'AUTO' will result in enabling this LAN for IPv6 and automatically assign a /64 IPv6 CIDR block to this LAN. If you specify your own IPv6 CIDR block then you must provide a unique /64 block, which is inside the IPv6 CIDR block of the virtual datacenter and unique inside all LANs from this virtual datacenter.
	Ipv6CidrBlock *string `pulumi:"ipv6CidrBlock"`
	// [string] The name of the LAN.
	Name *string `pulumi:"name"`
	// [String] The unique id of a `compute.Crossconnect` resource, in order. It needs to be ensured that IP addresses of the NICs of all LANs connected to a given Cross Connect is not duplicated and belongs to the same subnet range
	Pcc *string `pulumi:"pcc"`
	// [Boolean] Indicates if the LAN faces the public Internet (true) or not (false).
	Public *bool `pulumi:"public"`
}

// The set of arguments for constructing a Lan resource.
type LanArgs struct {
	// [string] The ID of a Virtual Data Center.
	DatacenterId pulumi.StringInput
	// IP failover configurations for lan
	IpFailovers LanIpFailoverArrayInput
	// Contains the LAN's /64 IPv6 CIDR block if this LAN is IPv6 enabled. 'AUTO' will result in enabling this LAN for IPv6 and automatically assign a /64 IPv6 CIDR block to this LAN. If you specify your own IPv6 CIDR block then you must provide a unique /64 block, which is inside the IPv6 CIDR block of the virtual datacenter and unique inside all LANs from this virtual datacenter.
	Ipv6CidrBlock pulumi.StringPtrInput
	// [string] The name of the LAN.
	Name pulumi.StringPtrInput
	// [String] The unique id of a `compute.Crossconnect` resource, in order. It needs to be ensured that IP addresses of the NICs of all LANs connected to a given Cross Connect is not duplicated and belongs to the same subnet range
	Pcc pulumi.StringPtrInput
	// [Boolean] Indicates if the LAN faces the public Internet (true) or not (false).
	Public pulumi.BoolPtrInput
}

func (LanArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*lanArgs)(nil)).Elem()
}

type LanInput interface {
	pulumi.Input

	ToLanOutput() LanOutput
	ToLanOutputWithContext(ctx context.Context) LanOutput
}

func (*Lan) ElementType() reflect.Type {
	return reflect.TypeOf((**Lan)(nil)).Elem()
}

func (i *Lan) ToLanOutput() LanOutput {
	return i.ToLanOutputWithContext(context.Background())
}

func (i *Lan) ToLanOutputWithContext(ctx context.Context) LanOutput {
	return pulumi.ToOutputWithContext(ctx, i).(LanOutput)
}

// LanArrayInput is an input type that accepts LanArray and LanArrayOutput values.
// You can construct a concrete instance of `LanArrayInput` via:
//
//	LanArray{ LanArgs{...} }
type LanArrayInput interface {
	pulumi.Input

	ToLanArrayOutput() LanArrayOutput
	ToLanArrayOutputWithContext(context.Context) LanArrayOutput
}

type LanArray []LanInput

func (LanArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Lan)(nil)).Elem()
}

func (i LanArray) ToLanArrayOutput() LanArrayOutput {
	return i.ToLanArrayOutputWithContext(context.Background())
}

func (i LanArray) ToLanArrayOutputWithContext(ctx context.Context) LanArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(LanArrayOutput)
}

// LanMapInput is an input type that accepts LanMap and LanMapOutput values.
// You can construct a concrete instance of `LanMapInput` via:
//
//	LanMap{ "key": LanArgs{...} }
type LanMapInput interface {
	pulumi.Input

	ToLanMapOutput() LanMapOutput
	ToLanMapOutputWithContext(context.Context) LanMapOutput
}

type LanMap map[string]LanInput

func (LanMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Lan)(nil)).Elem()
}

func (i LanMap) ToLanMapOutput() LanMapOutput {
	return i.ToLanMapOutputWithContext(context.Background())
}

func (i LanMap) ToLanMapOutputWithContext(ctx context.Context) LanMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(LanMapOutput)
}

type LanOutput struct{ *pulumi.OutputState }

func (LanOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Lan)(nil)).Elem()
}

func (o LanOutput) ToLanOutput() LanOutput {
	return o
}

func (o LanOutput) ToLanOutputWithContext(ctx context.Context) LanOutput {
	return o
}

// [string] The ID of a Virtual Data Center.
func (o LanOutput) DatacenterId() pulumi.StringOutput {
	return o.ApplyT(func(v *Lan) pulumi.StringOutput { return v.DatacenterId }).(pulumi.StringOutput)
}

// IP failover configurations for lan
func (o LanOutput) IpFailovers() LanIpFailoverArrayOutput {
	return o.ApplyT(func(v *Lan) LanIpFailoverArrayOutput { return v.IpFailovers }).(LanIpFailoverArrayOutput)
}

// [String] For public LANs this property is null, for private LANs it contains the private IPv4 CIDR range. This property is a read only property.
func (o LanOutput) Ipv4CidrBlock() pulumi.StringOutput {
	return o.ApplyT(func(v *Lan) pulumi.StringOutput { return v.Ipv4CidrBlock }).(pulumi.StringOutput)
}

// Contains the LAN's /64 IPv6 CIDR block if this LAN is IPv6 enabled. 'AUTO' will result in enabling this LAN for IPv6 and automatically assign a /64 IPv6 CIDR block to this LAN. If you specify your own IPv6 CIDR block then you must provide a unique /64 block, which is inside the IPv6 CIDR block of the virtual datacenter and unique inside all LANs from this virtual datacenter.
func (o LanOutput) Ipv6CidrBlock() pulumi.StringOutput {
	return o.ApplyT(func(v *Lan) pulumi.StringOutput { return v.Ipv6CidrBlock }).(pulumi.StringOutput)
}

// [string] The name of the LAN.
func (o LanOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Lan) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// [String] The unique id of a `compute.Crossconnect` resource, in order. It needs to be ensured that IP addresses of the NICs of all LANs connected to a given Cross Connect is not duplicated and belongs to the same subnet range
func (o LanOutput) Pcc() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Lan) pulumi.StringPtrOutput { return v.Pcc }).(pulumi.StringPtrOutput)
}

// [Boolean] Indicates if the LAN faces the public Internet (true) or not (false).
func (o LanOutput) Public() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Lan) pulumi.BoolPtrOutput { return v.Public }).(pulumi.BoolPtrOutput)
}

type LanArrayOutput struct{ *pulumi.OutputState }

func (LanArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Lan)(nil)).Elem()
}

func (o LanArrayOutput) ToLanArrayOutput() LanArrayOutput {
	return o
}

func (o LanArrayOutput) ToLanArrayOutputWithContext(ctx context.Context) LanArrayOutput {
	return o
}

func (o LanArrayOutput) Index(i pulumi.IntInput) LanOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Lan {
		return vs[0].([]*Lan)[vs[1].(int)]
	}).(LanOutput)
}

type LanMapOutput struct{ *pulumi.OutputState }

func (LanMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Lan)(nil)).Elem()
}

func (o LanMapOutput) ToLanMapOutput() LanMapOutput {
	return o
}

func (o LanMapOutput) ToLanMapOutputWithContext(ctx context.Context) LanMapOutput {
	return o
}

func (o LanMapOutput) MapIndex(k pulumi.StringInput) LanOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Lan {
		return vs[0].(map[string]*Lan)[vs[1].(string)]
	}).(LanOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*LanInput)(nil)).Elem(), &Lan{})
	pulumi.RegisterInputType(reflect.TypeOf((*LanArrayInput)(nil)).Elem(), LanArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*LanMapInput)(nil)).Elem(), LanMap{})
	pulumi.RegisterOutputType(LanOutput{})
	pulumi.RegisterOutputType(LanArrayOutput{})
	pulumi.RegisterOutputType(LanMapOutput{})
}
