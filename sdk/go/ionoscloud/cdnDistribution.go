// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ionoscloud

import (
	"context"
	"reflect"

	"errors"
	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Manages a **CDN Distribution** on IonosCloud.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"os"
//
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func readFileOrPanic(path string) pulumi.StringPtrInput {
//		data, err := os.ReadFile(path)
//		if err != nil {
//			panic(err.Error())
//		}
//		return pulumi.String(string(data))
//	}
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			// optionally you can add a certificate to the distribution
//			cert, err := ionoscloud.NewCertificate(ctx, "cert", &ionoscloud.CertificateArgs{
//				Certificate:      pulumi.String(readFileOrPanic("path_to_cert")),
//				CertificateChain: pulumi.String(readFileOrPanic("path_to_cert_chain")),
//				PrivateKey:       pulumi.String(readFileOrPanic("path_to_private_key")),
//			})
//			if err != nil {
//				return err
//			}
//			_, err = ionoscloud.NewCdnDistribution(ctx, "example", &ionoscloud.CdnDistributionArgs{
//				Domain:        pulumi.String("example.com"),
//				CertificateId: cert.ID(),
//				RoutingRules: ionoscloud.CdnDistributionRoutingRuleArray{
//					&ionoscloud.CdnDistributionRoutingRuleArgs{
//						Scheme: pulumi.String("https"),
//						Prefix: pulumi.String("/api"),
//						Upstream: &ionoscloud.CdnDistributionRoutingRuleUpstreamArgs{
//							Host:           pulumi.String("server.example.com"),
//							Caching:        pulumi.Bool(true),
//							Waf:            pulumi.Bool(true),
//							SniMode:        pulumi.String("distribution"),
//							RateLimitClass: pulumi.String("R500"),
//							GeoRestrictions: &ionoscloud.CdnDistributionRoutingRuleUpstreamGeoRestrictionsArgs{
//								AllowLists: pulumi.StringArray{
//									pulumi.String("CN"),
//									pulumi.String("RU"),
//								},
//							},
//						},
//					},
//					&ionoscloud.CdnDistributionRoutingRuleArgs{
//						Scheme: pulumi.String("http/https"),
//						Prefix: pulumi.String("/api2"),
//						Upstream: &ionoscloud.CdnDistributionRoutingRuleUpstreamArgs{
//							Host:           pulumi.String("server2.example.com"),
//							Caching:        pulumi.Bool(false),
//							Waf:            pulumi.Bool(false),
//							SniMode:        pulumi.String("origin"),
//							RateLimitClass: pulumi.String("R10"),
//							GeoRestrictions: &ionoscloud.CdnDistributionRoutingRuleUpstreamGeoRestrictionsArgs{
//								BlockLists: pulumi.StringArray{
//									pulumi.String("CN"),
//									pulumi.String("RU"),
//								},
//							},
//						},
//					},
//				},
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
//
// ## Import
//
// Resource Distribution can be imported using the `resource id`, e.g.
//
// ```sh
// $ pulumi import ionoscloud:index/cdnDistribution:CdnDistribution myDistribution {distribution uuid}
// ```
type CdnDistribution struct {
	pulumi.CustomResourceState

	// [string] The ID of the certificate to use for the distribution. You can create certificates with the certificate resource.
	CertificateId pulumi.StringPtrOutput `pulumi:"certificateId"`
	// [string] The domain of the distribution.
	Domain pulumi.StringOutput `pulumi:"domain"`
	// IP of the distribution, it has to be included on the domain DNS Zone as A record.
	PublicEndpointV4 pulumi.StringOutput `pulumi:"publicEndpointV4"`
	// IP of the distribution, it has to be included on the domain DNS Zone as AAAA record.
	PublicEndpointV6 pulumi.StringOutput `pulumi:"publicEndpointV6"`
	// Unique resource indentifier.
	ResourceUrn pulumi.StringOutput `pulumi:"resourceUrn"`
	// [list] The routing rules for the distribution.
	RoutingRules CdnDistributionRoutingRuleArrayOutput `pulumi:"routingRules"`
}

// NewCdnDistribution registers a new resource with the given unique name, arguments, and options.
func NewCdnDistribution(ctx *pulumi.Context,
	name string, args *CdnDistributionArgs, opts ...pulumi.ResourceOption) (*CdnDistribution, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Domain == nil {
		return nil, errors.New("invalid value for required argument 'Domain'")
	}
	if args.RoutingRules == nil {
		return nil, errors.New("invalid value for required argument 'RoutingRules'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource CdnDistribution
	err := ctx.RegisterResource("ionoscloud:index/cdnDistribution:CdnDistribution", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCdnDistribution gets an existing CdnDistribution resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCdnDistribution(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CdnDistributionState, opts ...pulumi.ResourceOption) (*CdnDistribution, error) {
	var resource CdnDistribution
	err := ctx.ReadResource("ionoscloud:index/cdnDistribution:CdnDistribution", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering CdnDistribution resources.
type cdnDistributionState struct {
	// [string] The ID of the certificate to use for the distribution. You can create certificates with the certificate resource.
	CertificateId *string `pulumi:"certificateId"`
	// [string] The domain of the distribution.
	Domain *string `pulumi:"domain"`
	// IP of the distribution, it has to be included on the domain DNS Zone as A record.
	PublicEndpointV4 *string `pulumi:"publicEndpointV4"`
	// IP of the distribution, it has to be included on the domain DNS Zone as AAAA record.
	PublicEndpointV6 *string `pulumi:"publicEndpointV6"`
	// Unique resource indentifier.
	ResourceUrn *string `pulumi:"resourceUrn"`
	// [list] The routing rules for the distribution.
	RoutingRules []CdnDistributionRoutingRule `pulumi:"routingRules"`
}

type CdnDistributionState struct {
	// [string] The ID of the certificate to use for the distribution. You can create certificates with the certificate resource.
	CertificateId pulumi.StringPtrInput
	// [string] The domain of the distribution.
	Domain pulumi.StringPtrInput
	// IP of the distribution, it has to be included on the domain DNS Zone as A record.
	PublicEndpointV4 pulumi.StringPtrInput
	// IP of the distribution, it has to be included on the domain DNS Zone as AAAA record.
	PublicEndpointV6 pulumi.StringPtrInput
	// Unique resource indentifier.
	ResourceUrn pulumi.StringPtrInput
	// [list] The routing rules for the distribution.
	RoutingRules CdnDistributionRoutingRuleArrayInput
}

func (CdnDistributionState) ElementType() reflect.Type {
	return reflect.TypeOf((*cdnDistributionState)(nil)).Elem()
}

type cdnDistributionArgs struct {
	// [string] The ID of the certificate to use for the distribution. You can create certificates with the certificate resource.
	CertificateId *string `pulumi:"certificateId"`
	// [string] The domain of the distribution.
	Domain string `pulumi:"domain"`
	// [list] The routing rules for the distribution.
	RoutingRules []CdnDistributionRoutingRule `pulumi:"routingRules"`
}

// The set of arguments for constructing a CdnDistribution resource.
type CdnDistributionArgs struct {
	// [string] The ID of the certificate to use for the distribution. You can create certificates with the certificate resource.
	CertificateId pulumi.StringPtrInput
	// [string] The domain of the distribution.
	Domain pulumi.StringInput
	// [list] The routing rules for the distribution.
	RoutingRules CdnDistributionRoutingRuleArrayInput
}

func (CdnDistributionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*cdnDistributionArgs)(nil)).Elem()
}

type CdnDistributionInput interface {
	pulumi.Input

	ToCdnDistributionOutput() CdnDistributionOutput
	ToCdnDistributionOutputWithContext(ctx context.Context) CdnDistributionOutput
}

func (*CdnDistribution) ElementType() reflect.Type {
	return reflect.TypeOf((**CdnDistribution)(nil)).Elem()
}

func (i *CdnDistribution) ToCdnDistributionOutput() CdnDistributionOutput {
	return i.ToCdnDistributionOutputWithContext(context.Background())
}

func (i *CdnDistribution) ToCdnDistributionOutputWithContext(ctx context.Context) CdnDistributionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CdnDistributionOutput)
}

// CdnDistributionArrayInput is an input type that accepts CdnDistributionArray and CdnDistributionArrayOutput values.
// You can construct a concrete instance of `CdnDistributionArrayInput` via:
//
//	CdnDistributionArray{ CdnDistributionArgs{...} }
type CdnDistributionArrayInput interface {
	pulumi.Input

	ToCdnDistributionArrayOutput() CdnDistributionArrayOutput
	ToCdnDistributionArrayOutputWithContext(context.Context) CdnDistributionArrayOutput
}

type CdnDistributionArray []CdnDistributionInput

func (CdnDistributionArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*CdnDistribution)(nil)).Elem()
}

func (i CdnDistributionArray) ToCdnDistributionArrayOutput() CdnDistributionArrayOutput {
	return i.ToCdnDistributionArrayOutputWithContext(context.Background())
}

func (i CdnDistributionArray) ToCdnDistributionArrayOutputWithContext(ctx context.Context) CdnDistributionArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CdnDistributionArrayOutput)
}

