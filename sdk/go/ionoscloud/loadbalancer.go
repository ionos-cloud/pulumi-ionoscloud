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

type Loadbalancer struct {
	pulumi.CustomResourceState

	DatacenterId pulumi.StringOutput      `pulumi:"datacenterId"`
	Dhcp         pulumi.BoolPtrOutput     `pulumi:"dhcp"`
	Ip           pulumi.StringOutput      `pulumi:"ip"`
	Name         pulumi.StringOutput      `pulumi:"name"`
	NicIds       pulumi.StringArrayOutput `pulumi:"nicIds"`
}

// NewLoadbalancer registers a new resource with the given unique name, arguments, and options.
func NewLoadbalancer(ctx *pulumi.Context,
	name string, args *LoadbalancerArgs, opts ...pulumi.ResourceOption) (*Loadbalancer, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DatacenterId == nil {
		return nil, errors.New("invalid value for required argument 'DatacenterId'")
	}
	if args.NicIds == nil {
		return nil, errors.New("invalid value for required argument 'NicIds'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Loadbalancer
	err := ctx.RegisterResource("ionoscloud:index/loadbalancer:Loadbalancer", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetLoadbalancer gets an existing Loadbalancer resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetLoadbalancer(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *LoadbalancerState, opts ...pulumi.ResourceOption) (*Loadbalancer, error) {
	var resource Loadbalancer
	err := ctx.ReadResource("ionoscloud:index/loadbalancer:Loadbalancer", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Loadbalancer resources.
type loadbalancerState struct {
	DatacenterId *string  `pulumi:"datacenterId"`
	Dhcp         *bool    `pulumi:"dhcp"`
	Ip           *string  `pulumi:"ip"`
	Name         *string  `pulumi:"name"`
	NicIds       []string `pulumi:"nicIds"`
}

type LoadbalancerState struct {
	DatacenterId pulumi.StringPtrInput
	Dhcp         pulumi.BoolPtrInput
	Ip           pulumi.StringPtrInput
	Name         pulumi.StringPtrInput
	NicIds       pulumi.StringArrayInput
}

func (LoadbalancerState) ElementType() reflect.Type {
	return reflect.TypeOf((*loadbalancerState)(nil)).Elem()
}

type loadbalancerArgs struct {
	DatacenterId string   `pulumi:"datacenterId"`
	Dhcp         *bool    `pulumi:"dhcp"`
	Ip           *string  `pulumi:"ip"`
	Name         *string  `pulumi:"name"`
	NicIds       []string `pulumi:"nicIds"`
}

// The set of arguments for constructing a Loadbalancer resource.
type LoadbalancerArgs struct {
	DatacenterId pulumi.StringInput
	Dhcp         pulumi.BoolPtrInput
	Ip           pulumi.StringPtrInput
	Name         pulumi.StringPtrInput
	NicIds       pulumi.StringArrayInput
}

func (LoadbalancerArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*loadbalancerArgs)(nil)).Elem()
}

type LoadbalancerInput interface {
	pulumi.Input

	ToLoadbalancerOutput() LoadbalancerOutput
	ToLoadbalancerOutputWithContext(ctx context.Context) LoadbalancerOutput
}

func (*Loadbalancer) ElementType() reflect.Type {
	return reflect.TypeOf((**Loadbalancer)(nil)).Elem()
}

func (i *Loadbalancer) ToLoadbalancerOutput() LoadbalancerOutput {
	return i.ToLoadbalancerOutputWithContext(context.Background())
}

func (i *Loadbalancer) ToLoadbalancerOutputWithContext(ctx context.Context) LoadbalancerOutput {
	return pulumi.ToOutputWithContext(ctx, i).(LoadbalancerOutput)
}

// LoadbalancerArrayInput is an input type that accepts LoadbalancerArray and LoadbalancerArrayOutput values.
// You can construct a concrete instance of `LoadbalancerArrayInput` via:
//
//	LoadbalancerArray{ LoadbalancerArgs{...} }
type LoadbalancerArrayInput interface {
	pulumi.Input

	ToLoadbalancerArrayOutput() LoadbalancerArrayOutput
	ToLoadbalancerArrayOutputWithContext(context.Context) LoadbalancerArrayOutput
}

type LoadbalancerArray []LoadbalancerInput

func (LoadbalancerArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Loadbalancer)(nil)).Elem()
}

func (i LoadbalancerArray) ToLoadbalancerArrayOutput() LoadbalancerArrayOutput {
	return i.ToLoadbalancerArrayOutputWithContext(context.Background())
}

func (i LoadbalancerArray) ToLoadbalancerArrayOutputWithContext(ctx context.Context) LoadbalancerArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(LoadbalancerArrayOutput)
}

// LoadbalancerMapInput is an input type that accepts LoadbalancerMap and LoadbalancerMapOutput values.
// You can construct a concrete instance of `LoadbalancerMapInput` via:
//
//	LoadbalancerMap{ "key": LoadbalancerArgs{...} }
type LoadbalancerMapInput interface {
	pulumi.Input

	ToLoadbalancerMapOutput() LoadbalancerMapOutput
	ToLoadbalancerMapOutputWithContext(context.Context) LoadbalancerMapOutput
}

type LoadbalancerMap map[string]LoadbalancerInput

func (LoadbalancerMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Loadbalancer)(nil)).Elem()
}

