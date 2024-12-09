// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ionoscloud

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The **Logging pipeline** datasource can be used to search for and return an existing Logging pipeline.
// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
//
// > ⚠️  Only tokens are accepted for authorization in the **logging_pipeline** data source. Please ensure you are using tokens as other methods will not be valid.
//
// ## Example Usage
//
// ### By name
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
//			_, err := ionoscloud.LookupLoggingPipeline(ctx, &ionoscloud.LookupLoggingPipelineArgs{
//				Location: pulumi.StringRef("de/txl"),
//				Name:     pulumi.StringRef("pipeline_name"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func LookupLoggingPipeline(ctx *pulumi.Context, args *LookupLoggingPipelineArgs, opts ...pulumi.InvokeOption) (*LookupLoggingPipelineResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupLoggingPipelineResult
	err := ctx.Invoke("ionoscloud:index/getLoggingPipeline:getLoggingPipeline", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getLoggingPipeline.
type LookupLoggingPipelineArgs struct {
	// [string] The ID of the Logging pipeline you want to search for.
	Id *string `pulumi:"id"`
	// [string] The location of the Logging pipeline. Default: `de/txl`. One of `de/fra`, `de/txl`, `gb/lhr`, `es/vit`, `fr/par`.
	Location *string `pulumi:"location"`
	// [string] The name of the Logging pipeline you want to search for.
	//
	// Either `id` or `name` must be provided. If none, or both are provided, the datasource will return an error.
	Name *string `pulumi:"name"`
}

// A collection of values returned by getLoggingPipeline.
type LookupLoggingPipelineResult struct {
	// The address of the client's grafana instance.
	GrafanaAddress string `pulumi:"grafanaAddress"`
	// The UUID of the Logging pipeline.
	Id       *string `pulumi:"id"`
	Location *string `pulumi:"location"`
	// [list] Pipeline logs, a list that contains elements with the following structure:
	Logs []GetLoggingPipelineLog `pulumi:"logs"`
	// The name of the Logging pipeline.
	Name string `pulumi:"name"`
}

func LookupLoggingPipelineOutput(ctx *pulumi.Context, args LookupLoggingPipelineOutputArgs, opts ...pulumi.InvokeOption) LookupLoggingPipelineResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupLoggingPipelineResultOutput, error) {
			args := v.(LookupLoggingPipelineArgs)
			opts = internal.PkgInvokeDefaultOpts(opts)
			var rv LookupLoggingPipelineResult
			secret, err := ctx.InvokePackageRaw("ionoscloud:index/getLoggingPipeline:getLoggingPipeline", args, &rv, "", opts...)
			if err != nil {
				return LookupLoggingPipelineResultOutput{}, err
			}

			output := pulumi.ToOutput(rv).(LookupLoggingPipelineResultOutput)
			if secret {
				return pulumi.ToSecret(output).(LookupLoggingPipelineResultOutput), nil
			}
			return output, nil
		}).(LookupLoggingPipelineResultOutput)
}

// A collection of arguments for invoking getLoggingPipeline.
type LookupLoggingPipelineOutputArgs struct {
	// [string] The ID of the Logging pipeline you want to search for.
	Id pulumi.StringPtrInput `pulumi:"id"`
	// [string] The location of the Logging pipeline. Default: `de/txl`. One of `de/fra`, `de/txl`, `gb/lhr`, `es/vit`, `fr/par`.
	Location pulumi.StringPtrInput `pulumi:"location"`
	// [string] The name of the Logging pipeline you want to search for.
	//
	// Either `id` or `name` must be provided. If none, or both are provided, the datasource will return an error.
	Name pulumi.StringPtrInput `pulumi:"name"`
}

func (LookupLoggingPipelineOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupLoggingPipelineArgs)(nil)).Elem()
}

// A collection of values returned by getLoggingPipeline.
type LookupLoggingPipelineResultOutput struct{ *pulumi.OutputState }

func (LookupLoggingPipelineResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupLoggingPipelineResult)(nil)).Elem()
}

func (o LookupLoggingPipelineResultOutput) ToLookupLoggingPipelineResultOutput() LookupLoggingPipelineResultOutput {
	return o
}

func (o LookupLoggingPipelineResultOutput) ToLookupLoggingPipelineResultOutputWithContext(ctx context.Context) LookupLoggingPipelineResultOutput {
	return o
}

// The address of the client's grafana instance.
func (o LookupLoggingPipelineResultOutput) GrafanaAddress() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLoggingPipelineResult) string { return v.GrafanaAddress }).(pulumi.StringOutput)
}

// The UUID of the Logging pipeline.
func (o LookupLoggingPipelineResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLoggingPipelineResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupLoggingPipelineResultOutput) Location() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLoggingPipelineResult) *string { return v.Location }).(pulumi.StringPtrOutput)
}

// [list] Pipeline logs, a list that contains elements with the following structure:
func (o LookupLoggingPipelineResultOutput) Logs() GetLoggingPipelineLogArrayOutput {
	return o.ApplyT(func(v LookupLoggingPipelineResult) []GetLoggingPipelineLog { return v.Logs }).(GetLoggingPipelineLogArrayOutput)
}

// The name of the Logging pipeline.
func (o LookupLoggingPipelineResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLoggingPipelineResult) string { return v.Name }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupLoggingPipelineResultOutput{})
}
