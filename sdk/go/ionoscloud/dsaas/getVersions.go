// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package dsaas

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The **Dataplatform Versions Data Source** can be used to search for and retrieve list of available Managed Dataplatform API versions.
//
// ## Example Usage
//
// ### Retrieve list of Managed Dataplatform API versions
// ```go
// package main
//
// import (
//
//	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/dsaas"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := dsaas.GetVersions(ctx, map[string]interface{}{}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func GetVersions(ctx *pulumi.Context, opts ...pulumi.InvokeOption) (*GetVersionsResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetVersionsResult
	err := ctx.Invoke("ionoscloud:dsaas/getVersions:getVersions", nil, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of values returned by getVersions.
type GetVersionsResult struct {
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// list of Managed Dataplatform API versions.
	Versions []string `pulumi:"versions"`
}

func GetVersionsOutput(ctx *pulumi.Context, opts ...pulumi.InvokeOption) GetVersionsResultOutput {
	return pulumi.ToOutput(0).ApplyT(func(int) (GetVersionsResultOutput, error) {
		options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
		return ctx.InvokeOutput("ionoscloud:dsaas/getVersions:getVersions", nil, GetVersionsResultOutput{}, options).(GetVersionsResultOutput), nil
	}).(GetVersionsResultOutput)
}

// A collection of values returned by getVersions.
type GetVersionsResultOutput struct{ *pulumi.OutputState }

func (GetVersionsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetVersionsResult)(nil)).Elem()
}

func (o GetVersionsResultOutput) ToGetVersionsResultOutput() GetVersionsResultOutput {
	return o
}

func (o GetVersionsResultOutput) ToGetVersionsResultOutputWithContext(ctx context.Context) GetVersionsResultOutput {
	return o
}

// The provider-assigned unique ID for this managed resource.
func (o GetVersionsResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetVersionsResult) string { return v.Id }).(pulumi.StringOutput)
}

// list of Managed Dataplatform API versions.
func (o GetVersionsResultOutput) Versions() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetVersionsResult) []string { return v.Versions }).(pulumi.StringArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(GetVersionsResultOutput{})
}
