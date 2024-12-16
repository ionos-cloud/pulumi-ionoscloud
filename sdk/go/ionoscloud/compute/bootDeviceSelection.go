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

type BootDeviceSelection struct {
	pulumi.CustomResourceState

	// ID of the entity to set as primary boot device. Possible boot devices are CDROM Images and Volumes. If omitted, server
	// will boot from PXE
	BootDeviceId pulumi.StringPtrOutput `pulumi:"bootDeviceId"`
	// ID of the Datacenter that holds the server for which the boot volume is selected
	DatacenterId pulumi.StringOutput `pulumi:"datacenterId"`
	// ID of the first attached volume of the Server, which will be the default boot volume.
	DefaultBootVolumeId pulumi.StringOutput `pulumi:"defaultBootVolumeId"`
	// ID of the Server for which the boot device will be selected.
	ServerId pulumi.StringOutput `pulumi:"serverId"`
}

// NewBootDeviceSelection registers a new resource with the given unique name, arguments, and options.
func NewBootDeviceSelection(ctx *pulumi.Context,
	name string, args *BootDeviceSelectionArgs, opts ...pulumi.ResourceOption) (*BootDeviceSelection, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DatacenterId == nil {
		return nil, errors.New("invalid value for required argument 'DatacenterId'")
	}
	if args.ServerId == nil {
		return nil, errors.New("invalid value for required argument 'ServerId'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource BootDeviceSelection
	err := ctx.RegisterResource("ionoscloud:compute/bootDeviceSelection:BootDeviceSelection", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetBootDeviceSelection gets an existing BootDeviceSelection resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetBootDeviceSelection(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *BootDeviceSelectionState, opts ...pulumi.ResourceOption) (*BootDeviceSelection, error) {
	var resource BootDeviceSelection
	err := ctx.ReadResource("ionoscloud:compute/bootDeviceSelection:BootDeviceSelection", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering BootDeviceSelection resources.
type bootDeviceSelectionState struct {
	// ID of the entity to set as primary boot device. Possible boot devices are CDROM Images and Volumes. If omitted, server
	// will boot from PXE
	BootDeviceId *string `pulumi:"bootDeviceId"`
	// ID of the Datacenter that holds the server for which the boot volume is selected
	DatacenterId *string `pulumi:"datacenterId"`
	// ID of the first attached volume of the Server, which will be the default boot volume.
	DefaultBootVolumeId *string `pulumi:"defaultBootVolumeId"`
	// ID of the Server for which the boot device will be selected.
	ServerId *string `pulumi:"serverId"`
}

type BootDeviceSelectionState struct {
	// ID of the entity to set as primary boot device. Possible boot devices are CDROM Images and Volumes. If omitted, server
	// will boot from PXE
	BootDeviceId pulumi.StringPtrInput
	// ID of the Datacenter that holds the server for which the boot volume is selected
	DatacenterId pulumi.StringPtrInput
	// ID of the first attached volume of the Server, which will be the default boot volume.
	DefaultBootVolumeId pulumi.StringPtrInput
	// ID of the Server for which the boot device will be selected.
	ServerId pulumi.StringPtrInput
}

func (BootDeviceSelectionState) ElementType() reflect.Type {
	return reflect.TypeOf((*bootDeviceSelectionState)(nil)).Elem()
}

type bootDeviceSelectionArgs struct {
	// ID of the entity to set as primary boot device. Possible boot devices are CDROM Images and Volumes. If omitted, server
	// will boot from PXE
	BootDeviceId *string `pulumi:"bootDeviceId"`
	// ID of the Datacenter that holds the server for which the boot volume is selected
	DatacenterId string `pulumi:"datacenterId"`
	// ID of the Server for which the boot device will be selected.
	ServerId string `pulumi:"serverId"`
}

// The set of arguments for constructing a BootDeviceSelection resource.
type BootDeviceSelectionArgs struct {
	// ID of the entity to set as primary boot device. Possible boot devices are CDROM Images and Volumes. If omitted, server
	// will boot from PXE
	BootDeviceId pulumi.StringPtrInput
	// ID of the Datacenter that holds the server for which the boot volume is selected
	DatacenterId pulumi.StringInput
	// ID of the Server for which the boot device will be selected.
	ServerId pulumi.StringInput
}

func (BootDeviceSelectionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*bootDeviceSelectionArgs)(nil)).Elem()
}

type BootDeviceSelectionInput interface {
	pulumi.Input

	ToBootDeviceSelectionOutput() BootDeviceSelectionOutput
	ToBootDeviceSelectionOutputWithContext(ctx context.Context) BootDeviceSelectionOutput
}

func (*BootDeviceSelection) ElementType() reflect.Type {
	return reflect.TypeOf((**BootDeviceSelection)(nil)).Elem()
}

func (i *BootDeviceSelection) ToBootDeviceSelectionOutput() BootDeviceSelectionOutput {
	return i.ToBootDeviceSelectionOutputWithContext(context.Background())
}

func (i *BootDeviceSelection) ToBootDeviceSelectionOutputWithContext(ctx context.Context) BootDeviceSelectionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(BootDeviceSelectionOutput)
}

// BootDeviceSelectionArrayInput is an input type that accepts BootDeviceSelectionArray and BootDeviceSelectionArrayOutput values.
// You can construct a concrete instance of `BootDeviceSelectionArrayInput` via:
//
//	BootDeviceSelectionArray{ BootDeviceSelectionArgs{...} }
type BootDeviceSelectionArrayInput interface {
	pulumi.Input

	ToBootDeviceSelectionArrayOutput() BootDeviceSelectionArrayOutput
	ToBootDeviceSelectionArrayOutputWithContext(context.Context) BootDeviceSelectionArrayOutput
}

type BootDeviceSelectionArray []BootDeviceSelectionInput

func (BootDeviceSelectionArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*BootDeviceSelection)(nil)).Elem()
}

func (i BootDeviceSelectionArray) ToBootDeviceSelectionArrayOutput() BootDeviceSelectionArrayOutput {
	return i.ToBootDeviceSelectionArrayOutputWithContext(context.Background())
}

func (i BootDeviceSelectionArray) ToBootDeviceSelectionArrayOutputWithContext(ctx context.Context) BootDeviceSelectionArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(BootDeviceSelectionArrayOutput)
}

