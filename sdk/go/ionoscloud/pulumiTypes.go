// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ionoscloud

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

var _ = internal.GetEnvOrDefault

type ObjectStorageAccesskeyTimeouts struct {
	// [string] Time to wait for the bucket to be created. Default is `10m`.
	Create *string `pulumi:"create"`
	// [string] Time to wait for the bucket to be deleted. Default is `10m`.
	Delete *string `pulumi:"delete"`
	// A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours). Read operations occur during any refresh or planning operation when refresh is enabled.
	Read *string `pulumi:"read"`
}

// ObjectStorageAccesskeyTimeoutsInput is an input type that accepts ObjectStorageAccesskeyTimeoutsArgs and ObjectStorageAccesskeyTimeoutsOutput values.
// You can construct a concrete instance of `ObjectStorageAccesskeyTimeoutsInput` via:
//
//	ObjectStorageAccesskeyTimeoutsArgs{...}
type ObjectStorageAccesskeyTimeoutsInput interface {
	pulumi.Input

	ToObjectStorageAccesskeyTimeoutsOutput() ObjectStorageAccesskeyTimeoutsOutput
	ToObjectStorageAccesskeyTimeoutsOutputWithContext(context.Context) ObjectStorageAccesskeyTimeoutsOutput
}

type ObjectStorageAccesskeyTimeoutsArgs struct {
	// [string] Time to wait for the bucket to be created. Default is `10m`.
	Create pulumi.StringPtrInput `pulumi:"create"`
	// [string] Time to wait for the bucket to be deleted. Default is `10m`.
	Delete pulumi.StringPtrInput `pulumi:"delete"`
	// A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours). Read operations occur during any refresh or planning operation when refresh is enabled.
	Read pulumi.StringPtrInput `pulumi:"read"`
}

func (ObjectStorageAccesskeyTimeoutsArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ObjectStorageAccesskeyTimeouts)(nil)).Elem()
}

func (i ObjectStorageAccesskeyTimeoutsArgs) ToObjectStorageAccesskeyTimeoutsOutput() ObjectStorageAccesskeyTimeoutsOutput {
	return i.ToObjectStorageAccesskeyTimeoutsOutputWithContext(context.Background())
}

func (i ObjectStorageAccesskeyTimeoutsArgs) ToObjectStorageAccesskeyTimeoutsOutputWithContext(ctx context.Context) ObjectStorageAccesskeyTimeoutsOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ObjectStorageAccesskeyTimeoutsOutput)
}

func (i ObjectStorageAccesskeyTimeoutsArgs) ToObjectStorageAccesskeyTimeoutsPtrOutput() ObjectStorageAccesskeyTimeoutsPtrOutput {
	return i.ToObjectStorageAccesskeyTimeoutsPtrOutputWithContext(context.Background())
}

func (i ObjectStorageAccesskeyTimeoutsArgs) ToObjectStorageAccesskeyTimeoutsPtrOutputWithContext(ctx context.Context) ObjectStorageAccesskeyTimeoutsPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ObjectStorageAccesskeyTimeoutsOutput).ToObjectStorageAccesskeyTimeoutsPtrOutputWithContext(ctx)
}

// ObjectStorageAccesskeyTimeoutsPtrInput is an input type that accepts ObjectStorageAccesskeyTimeoutsArgs, ObjectStorageAccesskeyTimeoutsPtr and ObjectStorageAccesskeyTimeoutsPtrOutput values.
// You can construct a concrete instance of `ObjectStorageAccesskeyTimeoutsPtrInput` via:
//
//	        ObjectStorageAccesskeyTimeoutsArgs{...}
//
//	or:
//
//	        nil
type ObjectStorageAccesskeyTimeoutsPtrInput interface {
	pulumi.Input

	ToObjectStorageAccesskeyTimeoutsPtrOutput() ObjectStorageAccesskeyTimeoutsPtrOutput
	ToObjectStorageAccesskeyTimeoutsPtrOutputWithContext(context.Context) ObjectStorageAccesskeyTimeoutsPtrOutput
}

type objectStorageAccesskeyTimeoutsPtrType ObjectStorageAccesskeyTimeoutsArgs

func ObjectStorageAccesskeyTimeoutsPtr(v *ObjectStorageAccesskeyTimeoutsArgs) ObjectStorageAccesskeyTimeoutsPtrInput {
	return (*objectStorageAccesskeyTimeoutsPtrType)(v)
}

func (*objectStorageAccesskeyTimeoutsPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**ObjectStorageAccesskeyTimeouts)(nil)).Elem()
}

func (i *objectStorageAccesskeyTimeoutsPtrType) ToObjectStorageAccesskeyTimeoutsPtrOutput() ObjectStorageAccesskeyTimeoutsPtrOutput {
	return i.ToObjectStorageAccesskeyTimeoutsPtrOutputWithContext(context.Background())
}

func (i *objectStorageAccesskeyTimeoutsPtrType) ToObjectStorageAccesskeyTimeoutsPtrOutputWithContext(ctx context.Context) ObjectStorageAccesskeyTimeoutsPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ObjectStorageAccesskeyTimeoutsPtrOutput)
}

type ObjectStorageAccesskeyTimeoutsOutput struct{ *pulumi.OutputState }

func (ObjectStorageAccesskeyTimeoutsOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ObjectStorageAccesskeyTimeouts)(nil)).Elem()
}

func (o ObjectStorageAccesskeyTimeoutsOutput) ToObjectStorageAccesskeyTimeoutsOutput() ObjectStorageAccesskeyTimeoutsOutput {
	return o
}

func (o ObjectStorageAccesskeyTimeoutsOutput) ToObjectStorageAccesskeyTimeoutsOutputWithContext(ctx context.Context) ObjectStorageAccesskeyTimeoutsOutput {
	return o
}

func (o ObjectStorageAccesskeyTimeoutsOutput) ToObjectStorageAccesskeyTimeoutsPtrOutput() ObjectStorageAccesskeyTimeoutsPtrOutput {
	return o.ToObjectStorageAccesskeyTimeoutsPtrOutputWithContext(context.Background())
}

func (o ObjectStorageAccesskeyTimeoutsOutput) ToObjectStorageAccesskeyTimeoutsPtrOutputWithContext(ctx context.Context) ObjectStorageAccesskeyTimeoutsPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v ObjectStorageAccesskeyTimeouts) *ObjectStorageAccesskeyTimeouts {
		return &v
	}).(ObjectStorageAccesskeyTimeoutsPtrOutput)
}

// [string] Time to wait for the bucket to be created. Default is `10m`.
func (o ObjectStorageAccesskeyTimeoutsOutput) Create() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ObjectStorageAccesskeyTimeouts) *string { return v.Create }).(pulumi.StringPtrOutput)
}

// [string] Time to wait for the bucket to be deleted. Default is `10m`.
func (o ObjectStorageAccesskeyTimeoutsOutput) Delete() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ObjectStorageAccesskeyTimeouts) *string { return v.Delete }).(pulumi.StringPtrOutput)
}

// A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours). Read operations occur during any refresh or planning operation when refresh is enabled.
func (o ObjectStorageAccesskeyTimeoutsOutput) Read() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ObjectStorageAccesskeyTimeouts) *string { return v.Read }).(pulumi.StringPtrOutput)
}

type ObjectStorageAccesskeyTimeoutsPtrOutput struct{ *pulumi.OutputState }

func (ObjectStorageAccesskeyTimeoutsPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ObjectStorageAccesskeyTimeouts)(nil)).Elem()
}

func (o ObjectStorageAccesskeyTimeoutsPtrOutput) ToObjectStorageAccesskeyTimeoutsPtrOutput() ObjectStorageAccesskeyTimeoutsPtrOutput {
	return o
}

func (o ObjectStorageAccesskeyTimeoutsPtrOutput) ToObjectStorageAccesskeyTimeoutsPtrOutputWithContext(ctx context.Context) ObjectStorageAccesskeyTimeoutsPtrOutput {
	return o
}

func (o ObjectStorageAccesskeyTimeoutsPtrOutput) Elem() ObjectStorageAccesskeyTimeoutsOutput {
	return o.ApplyT(func(v *ObjectStorageAccesskeyTimeouts) ObjectStorageAccesskeyTimeouts {
		if v != nil {
			return *v
		}
		var ret ObjectStorageAccesskeyTimeouts
		return ret
	}).(ObjectStorageAccesskeyTimeoutsOutput)
}

// [string] Time to wait for the bucket to be created. Default is `10m`.
func (o ObjectStorageAccesskeyTimeoutsPtrOutput) Create() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ObjectStorageAccesskeyTimeouts) *string {
		if v == nil {
			return nil
		}
		return v.Create
	}).(pulumi.StringPtrOutput)
}

