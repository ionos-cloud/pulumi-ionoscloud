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

// Manages a **Nat Gateway** on IonosCloud.
//
// ## Example Usage
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
//			exampleDatacenter, err := compute.NewDatacenter(ctx, "exampleDatacenter", &compute.DatacenterArgs{
//				Location:          pulumi.String("us/las"),
//				Description:       pulumi.String("Datacenter Description"),
//				SecAuthProtection: pulumi.Bool(false),
//			})
//			if err != nil {
//				return err
//			}
//			exampleIPBlock, err := compute.NewIPBlock(ctx, "exampleIPBlock", &compute.IPBlockArgs{
//				Location: pulumi.String("us/las"),
//				Size:     pulumi.Int(2),
//			})
//			if err != nil {
//				return err
//			}
//			exampleLan, err := compute.NewLan(ctx, "exampleLan", &compute.LanArgs{
//				DatacenterId: exampleDatacenter.ID(),
//				Public:       pulumi.Bool(true),
//			})
//			if err != nil {
//				return err
//			}
//			_, err = ionoscloud.NewNatgateway(ctx, "exampleNatgateway", &ionoscloud.NatgatewayArgs{
//				DatacenterId: exampleDatacenter.ID(),
//				PublicIps: pulumi.StringArray{
//					exampleIPBlock.Ips.ApplyT(func(ips []string) (string, error) {
//						return ips[0], nil
//					}).(pulumi.StringOutput),
//					exampleIPBlock.Ips.ApplyT(func(ips []string) (string, error) {
//						return ips[1], nil
//					}).(pulumi.StringOutput),
//				},
//				Lans: ionoscloud.NatgatewayLanArray{
//					&ionoscloud.NatgatewayLanArgs{
//						Id: exampleLan.ID(),
//						GatewayIps: pulumi.StringArray{
//							pulumi.String("10.11.2.5"),
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
// <!--End PulumiCodeChooser -->
//
// ## Import
//
// A Nat Gateway resource can be imported using its `resource id` and the `datacenter id`, e.g.
//
// ```sh
// $ pulumi import ionoscloud:index/natgateway:Natgateway my_natgateway {datacenter uuid}/{nat gateway uuid}
// ```
type Natgateway struct {
	pulumi.CustomResourceState

	// [string] A Datacenter's UUID.
	DatacenterId pulumi.StringOutput `pulumi:"datacenterId"`
	// [list] A list of Local Area Networks the node pool should be part of.
	Lans NatgatewayLanArrayOutput `pulumi:"lans"`
	// [string] Name of the NAT gateway.
	Name pulumi.StringOutput `pulumi:"name"`
	// [list]Collection of public IP addresses of the NAT gateway. Should be customer reserved IP addresses in that location.
	PublicIps pulumi.StringArrayOutput `pulumi:"publicIps"`
}