// BootDeviceSelectionMapInput is an input type that accepts BootDeviceSelectionMap and BootDeviceSelectionMapOutput values.
// You can construct a concrete instance of `BootDeviceSelectionMapInput` via:
//
//	BootDeviceSelectionMap{ "key": BootDeviceSelectionArgs{...} }
type BootDeviceSelectionMapInput interface {
	pulumi.Input

	ToBootDeviceSelectionMapOutput() BootDeviceSelectionMapOutput
	ToBootDeviceSelectionMapOutputWithContext(context.Context) BootDeviceSelectionMapOutput
}

type BootDeviceSelectionMap map[string]BootDeviceSelectionInput

func (BootDeviceSelectionMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*BootDeviceSelection)(nil)).Elem()
}

func (i BootDeviceSelectionMap) ToBootDeviceSelectionMapOutput() BootDeviceSelectionMapOutput {
	return i.ToBootDeviceSelectionMapOutputWithContext(context.Background())
}

func (i BootDeviceSelectionMap) ToBootDeviceSelectionMapOutputWithContext(ctx context.Context) BootDeviceSelectionMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(BootDeviceSelectionMapOutput)
}

type BootDeviceSelectionOutput struct{ *pulumi.OutputState }

func (BootDeviceSelectionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**BootDeviceSelection)(nil)).Elem()
}

func (o BootDeviceSelectionOutput) ToBootDeviceSelectionOutput() BootDeviceSelectionOutput {
	return o
}

func (o BootDeviceSelectionOutput) ToBootDeviceSelectionOutputWithContext(ctx context.Context) BootDeviceSelectionOutput {
	return o
}

// ID of the entity to set as primary boot device. Possible boot devices are CDROM Images and Volumes. If omitted, server
// will boot from PXE
func (o BootDeviceSelectionOutput) BootDeviceId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *BootDeviceSelection) pulumi.StringPtrOutput { return v.BootDeviceId }).(pulumi.StringPtrOutput)
}

// ID of the Datacenter that holds the server for which the boot volume is selected
func (o BootDeviceSelectionOutput) DatacenterId() pulumi.StringOutput {
	return o.ApplyT(func(v *BootDeviceSelection) pulumi.StringOutput { return v.DatacenterId }).(pulumi.StringOutput)
}

// ID of the first attached volume of the Server, which will be the default boot volume.
func (o BootDeviceSelectionOutput) DefaultBootVolumeId() pulumi.StringOutput {
	return o.ApplyT(func(v *BootDeviceSelection) pulumi.StringOutput { return v.DefaultBootVolumeId }).(pulumi.StringOutput)
}

// ID of the Server for which the boot device will be selected.
func (o BootDeviceSelectionOutput) ServerId() pulumi.StringOutput {
	return o.ApplyT(func(v *BootDeviceSelection) pulumi.StringOutput { return v.ServerId }).(pulumi.StringOutput)
}

type BootDeviceSelectionArrayOutput struct{ *pulumi.OutputState }

func (BootDeviceSelectionArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*BootDeviceSelection)(nil)).Elem()
}

func (o BootDeviceSelectionArrayOutput) ToBootDeviceSelectionArrayOutput() BootDeviceSelectionArrayOutput {
	return o
}

func (o BootDeviceSelectionArrayOutput) ToBootDeviceSelectionArrayOutputWithContext(ctx context.Context) BootDeviceSelectionArrayOutput {
	return o
}

func (o BootDeviceSelectionArrayOutput) Index(i pulumi.IntInput) BootDeviceSelectionOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *BootDeviceSelection {
		return vs[0].([]*BootDeviceSelection)[vs[1].(int)]
	}).(BootDeviceSelectionOutput)
}

type BootDeviceSelectionMapOutput struct{ *pulumi.OutputState }

func (BootDeviceSelectionMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*BootDeviceSelection)(nil)).Elem()
}

func (o BootDeviceSelectionMapOutput) ToBootDeviceSelectionMapOutput() BootDeviceSelectionMapOutput {
	return o
}

func (o BootDeviceSelectionMapOutput) ToBootDeviceSelectionMapOutputWithContext(ctx context.Context) BootDeviceSelectionMapOutput {
	return o
}

func (o BootDeviceSelectionMapOutput) MapIndex(k pulumi.StringInput) BootDeviceSelectionOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *BootDeviceSelection {
		return vs[0].(map[string]*BootDeviceSelection)[vs[1].(string)]
	}).(BootDeviceSelectionOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*BootDeviceSelectionInput)(nil)).Elem(), &BootDeviceSelection{})
	pulumi.RegisterInputType(reflect.TypeOf((*BootDeviceSelectionArrayInput)(nil)).Elem(), BootDeviceSelectionArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*BootDeviceSelectionMapInput)(nil)).Elem(), BootDeviceSelectionMap{})
	pulumi.RegisterOutputType(BootDeviceSelectionOutput{})
	pulumi.RegisterOutputType(BootDeviceSelectionArrayOutput{})
	pulumi.RegisterOutputType(BootDeviceSelectionMapOutput{})
}
