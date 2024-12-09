// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ionoscloud

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The **IONOS Object Storage key data source** can be used to search for and return an existing IONOS Object Storage key.
// You can provide a string id which will be compared with provisioned IONOS Object Storage keys.
// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
// When this happens, please refine your search string so that it is specific enough to return only one result.
func GetS3Key(ctx *pulumi.Context, args *GetS3KeyArgs, opts ...pulumi.InvokeOption) (*GetS3KeyResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetS3KeyResult
	err := ctx.Invoke("ionoscloud:index/getS3Key:getS3Key", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getS3Key.
type GetS3KeyArgs struct {
	// The state of the IONOS Object Storage key
	Active *bool `pulumi:"active"`
	// ID of the IONOS Object Storage key you want to search for.
	Id *string `pulumi:"id"`
	// [string] The UUID of the user owning the IONOS Object Storage Key.
	UserId string `pulumi:"userId"`
}

// A collection of values returned by getS3Key.
type GetS3KeyResult struct {
	// The state of the IONOS Object Storage key
	Active *bool `pulumi:"active"`
	// The id of the IONOS Object Storage key
	Id *string `pulumi:"id"`
	// (Computed)The IONOS Object Storage Secret key.
	SecretKey string `pulumi:"secretKey"`
	// The ID of the user that owns the key
	UserId string `pulumi:"userId"`
}

func GetS3KeyOutput(ctx *pulumi.Context, args GetS3KeyOutputArgs, opts ...pulumi.InvokeOption) GetS3KeyResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetS3KeyResultOutput, error) {
			args := v.(GetS3KeyArgs)
			opts = internal.PkgInvokeDefaultOpts(opts)
			var rv GetS3KeyResult
			secret, err := ctx.InvokePackageRaw("ionoscloud:index/getS3Key:getS3Key", args, &rv, "", opts...)
			if err != nil {
				return GetS3KeyResultOutput{}, err
			}

			output := pulumi.ToOutput(rv).(GetS3KeyResultOutput)
			if secret {
				return pulumi.ToSecret(output).(GetS3KeyResultOutput), nil
			}
			return output, nil
		}).(GetS3KeyResultOutput)
}

// A collection of arguments for invoking getS3Key.
type GetS3KeyOutputArgs struct {
	// The state of the IONOS Object Storage key
	Active pulumi.BoolPtrInput `pulumi:"active"`
	// ID of the IONOS Object Storage key you want to search for.
	Id pulumi.StringPtrInput `pulumi:"id"`
	// [string] The UUID of the user owning the IONOS Object Storage Key.
	UserId pulumi.StringInput `pulumi:"userId"`
}

func (GetS3KeyOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetS3KeyArgs)(nil)).Elem()
}

// A collection of values returned by getS3Key.
type GetS3KeyResultOutput struct{ *pulumi.OutputState }

func (GetS3KeyResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetS3KeyResult)(nil)).Elem()
}

func (o GetS3KeyResultOutput) ToGetS3KeyResultOutput() GetS3KeyResultOutput {
	return o
}

func (o GetS3KeyResultOutput) ToGetS3KeyResultOutputWithContext(ctx context.Context) GetS3KeyResultOutput {
	return o
}

// The state of the IONOS Object Storage key
func (o GetS3KeyResultOutput) Active() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v GetS3KeyResult) *bool { return v.Active }).(pulumi.BoolPtrOutput)
}

// The id of the IONOS Object Storage key
func (o GetS3KeyResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetS3KeyResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// (Computed)The IONOS Object Storage Secret key.
func (o GetS3KeyResultOutput) SecretKey() pulumi.StringOutput {
	return o.ApplyT(func(v GetS3KeyResult) string { return v.SecretKey }).(pulumi.StringOutput)
}

// The ID of the user that owns the key
func (o GetS3KeyResultOutput) UserId() pulumi.StringOutput {
	return o.ApplyT(func(v GetS3KeyResult) string { return v.UserId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetS3KeyResultOutput{})
}
