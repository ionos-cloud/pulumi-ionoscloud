// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package objectstorage

import (
	"context"
	"reflect"

	"errors"
	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Manages Server Side Encryption Configuration for Buckets on IonosCloud.
//
// ## Import
//
// IONOS Object Storage Bucket server side encryption configuration can be imported using the `bucket` name.
//
// ```sh
// $ pulumi import ionoscloud:objectstorage/bucketServerSideEncryptionConfiguration:BucketServerSideEncryptionConfiguration example example
// ```
type BucketServerSideEncryptionConfiguration struct {
	pulumi.CustomResourceState

	// [string] The name of the bucket where the object will be stored.
	Bucket pulumi.StringOutput `pulumi:"bucket"`
	// [block] A block of rule as defined below.
	Rules BucketServerSideEncryptionConfigurationRuleArrayOutput `pulumi:"rules"`
}

// NewBucketServerSideEncryptionConfiguration registers a new resource with the given unique name, arguments, and options.
func NewBucketServerSideEncryptionConfiguration(ctx *pulumi.Context,
	name string, args *BucketServerSideEncryptionConfigurationArgs, opts ...pulumi.ResourceOption) (*BucketServerSideEncryptionConfiguration, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Bucket == nil {
		return nil, errors.New("invalid value for required argument 'Bucket'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource BucketServerSideEncryptionConfiguration
	err := ctx.RegisterResource("ionoscloud:objectstorage/bucketServerSideEncryptionConfiguration:BucketServerSideEncryptionConfiguration", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetBucketServerSideEncryptionConfiguration gets an existing BucketServerSideEncryptionConfiguration resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetBucketServerSideEncryptionConfiguration(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *BucketServerSideEncryptionConfigurationState, opts ...pulumi.ResourceOption) (*BucketServerSideEncryptionConfiguration, error) {
	var resource BucketServerSideEncryptionConfiguration
	err := ctx.ReadResource("ionoscloud:objectstorage/bucketServerSideEncryptionConfiguration:BucketServerSideEncryptionConfiguration", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering BucketServerSideEncryptionConfiguration resources.
type bucketServerSideEncryptionConfigurationState struct {
	// [string] The name of the bucket where the object will be stored.
	Bucket *string `pulumi:"bucket"`
	// [block] A block of rule as defined below.
	Rules []BucketServerSideEncryptionConfigurationRule `pulumi:"rules"`
}

type BucketServerSideEncryptionConfigurationState struct {
	// [string] The name of the bucket where the object will be stored.
	Bucket pulumi.StringPtrInput
	// [block] A block of rule as defined below.
	Rules BucketServerSideEncryptionConfigurationRuleArrayInput
}

func (BucketServerSideEncryptionConfigurationState) ElementType() reflect.Type {
	return reflect.TypeOf((*bucketServerSideEncryptionConfigurationState)(nil)).Elem()
}

type bucketServerSideEncryptionConfigurationArgs struct {
	// [string] The name of the bucket where the object will be stored.
	Bucket string `pulumi:"bucket"`
	// [block] A block of rule as defined below.
	Rules []BucketServerSideEncryptionConfigurationRule `pulumi:"rules"`
}

// The set of arguments for constructing a BucketServerSideEncryptionConfiguration resource.
type BucketServerSideEncryptionConfigurationArgs struct {
	// [string] The name of the bucket where the object will be stored.
	Bucket pulumi.StringInput
	// [block] A block of rule as defined below.
	Rules BucketServerSideEncryptionConfigurationRuleArrayInput
}

func (BucketServerSideEncryptionConfigurationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*bucketServerSideEncryptionConfigurationArgs)(nil)).Elem()
}

type BucketServerSideEncryptionConfigurationInput interface {
	pulumi.Input

	ToBucketServerSideEncryptionConfigurationOutput() BucketServerSideEncryptionConfigurationOutput
	ToBucketServerSideEncryptionConfigurationOutputWithContext(ctx context.Context) BucketServerSideEncryptionConfigurationOutput
}

func (*BucketServerSideEncryptionConfiguration) ElementType() reflect.Type {
	return reflect.TypeOf((**BucketServerSideEncryptionConfiguration)(nil)).Elem()
}

func (i *BucketServerSideEncryptionConfiguration) ToBucketServerSideEncryptionConfigurationOutput() BucketServerSideEncryptionConfigurationOutput {
	return i.ToBucketServerSideEncryptionConfigurationOutputWithContext(context.Background())
}

func (i *BucketServerSideEncryptionConfiguration) ToBucketServerSideEncryptionConfigurationOutputWithContext(ctx context.Context) BucketServerSideEncryptionConfigurationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(BucketServerSideEncryptionConfigurationOutput)
}

// BucketServerSideEncryptionConfigurationArrayInput is an input type that accepts BucketServerSideEncryptionConfigurationArray and BucketServerSideEncryptionConfigurationArrayOutput values.
// You can construct a concrete instance of `BucketServerSideEncryptionConfigurationArrayInput` via:
//
//	BucketServerSideEncryptionConfigurationArray{ BucketServerSideEncryptionConfigurationArgs{...} }
type BucketServerSideEncryptionConfigurationArrayInput interface {
	pulumi.Input

	ToBucketServerSideEncryptionConfigurationArrayOutput() BucketServerSideEncryptionConfigurationArrayOutput
	ToBucketServerSideEncryptionConfigurationArrayOutputWithContext(context.Context) BucketServerSideEncryptionConfigurationArrayOutput
}

type BucketServerSideEncryptionConfigurationArray []BucketServerSideEncryptionConfigurationInput

func (BucketServerSideEncryptionConfigurationArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*BucketServerSideEncryptionConfiguration)(nil)).Elem()
}

func (i BucketServerSideEncryptionConfigurationArray) ToBucketServerSideEncryptionConfigurationArrayOutput() BucketServerSideEncryptionConfigurationArrayOutput {
	return i.ToBucketServerSideEncryptionConfigurationArrayOutputWithContext(context.Background())
}

func (i BucketServerSideEncryptionConfigurationArray) ToBucketServerSideEncryptionConfigurationArrayOutputWithContext(ctx context.Context) BucketServerSideEncryptionConfigurationArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(BucketServerSideEncryptionConfigurationArrayOutput)
}

// BucketServerSideEncryptionConfigurationMapInput is an input type that accepts BucketServerSideEncryptionConfigurationMap and BucketServerSideEncryptionConfigurationMapOutput values.
// You can construct a concrete instance of `BucketServerSideEncryptionConfigurationMapInput` via:
//
//	BucketServerSideEncryptionConfigurationMap{ "key": BucketServerSideEncryptionConfigurationArgs{...} }
type BucketServerSideEncryptionConfigurationMapInput interface {
	pulumi.Input

	ToBucketServerSideEncryptionConfigurationMapOutput() BucketServerSideEncryptionConfigurationMapOutput
	ToBucketServerSideEncryptionConfigurationMapOutputWithContext(context.Context) BucketServerSideEncryptionConfigurationMapOutput
}

type BucketServerSideEncryptionConfigurationMap map[string]BucketServerSideEncryptionConfigurationInput

func (BucketServerSideEncryptionConfigurationMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*BucketServerSideEncryptionConfiguration)(nil)).Elem()
}

