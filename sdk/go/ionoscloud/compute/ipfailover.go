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

type IPFailover struct {
	pulumi.CustomResourceState

	DatacenterId pulumi.StringOutput `pulumi:"datacenterId"`
	// Failover IP
	Ip    pulumi.StringOutput `pulumi:"ip"`
	LanId pulumi.StringOutput `pulumi:"lanId"`
	// The UUID of the master NIC
	Nicuuid pulumi.StringOutput `pulumi:"nicuuid"`
}

// NewIPFailover registers a new resource with the given unique name, arguments, and options.
func NewIPFailover(ctx *pulumi.Context,
	name string, args *IPFailoverArgs, opts ...pulumi.ResourceOption) (*IPFailover, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DatacenterId == nil {
		return nil, errors.New("invalid value for required argument 'DatacenterId'")
	}
	if args.Ip == nil {
		return nil, errors.New("invalid value for required argument 'Ip'")
	}
	if args.LanId == nil {
		return nil, errors.New("invalid value for required argument 'LanId'")
	}
	if args.Nicuuid == nil {
		return nil, errors.New("invalid value for required argument 'Nicuuid'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource IPFailover
	err := ctx.RegisterResource("ionoscloud:compute/iPFailover:IPFailover", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetIPFailover gets an existing IPFailover resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetIPFailover(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *IPFailoverState, opts ...pulumi.ResourceOption) (*IPFailover, error) {
	var resource IPFailover
	err := ctx.ReadResource("ionoscloud:compute/iPFailover:IPFailover", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering IPFailover resources.
type ipfailoverState struct {
	DatacenterId *string `pulumi:"datacenterId"`
	// Failover IP
	Ip    *string `pulumi:"ip"`
	LanId *string `pulumi:"lanId"`
	// The UUID of the master NIC
	Nicuuid *string `pulumi:"nicuuid"`
}

type IPFailoverState struct {
	DatacenterId pulumi.StringPtrInput
	// Failover IP
	Ip    pulumi.StringPtrInput
	LanId pulumi.StringPtrInput
	// The UUID of the master NIC
	Nicuuid pulumi.StringPtrInput
}

func (IPFailoverState) ElementType() reflect.Type {
	return reflect.TypeOf((*ipfailoverState)(nil)).Elem()
}

type ipfailoverArgs struct {
	DatacenterId string `pulumi:"datacenterId"`
	// Failover IP
	Ip    string `pulumi:"ip"`
	LanId string `pulumi:"lanId"`
	// The UUID of the master NIC
	Nicuuid string `pulumi:"nicuuid"`
}

// The set of arguments for constructing a IPFailover resource.
type IPFailoverArgs struct {
	DatacenterId pulumi.StringInput
	// Failover IP
	Ip    pulumi.StringInput
	LanId pulumi.StringInput
	// The UUID of the master NIC
	Nicuuid pulumi.StringInput
}

func (IPFailoverArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ipfailoverArgs)(nil)).Elem()
}

type IPFailoverInput interface {
	pulumi.Input

	ToIPFailoverOutput() IPFailoverOutput
	ToIPFailoverOutputWithContext(ctx context.Context) IPFailoverOutput
}

func (*IPFailover) ElementType() reflect.Type {
	return reflect.TypeOf((**IPFailover)(nil)).Elem()
}

func (i *IPFailover) ToIPFailoverOutput() IPFailoverOutput {
	return i.ToIPFailoverOutputWithContext(context.Background())
}

func (i *IPFailover) ToIPFailoverOutputWithContext(ctx context.Context) IPFailoverOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IPFailoverOutput)
}

// IPFailoverArrayInput is an input type that accepts IPFailoverArray and IPFailoverArrayOutput values.
// You can construct a concrete instance of `IPFailoverArrayInput` via:
//
//	IPFailoverArray{ IPFailoverArgs{...} }
type IPFailoverArrayInput interface {
	pulumi.Input

	ToIPFailoverArrayOutput() IPFailoverArrayOutput
	ToIPFailoverArrayOutputWithContext(context.Context) IPFailoverArrayOutput
}

type IPFailoverArray []IPFailoverInput

func (IPFailoverArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*IPFailover)(nil)).Elem()
}