// CdnDistributionMapInput is an input type that accepts CdnDistributionMap and CdnDistributionMapOutput values.
// You can construct a concrete instance of `CdnDistributionMapInput` via:
//
//	CdnDistributionMap{ "key": CdnDistributionArgs{...} }
type CdnDistributionMapInput interface {
	pulumi.Input

	ToCdnDistributionMapOutput() CdnDistributionMapOutput
	ToCdnDistributionMapOutputWithContext(context.Context) CdnDistributionMapOutput
}

type CdnDistributionMap map[string]CdnDistributionInput

func (CdnDistributionMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*CdnDistribution)(nil)).Elem()
}

func (i CdnDistributionMap) ToCdnDistributionMapOutput() CdnDistributionMapOutput {
	return i.ToCdnDistributionMapOutputWithContext(context.Background())
}

func (i CdnDistributionMap) ToCdnDistributionMapOutputWithContext(ctx context.Context) CdnDistributionMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CdnDistributionMapOutput)
}

type CdnDistributionOutput struct{ *pulumi.OutputState }

func (CdnDistributionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**CdnDistribution)(nil)).Elem()
}

func (o CdnDistributionOutput) ToCdnDistributionOutput() CdnDistributionOutput {
	return o
}

func (o CdnDistributionOutput) ToCdnDistributionOutputWithContext(ctx context.Context) CdnDistributionOutput {
	return o
}