func (i BucketServerSideEncryptionConfigurationMap) ToBucketServerSideEncryptionConfigurationMapOutput() BucketServerSideEncryptionConfigurationMapOutput {
	return i.ToBucketServerSideEncryptionConfigurationMapOutputWithContext(context.Background())
}

func (i BucketServerSideEncryptionConfigurationMap) ToBucketServerSideEncryptionConfigurationMapOutputWithContext(ctx context.Context) BucketServerSideEncryptionConfigurationMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(BucketServerSideEncryptionConfigurationMapOutput)
}

type BucketServerSideEncryptionConfigurationOutput struct{ *pulumi.OutputState }

func (BucketServerSideEncryptionConfigurationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**BucketServerSideEncryptionConfiguration)(nil)).Elem()
}

func (o BucketServerSideEncryptionConfigurationOutput) ToBucketServerSideEncryptionConfigurationOutput() BucketServerSideEncryptionConfigurationOutput {
	return o
}

func (o BucketServerSideEncryptionConfigurationOutput) ToBucketServerSideEncryptionConfigurationOutputWithContext(ctx context.Context) BucketServerSideEncryptionConfigurationOutput {
	return o
}

// [string] The name of the bucket where the object will be stored.
func (o BucketServerSideEncryptionConfigurationOutput) Bucket() pulumi.StringOutput {
	return o.ApplyT(func(v *BucketServerSideEncryptionConfiguration) pulumi.StringOutput { return v.Bucket }).(pulumi.StringOutput)
}

