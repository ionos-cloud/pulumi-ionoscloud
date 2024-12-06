// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ionoscloud

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
//			_, err := ionoscloud.GetUser(ctx, &ionoscloud.GetUserArgs{
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
// <!--End PulumiCodeChooser -->
//
// ### By Email from Env Variables - Current User
// data "compute.User" "example" {
// }
func GetUser(ctx *pulumi.Context, args *GetUserArgs, opts ...pulumi.InvokeOption) (*GetUserResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetUserResult
	err := ctx.Invoke("ionoscloud:index/getUser:getUser", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getUser.
type GetUserArgs struct {
	// Email of an existing user that you want to search for.
	Email *string `pulumi:"email"`
	// ID of the user you want to search for.
	//
	// Either `email` or `id` can be provided. If no argument is set, the provider will search for the **email that was provided for the configuration**. If none is found, the provider will return an error.
	Id *string `pulumi:"id"`
}

// A collection of values returned by getUser.
type GetUserResult struct {
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

func GetUserOutput(ctx *pulumi.Context, args GetUserOutputArgs, opts ...pulumi.InvokeOption) GetUserResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetUserResult, error) {
			args := v.(GetUserArgs)
			r, err := GetUser(ctx, &args, opts...)
			var s GetUserResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetUserResultOutput)
}

// A collection of arguments for invoking getUser.
type GetUserOutputArgs struct {
	// Email of an existing user that you want to search for.
	Email pulumi.StringPtrInput `pulumi:"email"`
	// ID of the user you want to search for.
	//
	// Either `email` or `id` can be provided. If no argument is set, the provider will search for the **email that was provided for the configuration**. If none is found, the provider will return an error.
	Id pulumi.StringPtrInput `pulumi:"id"`
}

func (GetUserOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetUserArgs)(nil)).Elem()
}

// A collection of values returned by getUser.
type GetUserResultOutput struct{ *pulumi.OutputState }

func (GetUserResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetUserResult)(nil)).Elem()
}

func (o GetUserResultOutput) ToGetUserResultOutput() GetUserResultOutput {
	return o
}

func (o GetUserResultOutput) ToGetUserResultOutputWithContext(ctx context.Context) GetUserResultOutput {
	return o
}

// Indicates if the user is active
func (o GetUserResultOutput) Active() pulumi.BoolOutput {
	return o.ApplyT(func(v GetUserResult) bool { return v.Active }).(pulumi.BoolOutput)
}

// Indicates if the user has administrative rights. Administrators do not need to be managed in groups, as they automatically have access to all resources associated with the contract.
func (o GetUserResultOutput) Administrator() pulumi.BoolOutput {
	return o.ApplyT(func(v GetUserResult) bool { return v.Administrator }).(pulumi.BoolOutput)
}

// The e-mail address for the user.
func (o GetUserResultOutput) Email() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetUserResult) *string { return v.Email }).(pulumi.StringPtrOutput)
}

// The first name for the user.
func (o GetUserResultOutput) FirstName() pulumi.StringOutput {
	return o.ApplyT(func(v GetUserResult) string { return v.FirstName }).(pulumi.StringOutput)
}

// Indicates if secure (two-factor) authentication should be forced for the user (true) or not (false).
func (o GetUserResultOutput) ForceSecAuth() pulumi.BoolOutput {
	return o.ApplyT(func(v GetUserResult) bool { return v.ForceSecAuth }).(pulumi.BoolOutput)
}

// Shows the id and name of the groups that the user is a member of
func (o GetUserResultOutput) Groups() GetUserGroupArrayOutput {
	return o.ApplyT(func(v GetUserResult) []GetUserGroup { return v.Groups }).(GetUserGroupArrayOutput)
}

// The id of the user.
func (o GetUserResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetUserResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// The last name for the user.
func (o GetUserResultOutput) LastName() pulumi.StringOutput {
	return o.ApplyT(func(v GetUserResult) string { return v.LastName }).(pulumi.StringOutput)
}

// Canonical (S3) id of the user for a given identity
func (o GetUserResultOutput) S3CanonicalUserId() pulumi.StringOutput {
	return o.ApplyT(func(v GetUserResult) string { return v.S3CanonicalUserId }).(pulumi.StringOutput)
}

// Indicates if secure authentication is active for the user or not
func (o GetUserResultOutput) SecAuthActive() pulumi.BoolOutput {
	return o.ApplyT(func(v GetUserResult) bool { return v.SecAuthActive }).(pulumi.BoolOutput)
}

func init() {
	pulumi.RegisterOutputType(GetUserResultOutput{})
}
