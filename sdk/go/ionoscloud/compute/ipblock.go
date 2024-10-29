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

// Manages **IP Blocks** on IonosCloud. IP Blocks contain reserved public IP addresses that can be assigned servers or other resources.
//
// ## Example Usage
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
//			_, err := compute.NewIPBlock(ctx, "example", &compute.IPBlockArgs{
//				Location: pulumi.String("us/las"),
//				Size:     pulumi.Int(1),
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
// Resource Ipblock can be imported using the `resource id`, e.g.
//
// ```sh
// $ pulumi import ionoscloud:compute/iPBlock:IPBlock myipblock {ipblock uuid}
// ```
type IPBlock struct {
	pulumi.CustomResourceState

	// Read-Only attribute. Lists consumption detail of an individual ip
	IpConsumers IPBlockIpConsumerArrayOutput `pulumi:"ipConsumers"`
	// [integer] The list of IP addresses associated with this block.
	Ips pulumi.StringArrayOutput `pulumi:"ips"`
	// [string] The regional location for this IP Block: us/las, us/ewr, de/fra, de/fkb.
	Location pulumi.StringOutput `pulumi:"location"`
	// [string] The name of Ip Block
	Name pulumi.StringOutput `pulumi:"name"`
	// [integer] The number of IP addresses to reserve for this block.
	Size pulumi.IntOutput `pulumi:"size"`
}

// NewIPBlock registers a new resource with the given unique name, arguments, and options.
func NewIPBlock(ctx *pulumi.Context,
	name string, args *IPBlockArgs, opts ...pulumi.ResourceOption) (*IPBlock, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Location == nil {
		return nil, errors.New("invalid value for required argument 'Location'")
	}
	if args.Size == nil {
		return nil, errors.New("invalid value for required argument 'Size'")
	}
	aliases := pulumi.Aliases([]pulumi.Alias{
		{
			Type: pulumi.String("ionoscloud:index/ipblock:Ipblock"),
		},
	})
	opts = append(opts, aliases)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource IPBlock
	err := ctx.RegisterResource("ionoscloud:compute/iPBlock:IPBlock", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetIPBlock gets an existing IPBlock resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetIPBlock(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *IPBlockState, opts ...pulumi.ResourceOption) (*IPBlock, error) {
	var resource IPBlock
	err := ctx.ReadResource("ionoscloud:compute/iPBlock:IPBlock", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering IPBlock resources.
type ipblockState struct {
	// Read-Only attribute. Lists consumption detail of an individual ip
	IpConsumers []IPBlockIpConsumer `pulumi:"ipConsumers"`
	// [integer] The list of IP addresses associated with this block.
	Ips []string `pulumi:"ips"`
	// [string] The regional location for this IP Block: us/las, us/ewr, de/fra, de/fkb.
	Location *string `pulumi:"location"`
	// [string] The name of Ip Block
	Name *string `pulumi:"name"`
	// [integer] The number of IP addresses to reserve for this block.
	Size *int `pulumi:"size"`
}

type IPBlockState struct {
	// Read-Only attribute. Lists consumption detail of an individual ip
	IpConsumers IPBlockIpConsumerArrayInput
	// [integer] The list of IP addresses associated with this block.
	Ips pulumi.StringArrayInput
	// [string] The regional location for this IP Block: us/las, us/ewr, de/fra, de/fkb.
	Location pulumi.StringPtrInput
	// [string] The name of Ip Block
	Name pulumi.StringPtrInput
	// [integer] The number of IP addresses to reserve for this block.
	Size pulumi.IntPtrInput
}

func (IPBlockState) ElementType() reflect.Type {
	return reflect.TypeOf((*ipblockState)(nil)).Elem()
}

type ipblockArgs struct {
	// Read-Only attribute. Lists consumption detail of an individual ip
	IpConsumers []IPBlockIpConsumer `pulumi:"ipConsumers"`
	// [string] The regional location for this IP Block: us/las, us/ewr, de/fra, de/fkb.
	Location string `pulumi:"location"`
	// [string] The name of Ip Block
	Name *string `pulumi:"name"`
	// [integer] The number of IP addresses to reserve for this block.
	Size int `pulumi:"size"`
}

// The set of arguments for constructing a IPBlock resource.
type IPBlockArgs struct {
	// Read-Only attribute. Lists consumption detail of an individual ip
	IpConsumers IPBlockIpConsumerArrayInput
	// [string] The regional location for this IP Block: us/las, us/ewr, de/fra, de/fkb.
	Location pulumi.StringInput
	// [string] The name of Ip Block
	Name pulumi.StringPtrInput
	// [integer] The number of IP addresses to reserve for this block.
	Size pulumi.IntInput
}

func (IPBlockArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ipblockArgs)(nil)).Elem()
}

type IPBlockInput interface {
	pulumi.Input

	ToIPBlockOutput() IPBlockOutput
	ToIPBlockOutputWithContext(ctx context.Context) IPBlockOutput
}

func (*IPBlock) ElementType() reflect.Type {
	return reflect.TypeOf((**IPBlock)(nil)).Elem()
}

func (i *IPBlock) ToIPBlockOutput() IPBlockOutput {
	return i.ToIPBlockOutputWithContext(context.Background())
}

func (i *IPBlock) ToIPBlockOutputWithContext(ctx context.Context) IPBlockOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IPBlockOutput)
}

