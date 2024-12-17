// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ionoscloud

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func GetCertificate(ctx *pulumi.Context, args *GetCertificateArgs, opts ...pulumi.InvokeOption) (*GetCertificateResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetCertificateResult
	err := ctx.Invoke("ionoscloud:index/getCertificate:getCertificate", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getCertificate.
type GetCertificateArgs struct {
	Certificate      *string `pulumi:"certificate"`
	CertificateChain *string `pulumi:"certificateChain"`
	Id               *string `pulumi:"id"`
	Name             *string `pulumi:"name"`
}

// A collection of values returned by getCertificate.
type GetCertificateResult struct {
	Certificate      string  `pulumi:"certificate"`
	CertificateChain string  `pulumi:"certificateChain"`
	Id               *string `pulumi:"id"`
	Name             *string `pulumi:"name"`
}

func GetCertificateOutput(ctx *pulumi.Context, args GetCertificateOutputArgs, opts ...pulumi.InvokeOption) GetCertificateResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (GetCertificateResultOutput, error) {
			args := v.(GetCertificateArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("ionoscloud:index/getCertificate:getCertificate", args, GetCertificateResultOutput{}, options).(GetCertificateResultOutput), nil
		}).(GetCertificateResultOutput)
}

// A collection of arguments for invoking getCertificate.
type GetCertificateOutputArgs struct {
	Certificate      pulumi.StringPtrInput `pulumi:"certificate"`
	CertificateChain pulumi.StringPtrInput `pulumi:"certificateChain"`
	Id               pulumi.StringPtrInput `pulumi:"id"`
	Name             pulumi.StringPtrInput `pulumi:"name"`
}

func (GetCertificateOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetCertificateArgs)(nil)).Elem()
}

// A collection of values returned by getCertificate.
type GetCertificateResultOutput struct{ *pulumi.OutputState }

func (GetCertificateResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetCertificateResult)(nil)).Elem()
}

func (o GetCertificateResultOutput) ToGetCertificateResultOutput() GetCertificateResultOutput {
	return o
}

func (o GetCertificateResultOutput) ToGetCertificateResultOutputWithContext(ctx context.Context) GetCertificateResultOutput {
	return o
}

func (o GetCertificateResultOutput) Certificate() pulumi.StringOutput {
	return o.ApplyT(func(v GetCertificateResult) string { return v.Certificate }).(pulumi.StringOutput)
}

func (o GetCertificateResultOutput) CertificateChain() pulumi.StringOutput {
	return o.ApplyT(func(v GetCertificateResult) string { return v.CertificateChain }).(pulumi.StringOutput)
}

func (o GetCertificateResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetCertificateResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o GetCertificateResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetCertificateResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(GetCertificateResultOutput{})
}