// [block] A block of rule as defined below.
func (o BucketServerSideEncryptionConfigurationOutput) Rules() BucketServerSideEncryptionConfigurationRuleArrayOutput {
	return o.ApplyT(func(v *BucketServerSideEncryptionConfiguration) BucketServerSideEncryptionConfigurationRuleArrayOutput {
		return v.Rules
	}).(BucketServerSideEncryptionConfigurationRuleArrayOutput)
}

type BucketServerSideEncryptionConfigurationArrayOutput struct{ *pulumi.OutputState }

func (BucketServerSideEncryptionConfigurationArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*BucketServerSideEncryptionConfiguration)(nil)).Elem()
}

func (o BucketServerSideEncryptionConfigurationArrayOutput) ToBucketServerSideEncryptionConfigurationArrayOutput() BucketServerSideEncryptionConfigurationArrayOutput {
	return o
}

func (o BucketServerSideEncryptionConfigurationArrayOutput) ToBucketServerSideEncryptionConfigurationArrayOutputWithContext(ctx context.Context) BucketServerSideEncryptionConfigurationArrayOutput {
	return o
}

func (o BucketServerSideEncryptionConfigurationArrayOutput) Index(i pulumi.IntInput) BucketServerSideEncryptionConfigurationOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *BucketServerSideEncryptionConfiguration {
		return vs[0].([]*BucketServerSideEncryptionConfiguration)[vs[1].(int)]
	}).(BucketServerSideEncryptionConfigurationOutput)
}

type BucketServerSideEncryptionConfigurationMapOutput struct{ *pulumi.OutputState }

func (BucketServerSideEncryptionConfigurationMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*BucketServerSideEncryptionConfiguration)(nil)).Elem()
}

func (o BucketServerSideEncryptionConfigurationMapOutput) ToBucketServerSideEncryptionConfigurationMapOutput() BucketServerSideEncryptionConfigurationMapOutput {
	return o
}

func (o BucketServerSideEncryptionConfigurationMapOutput) ToBucketServerSideEncryptionConfigurationMapOutputWithContext(ctx context.Context) BucketServerSideEncryptionConfigurationMapOutput {
	return o
}

func (o BucketServerSideEncryptionConfigurationMapOutput) MapIndex(k pulumi.StringInput) BucketServerSideEncryptionConfigurationOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *BucketServerSideEncryptionConfiguration {
		return vs[0].(map[string]*BucketServerSideEncryptionConfiguration)[vs[1].(string)]
	}).(BucketServerSideEncryptionConfigurationOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*BucketServerSideEncryptionConfigurationInput)(nil)).Elem(), &BucketServerSideEncryptionConfiguration{})
	pulumi.RegisterInputType(reflect.TypeOf((*BucketServerSideEncryptionConfigurationArrayInput)(nil)).Elem(), BucketServerSideEncryptionConfigurationArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*BucketServerSideEncryptionConfigurationMapInput)(nil)).Elem(), BucketServerSideEncryptionConfigurationMap{})
	pulumi.RegisterOutputType(BucketServerSideEncryptionConfigurationOutput{})
	pulumi.RegisterOutputType(BucketServerSideEncryptionConfigurationArrayOutput{})
	pulumi.RegisterOutputType(BucketServerSideEncryptionConfigurationMapOutput{})
}
