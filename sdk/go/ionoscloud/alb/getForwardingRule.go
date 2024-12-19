// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package alb

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The Application Load Balancer Forwarding Rule data source can be used to search for and return an existing Application Load Balancer Forwarding Rules.
// You can provide a string for the name parameter which will be compared with provisioned Application Load Balancers Forwarding Rules.
// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
// When this happens, please refine your search and make sure that your resources have unique names.
//
// ## Example Usage
//
// ### By Name
// ```go
// package main
//
// import (
//
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/alb"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := alb.LookupForwardingRule(ctx, &alb.LookupForwardingRuleArgs{
//				DatacenterId:              exampleIonoscloudDatacenter.Id,
//				ApplicationLoadbalancerId: exampleIonoscloudApplicationLoadbalancer.Id,
//				Name:                      pulumi.StringRef("ALB FR Example"),
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
// ### By Name with Partial Match
// ```go
// package main
//
// import (
//
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/alb"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := alb.LookupForwardingRule(ctx, &alb.LookupForwardingRuleArgs{
//				DatacenterId:              exampleIonoscloudDatacenter.Id,
//				ApplicationLoadbalancerId: exampleIonoscloudApplicationLoadbalancer.Id,
//				Name:                      pulumi.StringRef("Example"),
//				PartialMatch:              pulumi.BoolRef(true),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func LookupForwardingRule(ctx *pulumi.Context, args *LookupForwardingRuleArgs, opts ...pulumi.InvokeOption) (*LookupForwardingRuleResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupForwardingRuleResult
	err := ctx.Invoke("ionoscloud:alb/getForwardingRule:getForwardingRule", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getForwardingRule.
type LookupForwardingRuleArgs struct {
	// Application Load Balancer's UUID.
	ApplicationLoadbalancerId string `pulumi:"applicationLoadbalancerId"`
	// Datacenter's UUID.
	DatacenterId string `pulumi:"datacenterId"`
	// ID of the application load balancer you want to search for.
	Id *string `pulumi:"id"`
	// Name of an existing application load balancer that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partialMatch` parameter is not set to true.
	Name *string `pulumi:"name"`
	// Whether partial matching is allowed or not when using name argument. Default value is false.
	//
	// Both `datacenterId` and `applicationLoadbalancerId` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
	PartialMatch *bool `pulumi:"partialMatch"`
}

// A collection of values returned by getForwardingRule.
type LookupForwardingRuleResult struct {
	ApplicationLoadbalancerId string `pulumi:"applicationLoadbalancerId"`
	// The maximum time in milliseconds to wait for the client to acknowledge or send data; default is 50,000 (50 seconds).
	// - `server certificates` - Array of items in that collection.
	ClientTimeout int    `pulumi:"clientTimeout"`
	DatacenterId  string `pulumi:"datacenterId"`
	// Array of items in that collection
	HttpRules []GetForwardingRuleHttpRule `pulumi:"httpRules"`
	// Id of Application Load Balancer Forwarding Rule
	Id *string `pulumi:"id"`
	// Listening (inbound) IP.
	ListenerIp string `pulumi:"listenerIp"`
	// Listening (inbound) port number; valid range is 1 to 65535.
	ListenerPort int `pulumi:"listenerPort"`
	// The unique name of the Application Load Balancer HTTP rule.
	Name         *string `pulumi:"name"`
	PartialMatch *bool   `pulumi:"partialMatch"`
	// Balancing protocol.
	Protocol           string   `pulumi:"protocol"`
	ServerCertificates []string `pulumi:"serverCertificates"`
}

func LookupForwardingRuleOutput(ctx *pulumi.Context, args LookupForwardingRuleOutputArgs, opts ...pulumi.InvokeOption) LookupForwardingRuleResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupForwardingRuleResultOutput, error) {
			args := v.(LookupForwardingRuleArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("ionoscloud:alb/getForwardingRule:getForwardingRule", args, LookupForwardingRuleResultOutput{}, options).(LookupForwardingRuleResultOutput), nil
		}).(LookupForwardingRuleResultOutput)
}

