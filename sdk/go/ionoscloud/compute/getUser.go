// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The **User data source** can be used to search for and return existing users.
// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
// When this happens, please refine your search string so that it is specific enough to return only one result.
//
// ## Example Usage
//
// ### By Email
// ```go
// package main
//
// import (
//
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/compute"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := compute.LookupUser(ctx, &compute.LookupUserArgs{
//				Email: pulumi.StringRef("example@email.com"),
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
// ### By Email from Env Variables - Current User
// data "compute.User" "example" {
// }
func LookupUser(ctx *pulumi.Context, args *LookupUserArgs, opts ...pulumi.InvokeOption) (*LookupUserResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupUserResult
	err := ctx.Invoke("ionoscloud:compute/getUser:getUser", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getUser.
type LookupUserArgs struct {
	// Email of an existing user that you want to search for.
	Email *string `pulumi:"email"`
	// ID of the user you want to search for.
	//
	// Either `email` or `id` can be provided. If no argument is set, the provider will search for the **email that was provided for the configuration**. If none is found, the provider will return an error.
	Id *string `pulumi:"id"`
}

// A collection of values returned by getUser.
type LookupUserResult struct {
	// Indicates if the user is active
	Active bool `pulumi:"active"`
	// Indicates if the user has administrative rights. Administrators do not need to be managed in groups, as they automatically have access to all resources associated with the contract.
	Administrator bool `pulumi:"administrator"`
	// The e-mail address for the user.
	Email *string `pulumi:"email"`
	// The first name for the user.
	FirstName string `pulumi:"firstName"`
	// Indicates if secure (two-factor) authentication should be forced for the user (true) or not (false).
	ForceSecAuth bool `pulumi:"forceSecAuth"`
	// Shows the id and name of the groups that the user is a member of
	Groups []GetUserGroup `pulumi:"groups"`
	// The id of the user.
	Id *string `pulumi:"id"`
	// The last name for the user.
	LastName string `pulumi:"lastName"`
	// Canonical (S3) id of the user for a given identity
	S3CanonicalUserId string `pulumi:"s3CanonicalUserId"`
	// Indicates if secure authentication is active for the user or not
	SecAuthActive bool `pulumi:"secAuthActive"`
}

func LookupUserOutput(ctx *pulumi.Context, args LookupUserOutputArgs, opts ...pulumi.InvokeOption) LookupUserResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupUserResultOutput, error) {
			args := v.(LookupUserArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("ionoscloud:compute/getUser:getUser", args, LookupUserResultOutput{}, options).(LookupUserResultOutput), nil
		}).(LookupUserResultOutput)
}

// A collection of arguments for invoking getUser.
type LookupUserOutputArgs struct {
	// Email of an existing user that you want to search for.
	Email pulumi.StringPtrInput `pulumi:"email"`
	// ID of the user you want to search for.
	//
	// Either `email` or `id` can be provided. If no argument is set, the provider will search for the **email that was provided for the configuration**. If none is found, the provider will return an error.
	Id pulumi.StringPtrInput `pulumi:"id"`
}

func (LookupUserOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupUserArgs)(nil)).Elem()
}

// A collection of values returned by getUser.
type LookupUserResultOutput struct{ *pulumi.OutputState }

func (LookupUserResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupUserResult)(nil)).Elem()
}

func (o LookupUserResultOutput) ToLookupUserResultOutput() LookupUserResultOutput {
	return o
}

func (o LookupUserResultOutput) ToLookupUserResultOutputWithContext(ctx context.Context) LookupUserResultOutput {
	return o
}

// Indicates if the user is active
func (o LookupUserResultOutput) Active() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupUserResult) bool { return v.Active }).(pulumi.BoolOutput)
}

// Indicates if the user has administrative rights. Administrators do not need to be managed in groups, as they automatically have access to all resources associated with the contract.
func (o LookupUserResultOutput) Administrator() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupUserResult) bool { return v.Administrator }).(pulumi.BoolOutput)
}

// The e-mail address for the user.
func (o LookupUserResultOutput) Email() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupUserResult) *string { return v.Email }).(pulumi.StringPtrOutput)
}

// The first name for the user.
func (o LookupUserResultOutput) FirstName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupUserResult) string { return v.FirstName }).(pulumi.StringOutput)
}

// Indicates if secure (two-factor) authentication should be forced for the user (true) or not (false).
func (o LookupUserResultOutput) ForceSecAuth() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupUserResult) bool { return v.ForceSecAuth }).(pulumi.BoolOutput)
}

// Shows the id and name of the groups that the user is a member of
func (o LookupUserResultOutput) Groups() GetUserGroupArrayOutput {
	return o.ApplyT(func(v LookupUserResult) []GetUserGroup { return v.Groups }).(GetUserGroupArrayOutput)
}

// The id of the user.
func (o LookupUserResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupUserResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// The last name for the user.
func (o LookupUserResultOutput) LastName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupUserResult) string { return v.LastName }).(pulumi.StringOutput)
}

// Canonical (S3) id of the user for a given identity
func (o LookupUserResultOutput) S3CanonicalUserId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupUserResult) string { return v.S3CanonicalUserId }).(pulumi.StringOutput)
}

// Indicates if secure authentication is active for the user or not
func (o LookupUserResultOutput) SecAuthActive() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupUserResult) bool { return v.SecAuthActive }).(pulumi.BoolOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupUserResultOutput{})
}
