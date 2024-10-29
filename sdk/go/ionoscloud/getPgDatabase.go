// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ionoscloud

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func LookupPgDatabase(ctx *pulumi.Context, args *LookupPgDatabaseArgs, opts ...pulumi.InvokeOption) (*LookupPgDatabaseResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupPgDatabaseResult
	err := ctx.Invoke("ionoscloud:index/getPgDatabase:getPgDatabase", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getPgDatabase.
type LookupPgDatabaseArgs struct {
	ClusterId string `pulumi:"clusterId"`
	Name      string `pulumi:"name"`
}

// A collection of values returned by getPgDatabase.
type LookupPgDatabaseResult struct {
	ClusterId string `pulumi:"clusterId"`
	Id        string `pulumi:"id"`
	Name      string `pulumi:"name"`
	Owner     string `pulumi:"owner"`
}

func LookupPgDatabaseOutput(ctx *pulumi.Context, args LookupPgDatabaseOutputArgs, opts ...pulumi.InvokeOption) LookupPgDatabaseResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupPgDatabaseResult, error) {
			args := v.(LookupPgDatabaseArgs)
			r, err := LookupPgDatabase(ctx, &args, opts...)
			var s LookupPgDatabaseResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupPgDatabaseResultOutput)
}

// A collection of arguments for invoking getPgDatabase.
type LookupPgDatabaseOutputArgs struct {
	ClusterId pulumi.StringInput `pulumi:"clusterId"`
	Name      pulumi.StringInput `pulumi:"name"`
}

func (LookupPgDatabaseOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupPgDatabaseArgs)(nil)).Elem()
}

// A collection of values returned by getPgDatabase.
type LookupPgDatabaseResultOutput struct{ *pulumi.OutputState }

func (LookupPgDatabaseResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupPgDatabaseResult)(nil)).Elem()
}

func (o LookupPgDatabaseResultOutput) ToLookupPgDatabaseResultOutput() LookupPgDatabaseResultOutput {
	return o
}

func (o LookupPgDatabaseResultOutput) ToLookupPgDatabaseResultOutputWithContext(ctx context.Context) LookupPgDatabaseResultOutput {
	return o
}

func (o LookupPgDatabaseResultOutput) ClusterId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPgDatabaseResult) string { return v.ClusterId }).(pulumi.StringOutput)
}

func (o LookupPgDatabaseResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPgDatabaseResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o LookupPgDatabaseResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPgDatabaseResult) string { return v.Name }).(pulumi.StringOutput)
}

func (o LookupPgDatabaseResultOutput) Owner() pulumi.StringOutput {
	return o.ApplyT(func(v LookupPgDatabaseResult) string { return v.Owner }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupPgDatabaseResultOutput{})
}
