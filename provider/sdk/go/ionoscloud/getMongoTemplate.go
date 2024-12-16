// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ionoscloud

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func GetMongoTemplate(ctx *pulumi.Context, args *GetMongoTemplateArgs, opts ...pulumi.InvokeOption) (*GetMongoTemplateResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetMongoTemplateResult
	err := ctx.Invoke("ionoscloud:index/getMongoTemplate:getMongoTemplate", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getMongoTemplate.
type GetMongoTemplateArgs struct {
	Id           *string `pulumi:"id"`
	Name         *string `pulumi:"name"`
	PartialMatch *bool   `pulumi:"partialMatch"`
}

// A collection of values returned by getMongoTemplate.
type GetMongoTemplateResult struct {
	Cores        int    `pulumi:"cores"`
	Edition      string `pulumi:"edition"`
	Id           string `pulumi:"id"`
	Name         string `pulumi:"name"`
	PartialMatch *bool  `pulumi:"partialMatch"`
	Ram          int    `pulumi:"ram"`
	StorageSize  int    `pulumi:"storageSize"`
}

func GetMongoTemplateOutput(ctx *pulumi.Context, args GetMongoTemplateOutputArgs, opts ...pulumi.InvokeOption) GetMongoTemplateResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (GetMongoTemplateResultOutput, error) {
			args := v.(GetMongoTemplateArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("ionoscloud:index/getMongoTemplate:getMongoTemplate", args, GetMongoTemplateResultOutput{}, options).(GetMongoTemplateResultOutput), nil
		}).(GetMongoTemplateResultOutput)
}

// A collection of arguments for invoking getMongoTemplate.
type GetMongoTemplateOutputArgs struct {
	Id           pulumi.StringPtrInput `pulumi:"id"`
	Name         pulumi.StringPtrInput `pulumi:"name"`
	PartialMatch pulumi.BoolPtrInput   `pulumi:"partialMatch"`
}

func (GetMongoTemplateOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetMongoTemplateArgs)(nil)).Elem()
}

// A collection of values returned by getMongoTemplate.
type GetMongoTemplateResultOutput struct{ *pulumi.OutputState }

func (GetMongoTemplateResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetMongoTemplateResult)(nil)).Elem()
}

func (o GetMongoTemplateResultOutput) ToGetMongoTemplateResultOutput() GetMongoTemplateResultOutput {
	return o
}

func (o GetMongoTemplateResultOutput) ToGetMongoTemplateResultOutputWithContext(ctx context.Context) GetMongoTemplateResultOutput {
	return o
}

func (o GetMongoTemplateResultOutput) Cores() pulumi.IntOutput {
	return o.ApplyT(func(v GetMongoTemplateResult) int { return v.Cores }).(pulumi.IntOutput)
}

func (o GetMongoTemplateResultOutput) Edition() pulumi.StringOutput {
	return o.ApplyT(func(v GetMongoTemplateResult) string { return v.Edition }).(pulumi.StringOutput)
}

func (o GetMongoTemplateResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetMongoTemplateResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o GetMongoTemplateResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v GetMongoTemplateResult) string { return v.Name }).(pulumi.StringOutput)
}

func (o GetMongoTemplateResultOutput) PartialMatch() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v GetMongoTemplateResult) *bool { return v.PartialMatch }).(pulumi.BoolPtrOutput)
}

func (o GetMongoTemplateResultOutput) Ram() pulumi.IntOutput {
	return o.ApplyT(func(v GetMongoTemplateResult) int { return v.Ram }).(pulumi.IntOutput)
}

func (o GetMongoTemplateResultOutput) StorageSize() pulumi.IntOutput {
	return o.ApplyT(func(v GetMongoTemplateResult) int { return v.StorageSize }).(pulumi.IntOutput)
}

func init() {
	pulumi.RegisterOutputType(GetMongoTemplateResultOutput{})
}