// [string] Time to wait for the bucket to be deleted. Default is `10m`.
func (o ObjectStorageAccesskeyTimeoutsPtrOutput) Delete() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ObjectStorageAccesskeyTimeouts) *string {
		if v == nil {
			return nil
		}
		return v.Delete
	}).(pulumi.StringPtrOutput)
}

// A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours). Read operations occur during any refresh or planning operation when refresh is enabled.
func (o ObjectStorageAccesskeyTimeoutsPtrOutput) Read() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ObjectStorageAccesskeyTimeouts) *string {
		if v == nil {
			return nil
		}
		return v.Read
	}).(pulumi.StringPtrOutput)
}

type GetObjectStorageRegionCapability struct {
	// Indicates if IAM policy based access is supported
	Iam bool `pulumi:"iam"`
	// Indicates if S3 Select is supported
	S3select bool `pulumi:"s3select"`
}

// GetObjectStorageRegionCapabilityInput is an input type that accepts GetObjectStorageRegionCapabilityArgs and GetObjectStorageRegionCapabilityOutput values.
// You can construct a concrete instance of `GetObjectStorageRegionCapabilityInput` via:
//
//	GetObjectStorageRegionCapabilityArgs{...}
type GetObjectStorageRegionCapabilityInput interface {
	pulumi.Input

	ToGetObjectStorageRegionCapabilityOutput() GetObjectStorageRegionCapabilityOutput
	ToGetObjectStorageRegionCapabilityOutputWithContext(context.Context) GetObjectStorageRegionCapabilityOutput
}

type GetObjectStorageRegionCapabilityArgs struct {
	// Indicates if IAM policy based access is supported
	Iam pulumi.BoolInput `pulumi:"iam"`
	// Indicates if S3 Select is supported
	S3select pulumi.BoolInput `pulumi:"s3select"`
}

func (GetObjectStorageRegionCapabilityArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetObjectStorageRegionCapability)(nil)).Elem()
}

func (i GetObjectStorageRegionCapabilityArgs) ToGetObjectStorageRegionCapabilityOutput() GetObjectStorageRegionCapabilityOutput {
	return i.ToGetObjectStorageRegionCapabilityOutputWithContext(context.Background())
}

func (i GetObjectStorageRegionCapabilityArgs) ToGetObjectStorageRegionCapabilityOutputWithContext(ctx context.Context) GetObjectStorageRegionCapabilityOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GetObjectStorageRegionCapabilityOutput)
}

type GetObjectStorageRegionCapabilityOutput struct{ *pulumi.OutputState }

func (GetObjectStorageRegionCapabilityOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetObjectStorageRegionCapability)(nil)).Elem()
}

func (o GetObjectStorageRegionCapabilityOutput) ToGetObjectStorageRegionCapabilityOutput() GetObjectStorageRegionCapabilityOutput {
	return o
}

func (o GetObjectStorageRegionCapabilityOutput) ToGetObjectStorageRegionCapabilityOutputWithContext(ctx context.Context) GetObjectStorageRegionCapabilityOutput {
	return o
}

// Indicates if IAM policy based access is supported
func (o GetObjectStorageRegionCapabilityOutput) Iam() pulumi.BoolOutput {
	return o.ApplyT(func(v GetObjectStorageRegionCapability) bool { return v.Iam }).(pulumi.BoolOutput)
}

// Indicates if S3 Select is supported
func (o GetObjectStorageRegionCapabilityOutput) S3select() pulumi.BoolOutput {
	return o.ApplyT(func(v GetObjectStorageRegionCapability) bool { return v.S3select }).(pulumi.BoolOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ObjectStorageAccesskeyTimeoutsInput)(nil)).Elem(), ObjectStorageAccesskeyTimeoutsArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*ObjectStorageAccesskeyTimeoutsPtrInput)(nil)).Elem(), ObjectStorageAccesskeyTimeoutsArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*GetObjectStorageRegionCapabilityInput)(nil)).Elem(), GetObjectStorageRegionCapabilityArgs{})
	pulumi.RegisterOutputType(ObjectStorageAccesskeyTimeoutsOutput{})
	pulumi.RegisterOutputType(ObjectStorageAccesskeyTimeoutsPtrOutput{})
	pulumi.RegisterOutputType(GetObjectStorageRegionCapabilityOutput{})
}
