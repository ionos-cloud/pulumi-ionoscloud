// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ionoscloud

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The **Dataplatform Node Pools Data Source** can be used to search for and return a list of existing Dataplatform Node Pools under a Dataplatform Cluster.
//
// ## Example Usage
func GetDataplatformNodePools(ctx *pulumi.Context, args *GetDataplatformNodePoolsArgs, opts ...pulumi.InvokeOption) (*GetDataplatformNodePoolsResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetDataplatformNodePoolsResult
	err := ctx.Invoke("ionoscloud:index/getDataplatformNodePools:getDataplatformNodePools", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getDataplatformNodePools.
type GetDataplatformNodePoolsArgs struct {
	// ID of the cluster the searched node pool is part of.
	ClusterId string `pulumi:"clusterId"`
	// Name of an existing cluster that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partialMatch` parameter is not set to true.
	Name *string `pulumi:"name"`
	// Whether partial matching is allowed or not when using name argument. Default value is false.
	PartialMatch *bool `pulumi:"partialMatch"`
}

// A collection of values returned by getDataplatformNodePools.
type GetDataplatformNodePoolsResult struct {
	// ID of the cluster the searched node pool is part of.
	ClusterId string `pulumi:"clusterId"`
	// The provider-assigned unique ID for this managed resource.
	Id   string  `pulumi:"id"`
	Name *string `pulumi:"name"`
	// List of Node Pools - See the Node Pool section.
	NodePools    []GetDataplatformNodePoolsNodePool `pulumi:"nodePools"`
	PartialMatch *bool                              `pulumi:"partialMatch"`
}

func GetDataplatformNodePoolsOutput(ctx *pulumi.Context, args GetDataplatformNodePoolsOutputArgs, opts ...pulumi.InvokeOption) GetDataplatformNodePoolsResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetDataplatformNodePoolsResult, error) {
			args := v.(GetDataplatformNodePoolsArgs)
			r, err := GetDataplatformNodePools(ctx, &args, opts...)
			var s GetDataplatformNodePoolsResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetDataplatformNodePoolsResultOutput)
}

// A collection of arguments for invoking getDataplatformNodePools.
type GetDataplatformNodePoolsOutputArgs struct {
	// ID of the cluster the searched node pool is part of.
	ClusterId pulumi.StringInput `pulumi:"clusterId"`
	// Name of an existing cluster that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partialMatch` parameter is not set to true.
	Name pulumi.StringPtrInput `pulumi:"name"`
	// Whether partial matching is allowed or not when using name argument. Default value is false.
	PartialMatch pulumi.BoolPtrInput `pulumi:"partialMatch"`
}

func (GetDataplatformNodePoolsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetDataplatformNodePoolsArgs)(nil)).Elem()
}

// A collection of values returned by getDataplatformNodePools.
type GetDataplatformNodePoolsResultOutput struct{ *pulumi.OutputState }

func (GetDataplatformNodePoolsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetDataplatformNodePoolsResult)(nil)).Elem()
}

func (o GetDataplatformNodePoolsResultOutput) ToGetDataplatformNodePoolsResultOutput() GetDataplatformNodePoolsResultOutput {
	return o
}

func (o GetDataplatformNodePoolsResultOutput) ToGetDataplatformNodePoolsResultOutputWithContext(ctx context.Context) GetDataplatformNodePoolsResultOutput {
	return o
}

// ID of the cluster the searched node pool is part of.
func (o GetDataplatformNodePoolsResultOutput) ClusterId() pulumi.StringOutput {
	return o.ApplyT(func(v GetDataplatformNodePoolsResult) string { return v.ClusterId }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetDataplatformNodePoolsResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetDataplatformNodePoolsResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o GetDataplatformNodePoolsResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetDataplatformNodePoolsResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

// List of Node Pools - See the Node Pool section.
func (o GetDataplatformNodePoolsResultOutput) NodePools() GetDataplatformNodePoolsNodePoolArrayOutput {
	return o.ApplyT(func(v GetDataplatformNodePoolsResult) []GetDataplatformNodePoolsNodePool { return v.NodePools }).(GetDataplatformNodePoolsNodePoolArrayOutput)
}

func (o GetDataplatformNodePoolsResultOutput) PartialMatch() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v GetDataplatformNodePoolsResult) *bool { return v.PartialMatch }).(pulumi.BoolPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(GetDataplatformNodePoolsResultOutput{})
}