func (i IPFailoverArray) ToIPFailoverArrayOutput() IPFailoverArrayOutput {
	return i.ToIPFailoverArrayOutputWithContext(context.Background())
}

func (i IPFailoverArray) ToIPFailoverArrayOutputWithContext(ctx context.Context) IPFailoverArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IPFailoverArrayOutput)
}

// IPFailoverMapInput is an input type that accepts IPFailoverMap and IPFailoverMapOutput values.
// You can construct a concrete instance of `IPFailoverMapInput` via:
//
//	IPFailoverMap{ "key": IPFailoverArgs{...} }
type IPFailoverMapInput interface {
	pulumi.Input

	ToIPFailoverMapOutput() IPFailoverMapOutput
	ToIPFailoverMapOutputWithContext(context.Context) IPFailoverMapOutput
}

type IPFailoverMap map[string]IPFailoverInput

func (IPFailoverMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*IPFailover)(nil)).Elem()
}

func (i IPFailoverMap) ToIPFailoverMapOutput() IPFailoverMapOutput {
	return i.ToIPFailoverMapOutputWithContext(context.Background())
}

func (i IPFailoverMap) ToIPFailoverMapOutputWithContext(ctx context.Context) IPFailoverMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IPFailoverMapOutput)
}

type IPFailoverOutput struct{ *pulumi.OutputState }

func (IPFailoverOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**IPFailover)(nil)).Elem()
}

func (o IPFailoverOutput) ToIPFailoverOutput() IPFailoverOutput {
	return o
}

func (o IPFailoverOutput) ToIPFailoverOutputWithContext(ctx context.Context) IPFailoverOutput {
	return o
}

func (o IPFailoverOutput) DatacenterId() pulumi.StringOutput {
	return o.ApplyT(func(v *IPFailover) pulumi.StringOutput { return v.DatacenterId }).(pulumi.StringOutput)
}

// Failover IP
func (o IPFailoverOutput) Ip() pulumi.StringOutput {
	return o.ApplyT(func(v *IPFailover) pulumi.StringOutput { return v.Ip }).(pulumi.StringOutput)
}

func (o IPFailoverOutput) LanId() pulumi.StringOutput {
	return o.ApplyT(func(v *IPFailover) pulumi.StringOutput { return v.LanId }).(pulumi.StringOutput)
}

// The UUID of the master NIC
func (o IPFailoverOutput) Nicuuid() pulumi.StringOutput {
	return o.ApplyT(func(v *IPFailover) pulumi.StringOutput { return v.Nicuuid }).(pulumi.StringOutput)
}

type IPFailoverArrayOutput struct{ *pulumi.OutputState }

func (IPFailoverArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*IPFailover)(nil)).Elem()
}

func (o IPFailoverArrayOutput) ToIPFailoverArrayOutput() IPFailoverArrayOutput {
	return o
}

func (o IPFailoverArrayOutput) ToIPFailoverArrayOutputWithContext(ctx context.Context) IPFailoverArrayOutput {
	return o
}

func (o IPFailoverArrayOutput) Index(i pulumi.IntInput) IPFailoverOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *IPFailover {
		return vs[0].([]*IPFailover)[vs[1].(int)]
	}).(IPFailoverOutput)
}

type IPFailoverMapOutput struct{ *pulumi.OutputState }

func (IPFailoverMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*IPFailover)(nil)).Elem()
}

func (o IPFailoverMapOutput) ToIPFailoverMapOutput() IPFailoverMapOutput {
	return o
}

func (o IPFailoverMapOutput) ToIPFailoverMapOutputWithContext(ctx context.Context) IPFailoverMapOutput {
	return o
}

func (o IPFailoverMapOutput) MapIndex(k pulumi.StringInput) IPFailoverOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *IPFailover {
		return vs[0].(map[string]*IPFailover)[vs[1].(string)]
	}).(IPFailoverOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*IPFailoverInput)(nil)).Elem(), &IPFailover{})
	pulumi.RegisterInputType(reflect.TypeOf((*IPFailoverArrayInput)(nil)).Elem(), IPFailoverArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*IPFailoverMapInput)(nil)).Elem(), IPFailoverMap{})
	pulumi.RegisterOutputType(IPFailoverOutput{})
	pulumi.RegisterOutputType(IPFailoverArrayOutput{})
	pulumi.RegisterOutputType(IPFailoverMapOutput{})
}