// NewNatgateway registers a new resource with the given unique name, arguments, and options.
func NewNatgateway(ctx *pulumi.Context,
	name string, args *NatgatewayArgs, opts ...pulumi.ResourceOption) (*Natgateway, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DatacenterId == nil {
		return nil, errors.New("invalid value for required argument 'DatacenterId'")
	}
	if args.Lans == nil {
		return nil, errors.New("invalid value for required argument 'Lans'")
	}
	if args.PublicIps == nil {
		return nil, errors.New("invalid value for required argument 'PublicIps'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Natgateway
	err := ctx.RegisterResource("ionoscloud:index/natgateway:Natgateway", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetNatgateway gets an existing Natgateway resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetNatgateway(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *NatgatewayState, opts ...pulumi.ResourceOption) (*Natgateway, error) {
	var resource Natgateway
	err := ctx.ReadResource("ionoscloud:index/natgateway:Natgateway", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Natgateway resources.
type natgatewayState struct {
	// [string] A Datacenter's UUID.
	DatacenterId *string `pulumi:"datacenterId"`
	// [list] A list of Local Area Networks the node pool should be part of.
	Lans []NatgatewayLan `pulumi:"lans"`
	// [string] Name of the NAT gateway.
	Name *string `pulumi:"name"`
	// [list]Collection of public IP addresses of the NAT gateway. Should be customer reserved IP addresses in that location.
	PublicIps []string `pulumi:"publicIps"`
}

type NatgatewayState struct {
	// [string] A Datacenter's UUID.
	DatacenterId pulumi.StringPtrInput
	// [list] A list of Local Area Networks the node pool should be part of.
	Lans NatgatewayLanArrayInput
	// [string] Name of the NAT gateway.
	Name pulumi.StringPtrInput
	// [list]Collection of public IP addresses of the NAT gateway. Should be customer reserved IP addresses in that location.
	PublicIps pulumi.StringArrayInput
}

func (NatgatewayState) ElementType() reflect.Type {
	return reflect.TypeOf((*natgatewayState)(nil)).Elem()
}

type natgatewayArgs struct {
	// [string] A Datacenter's UUID.
	DatacenterId string `pulumi:"datacenterId"`
	// [list] A list of Local Area Networks the node pool should be part of.
	Lans []NatgatewayLan `pulumi:"lans"`
	// [string] Name of the NAT gateway.
	Name *string `pulumi:"name"`
	// [list]Collection of public IP addresses of the NAT gateway. Should be customer reserved IP addresses in that location.
	PublicIps []string `pulumi:"publicIps"`
}

// The set of arguments for constructing a Natgateway resource.
type NatgatewayArgs struct {
	// [string] A Datacenter's UUID.
	DatacenterId pulumi.StringInput
	// [list] A list of Local Area Networks the node pool should be part of.
	Lans NatgatewayLanArrayInput
	// [string] Name of the NAT gateway.
	Name pulumi.StringPtrInput
	// [list]Collection of public IP addresses of the NAT gateway. Should be customer reserved IP addresses in that location.
	PublicIps pulumi.StringArrayInput
}

func (NatgatewayArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*natgatewayArgs)(nil)).Elem()
}

type NatgatewayInput interface {
	pulumi.Input

	ToNatgatewayOutput() NatgatewayOutput
	ToNatgatewayOutputWithContext(ctx context.Context) NatgatewayOutput
}

func (*Natgateway) ElementType() reflect.Type {
	return reflect.TypeOf((**Natgateway)(nil)).Elem()
}

func (i *Natgateway) ToNatgatewayOutput() NatgatewayOutput {
	return i.ToNatgatewayOutputWithContext(context.Background())
}

func (i *Natgateway) ToNatgatewayOutputWithContext(ctx context.Context) NatgatewayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NatgatewayOutput)
}

// NatgatewayArrayInput is an input type that accepts NatgatewayArray and NatgatewayArrayOutput values.
// You can construct a concrete instance of `NatgatewayArrayInput` via:
//
//	NatgatewayArray{ NatgatewayArgs{...} }
type NatgatewayArrayInput interface {
	pulumi.Input

	ToNatgatewayArrayOutput() NatgatewayArrayOutput
	ToNatgatewayArrayOutputWithContext(context.Context) NatgatewayArrayOutput
}

type NatgatewayArray []NatgatewayInput

func (NatgatewayArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Natgateway)(nil)).Elem()
}

func (i NatgatewayArray) ToNatgatewayArrayOutput() NatgatewayArrayOutput {
	return i.ToNatgatewayArrayOutputWithContext(context.Background())
}

func (i NatgatewayArray) ToNatgatewayArrayOutputWithContext(ctx context.Context) NatgatewayArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NatgatewayArrayOutput)
}

