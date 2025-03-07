// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cert

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The **CM AutoCertificate data source** can be used to search for and return an existing auto-certificate.
// You can provide a string for either id or name parameters which will be compared with provisioned auto-certificates.
// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
// When this happens, please refine your search string so that it is specific enough to return only one result.
//
// ## Example Usage
//
// ### By ID
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
//			_, err := cert.LookupAutoCertificate(ctx, &cert.LookupAutoCertificateArgs{
//				Id:       pulumi.StringRef("auto_certificate_id"),
//				Location: "auto_certificate_location",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
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
//			_, err := cert.LookupAutoCertificate(ctx, &cert.LookupAutoCertificateArgs{
//				Name:     pulumi.StringRef("AutoCertificate Name Example"),
//				Location: "auto_certificate_location",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func LookupAutoCertificate(ctx *pulumi.Context, args *LookupAutoCertificateArgs, opts ...pulumi.InvokeOption) (*LookupAutoCertificateResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupAutoCertificateResult
	err := ctx.Invoke("ionoscloud:cert/getAutoCertificate:getAutoCertificate", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getAutoCertificate.
type LookupAutoCertificateArgs struct {
	// [string] ID of the auto-certificate you want to search for.
	//
	// Either `name` or `id` must be provided. If none, or both are provided, the datasource will return an error.
	Id *string `pulumi:"id"`
	// [string] The location of the auto-certificate.
	Location string `pulumi:"location"`
	// [string] Name of an existing auto-certificate that you want to search for.
	Name *string `pulumi:"name"`
}

// A collection of values returned by getAutoCertificate.
type LookupAutoCertificateResult struct {
	// [string] The common name (DNS) of the certificate to issue. The common name needs to be part of a zone in IONOS Cloud DNS.
	CommonName string `pulumi:"commonName"`
	Id         string `pulumi:"id"`
	// [string] The key algorithm used to generate the certificate.
	KeyAlgorithm string `pulumi:"keyAlgorithm"`
	// [string] The ID of the last certificate that was issued.
	LastIssuedCertificateId string `pulumi:"lastIssuedCertificateId"`
	Location                string `pulumi:"location"`
	Name                    string `pulumi:"name"`
	ProviderId              string `pulumi:"providerId"`
	// [list][string] Optional additional names to be added to the issued certificate. The additional names needs to be part of a zone in IONOS Cloud DNS.
	SubjectAlternativeNames []string `pulumi:"subjectAlternativeNames"`
}

func LookupAutoCertificateOutput(ctx *pulumi.Context, args LookupAutoCertificateOutputArgs, opts ...pulumi.InvokeOption) LookupAutoCertificateResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupAutoCertificateResultOutput, error) {
			args := v.(LookupAutoCertificateArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("ionoscloud:cert/getAutoCertificate:getAutoCertificate", args, LookupAutoCertificateResultOutput{}, options).(LookupAutoCertificateResultOutput), nil
		}).(LookupAutoCertificateResultOutput)
}

// A collection of arguments for invoking getAutoCertificate.
type LookupAutoCertificateOutputArgs struct {
	// [string] ID of the auto-certificate you want to search for.
	//
	// Either `name` or `id` must be provided. If none, or both are provided, the datasource will return an error.
	Id pulumi.StringPtrInput `pulumi:"id"`
	// [string] The location of the auto-certificate.
	Location pulumi.StringInput `pulumi:"location"`
	// [string] Name of an existing auto-certificate that you want to search for.
	Name pulumi.StringPtrInput `pulumi:"name"`
}

func (LookupAutoCertificateOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupAutoCertificateArgs)(nil)).Elem()
}

// A collection of values returned by getAutoCertificate.
type LookupAutoCertificateResultOutput struct{ *pulumi.OutputState }

func (LookupAutoCertificateResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupAutoCertificateResult)(nil)).Elem()
}

func (o LookupAutoCertificateResultOutput) ToLookupAutoCertificateResultOutput() LookupAutoCertificateResultOutput {
	return o
}

func (o LookupAutoCertificateResultOutput) ToLookupAutoCertificateResultOutputWithContext(ctx context.Context) LookupAutoCertificateResultOutput {
	return o
}

// [string] The common name (DNS) of the certificate to issue. The common name needs to be part of a zone in IONOS Cloud DNS.
func (o LookupAutoCertificateResultOutput) CommonName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAutoCertificateResult) string { return v.CommonName }).(pulumi.StringOutput)
}

func (o LookupAutoCertificateResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAutoCertificateResult) string { return v.Id }).(pulumi.StringOutput)
}

// [string] The key algorithm used to generate the certificate.
func (o LookupAutoCertificateResultOutput) KeyAlgorithm() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAutoCertificateResult) string { return v.KeyAlgorithm }).(pulumi.StringOutput)
}

// [string] The ID of the last certificate that was issued.
func (o LookupAutoCertificateResultOutput) LastIssuedCertificateId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAutoCertificateResult) string { return v.LastIssuedCertificateId }).(pulumi.StringOutput)
}

func (o LookupAutoCertificateResultOutput) Location() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAutoCertificateResult) string { return v.Location }).(pulumi.StringOutput)
}

func (o LookupAutoCertificateResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAutoCertificateResult) string { return v.Name }).(pulumi.StringOutput)
}

func (o LookupAutoCertificateResultOutput) ProviderId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAutoCertificateResult) string { return v.ProviderId }).(pulumi.StringOutput)
}

// [list][string] Optional additional names to be added to the issued certificate. The additional names needs to be part of a zone in IONOS Cloud DNS.
func (o LookupAutoCertificateResultOutput) SubjectAlternativeNames() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupAutoCertificateResult) []string { return v.SubjectAlternativeNames }).(pulumi.StringArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupAutoCertificateResultOutput{})
}
