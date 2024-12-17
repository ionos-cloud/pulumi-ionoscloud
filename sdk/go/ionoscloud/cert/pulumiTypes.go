// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cert

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

var _ = internal.GetEnvOrDefault

type AutoCertificateProviderExternalAccountBinding struct {
	// The key ID of the external account binding
	KeyId string `pulumi:"keyId"`
	// The secret of the external account binding
	KeySecret string `pulumi:"keySecret"`
}

// AutoCertificateProviderExternalAccountBindingInput is an input type that accepts AutoCertificateProviderExternalAccountBindingArgs and AutoCertificateProviderExternalAccountBindingOutput values.
// You can construct a concrete instance of `AutoCertificateProviderExternalAccountBindingInput` via:
//
//	AutoCertificateProviderExternalAccountBindingArgs{...}
type AutoCertificateProviderExternalAccountBindingInput interface {
	pulumi.Input

	ToAutoCertificateProviderExternalAccountBindingOutput() AutoCertificateProviderExternalAccountBindingOutput
	ToAutoCertificateProviderExternalAccountBindingOutputWithContext(context.Context) AutoCertificateProviderExternalAccountBindingOutput
}

type AutoCertificateProviderExternalAccountBindingArgs struct {
	// The key ID of the external account binding
	KeyId pulumi.StringInput `pulumi:"keyId"`
	// The secret of the external account binding
	KeySecret pulumi.StringInput `pulumi:"keySecret"`
}

func (AutoCertificateProviderExternalAccountBindingArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*AutoCertificateProviderExternalAccountBinding)(nil)).Elem()
}

func (i AutoCertificateProviderExternalAccountBindingArgs) ToAutoCertificateProviderExternalAccountBindingOutput() AutoCertificateProviderExternalAccountBindingOutput {
	return i.ToAutoCertificateProviderExternalAccountBindingOutputWithContext(context.Background())
}

func (i AutoCertificateProviderExternalAccountBindingArgs) ToAutoCertificateProviderExternalAccountBindingOutputWithContext(ctx context.Context) AutoCertificateProviderExternalAccountBindingOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AutoCertificateProviderExternalAccountBindingOutput)
}

func (i AutoCertificateProviderExternalAccountBindingArgs) ToAutoCertificateProviderExternalAccountBindingPtrOutput() AutoCertificateProviderExternalAccountBindingPtrOutput {
	return i.ToAutoCertificateProviderExternalAccountBindingPtrOutputWithContext(context.Background())
}

func (i AutoCertificateProviderExternalAccountBindingArgs) ToAutoCertificateProviderExternalAccountBindingPtrOutputWithContext(ctx context.Context) AutoCertificateProviderExternalAccountBindingPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AutoCertificateProviderExternalAccountBindingOutput).ToAutoCertificateProviderExternalAccountBindingPtrOutputWithContext(ctx)
}

// AutoCertificateProviderExternalAccountBindingPtrInput is an input type that accepts AutoCertificateProviderExternalAccountBindingArgs, AutoCertificateProviderExternalAccountBindingPtr and AutoCertificateProviderExternalAccountBindingPtrOutput values.
// You can construct a concrete instance of `AutoCertificateProviderExternalAccountBindingPtrInput` via:
//
//	        AutoCertificateProviderExternalAccountBindingArgs{...}
//
//	or:
//
//	        nil
type AutoCertificateProviderExternalAccountBindingPtrInput interface {
	pulumi.Input

	ToAutoCertificateProviderExternalAccountBindingPtrOutput() AutoCertificateProviderExternalAccountBindingPtrOutput
	ToAutoCertificateProviderExternalAccountBindingPtrOutputWithContext(context.Context) AutoCertificateProviderExternalAccountBindingPtrOutput
}

type autoCertificateProviderExternalAccountBindingPtrType AutoCertificateProviderExternalAccountBindingArgs

