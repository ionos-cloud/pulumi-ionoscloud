// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package dbaas

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The **DbaaS Mongo User data source** can be used to search for and return an existing DbaaS MongoDB User.
// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
// When this happens, please refine your search string so that it is specific enough to return only one result.
//
// ## Example Usage
//
// ### By username
// ```go
// package main
//
// import (
//
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/dbaas"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := dbaas.LookupMongoUser(ctx, &dbaas.LookupMongoUserArgs{
//				ClusterId: "cluster_id",
//				Username:  "username",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func LookupMongoUser(ctx *pulumi.Context, args *LookupMongoUserArgs, opts ...pulumi.InvokeOption) (*LookupMongoUserResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupMongoUserResult
	err := ctx.Invoke("ionoscloud:dbaas/getMongoUser:getMongoUser", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getMongoUser.
type LookupMongoUserArgs struct {
	// [string] The unique ID of the cluster. Updates to the value of the field force the cluster to be re-created.
	ClusterId string `pulumi:"clusterId"`
	// [string] The user database to use for authentication. Updates to the value of the field force the cluster to be re-created.
	Database *string `pulumi:"database"`
	Id       *string `pulumi:"id"`
	// [string] a list of mongodb user roles. Updates to the value of the field force the cluster to be re-created.
	Roles []GetMongoUserRole `pulumi:"roles"`
	// [string] Used for authentication. Updates to the value of the field force the cluster to be re-created.
	Username string `pulumi:"username"`
}

// A collection of values returned by getMongoUser.
type LookupMongoUserResult struct {
	ClusterId string             `pulumi:"clusterId"`
	Database  string             `pulumi:"database"`
	Id        string             `pulumi:"id"`
	Roles     []GetMongoUserRole `pulumi:"roles"`
	Username  string             `pulumi:"username"`
}

func LookupMongoUserOutput(ctx *pulumi.Context, args LookupMongoUserOutputArgs, opts ...pulumi.InvokeOption) LookupMongoUserResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupMongoUserResultOutput, error) {
			args := v.(LookupMongoUserArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("ionoscloud:dbaas/getMongoUser:getMongoUser", args, LookupMongoUserResultOutput{}, options).(LookupMongoUserResultOutput), nil
		}).(LookupMongoUserResultOutput)
}

// A collection of arguments for invoking getMongoUser.
type LookupMongoUserOutputArgs struct {
	// [string] The unique ID of the cluster. Updates to the value of the field force the cluster to be re-created.
	ClusterId pulumi.StringInput `pulumi:"clusterId"`
	// [string] The user database to use for authentication. Updates to the value of the field force the cluster to be re-created.
	Database pulumi.StringPtrInput `pulumi:"database"`
	Id       pulumi.StringPtrInput `pulumi:"id"`
	// [string] a list of mongodb user roles. Updates to the value of the field force the cluster to be re-created.
	Roles GetMongoUserRoleArrayInput `pulumi:"roles"`
	// [string] Used for authentication. Updates to the value of the field force the cluster to be re-created.
	Username pulumi.StringInput `pulumi:"username"`
}

func (LookupMongoUserOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupMongoUserArgs)(nil)).Elem()
}

// A collection of values returned by getMongoUser.
type LookupMongoUserResultOutput struct{ *pulumi.OutputState }

func (LookupMongoUserResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupMongoUserResult)(nil)).Elem()
}

func (o LookupMongoUserResultOutput) ToLookupMongoUserResultOutput() LookupMongoUserResultOutput {
	return o
}

func (o LookupMongoUserResultOutput) ToLookupMongoUserResultOutputWithContext(ctx context.Context) LookupMongoUserResultOutput {
	return o
}

func (o LookupMongoUserResultOutput) ClusterId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupMongoUserResult) string { return v.ClusterId }).(pulumi.StringOutput)
}

func (o LookupMongoUserResultOutput) Database() pulumi.StringOutput {
	return o.ApplyT(func(v LookupMongoUserResult) string { return v.Database }).(pulumi.StringOutput)
}

func (o LookupMongoUserResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupMongoUserResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o LookupMongoUserResultOutput) Roles() GetMongoUserRoleArrayOutput {
	return o.ApplyT(func(v LookupMongoUserResult) []GetMongoUserRole { return v.Roles }).(GetMongoUserRoleArrayOutput)
}

func (o LookupMongoUserResultOutput) Username() pulumi.StringOutput {
	return o.ApplyT(func(v LookupMongoUserResult) string { return v.Username }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupMongoUserResultOutput{})
}
