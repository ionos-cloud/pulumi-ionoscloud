// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The **Share data source** can be used to search for and return an existing share object.
// You need to provide the groupId and resourceId to get the group resources for the shared resource.
// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
// When this happens, please refine your search string so that it is specific enough to return only one result.
func LookupShare(ctx *pulumi.Context, args *LookupShareArgs, opts ...pulumi.InvokeOption) (*LookupShareResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupShareResult
	err := ctx.Invoke("ionoscloud:compute/getShare:getShare", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getShare.
type LookupShareArgs struct {
	// The ID of the specific group containing the resource to update.
	GroupId string `pulumi:"groupId"`
	// The ID of the specific resource to update.
	ResourceId string `pulumi:"resourceId"`
}

// A collection of values returned by getShare.
type LookupShareResult struct {
	// The flag that specifies if the group has permission to edit privileges on this resource.
	EditPrivilege bool `pulumi:"editPrivilege"`
	// The ID of the specific group containing the resource to update.
	GroupId string `pulumi:"groupId"`
	// The id of the share resource.
	Id string `pulumi:"id"`
	// The ID of the specific resource to update.
	ResourceId string `pulumi:"resourceId"`
	// The group has permission to share this resource.
	SharePrivilege bool `pulumi:"sharePrivilege"`
}

func LookupShareOutput(ctx *pulumi.Context, args LookupShareOutputArgs, opts ...pulumi.InvokeOption) LookupShareResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupShareResultOutput, error) {
			args := v.(LookupShareArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("ionoscloud:compute/getShare:getShare", args, LookupShareResultOutput{}, options).(LookupShareResultOutput), nil
		}).(LookupShareResultOutput)
}

// A collection of arguments for invoking getShare.
type LookupShareOutputArgs struct {
	// The ID of the specific group containing the resource to update.
	GroupId pulumi.StringInput `pulumi:"groupId"`
	// The ID of the specific resource to update.
	ResourceId pulumi.StringInput `pulumi:"resourceId"`
}

func (LookupShareOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupShareArgs)(nil)).Elem()
}

// A collection of values returned by getShare.
type LookupShareResultOutput struct{ *pulumi.OutputState }

func (LookupShareResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupShareResult)(nil)).Elem()
}

func (o LookupShareResultOutput) ToLookupShareResultOutput() LookupShareResultOutput {
	return o
}

func (o LookupShareResultOutput) ToLookupShareResultOutputWithContext(ctx context.Context) LookupShareResultOutput {
	return o
}

// The flag that specifies if the group has permission to edit privileges on this resource.
func (o LookupShareResultOutput) EditPrivilege() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupShareResult) bool { return v.EditPrivilege }).(pulumi.BoolOutput)
}

// The ID of the specific group containing the resource to update.
func (o LookupShareResultOutput) GroupId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupShareResult) string { return v.GroupId }).(pulumi.StringOutput)
}

// The id of the share resource.
func (o LookupShareResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupShareResult) string { return v.Id }).(pulumi.StringOutput)
}

// The ID of the specific resource to update.
func (o LookupShareResultOutput) ResourceId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupShareResult) string { return v.ResourceId }).(pulumi.StringOutput)
}

// The group has permission to share this resource.
func (o LookupShareResultOutput) SharePrivilege() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupShareResult) bool { return v.SharePrivilege }).(pulumi.BoolOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupShareResultOutput{})
}