func AutoCertificateProviderExternalAccountBindingPtr(v *AutoCertificateProviderExternalAccountBindingArgs) AutoCertificateProviderExternalAccountBindingPtrInput {
	return (*autoCertificateProviderExternalAccountBindingPtrType)(v)
}

func (*autoCertificateProviderExternalAccountBindingPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**AutoCertificateProviderExternalAccountBinding)(nil)).Elem()
}

func (i *autoCertificateProviderExternalAccountBindingPtrType) ToAutoCertificateProviderExternalAccountBindingPtrOutput() AutoCertificateProviderExternalAccountBindingPtrOutput {
	return i.ToAutoCertificateProviderExternalAccountBindingPtrOutputWithContext(context.Background())
}

func (i *autoCertificateProviderExternalAccountBindingPtrType) ToAutoCertificateProviderExternalAccountBindingPtrOutputWithContext(ctx context.Context) AutoCertificateProviderExternalAccountBindingPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AutoCertificateProviderExternalAccountBindingPtrOutput)
}

type AutoCertificateProviderExternalAccountBindingOutput struct{ *pulumi.OutputState }

func (AutoCertificateProviderExternalAccountBindingOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AutoCertificateProviderExternalAccountBinding)(nil)).Elem()
}

func (o AutoCertificateProviderExternalAccountBindingOutput) ToAutoCertificateProviderExternalAccountBindingOutput() AutoCertificateProviderExternalAccountBindingOutput {
	return o
}

func (o AutoCertificateProviderExternalAccountBindingOutput) ToAutoCertificateProviderExternalAccountBindingOutputWithContext(ctx context.Context) AutoCertificateProviderExternalAccountBindingOutput {
	return o
}

func (o AutoCertificateProviderExternalAccountBindingOutput) ToAutoCertificateProviderExternalAccountBindingPtrOutput() AutoCertificateProviderExternalAccountBindingPtrOutput {
	return o.ToAutoCertificateProviderExternalAccountBindingPtrOutputWithContext(context.Background())
}

func (o AutoCertificateProviderExternalAccountBindingOutput) ToAutoCertificateProviderExternalAccountBindingPtrOutputWithContext(ctx context.Context) AutoCertificateProviderExternalAccountBindingPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v AutoCertificateProviderExternalAccountBinding) *AutoCertificateProviderExternalAccountBinding {
		return &v
	}).(AutoCertificateProviderExternalAccountBindingPtrOutput)
}

// The key ID of the external account binding
func (o AutoCertificateProviderExternalAccountBindingOutput) KeyId() pulumi.StringOutput {
	return o.ApplyT(func(v AutoCertificateProviderExternalAccountBinding) string { return v.KeyId }).(pulumi.StringOutput)
}

// The secret of the external account binding
func (o AutoCertificateProviderExternalAccountBindingOutput) KeySecret() pulumi.StringOutput {
	return o.ApplyT(func(v AutoCertificateProviderExternalAccountBinding) string { return v.KeySecret }).(pulumi.StringOutput)
}

type AutoCertificateProviderExternalAccountBindingPtrOutput struct{ *pulumi.OutputState }

func (AutoCertificateProviderExternalAccountBindingPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**AutoCertificateProviderExternalAccountBinding)(nil)).Elem()
}

func (o AutoCertificateProviderExternalAccountBindingPtrOutput) ToAutoCertificateProviderExternalAccountBindingPtrOutput() AutoCertificateProviderExternalAccountBindingPtrOutput {
	return o
}

func (o AutoCertificateProviderExternalAccountBindingPtrOutput) ToAutoCertificateProviderExternalAccountBindingPtrOutputWithContext(ctx context.Context) AutoCertificateProviderExternalAccountBindingPtrOutput {
	return o
}

