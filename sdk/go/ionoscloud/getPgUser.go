// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ionoscloud

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func GetPgUser(ctx *pulumi.Context, args *GetPgUserArgs, opts ...pulumi.InvokeOption) (*GetPgUserResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetPgUserResult
	err := ctx.Invoke("ionoscloud:index/getPgUser:getPgUser", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getPgUser.
type GetPgUserArgs struct {
	ClusterId string `pulumi:"clusterId"`
	Username  string `pulumi:"username"`
}

// A collection of values returned by getPgUser.
type GetPgUserResult struct {
	ClusterId    string `pulumi:"clusterId"`
	Id           string `pulumi:"id"`
	IsSystemUser bool   `pulumi:"isSystemUser"`
	Username     string `pulumi:"username"`
}

func GetPgUserOutput(ctx *pulumi.Context, args GetPgUserOutputArgs, opts ...pulumi.InvokeOption) GetPgUserResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetPgUserResult, error) {
			args := v.(GetPgUserArgs)
			r, err := GetPgUser(ctx, &args, opts...)
			var s GetPgUserResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetPgUserResultOutput)
}

// A collection of arguments for invoking getPgUser.
type GetPgUserOutputArgs struct {
	ClusterId pulumi.StringInput `pulumi:"clusterId"`
	Username  pulumi.StringInput `pulumi:"username"`
}

func (GetPgUserOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetPgUserArgs)(nil)).Elem()
}

// A collection of values returned by getPgUser.
type GetPgUserResultOutput struct{ *pulumi.OutputState }

func (GetPgUserResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetPgUserResult)(nil)).Elem()
}

func (o GetPgUserResultOutput) ToGetPgUserResultOutput() GetPgUserResultOutput {
	return o
}

func (o GetPgUserResultOutput) ToGetPgUserResultOutputWithContext(ctx context.Context) GetPgUserResultOutput {
	return o
}

func (o GetPgUserResultOutput) ClusterId() pulumi.StringOutput {
	return o.ApplyT(func(v GetPgUserResult) string { return v.ClusterId }).(pulumi.StringOutput)
}

func (o GetPgUserResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetPgUserResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o GetPgUserResultOutput) IsSystemUser() pulumi.BoolOutput {
	return o.ApplyT(func(v GetPgUserResult) bool { return v.IsSystemUser }).(pulumi.BoolOutput)
}

func (o GetPgUserResultOutput) Username() pulumi.StringOutput {
	return o.ApplyT(func(v GetPgUserResult) string { return v.Username }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetPgUserResultOutput{})
}
