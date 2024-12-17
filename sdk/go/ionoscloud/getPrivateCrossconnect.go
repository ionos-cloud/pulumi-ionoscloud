// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ionoscloud

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The **Cross Connect data source** can be used to search for and return existing cross connects.
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
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := ionoscloud.GetPrivateCrossconnect(ctx, &ionoscloud.GetPrivateCrossconnectArgs{
//				Name: pulumi.StringRef("Cross Connect Example"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func GetPrivateCrossconnect(ctx *pulumi.Context, args *GetPrivateCrossconnectArgs, opts ...pulumi.InvokeOption) (*GetPrivateCrossconnectResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetPrivateCrossconnectResult
	err := ctx.Invoke("ionoscloud:index/getPrivateCrossconnect:getPrivateCrossconnect", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getPrivateCrossconnect.
type GetPrivateCrossconnectArgs struct {
	// Description of cross connect
	Description *string `pulumi:"description"`
	// ID of the cross connect you want to search for.
	//
	// Either `name` or `id` must be provided. If none, or both are provided, the datasource will return an error.
	Id *string `pulumi:"id"`
	// Name of an existing cross connect that you want to search for.
	Name *string `pulumi:"name"`
}

// A collection of values returned by getPrivateCrossconnect.
type GetPrivateCrossconnectResult struct {
	// Lists datacenters that can be joined to this cross connect
	ConnectableDatacenters []GetPrivateCrossconnectConnectableDatacenter `pulumi:"connectableDatacenters"`
	// Description of cross connect
	Description *string `pulumi:"description"`
	// The UUID of the connectable datacenter
	Id *string `pulumi:"id"`
	// The name of the connectable datacenter
	Name *string `pulumi:"name"`
	// Lists LAN's joined to this cross connect
	Peers []GetPrivateCrossconnectPeer `pulumi:"peers"`
}

func GetPrivateCrossconnectOutput(ctx *pulumi.Context, args GetPrivateCrossconnectOutputArgs, opts ...pulumi.InvokeOption) GetPrivateCrossconnectResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (GetPrivateCrossconnectResultOutput, error) {
			args := v.(GetPrivateCrossconnectArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("ionoscloud:index/getPrivateCrossconnect:getPrivateCrossconnect", args, GetPrivateCrossconnectResultOutput{}, options).(GetPrivateCrossconnectResultOutput), nil
		}).(GetPrivateCrossconnectResultOutput)
}

// A collection of arguments for invoking getPrivateCrossconnect.
type GetPrivateCrossconnectOutputArgs struct {
	// Description of cross connect
	Description pulumi.StringPtrInput `pulumi:"description"`
	// ID of the cross connect you want to search for.
	//
	// Either `name` or `id` must be provided. If none, or both are provided, the datasource will return an error.
	Id pulumi.StringPtrInput `pulumi:"id"`
	// Name of an existing cross connect that you want to search for.
	Name pulumi.StringPtrInput `pulumi:"name"`
}

func (GetPrivateCrossconnectOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetPrivateCrossconnectArgs)(nil)).Elem()
}

// A collection of values returned by getPrivateCrossconnect.
type GetPrivateCrossconnectResultOutput struct{ *pulumi.OutputState }

func (GetPrivateCrossconnectResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetPrivateCrossconnectResult)(nil)).Elem()
}

func (o GetPrivateCrossconnectResultOutput) ToGetPrivateCrossconnectResultOutput() GetPrivateCrossconnectResultOutput {
	return o
}

func (o GetPrivateCrossconnectResultOutput) ToGetPrivateCrossconnectResultOutputWithContext(ctx context.Context) GetPrivateCrossconnectResultOutput {
	return o
}

// Lists datacenters that can be joined to this cross connect
func (o GetPrivateCrossconnectResultOutput) ConnectableDatacenters() GetPrivateCrossconnectConnectableDatacenterArrayOutput {
	return o.ApplyT(func(v GetPrivateCrossconnectResult) []GetPrivateCrossconnectConnectableDatacenter {
		return v.ConnectableDatacenters
	}).(GetPrivateCrossconnectConnectableDatacenterArrayOutput)
}

// Description of cross connect
func (o GetPrivateCrossconnectResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetPrivateCrossconnectResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// The UUID of the connectable datacenter
func (o GetPrivateCrossconnectResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetPrivateCrossconnectResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// The name of the connectable datacenter
func (o GetPrivateCrossconnectResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetPrivateCrossconnectResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

// Lists LAN's joined to this cross connect
func (o GetPrivateCrossconnectResultOutput) Peers() GetPrivateCrossconnectPeerArrayOutput {
	return o.ApplyT(func(v GetPrivateCrossconnectResult) []GetPrivateCrossconnectPeer { return v.Peers }).(GetPrivateCrossconnectPeerArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(GetPrivateCrossconnectResultOutput{})
}