// A collection of arguments for invoking getForwardingRule.
type LookupForwardingRuleOutputArgs struct {
	// Application Load Balancer's UUID.
	ApplicationLoadbalancerId pulumi.StringInput `pulumi:"applicationLoadbalancerId"`
	// Datacenter's UUID.
	DatacenterId pulumi.StringInput `pulumi:"datacenterId"`
	// ID of the application load balancer you want to search for.
	Id pulumi.StringPtrInput `pulumi:"id"`
	// Name of an existing application load balancer that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partialMatch` parameter is not set to true.
	Name pulumi.StringPtrInput `pulumi:"name"`
	// Whether partial matching is allowed or not when using name argument. Default value is false.
	//
	// Both `datacenterId` and `applicationLoadbalancerId` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
	PartialMatch pulumi.BoolPtrInput `pulumi:"partialMatch"`
}

func (LookupForwardingRuleOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupForwardingRuleArgs)(nil)).Elem()
}

// A collection of values returned by getForwardingRule.
type LookupForwardingRuleResultOutput struct{ *pulumi.OutputState }

func (LookupForwardingRuleResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupForwardingRuleResult)(nil)).Elem()
}

func (o LookupForwardingRuleResultOutput) ToLookupForwardingRuleResultOutput() LookupForwardingRuleResultOutput {
	return o
}

func (o LookupForwardingRuleResultOutput) ToLookupForwardingRuleResultOutputWithContext(ctx context.Context) LookupForwardingRuleResultOutput {
	return o
}

func (o LookupForwardingRuleResultOutput) ApplicationLoadbalancerId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupForwardingRuleResult) string { return v.ApplicationLoadbalancerId }).(pulumi.StringOutput)
}

// The maximum time in milliseconds to wait for the client to acknowledge or send data; default is 50,000 (50 seconds).
// - `server certificates` - Array of items in that collection.
func (o LookupForwardingRuleResultOutput) ClientTimeout() pulumi.IntOutput {
	return o.ApplyT(func(v LookupForwardingRuleResult) int { return v.ClientTimeout }).(pulumi.IntOutput)
}

func (o LookupForwardingRuleResultOutput) DatacenterId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupForwardingRuleResult) string { return v.DatacenterId }).(pulumi.StringOutput)
}

// Array of items in that collection
func (o LookupForwardingRuleResultOutput) HttpRules() GetForwardingRuleHttpRuleArrayOutput {
	return o.ApplyT(func(v LookupForwardingRuleResult) []GetForwardingRuleHttpRule { return v.HttpRules }).(GetForwardingRuleHttpRuleArrayOutput)
}

// Id of Application Load Balancer Forwarding Rule
func (o LookupForwardingRuleResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupForwardingRuleResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// Listening (inbound) IP.
func (o LookupForwardingRuleResultOutput) ListenerIp() pulumi.StringOutput {
	return o.ApplyT(func(v LookupForwardingRuleResult) string { return v.ListenerIp }).(pulumi.StringOutput)
}

// Listening (inbound) port number; valid range is 1 to 65535.
func (o LookupForwardingRuleResultOutput) ListenerPort() pulumi.IntOutput {
	return o.ApplyT(func(v LookupForwardingRuleResult) int { return v.ListenerPort }).(pulumi.IntOutput)
}

// The unique name of the Application Load Balancer HTTP rule.
func (o LookupForwardingRuleResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupForwardingRuleResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o LookupForwardingRuleResultOutput) PartialMatch() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupForwardingRuleResult) *bool { return v.PartialMatch }).(pulumi.BoolPtrOutput)
}

// Balancing protocol.
func (o LookupForwardingRuleResultOutput) Protocol() pulumi.StringOutput {
	return o.ApplyT(func(v LookupForwardingRuleResult) string { return v.Protocol }).(pulumi.StringOutput)
}

func (o LookupForwardingRuleResultOutput) ServerCertificates() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupForwardingRuleResult) []string { return v.ServerCertificates }).(pulumi.StringArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupForwardingRuleResultOutput{})
}