func (o AutoCertificateProviderExternalAccountBindingPtrOutput) Elem() AutoCertificateProviderExternalAccountBindingOutput {
	return o.ApplyT(func(v *AutoCertificateProviderExternalAccountBinding) AutoCertificateProviderExternalAccountBinding {
		if v != nil {
			return *v
		}
		var ret AutoCertificateProviderExternalAccountBinding
		return ret
	}).(AutoCertificateProviderExternalAccountBindingOutput)
}

// The key ID of the external account binding
func (o AutoCertificateProviderExternalAccountBindingPtrOutput) KeyId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *AutoCertificateProviderExternalAccountBinding) *string {
		if v == nil {
			return nil
		}
		return &v.KeyId
	}).(pulumi.StringPtrOutput)
}

// The secret of the external account binding
func (o AutoCertificateProviderExternalAccountBindingPtrOutput) KeySecret() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *AutoCertificateProviderExternalAccountBinding) *string {
		if v == nil {
			return nil
		}
		return &v.KeySecret
	}).(pulumi.StringPtrOutput)
}

type GetAutoCertificateProviderExternalAccountBinding struct {
	// The key ID of the external account binding
	KeyId string `pulumi:"keyId"`
}

// GetAutoCertificateProviderExternalAccountBindingInput is an input type that accepts GetAutoCertificateProviderExternalAccountBindingArgs and GetAutoCertificateProviderExternalAccountBindingOutput values.
// You can construct a concrete instance of `GetAutoCertificateProviderExternalAccountBindingInput` via:
//
//	GetAutoCertificateProviderExternalAccountBindingArgs{...}
type GetAutoCertificateProviderExternalAccountBindingInput interface {
	pulumi.Input

	ToGetAutoCertificateProviderExternalAccountBindingOutput() GetAutoCertificateProviderExternalAccountBindingOutput
	ToGetAutoCertificateProviderExternalAccountBindingOutputWithContext(context.Context) GetAutoCertificateProviderExternalAccountBindingOutput
}

type GetAutoCertificateProviderExternalAccountBindingArgs struct {
	// The key ID of the external account binding
	KeyId pulumi.StringInput `pulumi:"keyId"`
}

func (GetAutoCertificateProviderExternalAccountBindingArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetAutoCertificateProviderExternalAccountBinding)(nil)).Elem()
}

func (i GetAutoCertificateProviderExternalAccountBindingArgs) ToGetAutoCertificateProviderExternalAccountBindingOutput() GetAutoCertificateProviderExternalAccountBindingOutput {
	return i.ToGetAutoCertificateProviderExternalAccountBindingOutputWithContext(context.Background())
}

func (i GetAutoCertificateProviderExternalAccountBindingArgs) ToGetAutoCertificateProviderExternalAccountBindingOutputWithContext(ctx context.Context) GetAutoCertificateProviderExternalAccountBindingOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GetAutoCertificateProviderExternalAccountBindingOutput)
}

// GetAutoCertificateProviderExternalAccountBindingArrayInput is an input type that accepts GetAutoCertificateProviderExternalAccountBindingArray and GetAutoCertificateProviderExternalAccountBindingArrayOutput values.
// You can construct a concrete instance of `GetAutoCertificateProviderExternalAccountBindingArrayInput` via:
//
//	GetAutoCertificateProviderExternalAccountBindingArray{ GetAutoCertificateProviderExternalAccountBindingArgs{...} }
type GetAutoCertificateProviderExternalAccountBindingArrayInput interface {
	pulumi.Input

	ToGetAutoCertificateProviderExternalAccountBindingArrayOutput() GetAutoCertificateProviderExternalAccountBindingArrayOutput
	ToGetAutoCertificateProviderExternalAccountBindingArrayOutputWithContext(context.Context) GetAutoCertificateProviderExternalAccountBindingArrayOutput
}

type GetAutoCertificateProviderExternalAccountBindingArray []GetAutoCertificateProviderExternalAccountBindingInput

func (GetAutoCertificateProviderExternalAccountBindingArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]GetAutoCertificateProviderExternalAccountBinding)(nil)).Elem()
}