func (i LoadbalancerMap) ToLoadbalancerMapOutput() LoadbalancerMapOutput {
	return i.ToLoadbalancerMapOutputWithContext(context.Background())
}

func (i LoadbalancerMap) ToLoadbalancerMapOutputWithContext(ctx context.Context) LoadbalancerMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(LoadbalancerMapOutput)
}

type LoadbalancerOutput struct{ *pulumi.OutputState }

func (LoadbalancerOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Loadbalancer)(nil)).Elem()
}

func (o LoadbalancerOutput) ToLoadbalancerOutput() LoadbalancerOutput {
	return o
}

func (o LoadbalancerOutput) ToLoadbalancerOutputWithContext(ctx context.Context) LoadbalancerOutput {
	return o
}

func (o LoadbalancerOutput) DatacenterId() pulumi.StringOutput {
	return o.ApplyT(func(v *Loadbalancer) pulumi.StringOutput { return v.DatacenterId }).(pulumi.StringOutput)
}

func (o LoadbalancerOutput) Dhcp() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Loadbalancer) pulumi.BoolPtrOutput { return v.Dhcp }).(pulumi.BoolPtrOutput)
}

func (o LoadbalancerOutput) Ip() pulumi.StringOutput {
	return o.ApplyT(func(v *Loadbalancer) pulumi.StringOutput { return v.Ip }).(pulumi.StringOutput)
}

func (o LoadbalancerOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Loadbalancer) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o LoadbalancerOutput) NicIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Loadbalancer) pulumi.StringArrayOutput { return v.NicIds }).(pulumi.StringArrayOutput)
}

type LoadbalancerArrayOutput struct{ *pulumi.OutputState }

func (LoadbalancerArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Loadbalancer)(nil)).Elem()
}

func (o LoadbalancerArrayOutput) ToLoadbalancerArrayOutput() LoadbalancerArrayOutput {
	return o
}

func (o LoadbalancerArrayOutput) ToLoadbalancerArrayOutputWithContext(ctx context.Context) LoadbalancerArrayOutput {
	return o
}

func (o LoadbalancerArrayOutput) Index(i pulumi.IntInput) LoadbalancerOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Loadbalancer {
		return vs[0].([]*Loadbalancer)[vs[1].(int)]
	}).(LoadbalancerOutput)
}

type LoadbalancerMapOutput struct{ *pulumi.OutputState }

func (LoadbalancerMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Loadbalancer)(nil)).Elem()
}

func (o LoadbalancerMapOutput) ToLoadbalancerMapOutput() LoadbalancerMapOutput {
	return o
}

func (o LoadbalancerMapOutput) ToLoadbalancerMapOutputWithContext(ctx context.Context) LoadbalancerMapOutput {
	return o
}

func (o LoadbalancerMapOutput) MapIndex(k pulumi.StringInput) LoadbalancerOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Loadbalancer {
		return vs[0].(map[string]*Loadbalancer)[vs[1].(string)]
	}).(LoadbalancerOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*LoadbalancerInput)(nil)).Elem(), &Loadbalancer{})
	pulumi.RegisterInputType(reflect.TypeOf((*LoadbalancerArrayInput)(nil)).Elem(), LoadbalancerArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*LoadbalancerMapInput)(nil)).Elem(), LoadbalancerMap{})
	pulumi.RegisterOutputType(LoadbalancerOutput{})
	pulumi.RegisterOutputType(LoadbalancerArrayOutput{})
	pulumi.RegisterOutputType(LoadbalancerMapOutput{})
}
