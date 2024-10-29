// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ionoscloud

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The Distribution data source can be used to search for and return an existing Distributions.
// You can provide a string for the domain parameter which will be compared with provisioned Distributions.
// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
// When this happens, please refine your search and make sure that your resources have unique domains.
//
// ## Example Usage
//
// ### By Domain
// <!--Start PulumiCodeChooser -->
// ```go
// package main
//
// import (
//
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := ionoscloud.LookupCdnDistribution(ctx, &ionoscloud.LookupCdnDistributionArgs{
//				Domain: pulumi.StringRef("example.com"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
// <!--End PulumiCodeChooser -->
//
// ### By Domain with Partial Match
// <!--Start PulumiCodeChooser -->
// ```go
// package main
//
// import (
//
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := ionoscloud.LookupCdnDistribution(ctx, &ionoscloud.LookupCdnDistributionArgs{
//				Domain:       pulumi.StringRef("example"),
//				PartialMatch: pulumi.BoolRef(true),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
// <!--End PulumiCodeChooser -->
func LookupCdnDistribution(ctx *pulumi.Context, args *LookupCdnDistributionArgs, opts ...pulumi.InvokeOption) (*LookupCdnDistributionResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupCdnDistributionResult
	err := ctx.Invoke("ionoscloud:index/getCdnDistribution:getCdnDistribution", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getCdnDistribution.
type LookupCdnDistributionArgs struct {
	// Domain of an existing distribution that you want to search for. Search by domain is case-insensitive. The whole resource domain is required if `partialMatch` parameter is not set to true.
	Domain *string `pulumi:"domain"`
	// ID of the distribution you want to search for.
	Id *string `pulumi:"id"`
	// Whether partial matching is allowed or not when using domain argument. Default value is false.
	//
	// Either `domain` or `id` must be provided. If none, or both of `domain` and `id` are provided, the datasource will return an error.
	PartialMatch *bool `pulumi:"partialMatch"`
}

// A collection of values returned by getCdnDistribution.
type LookupCdnDistributionResult struct {
	// The ID of the certificate to use for the distribution. You can create certificates with the certificate resource.
	CertificateId string `pulumi:"certificateId"`
	// The domain of the distribution.
	Domain       *string `pulumi:"domain"`
	Id           *string `pulumi:"id"`
	PartialMatch *bool   `pulumi:"partialMatch"`
	// IP of the distribution, it has to be included on the domain DNS Zone as A record.
	PublicEndpointV4 string `pulumi:"publicEndpointV4"`
	// IP of the distribution, it has to be included on the domain DNS Zone as AAAA record.
	PublicEndpointV6 string `pulumi:"publicEndpointV6"`
	// Unique resource identifier.
	ResourceUrn string `pulumi:"resourceUrn"`
	// The routing rules for the distribution.
	RoutingRules []GetCdnDistributionRoutingRule `pulumi:"routingRules"`
}

func LookupCdnDistributionOutput(ctx *pulumi.Context, args LookupCdnDistributionOutputArgs, opts ...pulumi.InvokeOption) LookupCdnDistributionResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupCdnDistributionResult, error) {
			args := v.(LookupCdnDistributionArgs)
			r, err := LookupCdnDistribution(ctx, &args, opts...)
			var s LookupCdnDistributionResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupCdnDistributionResultOutput)
}

// A collection of arguments for invoking getCdnDistribution.
type LookupCdnDistributionOutputArgs struct {
	// Domain of an existing distribution that you want to search for. Search by domain is case-insensitive. The whole resource domain is required if `partialMatch` parameter is not set to true.
	Domain pulumi.StringPtrInput `pulumi:"domain"`
	// ID of the distribution you want to search for.
	Id pulumi.StringPtrInput `pulumi:"id"`
	// Whether partial matching is allowed or not when using domain argument. Default value is false.
	//
	// Either `domain` or `id` must be provided. If none, or both of `domain` and `id` are provided, the datasource will return an error.
	PartialMatch pulumi.BoolPtrInput `pulumi:"partialMatch"`
}

func (LookupCdnDistributionOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupCdnDistributionArgs)(nil)).Elem()
}

// A collection of values returned by getCdnDistribution.
type LookupCdnDistributionResultOutput struct{ *pulumi.OutputState }

func (LookupCdnDistributionResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupCdnDistributionResult)(nil)).Elem()
}

func (o LookupCdnDistributionResultOutput) ToLookupCdnDistributionResultOutput() LookupCdnDistributionResultOutput {
	return o
}

func (o LookupCdnDistributionResultOutput) ToLookupCdnDistributionResultOutputWithContext(ctx context.Context) LookupCdnDistributionResultOutput {
	return o
}

// The ID of the certificate to use for the distribution. You can create certificates with the certificate resource.
func (o LookupCdnDistributionResultOutput) CertificateId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCdnDistributionResult) string { return v.CertificateId }).(pulumi.StringOutput)
}

// The domain of the distribution.
func (o LookupCdnDistributionResultOutput) Domain() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupCdnDistributionResult) *string { return v.Domain }).(pulumi.StringPtrOutput)
}

func (o LookupCdnDistributionResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupCdnDistributionResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupCdnDistributionResultOutput) PartialMatch() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupCdnDistributionResult) *bool { return v.PartialMatch }).(pulumi.BoolPtrOutput)
}

// IP of the distribution, it has to be included on the domain DNS Zone as A record.
func (o LookupCdnDistributionResultOutput) PublicEndpointV4() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCdnDistributionResult) string { return v.PublicEndpointV4 }).(pulumi.StringOutput)
}

// IP of the distribution, it has to be included on the domain DNS Zone as AAAA record.
func (o LookupCdnDistributionResultOutput) PublicEndpointV6() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCdnDistributionResult) string { return v.PublicEndpointV6 }).(pulumi.StringOutput)
}

// Unique resource identifier.
func (o LookupCdnDistributionResultOutput) ResourceUrn() pulumi.StringOutput {
	return o.ApplyT(func(v LookupCdnDistributionResult) string { return v.ResourceUrn }).(pulumi.StringOutput)
}

// The routing rules for the distribution.
func (o LookupCdnDistributionResultOutput) RoutingRules() GetCdnDistributionRoutingRuleArrayOutput {
	return o.ApplyT(func(v LookupCdnDistributionResult) []GetCdnDistributionRoutingRule { return v.RoutingRules }).(GetCdnDistributionRoutingRuleArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupCdnDistributionResultOutput{})
}