func (i GetAutoCertificateProviderExternalAccountBindingArray) ToGetAutoCertificateProviderExternalAccountBindingArrayOutput() GetAutoCertificateProviderExternalAccountBindingArrayOutput {
	return i.ToGetAutoCertificateProviderExternalAccountBindingArrayOutputWithContext(context.Background())
}

func (i GetAutoCertificateProviderExternalAccountBindingArray) ToGetAutoCertificateProviderExternalAccountBindingArrayOutputWithContext(ctx context.Context) GetAutoCertificateProviderExternalAccountBindingArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GetAutoCertificateProviderExternalAccountBindingArrayOutput)
}

type GetAutoCertificateProviderExternalAccountBindingOutput struct{ *pulumi.OutputState }

func (GetAutoCertificateProviderExternalAccountBindingOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetAutoCertificateProviderExternalAccountBinding)(nil)).Elem()
}

func (o GetAutoCertificateProviderExternalAccountBindingOutput) ToGetAutoCertificateProviderExternalAccountBindingOutput() GetAutoCertificateProviderExternalAccountBindingOutput {
	return o
}

func (o GetAutoCertificateProviderExternalAccountBindingOutput) ToGetAutoCertificateProviderExternalAccountBindingOutputWithContext(ctx context.Context) GetAutoCertificateProviderExternalAccountBindingOutput {
	return o
}

// The key ID of the external account binding
func (o GetAutoCertificateProviderExternalAccountBindingOutput) KeyId() pulumi.StringOutput {
	return o.ApplyT(func(v GetAutoCertificateProviderExternalAccountBinding) string { return v.KeyId }).(pulumi.StringOutput)
}

type GetAutoCertificateProviderExternalAccountBindingArrayOutput struct{ *pulumi.OutputState }

func (GetAutoCertificateProviderExternalAccountBindingArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]GetAutoCertificateProviderExternalAccountBinding)(nil)).Elem()
}

func (o GetAutoCertificateProviderExternalAccountBindingArrayOutput) ToGetAutoCertificateProviderExternalAccountBindingArrayOutput() GetAutoCertificateProviderExternalAccountBindingArrayOutput {
	return o
}

func (o GetAutoCertificateProviderExternalAccountBindingArrayOutput) ToGetAutoCertificateProviderExternalAccountBindingArrayOutputWithContext(ctx context.Context) GetAutoCertificateProviderExternalAccountBindingArrayOutput {
	return o
}

func (o GetAutoCertificateProviderExternalAccountBindingArrayOutput) Index(i pulumi.IntInput) GetAutoCertificateProviderExternalAccountBindingOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) GetAutoCertificateProviderExternalAccountBinding {
		return vs[0].([]GetAutoCertificateProviderExternalAccountBinding)[vs[1].(int)]
	}).(GetAutoCertificateProviderExternalAccountBindingOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*AutoCertificateProviderExternalAccountBindingInput)(nil)).Elem(), AutoCertificateProviderExternalAccountBindingArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*AutoCertificateProviderExternalAccountBindingPtrInput)(nil)).Elem(), AutoCertificateProviderExternalAccountBindingArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*GetAutoCertificateProviderExternalAccountBindingInput)(nil)).Elem(), GetAutoCertificateProviderExternalAccountBindingArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*GetAutoCertificateProviderExternalAccountBindingArrayInput)(nil)).Elem(), GetAutoCertificateProviderExternalAccountBindingArray{})
	pulumi.RegisterOutputType(AutoCertificateProviderExternalAccountBindingOutput{})
	pulumi.RegisterOutputType(AutoCertificateProviderExternalAccountBindingPtrOutput{})
	pulumi.RegisterOutputType(GetAutoCertificateProviderExternalAccountBindingOutput{})
	pulumi.RegisterOutputType(GetAutoCertificateProviderExternalAccountBindingArrayOutput{})
}
