// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ionoscloud

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func GetMongoUser(ctx *pulumi.Context, args *GetMongoUserArgs, opts ...pulumi.InvokeOption) (*GetMongoUserResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetMongoUserResult
	err := ctx.Invoke("ionoscloud:index/getMongoUser:getMongoUser", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getMongoUser.
type GetMongoUserArgs struct {
	ClusterId string             `pulumi:"clusterId"`
	Database  *string            `pulumi:"database"`
	Id        *string            `pulumi:"id"`
	Roles     []GetMongoUserRole `pulumi:"roles"`
	Username  string             `pulumi:"username"`
}

// A collection of values returned by getMongoUser.
type GetMongoUserResult struct {
	ClusterId string             `pulumi:"clusterId"`
	Database  string             `pulumi:"database"`
	Id        *string            `pulumi:"id"`
	Roles     []GetMongoUserRole `pulumi:"roles"`
	Username  string             `pulumi:"username"`
}

func GetMongoUserOutput(ctx *pulumi.Context, args GetMongoUserOutputArgs, opts ...pulumi.InvokeOption) GetMongoUserResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetMongoUserResultOutput, error) {
			args := v.(GetMongoUserArgs)
			opts = internal.PkgInvokeDefaultOpts(opts)
			var rv GetMongoUserResult
			secret, err := ctx.InvokePackageRaw("ionoscloud:index/getMongoUser:getMongoUser", args, &rv, "", opts...)
			if err != nil {
				return GetMongoUserResultOutput{}, err
			}

			output := pulumi.ToOutput(rv).(GetMongoUserResultOutput)
			if secret {
				return pulumi.ToSecret(output).(GetMongoUserResultOutput), nil
			}
			return output, nil
		}).(GetMongoUserResultOutput)
}

// A collection of arguments for invoking getMongoUser.
type GetMongoUserOutputArgs struct {
	ClusterId pulumi.StringInput         `pulumi:"clusterId"`
	Database  pulumi.StringPtrInput      `pulumi:"database"`
	Id        pulumi.StringPtrInput      `pulumi:"id"`
	Roles     GetMongoUserRoleArrayInput `pulumi:"roles"`
	Username  pulumi.StringInput         `pulumi:"username"`
}

func (GetMongoUserOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetMongoUserArgs)(nil)).Elem()
}

// A collection of values returned by getMongoUser.
type GetMongoUserResultOutput struct{ *pulumi.OutputState }

func (GetMongoUserResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetMongoUserResult)(nil)).Elem()
}

func (o GetMongoUserResultOutput) ToGetMongoUserResultOutput() GetMongoUserResultOutput {
	return o
}

func (o GetMongoUserResultOutput) ToGetMongoUserResultOutputWithContext(ctx context.Context) GetMongoUserResultOutput {
	return o
}

func (o GetMongoUserResultOutput) ClusterId() pulumi.StringOutput {
	return o.ApplyT(func(v GetMongoUserResult) string { return v.ClusterId }).(pulumi.StringOutput)
}

func (o GetMongoUserResultOutput) Database() pulumi.StringOutput {
	return o.ApplyT(func(v GetMongoUserResult) string { return v.Database }).(pulumi.StringOutput)
}

func (o GetMongoUserResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetMongoUserResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o GetMongoUserResultOutput) Roles() GetMongoUserRoleArrayOutput {
	return o.ApplyT(func(v GetMongoUserResult) []GetMongoUserRole { return v.Roles }).(GetMongoUserRoleArrayOutput)
}

func (o GetMongoUserResultOutput) Username() pulumi.StringOutput {
	return o.ApplyT(func(v GetMongoUserResult) string { return v.Username }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetMongoUserResultOutput{})
}
