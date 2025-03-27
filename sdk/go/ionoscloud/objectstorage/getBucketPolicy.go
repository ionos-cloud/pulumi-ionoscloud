// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package objectstorage

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The **Bucket Policy data source** can be used to search for and return existing bucket policies.
// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
// When this happens, please refine your search string so that it is specific enough to return only one result.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/objectstorage"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := objectstorage.LookupBucketPolicy(ctx, &objectstorage.LookupBucketPolicyArgs{
//				Bucket: "example",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func LookupBucketPolicy(ctx *pulumi.Context, args *LookupBucketPolicyArgs, opts ...pulumi.InvokeOption) (*LookupBucketPolicyResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupBucketPolicyResult
	err := ctx.Invoke("ionoscloud:objectstorage/getBucketPolicy:getBucketPolicy", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getBucketPolicy.
type LookupBucketPolicyArgs struct {
	// [string] The name of the bucket where the object will be stored.
	Bucket string `pulumi:"bucket"`
}

// A collection of values returned by getBucketPolicy.
type LookupBucketPolicyResult struct {
	Bucket string `pulumi:"bucket"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The policy of the bucket.
	Policy string `pulumi:"policy"`
}

func LookupBucketPolicyOutput(ctx *pulumi.Context, args LookupBucketPolicyOutputArgs, opts ...pulumi.InvokeOption) LookupBucketPolicyResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupBucketPolicyResultOutput, error) {
			args := v.(LookupBucketPolicyArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("ionoscloud:objectstorage/getBucketPolicy:getBucketPolicy", args, LookupBucketPolicyResultOutput{}, options).(LookupBucketPolicyResultOutput), nil
		}).(LookupBucketPolicyResultOutput)
}

// A collection of arguments for invoking getBucketPolicy.
type LookupBucketPolicyOutputArgs struct {
	// [string] The name of the bucket where the object will be stored.
	Bucket pulumi.StringInput `pulumi:"bucket"`
}

func (LookupBucketPolicyOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupBucketPolicyArgs)(nil)).Elem()
}

// A collection of values returned by getBucketPolicy.
type LookupBucketPolicyResultOutput struct{ *pulumi.OutputState }

func (LookupBucketPolicyResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupBucketPolicyResult)(nil)).Elem()
}

func (o LookupBucketPolicyResultOutput) ToLookupBucketPolicyResultOutput() LookupBucketPolicyResultOutput {
	return o
}

func (o LookupBucketPolicyResultOutput) ToLookupBucketPolicyResultOutputWithContext(ctx context.Context) LookupBucketPolicyResultOutput {
	return o
}

func (o LookupBucketPolicyResultOutput) Bucket() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBucketPolicyResult) string { return v.Bucket }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupBucketPolicyResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBucketPolicyResult) string { return v.Id }).(pulumi.StringOutput)
}

// The policy of the bucket.
func (o LookupBucketPolicyResultOutput) Policy() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBucketPolicyResult) string { return v.Policy }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupBucketPolicyResultOutput{})
}
