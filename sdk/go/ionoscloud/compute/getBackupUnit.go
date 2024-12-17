// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The **Backup Unit data source** can be used to search for and return an existing Backup Unit.
// You can provide a string for either id or name parameters which will be compared with provisioned Backup Units.
// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
// When this happens, please refine your search string so that it is specific enough to return only one result.
//
// ## Example Usage
//
// ### By Name
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
//			_, err := compute.LookupBackupUnit(ctx, &compute.LookupBackupUnitArgs{
//				Name: pulumi.StringRef("Backup Unit Example"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func LookupBackupUnit(ctx *pulumi.Context, args *LookupBackupUnitArgs, opts ...pulumi.InvokeOption) (*LookupBackupUnitResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupBackupUnitResult
	err := ctx.Invoke("ionoscloud:compute/getBackupUnit:getBackupUnit", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getBackupUnit.
type LookupBackupUnitArgs struct {
	// ID of the backup unit you want to search for.
	//
	// Either `name` or `id` must be provided. If none, or both are provided, the datasource will return an error.
	Id *string `pulumi:"id"`
	// Name of an existing backup unit that you want to search for.
	Name *string `pulumi:"name"`
}

// A collection of values returned by getBackupUnit.
type LookupBackupUnitResult struct {
	// The e-mail address you want assigned to the backup unit.
	Email string `pulumi:"email"`
	// The id of the Backup Unit.
	Id *string `pulumi:"id"`
	// The login associated with the backup unit. Derived from the contract number.
	Login string `pulumi:"login"`
	// The name of the Backup Unit.
	Name *string `pulumi:"name"`
}

func LookupBackupUnitOutput(ctx *pulumi.Context, args LookupBackupUnitOutputArgs, opts ...pulumi.InvokeOption) LookupBackupUnitResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupBackupUnitResultOutput, error) {
			args := v.(LookupBackupUnitArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("ionoscloud:compute/getBackupUnit:getBackupUnit", args, LookupBackupUnitResultOutput{}, options).(LookupBackupUnitResultOutput), nil
		}).(LookupBackupUnitResultOutput)
}

// A collection of arguments for invoking getBackupUnit.
type LookupBackupUnitOutputArgs struct {
	// ID of the backup unit you want to search for.
	//
	// Either `name` or `id` must be provided. If none, or both are provided, the datasource will return an error.
	Id pulumi.StringPtrInput `pulumi:"id"`
	// Name of an existing backup unit that you want to search for.
	Name pulumi.StringPtrInput `pulumi:"name"`
}

func (LookupBackupUnitOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupBackupUnitArgs)(nil)).Elem()
}

// A collection of values returned by getBackupUnit.
type LookupBackupUnitResultOutput struct{ *pulumi.OutputState }

func (LookupBackupUnitResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupBackupUnitResult)(nil)).Elem()
}

func (o LookupBackupUnitResultOutput) ToLookupBackupUnitResultOutput() LookupBackupUnitResultOutput {
	return o
}

func (o LookupBackupUnitResultOutput) ToLookupBackupUnitResultOutputWithContext(ctx context.Context) LookupBackupUnitResultOutput {
	return o
}

// The e-mail address you want assigned to the backup unit.
func (o LookupBackupUnitResultOutput) Email() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBackupUnitResult) string { return v.Email }).(pulumi.StringOutput)
}

// The id of the Backup Unit.
func (o LookupBackupUnitResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupBackupUnitResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// The login associated with the backup unit. Derived from the contract number.
func (o LookupBackupUnitResultOutput) Login() pulumi.StringOutput {
	return o.ApplyT(func(v LookupBackupUnitResult) string { return v.Login }).(pulumi.StringOutput)
}

// The name of the Backup Unit.
func (o LookupBackupUnitResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupBackupUnitResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupBackupUnitResultOutput{})
}
