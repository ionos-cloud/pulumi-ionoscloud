// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ionoscloud

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The provider type for the ionoscloud package. By default, resources use package-wide configuration
// settings, however an explicit `Provider` instance may be created and passed during resource
// construction to achieve fine-grained programmatic control over provider settings. See the
// [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
type Provider struct {
	pulumi.ProviderResourceState

	ContractNumber pulumi.StringPtrOutput `pulumi:"contractNumber"`
	// IonosCloud REST API URL. Usually not necessary to be set, SDKs know internally how to route requests to the API.
	Endpoint pulumi.StringPtrOutput `pulumi:"endpoint"`
	// IonosCloud password for API operations. If token is provided, token is preferred
	Password pulumi.StringPtrOutput `pulumi:"password"`
	// Access key for IONOS Object Storage operations.
	S3AccessKey pulumi.StringPtrOutput `pulumi:"s3AccessKey"`
	// Region for IONOS Object Storage operations.
	S3Region pulumi.StringPtrOutput `pulumi:"s3Region"`
	// Secret key for IONOS Object Storage operations.
	S3SecretKey pulumi.StringPtrOutput `pulumi:"s3SecretKey"`
	// IonosCloud bearer token for API operations.
	Token pulumi.StringPtrOutput `pulumi:"token"`
	// IonosCloud username for API operations. If token is provided, token is preferred
	Username pulumi.StringPtrOutput `pulumi:"username"`
}

// NewProvider registers a new resource with the given unique name, arguments, and options.
func NewProvider(ctx *pulumi.Context,
	name string, args *ProviderArgs, opts ...pulumi.ResourceOption) (*Provider, error) {
	if args == nil {
		args = &ProviderArgs{}
	}

	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Provider
	err := ctx.RegisterResource("pulumi:providers:ionoscloud", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

type providerArgs struct {
	ContractNumber *string `pulumi:"contractNumber"`
	// IonosCloud REST API URL. Usually not necessary to be set, SDKs know internally how to route requests to the API.
	Endpoint *string `pulumi:"endpoint"`
	// IonosCloud password for API operations. If token is provided, token is preferred
	Password *string `pulumi:"password"`
	// Deprecated: Timeout is used instead of this functionality
	Retries *int `pulumi:"retries"`
	// Access key for IONOS Object Storage operations.
	S3AccessKey *string `pulumi:"s3AccessKey"`
	// Region for IONOS Object Storage operations.
	S3Region *string `pulumi:"s3Region"`
	// Secret key for IONOS Object Storage operations.
	S3SecretKey *string `pulumi:"s3SecretKey"`
	// IonosCloud bearer token for API operations.
	Token *string `pulumi:"token"`
	// IonosCloud username for API operations. If token is provided, token is preferred
	Username *string `pulumi:"username"`
}

// The set of arguments for constructing a Provider resource.
type ProviderArgs struct {
	ContractNumber pulumi.StringPtrInput
	// IonosCloud REST API URL. Usually not necessary to be set, SDKs know internally how to route requests to the API.
	Endpoint pulumi.StringPtrInput
	// IonosCloud password for API operations. If token is provided, token is preferred
	Password pulumi.StringPtrInput
	// Deprecated: Timeout is used instead of this functionality
	Retries pulumi.IntPtrInput
	// Access key for IONOS Object Storage operations.
	S3AccessKey pulumi.StringPtrInput
	// Region for IONOS Object Storage operations.
	S3Region pulumi.StringPtrInput
	// Secret key for IONOS Object Storage operations.
	S3SecretKey pulumi.StringPtrInput
	// IonosCloud bearer token for API operations.
	Token pulumi.StringPtrInput
	// IonosCloud username for API operations. If token is provided, token is preferred
	Username pulumi.StringPtrInput
}

func (ProviderArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*providerArgs)(nil)).Elem()
}

type ProviderInput interface {
	pulumi.Input

	ToProviderOutput() ProviderOutput
	ToProviderOutputWithContext(ctx context.Context) ProviderOutput
}

func (*Provider) ElementType() reflect.Type {
	return reflect.TypeOf((**Provider)(nil)).Elem()
}

func (i *Provider) ToProviderOutput() ProviderOutput {
	return i.ToProviderOutputWithContext(context.Background())
}

func (i *Provider) ToProviderOutputWithContext(ctx context.Context) ProviderOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProviderOutput)
}

type ProviderOutput struct{ *pulumi.OutputState }

func (ProviderOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Provider)(nil)).Elem()
}

func (o ProviderOutput) ToProviderOutput() ProviderOutput {
	return o
}

func (o ProviderOutput) ToProviderOutputWithContext(ctx context.Context) ProviderOutput {
	return o
}

func (o ProviderOutput) ContractNumber() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.ContractNumber }).(pulumi.StringPtrOutput)
}

// IonosCloud REST API URL. Usually not necessary to be set, SDKs know internally how to route requests to the API.
func (o ProviderOutput) Endpoint() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.Endpoint }).(pulumi.StringPtrOutput)
}

// IonosCloud password for API operations. If token is provided, token is preferred
func (o ProviderOutput) Password() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.Password }).(pulumi.StringPtrOutput)
}

// Access key for IONOS Object Storage operations.
func (o ProviderOutput) S3AccessKey() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.S3AccessKey }).(pulumi.StringPtrOutput)
}

// Region for IONOS Object Storage operations.
func (o ProviderOutput) S3Region() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.S3Region }).(pulumi.StringPtrOutput)
}

// Secret key for IONOS Object Storage operations.
func (o ProviderOutput) S3SecretKey() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.S3SecretKey }).(pulumi.StringPtrOutput)
}

// IonosCloud bearer token for API operations.
func (o ProviderOutput) Token() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.Token }).(pulumi.StringPtrOutput)
}

// IonosCloud username for API operations. If token is provided, token is preferred
func (o ProviderOutput) Username() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.Username }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ProviderInput)(nil)).Elem(), &Provider{})
	pulumi.RegisterOutputType(ProviderOutput{})
}
