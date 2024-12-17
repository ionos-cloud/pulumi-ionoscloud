// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ionoscloud

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
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := ionoscloud.LookupApplicationLoadbalancerForwardingrule(ctx, &ionoscloud.LookupApplicationLoadbalancerForwardingruleArgs{
//				DatacenterId:              ionoscloud_datacenter.Example.Id,
//				ApplicationLoadbalancerId: ionoscloud_application_loadbalancer.Example.Id,
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
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := ionoscloud.LookupApplicationLoadbalancerForwardingrule(ctx, &ionoscloud.LookupApplicationLoadbalancerForwardingruleArgs{
//				DatacenterId:              ionoscloud_datacenter.Example.Id,
//				ApplicationLoadbalancerId: ionoscloud_application_loadbalancer.Example.Id,
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
func LookupApplicationLoadbalancerForwardingrule(ctx *pulumi.Context, args *LookupApplicationLoadbalancerForwardingruleArgs, opts ...pulumi.InvokeOption) (*LookupApplicationLoadbalancerForwardingruleResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupApplicationLoadbalancerForwardingruleResult
	err := ctx.Invoke("ionoscloud:index/getApplicationLoadbalancerForwardingrule:getApplicationLoadbalancerForwardingrule", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getApplicationLoadbalancerForwardingrule.
type LookupApplicationLoadbalancerForwardingruleArgs struct {
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

// A collection of values returned by getApplicationLoadbalancerForwardingrule.
type LookupApplicationLoadbalancerForwardingruleResult struct {
	ApplicationLoadbalancerId string `pulumi:"applicationLoadbalancerId"`
	// The maximum time in milliseconds to wait for the client to acknowledge or send data; default is 50,000 (50 seconds).
	// - `server certificates` - Array of items in that collection.
	ClientTimeout int    `pulumi:"clientTimeout"`
	DatacenterId  string `pulumi:"datacenterId"`
	// Array of items in that collection
	HttpRules []GetApplicationLoadbalancerForwardingruleHttpRule `pulumi:"httpRules"`
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

func LookupApplicationLoadbalancerForwardingruleOutput(ctx *pulumi.Context, args LookupApplicationLoadbalancerForwardingruleOutputArgs, opts ...pulumi.InvokeOption) LookupApplicationLoadbalancerForwardingruleResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupApplicationLoadbalancerForwardingruleResultOutput, error) {
			args := v.(LookupApplicationLoadbalancerForwardingruleArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("ionoscloud:index/getApplicationLoadbalancerForwardingrule:getApplicationLoadbalancerForwardingrule", args, LookupApplicationLoadbalancerForwardingruleResultOutput{}, options).(LookupApplicationLoadbalancerForwardingruleResultOutput), nil
		}).(LookupApplicationLoadbalancerForwardingruleResultOutput)
}

// A collection of arguments for invoking getApplicationLoadbalancerForwardingrule.
type LookupApplicationLoadbalancerForwardingruleOutputArgs struct {
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

func (LookupApplicationLoadbalancerForwardingruleOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupApplicationLoadbalancerForwardingruleArgs)(nil)).Elem()
}

// A collection of values returned by getApplicationLoadbalancerForwardingrule.
type LookupApplicationLoadbalancerForwardingruleResultOutput struct{ *pulumi.OutputState }

func (LookupApplicationLoadbalancerForwardingruleResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupApplicationLoadbalancerForwardingruleResult)(nil)).Elem()
}

func (o LookupApplicationLoadbalancerForwardingruleResultOutput) ToLookupApplicationLoadbalancerForwardingruleResultOutput() LookupApplicationLoadbalancerForwardingruleResultOutput {
	return o
}

func (o LookupApplicationLoadbalancerForwardingruleResultOutput) ToLookupApplicationLoadbalancerForwardingruleResultOutputWithContext(ctx context.Context) LookupApplicationLoadbalancerForwardingruleResultOutput {
	return o
}

func (o LookupApplicationLoadbalancerForwardingruleResultOutput) ApplicationLoadbalancerId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupApplicationLoadbalancerForwardingruleResult) string { return v.ApplicationLoadbalancerId }).(pulumi.StringOutput)
}

// The maximum time in milliseconds to wait for the client to acknowledge or send data; default is 50,000 (50 seconds).
// - `server certificates` - Array of items in that collection.
func (o LookupApplicationLoadbalancerForwardingruleResultOutput) ClientTimeout() pulumi.IntOutput {
	return o.ApplyT(func(v LookupApplicationLoadbalancerForwardingruleResult) int { return v.ClientTimeout }).(pulumi.IntOutput)
}

func (o LookupApplicationLoadbalancerForwardingruleResultOutput) DatacenterId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupApplicationLoadbalancerForwardingruleResult) string { return v.DatacenterId }).(pulumi.StringOutput)
}

// Array of items in that collection
func (o LookupApplicationLoadbalancerForwardingruleResultOutput) HttpRules() GetApplicationLoadbalancerForwardingruleHttpRuleArrayOutput {
	return o.ApplyT(func(v LookupApplicationLoadbalancerForwardingruleResult) []GetApplicationLoadbalancerForwardingruleHttpRule {
		return v.HttpRules
	}).(GetApplicationLoadbalancerForwardingruleHttpRuleArrayOutput)
}

// Id of Application Load Balancer Forwarding Rule
func (o LookupApplicationLoadbalancerForwardingruleResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupApplicationLoadbalancerForwardingruleResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// Listening (inbound) IP.
func (o LookupApplicationLoadbalancerForwardingruleResultOutput) ListenerIp() pulumi.StringOutput {
	return o.ApplyT(func(v LookupApplicationLoadbalancerForwardingruleResult) string { return v.ListenerIp }).(pulumi.StringOutput)
}

// Listening (inbound) port number; valid range is 1 to 65535.
func (o LookupApplicationLoadbalancerForwardingruleResultOutput) ListenerPort() pulumi.IntOutput {
	return o.ApplyT(func(v LookupApplicationLoadbalancerForwardingruleResult) int { return v.ListenerPort }).(pulumi.IntOutput)
}

// The unique name of the Application Load Balancer HTTP rule.
func (o LookupApplicationLoadbalancerForwardingruleResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupApplicationLoadbalancerForwardingruleResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o LookupApplicationLoadbalancerForwardingruleResultOutput) PartialMatch() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupApplicationLoadbalancerForwardingruleResult) *bool { return v.PartialMatch }).(pulumi.BoolPtrOutput)
}

// Balancing protocol.
func (o LookupApplicationLoadbalancerForwardingruleResultOutput) Protocol() pulumi.StringOutput {
	return o.ApplyT(func(v LookupApplicationLoadbalancerForwardingruleResult) string { return v.Protocol }).(pulumi.StringOutput)
}

func (o LookupApplicationLoadbalancerForwardingruleResultOutput) ServerCertificates() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupApplicationLoadbalancerForwardingruleResult) []string { return v.ServerCertificates }).(pulumi.StringArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupApplicationLoadbalancerForwardingruleResultOutput{})
}