// IPBlockArrayInput is an input type that accepts IPBlockArray and IPBlockArrayOutput values.
// You can construct a concrete instance of `IPBlockArrayInput` via:
//
//	IPBlockArray{ IPBlockArgs{...} }
type IPBlockArrayInput interface {
	pulumi.Input

	ToIPBlockArrayOutput() IPBlockArrayOutput
	ToIPBlockArrayOutputWithContext(context.Context) IPBlockArrayOutput
}

type IPBlockArray []IPBlockInput

func (IPBlockArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*IPBlock)(nil)).Elem()
}

func (i IPBlockArray) ToIPBlockArrayOutput() IPBlockArrayOutput {
	return i.ToIPBlockArrayOutputWithContext(context.Background())
}

func (i IPBlockArray) ToIPBlockArrayOutputWithContext(ctx context.Context) IPBlockArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IPBlockArrayOutput)
}

// IPBlockMapInput is an input type that accepts IPBlockMap and IPBlockMapOutput values.
// You can construct a concrete instance of `IPBlockMapInput` via:
//
//	IPBlockMap{ "key": IPBlockArgs{...} }
type IPBlockMapInput interface {
	pulumi.Input

	ToIPBlockMapOutput() IPBlockMapOutput
	ToIPBlockMapOutputWithContext(context.Context) IPBlockMapOutput
}

type IPBlockMap map[string]IPBlockInput

func (IPBlockMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*IPBlock)(nil)).Elem()
}

func (i IPBlockMap) ToIPBlockMapOutput() IPBlockMapOutput {
	return i.ToIPBlockMapOutputWithContext(context.Background())
}

func (i IPBlockMap) ToIPBlockMapOutputWithContext(ctx context.Context) IPBlockMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IPBlockMapOutput)
}

type IPBlockOutput struct{ *pulumi.OutputState }

func (IPBlockOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**IPBlock)(nil)).Elem()
}

func (o IPBlockOutput) ToIPBlockOutput() IPBlockOutput {
	return o
}

func (o IPBlockOutput) ToIPBlockOutputWithContext(ctx context.Context) IPBlockOutput {
	return o
}

// Read-Only attribute. Lists consumption detail of an individual ip
func (o IPBlockOutput) IpConsumers() IPBlockIpConsumerArrayOutput {
	return o.ApplyT(func(v *IPBlock) IPBlockIpConsumerArrayOutput { return v.IpConsumers }).(IPBlockIpConsumerArrayOutput)
}

// [integer] The list of IP addresses associated with this block.
func (o IPBlockOutput) Ips() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *IPBlock) pulumi.StringArrayOutput { return v.Ips }).(pulumi.StringArrayOutput)
}

// [string] The regional location for this IP Block: us/las, us/ewr, de/fra, de/fkb.
func (o IPBlockOutput) Location() pulumi.StringOutput {
	return o.ApplyT(func(v *IPBlock) pulumi.StringOutput { return v.Location }).(pulumi.StringOutput)
}

// [string] The name of Ip Block
func (o IPBlockOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *IPBlock) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// [integer] The number of IP addresses to reserve for this block.
func (o IPBlockOutput) Size() pulumi.IntOutput {
	return o.ApplyT(func(v *IPBlock) pulumi.IntOutput { return v.Size }).(pulumi.IntOutput)
}

type IPBlockArrayOutput struct{ *pulumi.OutputState }

func (IPBlockArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*IPBlock)(nil)).Elem()
}

func (o IPBlockArrayOutput) ToIPBlockArrayOutput() IPBlockArrayOutput {
	return o
}

func (o IPBlockArrayOutput) ToIPBlockArrayOutputWithContext(ctx context.Context) IPBlockArrayOutput {
	return o
}

func (o IPBlockArrayOutput) Index(i pulumi.IntInput) IPBlockOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *IPBlock {
		return vs[0].([]*IPBlock)[vs[1].(int)]
	}).(IPBlockOutput)
}

type IPBlockMapOutput struct{ *pulumi.OutputState }

func (IPBlockMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*IPBlock)(nil)).Elem()
}

func (o IPBlockMapOutput) ToIPBlockMapOutput() IPBlockMapOutput {
	return o
}

func (o IPBlockMapOutput) ToIPBlockMapOutputWithContext(ctx context.Context) IPBlockMapOutput {
	return o
}

func (o IPBlockMapOutput) MapIndex(k pulumi.StringInput) IPBlockOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *IPBlock {
		return vs[0].(map[string]*IPBlock)[vs[1].(string)]
	}).(IPBlockOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*IPBlockInput)(nil)).Elem(), &IPBlock{})
	pulumi.RegisterInputType(reflect.TypeOf((*IPBlockArrayInput)(nil)).Elem(), IPBlockArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*IPBlockMapInput)(nil)).Elem(), IPBlockMap{})
	pulumi.RegisterOutputType(IPBlockOutput{})
	pulumi.RegisterOutputType(IPBlockArrayOutput{})
	pulumi.RegisterOutputType(IPBlockMapOutput{})
}
