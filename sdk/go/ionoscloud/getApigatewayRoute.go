// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ionoscloud

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The **API Gateway Route data source** can be used to search for and return an existing API Gateway route.
// You can provide a string for the name parameter which will be compared with provisioned API Gateway routes.
// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
// When this happens, please refine your search string so that it is specific enough to return only one result.
//
// ## Example Usage
func LookupApigatewayRoute(ctx *pulumi.Context, args *LookupApigatewayRouteArgs, opts ...pulumi.InvokeOption) (*LookupApigatewayRouteResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupApigatewayRouteResult
	err := ctx.Invoke("ionoscloud:index/getApigatewayRoute:getApigatewayRoute", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getApigatewayRoute.
type LookupApigatewayRouteArgs struct {
	// The ID of the API Gateway that the route belongs to.
	GatewayId string `pulumi:"gatewayId"`
	// ID of an existing API Gateway Route that you want to search for.
	Id *string `pulumi:"id"`
	// Name of an existing API Gateway Route that you want to search for.
	Name         *string `pulumi:"name"`
	PartialMatch *bool   `pulumi:"partialMatch"`
}

// A collection of values returned by getApigatewayRoute.
type LookupApigatewayRouteResult struct {
	GatewayId string `pulumi:"gatewayId"`
	// ID of the API Gateway Route.
	Id string `pulumi:"id"`
	// The HTTP methods that the route should match.
	Methods []string `pulumi:"methods"`
	// The name of the API Gateway Route.
	Name         string `pulumi:"name"`
	PartialMatch *bool  `pulumi:"partialMatch"`
	// The paths that the route should match.
	Paths []string `pulumi:"paths"`
	// This field specifies the protocol used by the ingress to route traffic to the backend service.
	Type      string                       `pulumi:"type"`
	Upstreams []GetApigatewayRouteUpstream `pulumi:"upstreams"`
	// Shows whether websocket support is enabled or disabled.
	Websocket bool `pulumi:"websocket"`
}

func LookupApigatewayRouteOutput(ctx *pulumi.Context, args LookupApigatewayRouteOutputArgs, opts ...pulumi.InvokeOption) LookupApigatewayRouteResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupApigatewayRouteResultOutput, error) {
			args := v.(LookupApigatewayRouteArgs)
			opts = internal.PkgInvokeDefaultOpts(opts)
			var rv LookupApigatewayRouteResult
			secret, err := ctx.InvokePackageRaw("ionoscloud:index/getApigatewayRoute:getApigatewayRoute", args, &rv, "", opts...)
			if err != nil {
				return LookupApigatewayRouteResultOutput{}, err
			}

			output := pulumi.ToOutput(rv).(LookupApigatewayRouteResultOutput)
			if secret {
				return pulumi.ToSecret(output).(LookupApigatewayRouteResultOutput), nil
			}
			return output, nil
		}).(LookupApigatewayRouteResultOutput)
}

// A collection of arguments for invoking getApigatewayRoute.
type LookupApigatewayRouteOutputArgs struct {
	// The ID of the API Gateway that the route belongs to.
	GatewayId pulumi.StringInput `pulumi:"gatewayId"`
	// ID of an existing API Gateway Route that you want to search for.
	Id pulumi.StringPtrInput `pulumi:"id"`
	// Name of an existing API Gateway Route that you want to search for.
	Name         pulumi.StringPtrInput `pulumi:"name"`
	PartialMatch pulumi.BoolPtrInput   `pulumi:"partialMatch"`
}

func (LookupApigatewayRouteOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupApigatewayRouteArgs)(nil)).Elem()
}

// A collection of values returned by getApigatewayRoute.
type LookupApigatewayRouteResultOutput struct{ *pulumi.OutputState }

func (LookupApigatewayRouteResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupApigatewayRouteResult)(nil)).Elem()
}

func (o LookupApigatewayRouteResultOutput) ToLookupApigatewayRouteResultOutput() LookupApigatewayRouteResultOutput {
	return o
}

func (o LookupApigatewayRouteResultOutput) ToLookupApigatewayRouteResultOutputWithContext(ctx context.Context) LookupApigatewayRouteResultOutput {
	return o
}

func (o LookupApigatewayRouteResultOutput) GatewayId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupApigatewayRouteResult) string { return v.GatewayId }).(pulumi.StringOutput)
}

// ID of the API Gateway Route.
func (o LookupApigatewayRouteResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupApigatewayRouteResult) string { return v.Id }).(pulumi.StringOutput)
}

// The HTTP methods that the route should match.
func (o LookupApigatewayRouteResultOutput) Methods() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupApigatewayRouteResult) []string { return v.Methods }).(pulumi.StringArrayOutput)
}

// The name of the API Gateway Route.
func (o LookupApigatewayRouteResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupApigatewayRouteResult) string { return v.Name }).(pulumi.StringOutput)
}

func (o LookupApigatewayRouteResultOutput) PartialMatch() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupApigatewayRouteResult) *bool { return v.PartialMatch }).(pulumi.BoolPtrOutput)
}

// The paths that the route should match.
func (o LookupApigatewayRouteResultOutput) Paths() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupApigatewayRouteResult) []string { return v.Paths }).(pulumi.StringArrayOutput)
}

// This field specifies the protocol used by the ingress to route traffic to the backend service.
func (o LookupApigatewayRouteResultOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v LookupApigatewayRouteResult) string { return v.Type }).(pulumi.StringOutput)
}

func (o LookupApigatewayRouteResultOutput) Upstreams() GetApigatewayRouteUpstreamArrayOutput {
	return o.ApplyT(func(v LookupApigatewayRouteResult) []GetApigatewayRouteUpstream { return v.Upstreams }).(GetApigatewayRouteUpstreamArrayOutput)
}

// Shows whether websocket support is enabled or disabled.
func (o LookupApigatewayRouteResultOutput) Websocket() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupApigatewayRouteResult) bool { return v.Websocket }).(pulumi.BoolOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupApigatewayRouteResultOutput{})
}