// NatgatewayMapInput is an input type that accepts NatgatewayMap and NatgatewayMapOutput values.
// You can construct a concrete instance of `NatgatewayMapInput` via:
//
//	NatgatewayMap{ "key": NatgatewayArgs{...} }
type NatgatewayMapInput interface {
	pulumi.Input

	ToNatgatewayMapOutput() NatgatewayMapOutput
	ToNatgatewayMapOutputWithContext(context.Context) NatgatewayMapOutput
}

type NatgatewayMap map[string]NatgatewayInput

func (NatgatewayMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Natgateway)(nil)).Elem()
}

func (i NatgatewayMap) ToNatgatewayMapOutput() NatgatewayMapOutput {
	return i.ToNatgatewayMapOutputWithContext(context.Background())
}

func (i NatgatewayMap) ToNatgatewayMapOutputWithContext(ctx context.Context) NatgatewayMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NatgatewayMapOutput)
}

type NatgatewayOutput struct{ *pulumi.OutputState }

func (NatgatewayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Natgateway)(nil)).Elem()
}

func (o NatgatewayOutput) ToNatgatewayOutput() NatgatewayOutput {
	return o
}

func (o NatgatewayOutput) ToNatgatewayOutputWithContext(ctx context.Context) NatgatewayOutput {
	return o
}

// [string] A Datacenter's UUID.
func (o NatgatewayOutput) DatacenterId() pulumi.StringOutput {
	return o.ApplyT(func(v *Natgateway) pulumi.StringOutput { return v.DatacenterId }).(pulumi.StringOutput)
}

// [list] A list of Local Area Networks the node pool should be part of.
func (o NatgatewayOutput) Lans() NatgatewayLanArrayOutput {
	return o.ApplyT(func(v *Natgateway) NatgatewayLanArrayOutput { return v.Lans }).(NatgatewayLanArrayOutput)
}

// [string] Name of the NAT gateway.
func (o NatgatewayOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Natgateway) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// [list]Collection of public IP addresses of the NAT gateway. Should be customer reserved IP addresses in that location.
func (o NatgatewayOutput) PublicIps() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Natgateway) pulumi.StringArrayOutput { return v.PublicIps }).(pulumi.StringArrayOutput)
}

type NatgatewayArrayOutput struct{ *pulumi.OutputState }

func (NatgatewayArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Natgateway)(nil)).Elem()
}

func (o NatgatewayArrayOutput) ToNatgatewayArrayOutput() NatgatewayArrayOutput {
	return o
}

func (o NatgatewayArrayOutput) ToNatgatewayArrayOutputWithContext(ctx context.Context) NatgatewayArrayOutput {
	return o
}

func (o NatgatewayArrayOutput) Index(i pulumi.IntInput) NatgatewayOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Natgateway {
		return vs[0].([]*Natgateway)[vs[1].(int)]
	}).(NatgatewayOutput)
}

type NatgatewayMapOutput struct{ *pulumi.OutputState }

func (NatgatewayMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Natgateway)(nil)).Elem()
}

func (o NatgatewayMapOutput) ToNatgatewayMapOutput() NatgatewayMapOutput {
	return o
}

func (o NatgatewayMapOutput) ToNatgatewayMapOutputWithContext(ctx context.Context) NatgatewayMapOutput {
	return o
}

func (o NatgatewayMapOutput) MapIndex(k pulumi.StringInput) NatgatewayOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Natgateway {
		return vs[0].(map[string]*Natgateway)[vs[1].(string)]
	}).(NatgatewayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*NatgatewayInput)(nil)).Elem(), &Natgateway{})
	pulumi.RegisterInputType(reflect.TypeOf((*NatgatewayArrayInput)(nil)).Elem(), NatgatewayArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*NatgatewayMapInput)(nil)).Elem(), NatgatewayMap{})
	pulumi.RegisterOutputType(NatgatewayOutput{})
	pulumi.RegisterOutputType(NatgatewayArrayOutput{})
	pulumi.RegisterOutputType(NatgatewayMapOutput{})
}