// [string] The ID of the certificate to use for the distribution. You can create certificates with the certificate resource.
func (o CdnDistributionOutput) CertificateId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *CdnDistribution) pulumi.StringPtrOutput { return v.CertificateId }).(pulumi.StringPtrOutput)
}

// [string] The domain of the distribution.
func (o CdnDistributionOutput) Domain() pulumi.StringOutput {
	return o.ApplyT(func(v *CdnDistribution) pulumi.StringOutput { return v.Domain }).(pulumi.StringOutput)
}

// IP of the distribution, it has to be included on the domain DNS Zone as A record.
func (o CdnDistributionOutput) PublicEndpointV4() pulumi.StringOutput {
	return o.ApplyT(func(v *CdnDistribution) pulumi.StringOutput { return v.PublicEndpointV4 }).(pulumi.StringOutput)
}

// IP of the distribution, it has to be included on the domain DNS Zone as AAAA record.
func (o CdnDistributionOutput) PublicEndpointV6() pulumi.StringOutput {
	return o.ApplyT(func(v *CdnDistribution) pulumi.StringOutput { return v.PublicEndpointV6 }).(pulumi.StringOutput)
}

// Unique resource indentifier.
func (o CdnDistributionOutput) ResourceUrn() pulumi.StringOutput {
	return o.ApplyT(func(v *CdnDistribution) pulumi.StringOutput { return v.ResourceUrn }).(pulumi.StringOutput)
}

// [list] The routing rules for the distribution.
func (o CdnDistributionOutput) RoutingRules() CdnDistributionRoutingRuleArrayOutput {
	return o.ApplyT(func(v *CdnDistribution) CdnDistributionRoutingRuleArrayOutput { return v.RoutingRules }).(CdnDistributionRoutingRuleArrayOutput)
}

type CdnDistributionArrayOutput struct{ *pulumi.OutputState }

func (CdnDistributionArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*CdnDistribution)(nil)).Elem()
}

func (o CdnDistributionArrayOutput) ToCdnDistributionArrayOutput() CdnDistributionArrayOutput {
	return o
}

func (o CdnDistributionArrayOutput) ToCdnDistributionArrayOutputWithContext(ctx context.Context) CdnDistributionArrayOutput {
	return o
}

func (o CdnDistributionArrayOutput) Index(i pulumi.IntInput) CdnDistributionOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *CdnDistribution {
		return vs[0].([]*CdnDistribution)[vs[1].(int)]
	}).(CdnDistributionOutput)
}

type CdnDistributionMapOutput struct{ *pulumi.OutputState }

func (CdnDistributionMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*CdnDistribution)(nil)).Elem()
}

func (o CdnDistributionMapOutput) ToCdnDistributionMapOutput() CdnDistributionMapOutput {
	return o
}

func (o CdnDistributionMapOutput) ToCdnDistributionMapOutputWithContext(ctx context.Context) CdnDistributionMapOutput {
	return o
}

func (o CdnDistributionMapOutput) MapIndex(k pulumi.StringInput) CdnDistributionOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *CdnDistribution {
		return vs[0].(map[string]*CdnDistribution)[vs[1].(string)]
	}).(CdnDistributionOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*CdnDistributionInput)(nil)).Elem(), &CdnDistribution{})
	pulumi.RegisterInputType(reflect.TypeOf((*CdnDistributionArrayInput)(nil)).Elem(), CdnDistributionArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*CdnDistributionMapInput)(nil)).Elem(), CdnDistributionMap{})
	pulumi.RegisterOutputType(CdnDistributionOutput{})
	pulumi.RegisterOutputType(CdnDistributionArrayOutput{})
	pulumi.RegisterOutputType(CdnDistributionMapOutput{})
}
