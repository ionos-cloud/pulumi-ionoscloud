// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cert

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The **Certificate data source** can be used to search for and return an existing certificate.
// You can provide a string for either id or name parameters which will be compared with provisioned certificates.
// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
// When this happens, please refine your search string so that it is specific enough to return only one result.
//
// ## Example Usage
//
// ### By Name
// ```go
// package main
//
// import (
//
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/cert"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := cert.LookupCertificate(ctx, &cert.LookupCertificateArgs{
//				Name: pulumi.StringRef("Certificate Name Example"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func LookupCertificate(ctx *pulumi.Context, args *LookupCertificateArgs, opts ...pulumi.InvokeOption) (*LookupCertificateResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupCertificateResult
	err := ctx.Invoke("ionoscloud:cert/getCertificate:getCertificate", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getCertificate.
type LookupCertificateArgs struct {
	// Certificate body.
	Certificate *string `pulumi:"certificate"`
	// Certificate chain.
	CertificateChain *string `pulumi:"certificateChain"`
	// ID of the certificate you want to search for.
	//
	// Either `name` or `id` must be provided, or both. If none are provided, the datasource will return an error.
	Id *string `pulumi:"id"`
	// Name of an existing certificate that you want to search for.
	Name *string `pulumi:"name"`
}

// A collection of values returned by getCertificate.
type LookupCertificateResult struct {
	// Certificate body.
	Certificate string `pulumi:"certificate"`
	// Certificate chain.
	CertificateChain string `pulumi:"certificateChain"`
	// The id of the certificate.
	Id *string `pulumi:"id"`
	// The name of the certificate.
	Name *string `pulumi:"name"`
}

func LookupCertificateOutput(ctx *pulumi.Context, args LookupCertificateOutputArgs, opts ...pulumi.InvokeOption) LookupCertificateResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupCertificateResultOutput, error) {
			args := v.(LookupCertificateArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("ionoscloud:cert/getCertificate:getCertificate", args, LookupCertificateResultOutput{}, options).(LookupCertificateResultOutput), nil
		}).(LookupCertificateResultOutput)
}

// A collection of arguments for invoking getCertificate.
type LookupCertificateOutputArgs struct {
	// Certificate body.
	Certificate pulumi.StringPtrInput `pulumi:"certificate"`
	// Certificate chain.
	CertificateChain pulumi.StringPtrInput `pulumi:"certificateChain"`
	// ID of the certificate you want to search for.
	//
	// Either `name` or `id` must be provided, or both. If none are provided, the datasource will return an error.
	Id pulumi.StringPtrInput `pulumi:"id"`
	// Name of an existing certificate that you want to search for.
	Name pulumi.StringPtrInput `pulumi:"name"`
}

func (LookupCertificateOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupCertificateArgs)(nil)).Elem()
}

// A collection of values returned by getCertificate.
type LookupCertificateResultOutput struct{ *pulumi.OutputState }

func (LookupCertificateResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupCertificateResult)(nil)).Elem()
}

func (o LookupCertificateResultOutput) ToLookupCertificateResultOutput() LookupCertificateResultOutput {
	return o
}

func (o LookupCertificateResultOutput) ToLookupCertificateResultOutputWithContext(ctx context.Context) LookupCertificateResultOutput {
	return o
}

// Certificate body.
func (o LookupCertificateResultOutput) Certificate() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCertificateResult) string { return v.Certificate }).(pulumi.StringOutput)
}

// Certificate chain.
func (o LookupCertificateResultOutput) CertificateChain() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCertificateResult) string { return v.CertificateChain }).(pulumi.StringOutput)
}

// The id of the certificate.
func (o LookupCertificateResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupCertificateResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// The name of the certificate.
func (o LookupCertificateResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupCertificateResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupCertificateResultOutput{})
}
